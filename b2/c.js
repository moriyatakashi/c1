const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

// 静的ファイルを公開する
app.use(express.static(__dirname));

app.listen(port, () => {
  console.log(`Expressサーバーが http://localhost:${port} で起動しました`);
});