const http = require('http');
const fs = require('fs');
const path = require('path');
function handleRequest(req, res) {
  const filePath = getFilePath(req.url);
  readFile(filePath, res);
}
function getFilePath(url) {
  return path.join(process.cwd(), url === '/' ? 'index.html' : url);
}
function readFile(filePath, res) {
  fs.readFile(filePath, function (_, data) {
    res.end(data);
  });
}
function startServer() {
  const server = http.createServer(handleRequest);
  server.listen(3000);
}
startServer();
