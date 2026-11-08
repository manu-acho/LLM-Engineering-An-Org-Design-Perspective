// Build a portable study ZIP from an explicit allowlist using Node built-ins.
import { promises as fs } from 'node:fs';
import path from 'node:path';
import { deflateRawSync } from 'node:zlib';
const table = Array.from({length: 256}, (_, value) => {
  for (let bit=0; bit<8; bit++) value = value & 1 ? 0xedb88320 ^ (value >>> 1) : value >>> 1;
  return value >>> 0;
});
function crc32(data) {
  let crc = 0xffffffff;
  for (const byte of data) crc = table[(crc ^ byte) & 255] ^ (crc >>> 8);
  return (crc ^ 0xffffffff) >>> 0;
}
export async function buildBundle(root, destination, readings, notebooks) {
  const files = new Set([...readings, ...notebooks, 'README.md', 'STUDY-WORKSPACE.md', 'DEVELOPMENT.md',
    'references/references.bib', 'references/catalog.json', 'BROWSER-READER.md', 'netlify.toml', 'browser-reader/module-readings.json', 'browser-reader/standalone-curriculum.json', 'pyproject.toml', 'uv.lock', '.python-version', '.env.example', '.gitignore',
    '.vscode/settings.json', '.vscode/extensions.json', 'study-manifest.json']);
  async function collect(relative) {
    for (const entry of await fs.readdir(path.join(root, relative), {withFileTypes: true})) {
      if (entry.name.startsWith('.') || entry.name === '__pycache__') continue;
      const file = path.posix.join(relative, entry.name);
      if (entry.isSymbolicLink()) throw new Error('Symlink refused in study bundle');
      if (entry.isDirectory()) await collect(file);
      else if (/\.(py|md|ipynb|mjs|js|json|css|html)$/.test(entry.name)) files.add(file);
    }
  }
  for (const directory of ['src/ai_orgdesign', 'examples/01-foundations', 'scripts', 'tests', 'templates', 'browser-reader/src', 'browser-reader/scripts']) await collect(directory);
  const local = [], central = [];
  let offset = 0;
  for (const file of [...files].sort()) {
    if (file.includes('..') || file === '.env' || file.startsWith('.private/') || file.startsWith('.venv/')) throw new Error('Private bundle path refused');
    const name = Buffer.from(file);
    const data = await fs.readFile(path.join(root, file));
    const compressed = deflateRawSync(data);
    const crc = crc32(data);
    const header = Buffer.alloc(30);
    header.writeUInt32LE(0x04034b50); header.writeUInt16LE(20, 4); header.writeUInt16LE(0x800, 6);
    header.writeUInt16LE(8, 8); header.writeUInt16LE(0x21, 12); header.writeUInt32LE(crc, 14);
    header.writeUInt32LE(compressed.length, 18); header.writeUInt32LE(data.length, 22); header.writeUInt16LE(name.length, 26);
    local.push(header, name, compressed);
    const item = Buffer.alloc(46);
    item.writeUInt32LE(0x02014b50); item.writeUInt16LE(20, 4); item.writeUInt16LE(20, 6); item.writeUInt16LE(0x800, 8);
    item.writeUInt16LE(8, 10); item.writeUInt16LE(0x21, 14); item.writeUInt32LE(crc, 16);
    item.writeUInt32LE(compressed.length, 20); item.writeUInt32LE(data.length, 24); item.writeUInt16LE(name.length, 28);
    item.writeUInt32LE(offset, 42); central.push(item, name);
    offset += header.length + name.length + compressed.length;
  }
  const directory = Buffer.concat(central);
  const end = Buffer.alloc(22); end.writeUInt32LE(0x06054b50);
  end.writeUInt16LE(files.size, 8); end.writeUInt16LE(files.size, 10);
  end.writeUInt32LE(directory.length, 12); end.writeUInt32LE(offset, 16);
  await fs.writeFile(destination, Buffer.concat([...local, directory, end]));
}
