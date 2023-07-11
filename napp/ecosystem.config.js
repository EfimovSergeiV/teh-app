module.exports = {
    apps: [
      {
        name: 'fileserv',
        port: '4000',
        exec_mode: 'cluster',
        instances: 1, // 'max' Or a number of instances
        script: './node_modules/nuxt/bin/nuxt.js',
        args: 'start'
      }
    ]
  }