import http from 'node:http';
import { promises as fs } from 'node:fs';
import path from 'node:path';
import { networkInterfaces } from 'node:os';
import { buildReader, distRoot } from './build.mjs';

const host = process.env.READER_HOST || '0.0.0.0';
const port = Number(process.env.READER_PORT || 4186);
let pendingBuild;
function refresh() {
  if (!pendingBuild) pendingBuild = buildReader().finally(() => { pendingBuild = null; });
  return pendingBuild;
}
console.log(await refresh());
const allowed = new Map([
  ['/', ['index.html', 'text/html; charset=utf-8']],
  ['/index.html', ['index.html', 'text/html; charset=utf-8']],
  ['/app.js', ['app.js', 'text/javascript; charset=utf-8']],
  ['/styles.css', ['styles.css', 'text/css; charset=utf-8']],
  ['/content-index.json', ['content-index.json', 'application/json; charset=utf-8']]
]);
const server = http.createServer(async (request, response) => {
  try {
    const url = new URL(request.url, `http://${host}:${port}`);
    if (url.pathname === '/health') {
      response.writeHead(200, { 'Content-Type': 'application/json' });
      response.end(JSON.stringify({ project: 'ai-engineering-learning-reader' })); return;
    }
    const entry = allowed.get(url.pathname);
    if (!entry || !['GET', 'HEAD'].includes(request.method)) { response.writeHead(404); response.end('Not found'); return; }
    if (url.pathname === '/content-index.json') await refresh();
    const body = await fs.readFile(path.join(distRoot, entry[0]));
    response.writeHead(200, { 'Content-Type': entry[1], 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff',
      'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'" });
    response.end(request.method === 'HEAD' ? undefined : body);
  } catch (error) { console.error(error.message); response.writeHead(500); response.end('Reader refresh failed. Check the server terminal.'); }
});
server.on('error', error => { console.error(error.code === 'EADDRINUSE' ? `Port ${port} is already in use. Check http://${host}:${port} or set READER_PORT.` : error.message); process.exit(1); });
server.listen(port, host, () => {
  console.log(`Learning Reader: http://127.0.0.1:${port}`);
  if (host === '0.0.0.0') {
    const addresses = new Set(Object.values(networkInterfaces()).flat().filter(address => address && address.family === 'IPv4' && !address.internal).map(address => address.address));
    for (const address of addresses) console.log(`Network reader: http://${address}:${port}`);
  } else if (host !== '127.0.0.1') console.log(`Network reader: http://${host}:${port}`);
  console.log('Keep this terminal running. Ctrl+C stops the reader.');
});
