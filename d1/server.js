const http = require('http');
const fs = require('fs');
const path = require('path');
const server = http.createServer((req, res) => {
  if (req.url === '/check') {
    const filePath = path.join(__dirname, 'aaa.txt');
    fs.readFile(filePath, 'utf8', (err, data) => {
      const result = (data.trim() === 'aaa') ? 'OK' : 'NG';
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ status: result }));
    });
  } else {
    const filePath = path.join(__dirname, 'index.html');
    fs.readFile(filePath, (err, data) => {
      res.writeHead(200, { 'Content-Type': 'text/html' });
      res.end(data);
    });
  }
});
server.listen(8000, () => {
  console.log('http://localhost:8000 start');
});