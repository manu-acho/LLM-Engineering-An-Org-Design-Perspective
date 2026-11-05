import { promises as fs } from 'node:fs';
import path from 'node:path';
import { buildBundle } from './bundle.mjs';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
export const readerRoot = path.resolve(here, '..');
export const projectRoot = path.resolve(readerRoot, '..');
export const distRoot = path.join(readerRoot, 'dist');
const curriculumData = JSON.parse(await fs.readFile(path.join(readerRoot, 'standalone-curriculum.json'), 'utf8'));
const moduleNames = Object.fromEntries(curriculumData.map(m => [m.path.split('/')[1], `${String(m.number).padStart(2, '0')} · ${m.title}`]));
// Only completed standalone teaching units enter the published collection.
const readingFiles = [
  'README.md', 'START-HERE.md', 'CURRICULUM.md', 'WORKBOOK.md', 'SOURCE-MAP.md',
  'LAB-GUIDE.md', 'STUDY-WORKSPACE.md', 'AGENT-ENGINEERING.md', 'reference/glossary.md',
  'reference/literature-guide.md', 'reference/python-patterns.md', 'reference/technical-foundations.md', 'reference/further-learning.md', 'reference/verification.md'
];

const researchFiles = [
  'reference/research/01-organisation-design.md', 'reference/research/02-coordination.md',
  'reference/research/03-decisions.md', 'reference/research/04-implementation.md',
  'reference/research/05-routines.md', 'reference/research/06-technology-in-practice.md'
];

function sectionFor(relative) {
  if (relative === 'reference/literature-guide.md' || researchFiles.includes(relative)) return 'Organisation design research';
  if (['README.md', 'START-HERE.md', 'WORKBOOK.md', 'AGENT-ENGINEERING.md', 'CURRICULUM.md', 'LAB-GUIDE.md', 'STUDY-WORKSPACE.md'].includes(relative)) return 'Start and study';
  if (relative.startsWith('modules/')) return moduleNames[relative.split('/')[1]] || 'Engineering references';
  return 'Sources and further reading';
}

