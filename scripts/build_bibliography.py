"""Render the public bibliography and BibTeX export from references/catalog.json.

Run from any directory. No network requests or third-party packages are required.
Edit the catalogue first, retaining stable keys and explicit source-access notes.
"""
from pathlib import Path
import json
from urllib.parse import quote
root = Path(__file__).resolve().parents[1]
records = {r["key"]: r for r in json.loads((root / "references/catalog.json").read_text())}
fields = ['author','title','year','journal','booktitle','publisher','edition','volume','number','pages','doi','url','editor','chapter','address']
bib=[]
for r in sorted(records.values(),key=lambda r:r['key']):
 fs=[]
 for f in fields+['eprint','archiveprefix','note']:
  if r.get(f):
   value=r[f].replace('&','\\&')
   fs.append(f'  {f} = {{{value}}}')
 bib.append('@'+r['type']+'{'+r['key']+',\n'+',\n'.join(fs)+'\n}')
(root/'references/references.bib').write_text('% AI engineering and organisation design: curated teaching bibliography\n% Metadata and access notes: see reference/bibliography.md and catalog.json\n\n'+'\n\n'.join(bib)+'\n')
def authors(s):
 result=[]
 for a in s.split(' and '):
  bits=a.split(', ')
  if len(bits)==2:
   family,given=bits; initials=' '.join(n[0]+'.' for n in given.replace('-',' ').split() if n)
   result.append(f'{family}, {initials}')
  elif len(bits)==3:result.append(f'{bits[0]}, {bits[1]}, '+ ' '.join(n[0]+'.' for n in bits[2].split()))
  else:result.append(a)
 return '; '.join(result)
intro='''# Project bibliography

[Research reading guide](literature-guide.md) · [Foundation and advanced study](research-study-pathways.md)

## Scope and use

This collection brings together organisation design, coordination, decisions, implementation, routines, technology in practice, infrastructure, governance and process research, alongside selected AI studies. It supports the explanations in the nine research chapters and offers a wider reading base. It is a curated teaching bibliography, not a systematic review or a claim to cover all current AI research.

Entries labelled **Chapter use** support a chapter citation. Entries labelled **Wider reading** extend the relevant theoretical conversation; inclusion does not mean that the course makes a finding from that publication. The engineering documentation in [further learning](further-learning.md) serves a separate, practical purpose.

Download the [BibTeX bibliography](/downloads/references.bib) for a reference manager. The repository also contains `references/catalog.json`, the structured catalogue from which this page and the BibTeX file are generated. Each entry includes a stable citation key. The export records bibliographic facts; it does not grant access to paywalled texts or permission to reproduce publications.

## Reading and evidence boundaries

Publication metadata and substantive reading are different checks. Crossref metadata was retrieved for the 79 DOI-bearing entries on 8 November 2026. Nine books or chapters without a DOI retain edition details from the existing scholarly bibliography; those editions were not independently rechecked in this update. The additional BPM preprint was checked against its arXiv record.

Most classic entries have no new full-text inspection recorded in this update. Their role is conceptual synthesis, with no page-specific quotations or claims of replication. New AI sources have individual access notes below, distinguishing manuscript passages from an abstract. A manuscript can differ from the published version. Consult the identified version before using a page-specific quotation or developing a close scholarly interpretation.

The Harbour cases are fictional applications. A proposed framework, a controlled experiment, an observational organisational study and a literature review supply different kinds of support. Their results should not be treated as interchangeable or as predicted benefits for Harbour.

## Find a theme

| Theme | Begin with these authors | Read the explanation |
|---|---|---|
| Organisation design | Galbraith; Thompson; Puranam; Raisch and Krakowski | [Chapter 1](research/01-organisation-design.md) |
| Coordination | Malone and Crowston; Okhuysen and Bechky; Carlile; Faraj et al. | [Chapter 2](research/02-coordination.md) |
| Decisions | Simon; March and Simon; Shrestha et al.; Buçinca et al. | [Chapter 3](research/03-decisions.md) |
| Implementation | Markus and Tanis; Brehm et al.; Brynjolfsson et al. | [Chapter 4](research/04-implementation.md) |
| Routines and knowing | Feldman and Pentland; D'Adderio; Pachidi et al. | [Chapter 5](research/05-routines.md) |
| Technology in practice | Orlikowski; Leonardi; Volkoff and Strong; Kellogg et al. | [Chapter 6](research/06-technology-in-practice.md) |
| Infrastructure and standards | Star and Ruhleder; Bowker and Star; Hanseth et al.; Sambasivan et al.; Gebru et al. | [Chapter 7](research/07-infrastructure-and-standards.md) |
| Governance and accountability | Ouchi; Kirsch; Bovens; Lindberg; Mitchell et al.; Raji et al. | [Chapter 8](research/08-governance-and-accountability.md) |
| Process architecture | Curtis et al.; Dumas et al.; van der Aalst; Dijkman et al.; Vidgof et al. | [Chapter 9](research/09-process-architecture.md) |

## Alphabetical reference entries

'''
parts=[intro]
for r in sorted(records.values(),key=lambda r:(r['author'].lower(),r['year'],r['title'])):
 text=f"### {r['heading']}\n\n{authors(r['author'])} ({r['year']}). {('*'+r['title']+'*') if r['type']=='book' else r['title']}. "
 if r.get('journal'):
  text+=f"*{r['journal']}"+(f", {r['volume']}" if r.get('volume') else '')+'*'+(f"({r['number'].replace('--','–')})" if r.get('number') else '')+(f", {r['pages'].replace('--','–')}" if r.get('pages') else '')+'. '
 elif r.get('booktitle'):text+=(f"In {authors(r['editor'])} (Ed.), " if r.get('editor') else 'In ')+f"*{r['booktitle']}*"+(f" (pp. {r['pages'].replace('--','–')})" if r.get('pages') else '')+'. '+(r.get('publisher','')+'. ' if r.get('publisher') else '')
 else:text+=(f"({'2nd' if r['edition']=='2' else '4th' if r['edition']=='4' else r['edition']} ed.). " if r.get('edition') else '')+(r.get('publisher','')+'. ' if r.get('publisher') else '')
 if r.get('eprint'):text+=f"arXiv:{r['eprint']} (preprint). "
 if r.get('doi'):
  doi_path = quote(r['doi'], safe='/')
  text += f"[Publication](https://doi.org/{doi_path}). "
 elif r.get('url'):text+=f"[Publication record]({r['url']}). "
 if r.get('note'):text+=r['note']+' '
 if r['chapters']:text+='\n\nChapter use: '+', '.join(f"[{n.split('-')[0]}](research/{n})" for n in r['chapters'])+'.'
 else:text+='\n\nWider reading.'
 text+=f" Citation key: `{r['key']}`. "+r['access']
 if r.get('reading_url') and r['reading_url']!='https://doi.org/'+r.get('doi',''):text+=f" [Reading version]({r['reading_url']})."
 parts.append('\n'.join(line.rstrip() for line in text.splitlines())+'\n\n')
(root/'reference/bibliography.md').write_text(''.join(parts).rstrip() + '\n')
print({'entries':len(records),'with_chapter_use':sum(bool(r['chapters']) for r in records.values()),'crossref':sum('Crossref' in r['metadata_status'] for r in records.values())})
