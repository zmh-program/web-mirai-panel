const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 1200,
    autoHideMenuBar: true,
  });

  mainWindow.loadURL('http://localhost:5000/').then(r => 0);

  // 在窗口关闭时终止应用程序
  mainWindow.on('closed', () => {
    app.quit();
  });
}

app.whenReady().then(() => {
  const iconPath = path.join(__dirname, 'public', 'favicon.ico');
  if (process.platform === 'win32') {
    app.commandLine.appendSwitch('wm-window-ico', iconPath);
  } else {
    app.dock.setIcon(iconPath);
  }
  createWindow();

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});