function makeDocument(relative, content, modified) {
  const title = content.match(/^#\s+(.+)$/m)?.[1] || path.basename(relative);
  const prose = content.replace(/```[\s\S]*?```/g, '');
  const counts = new Map();
  const headings = [...prose.matchAll(/^(#{2,4})\s+(.+)$/gm)].map(match => {
    const text = match[2].replace(/[*_`]/g, '').trim();
    const slug = text.toLowerCase().replace(/&[a-z]+;/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    const count = counts.get(slug) || 0; counts.set(slug, count + 1);
    return { level: match[1].length, text, anchor: count ? `${slug}-${count}` : slug };
  });
  // Build-time machine paths never enter the downloadable content index.
  return { id: Buffer.from(relative).toString('base64url'), path: relative, title, section: sectionFor(relative),
    visibility: 'public', format: 'md', sourceFormat: 'md', content, modified,
    searchText: content.replace(/[#>*_`|]/g, ' ').replace(/\s+/g, ' ').toLowerCase(), headings };
}

export async function buildReader() {
  // Read the explicit public manifest for every rebuild. Adding an approved
  // lesson does not require a running server to reload this module.
  const moduleFiles = JSON.parse(await fs.readFile(path.join(readerRoot, 'module-readings.json'), 'utf8'));
  if (!Array.isArray(moduleFiles) || moduleFiles.some(file => typeof file !== 'string' || !/^modules\/[a-z0-9-]+\/(?:README|\d{2}-[a-z0-9-]+)\.md$/.test(file))) throw new Error('Invalid public module reading manifest');
  const publicFiles = [...readingFiles, ...moduleFiles, ...researchFiles];
  if (new Set(publicFiles).size !== publicFiles.length) throw new Error('Duplicate public reading path');
  const documents = [];
  for (const relative of publicFiles) {
    if (relative.split('/').some(part => part.startsWith('.')) || relative.startsWith('teaching/')) throw new Error(`Non-learner file in public reading list: ${relative}`);
    const full = path.join(projectRoot, relative);
    const content = await fs.readFile(full, 'utf8');
    if (/\u2014|&mdash;|&#8212;|&#x2014;/i.test(content)) throw new Error(`Em dash in ${relative}`);
    if (/\/Users\/|file:\/\//.test(content)) throw new Error(`Local filesystem reference in ${relative}`);
    if (/\bManu\b|Articulate AI|articulateai\.pro/i.test(content.replace(/https:\/\/github\.com\/[^\s)]+/g, ''))) throw new Error(`Personal framing in ${relative}`);
    if (/give participants|ask participants|offer participants|participants should|for executive teaching|facilitator guide|teaching output|session plans|debrief criterion|assessment rubric/i.test(content)) throw new Error(`Instructor guidance in public material: ${relative}`);
    if (/\]\([^)]*(?:\.private\/|FACILITATOR-GUIDE|WRITING-STANDARD|PUBLICATION-PLAN)/i.test(content)) throw new Error(`Private working-document link in ${relative}`);
    documents.push(makeDocument(relative, content, (await fs.stat(full)).mtime.toISOString()));
  }
  const sectionOrder = ['Start and study', ...Object.values(moduleNames), 'Organisation design research', 'Engineering references', 'Sources and further reading'];
  const priority = doc => doc.path === 'START-HERE.md' || doc.path === 'reference/literature-guide.md' ? 0 : doc.path === 'README.md' ? 1 : doc.path.endsWith('/README.md') ? 0 : 2;
  documents.sort((a, b) => sectionOrder.indexOf(a.section) - sectionOrder.indexOf(b.section) || priority(a) - priority(b) || a.path.localeCompare(b.path));
  const curriculum = JSON.parse(await fs.readFile(path.join(readerRoot, 'standalone-curriculum.json'), 'utf8'));
  const moduleGroups = [
    { title: 'Part I: AI engineering foundations', sections: curriculumData.filter(m => m.part === 1).map(m => moduleNames[m.path.split('/')[1]]) },
    { title: 'Part II: Agent engineering', sections: curriculumData.filter(m => m.part === 2).map(m => moduleNames[m.path.split('/')[1]]) },
    { title: 'Part III: Business implementation and operations', sections: curriculumData.filter(m => m.part === 3).map(m => moduleNames[m.path.split('/')[1]]) }
  ];
  const payload = { generatedAt: new Date().toISOString(), edition: 'course', curriculum,
    repoName: 'AI engineering and organisation design', documents,
    sectionOrder, moduleGroups, warnings: [] };
  await fs.mkdir(distRoot, { recursive: true });
  await fs.writeFile(path.join(distRoot, 'content-index.json.tmp'), JSON.stringify(payload));
  await fs.rename(path.join(distRoot, 'content-index.json.tmp'), path.join(distRoot, 'content-index.json'));
  for (const file of ['index.html', 'app.js', 'styles.css']) await fs.copyFile(path.join(readerRoot, 'src', file), path.join(distRoot, file));
  await fs.mkdir(path.join(distRoot, 'downloads'), { recursive: true });
  for (const file of ['foundations_lab.py', 'test_foundations.py']) {
    await fs.copyFile(path.join(projectRoot, 'examples/01-foundations', file), path.join(distRoot, 'downloads', file));
  }
  const study = JSON.parse(await fs.readFile(path.join(projectRoot, 'study-manifest.json'), 'utf8'));
  for (const lesson of study.lessons) {
    if (!/^notebooks\/[a-z0-9-]+\/\d{2}-[a-z0-9-]+\.ipynb$/.test(lesson.notebook)) throw new Error('Invalid notebook path');
    await fs.copyFile(path.join(projectRoot, lesson.notebook), path.join(distRoot, 'downloads', path.basename(lesson.notebook)));
  }
  await buildBundle(projectRoot, path.join(distRoot, "downloads/study-workspace.zip"), publicFiles, study.lessons.map(item => item.notebook));
  return { documents: documents.length, lessons: documents.filter(d => /^modules\/[^/]+\/\d{2}-/.test(d.path)).length, warnings: [] };
}

if (process.argv[1] && await fs.realpath(process.argv[1]) === await fs.realpath(fileURLToPath(import.meta.url))) console.log(await buildReader());
