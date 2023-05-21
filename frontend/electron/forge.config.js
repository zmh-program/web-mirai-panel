module.exports = {
  packagerConfig: {},
  icon: '../public/icon.ico',
  makers: [{
    name: '@electron-forge/maker-squirrel',
    platforms: ['win32'],
  }],
}
