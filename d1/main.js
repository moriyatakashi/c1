const a=require('electron');
a.app.whenReady().then(()=>{new a.BrowserWindow({ width:640,height:480}).loadFile('index.html');});