const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
  const stream = fs.createReadStream('index.html');
  stream.pipe(res);
});

server.listen(3000, () => {
  console.log('Server is running at http://localhost:3000');
});