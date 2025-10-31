function a(b,c){require('fs').createReadStream('index.html').pipe(c)}
require('http').createServer(a).listen(3000,()=>{})
