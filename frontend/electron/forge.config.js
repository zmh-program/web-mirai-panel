module.exports = {
  packagerConfig: {},
  icon: '../public/icon.ico',
  makers: [{
    name: '@electron-forge/maker-squirrel',
    platforms: ['win32'],
  }],
  publishers: [
    {
      name: '@electron-forge/publisher-github',
      config: {
        repository: {
          owner: 'zmh-program',
          name: 'web-chatgpt-qq-bot',
        },
        prerelease: false,
        draft: false,
      },
    },
  ],
}
