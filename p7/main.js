const { app, BrowserWindow } = require('electron');

app.whenReady().then(() => {
  const win = new BrowserWindow({
    width: 640,
    height: 480,
    resizable: false,
  });
  win.loadFile('index.html'); // 空でもOK
});
