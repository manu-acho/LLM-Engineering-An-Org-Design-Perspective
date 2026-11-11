import { promises as fs } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
export const readerRoot = path.resolve(here, '..');
export const projectRoot = path.resolve(readerRoot, '..');
export const distRoot = path.join(readerRoot, 'dist');
const moduleNames = {
  '01-foundations': '01 · Foundations', '02-conversation': '02 · Conversation and tools',
  '03-open-models': '03 · Open models', '04-evaluation': '04 · Evaluation',
  '05-rag': '05 · Knowledge and RAG', '06-data': '06 · Data and baselines',
  '07-specialisation': '07 · Specialisation', '08-agents': '08 · Agents and operations',
  '09-agent-loops': '09 · Agent loops', '10-agent-orchestration': '10 · Agent orchestration',
  '11-agent-teams': '11 · Agent teams', '12-stateful-agents': '12 · Stateful agents',
  '13-agent-frameworks': '13 · Frameworks and interoperability', '14-agent-integration': '14 · MCP and business integration'
};
// An explicit reading list prevents authoring records or future working files
// from appearing on the site just because they are Markdown.
const readingFiles = [
  'README.md', 'START-HERE.md', 'HARBOUR.md', 'WORKBOOK.md', 'AGENT-ENGINEERING.md', 'SOURCE-MAP.md',
  'notebooks/README.md', 'reference/further-learning.md', 'reference/research-study-pathways.md', 'reference/bibliography.md',
  'reference/glossary.md', 'reference/python-patterns.md', 'reference/literature-guide.md', 'reference/agents-source-guide.md',
  'modules/01-foundations-and-pipelines.md', 'modules/02-conversation-and-tools.md',
  'modules/03-open-models-and-inference.md', 'modules/04-evaluation-and-code-generation.md',
  'modules/05-knowledge-and-rag.md', 'modules/06-data-baselines-and-adaptation.md',
  'modules/07-fine-tuning-and-qlora.md', 'modules/08-agents-and-operations.md',
  'reference/local-labs.md'
];
const researchFiles = [
  'reference/research/01-organisation-design.md', 'reference/research/02-coordination.md',
  'reference/research/03-decisions.md', 'reference/research/04-implementation.md',
  'reference/research/05-routines.md', 'reference/research/06-technology-in-practice.md',
  'reference/research/07-infrastructure-and-standards.md',
  'reference/research/08-governance-and-accountability.md', 'reference/research/09-process-architecture.md'
];

export const downloads = Object.fromEntries([
  ...Object.keys(moduleNames).map(name => [`notebooks/${name}.ipynb`, 'application/x-ipynb+json; charset=utf-8']),
  ['references/references.bib', 'text/plain; charset=utf-8']
].map(([source, type]) => [source, { url: `/downloads/${path.basename(source)}`, type }]));

function sectionFor(relative) {
  if (['reference/literature-guide.md', 'reference/research-study-pathways.md', 'reference/bibliography.md'].includes(relative) || researchFiles.includes(relative)) return 'Organisation design research';
  if (['README.md', 'START-HERE.md', 'HARBOUR.md', 'WORKBOOK.md', 'AGENT-ENGINEERING.md', 'notebooks/README.md'].includes(relative)) return 'Start and study';
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
  const moduleGroups = [
    { title: 'Part I: AI engineering foundations', sections: Object.values(moduleNames).slice(0, 8) },
    { title: 'Part II: Agent engineering and business integration', sections: Object.values(moduleNames).slice(8) }
  ];
  const payload = { generatedAt: new Date().toISOString(), repoName: 'AI engineering and organisation design', documents, sectionOrder, moduleGroups, downloads, warnings: [] };
  await fs.mkdir(path.join(distRoot, 'downloads'), { recursive: true });
  for (const [source, { url }] of Object.entries(downloads)) {
    await fs.copyFile(path.join(projectRoot, source), path.join(distRoot, url.slice(1)));
  }
  await fs.mkdir(distRoot, { recursive: true });
  await fs.writeFile(path.join(distRoot, 'content-index.json.tmp'), JSON.stringify(payload));
  await fs.rename(path.join(distRoot, 'content-index.json.tmp'), path.join(distRoot, 'content-index.json'));
  for (const file of ['index.html', 'app.js', 'styles.css']) await fs.copyFile(path.join(readerRoot, 'src', file), path.join(distRoot, file));
  return { documents: documents.length, lessons: documents.filter(d => /^modules\/[^/]+\/\d{2}-/.test(d.path)).length, downloads: Object.keys(downloads).length, warnings: [] };
}

if (process.argv[1] && await fs.realpath(process.argv[1]) === await fs.realpath(fileURLToPath(import.meta.url))) console.log(await buildReader());
