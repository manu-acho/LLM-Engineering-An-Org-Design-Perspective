import { promises as fs } from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import { buildReader, distRoot, projectRoot } from './build.mjs';

const build = await buildReader();
const payload = JSON.parse(await fs.readFile(path.join(distRoot, 'content-index.json'), 'utf8'));
const documents = new Map(payload.documents.map(doc => [doc.path, doc]));
assert.equal(payload.edition, 'standalone-pilot');
assert.equal(payload.curriculum.length, 20);
assert.equal(new Set(payload.curriculum.map(module => module.number)).size, 20);
assert.equal(payload.curriculum.filter(module => module.status === 'pilot').length, 1);
assert.equal(payload.curriculum.filter(module => module.status === 'planned').length, 19);
assert.equal(build.lessons, 7);
assert.equal(payload.documents.filter(doc => doc.path.startsWith('reference/research/')).length, 6);

let links = 0;
for (const document of payload.documents) {
  assert(!document.content.includes('org-design-as-code'), `Original research link in ${document.path}`);
  if (document.path.startsWith('modules/')) {
    assert(document.path.startsWith('modules/01-standalone-foundations/'), 'Companion lesson published');
  }
  const prose = document.content.replace(/```[\s\S]*?```|`[^`]+`/g, '');
  for (const match of prose.matchAll(/\[[^\]]+\]\(([^)]+)\)/g)) {
    const href = decodeURIComponent(match[1]);
    if (/^(https?:|mailto:)/.test(href)) continue;
    const [file, heading] = href.split('#');
    if (file.startsWith('/downloads/')) {
      assert(['foundations_lab.py', 'test_foundations.py'].includes(path.posix.basename(file)));
      await fs.access(path.join(distRoot, file.slice(1)));
    } else {
      const target = file ? path.posix.normalize(path.posix.join(path.posix.dirname(document.path), file)) : document.path;
      assert(documents.has(target), `${document.path}: absent reading ${href}`);
      if (heading) assert(documents.get(target).headings.some(item => item.anchor === heading), `${document.path}: absent heading ${href}`);
    }
    links++;
  }
}
for (const file of ['foundations_lab.py', 'test_foundations.py']) {
  const source = await fs.readFile(path.join(projectRoot, 'examples/01-foundations', file));
  const published = await fs.readFile(path.join(distRoot, 'downloads', file));
  assert(source.equals(published), `Changed download: ${file}`);
}
console.log({ ...build, internalLinksChecked: links, curriculumModules: 20, completeStandaloneModules: 1, downloadFiles: 2 });
