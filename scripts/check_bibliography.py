"""Validate reference exports and research citation coverage without network calls."""
from pathlib import Path
import json
import re
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
records = json.loads((root / 'references/catalog.json').read_text())
keys = [r['key'] for r in records]
assert len(keys) == len(set(keys)), 'Duplicate reference key'
dois = [r['doi'].lower() for r in records if r.get('doi')]
assert len(dois) == len(set(dois)), 'Duplicate DOI'
by_anchor = {r['anchor']: r for r in records}
assert len(by_anchor) == len(records), 'Duplicate reference anchor'
bib = (root / 'references/references.bib').read_text()
page = (root / 'reference/bibliography.md').read_text()
assert set(re.findall(r'^@\w+\{([^,]+),', bib, re.M)) == set(keys), 'BibTeX/catalogue mismatch'
assert set(re.findall(r'Citation key: `([a-z0-9]+)`', page)) == set(keys), 'Page/catalogue mismatch'
for r in records:
    for field in ['key', 'type', 'author', 'title', 'year', 'access', 'metadata_status', 'chapters']:
        assert field in r and (r[field] or field == 'chapters'), (r['key'], field)
    assert re.fullmatch(r'\d{4}', r['year']), r['key']
    assert '\\' not in r['author'], f'Unrendered author markup: {r["key"]}'
    for chapter in r['chapters']:
        assert (root / 'reference/research' / chapter).is_file(), (r['key'], chapter)
# DOI aliases and escaped parentheses must not create false missing-reference errors.
aliases = {'10.1080/19416520903047533': '10.5465/19416520903047533'}
checked = 0
for chapter in sorted((root / 'reference/research').glob('*.md')):
    text = chapter.read_text()
    for key in re.findall(r'\.\./bibliography\.md#([a-z0-9-]+)', text):
        assert key in by_anchor, (chapter.name, key)
        assert chapter.name in by_anchor[key]['chapters'], (chapter.name, key, 'missing usage mapping')
        checked += 1
    # Read URLs with balanced parentheses, which occur in some older DOI strings.
    for match in re.finditer(r'https://doi\.org/', text):
        start = match.end(); pos = start; depth = 0
        while pos < len(text):
            char = text[pos]
            if char == '(':
                depth += 1
            elif char == ')':
                if depth == 0:
                    break
                depth -= 1
            if char.isspace():
                break
            pos += 1
        doi = unquote(text[start:pos]).lower()
        assert aliases.get(doi, doi) in dois, (chapter.name, doi, 'absent reference')
        checked += 1
print({'reference_entries': len(records), 'unique_dois': len(dois), 'research_citations_checked': checked})
