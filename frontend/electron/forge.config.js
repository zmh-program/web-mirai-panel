module.exports = {
  packagerConfig: {},
  icon: '../public/favicon.ico',
  makers: [{
    name: '@electron-forge/maker-squirrel',
    platforms: ['win32'],
  }],
  publishers: [
    {
      tagPrefix: "",
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
