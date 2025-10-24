// ファイル名: basic-server.js
const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url === '/' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<h1>Hello World from pure Node.js!</h1>');
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('ページが見つかりません');
  }
});

server.listen(3000, () => {
  console.log('Node.jsサーバーが http://localhost:3000 で起動しました');
});