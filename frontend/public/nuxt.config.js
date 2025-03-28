
export default {
  ssr: true,
  head: {
    title: 'HikeHub - Публичный сайт',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' }
    ]
  },
  server: {
    host: '0.0.0.0', // позволяет принимать соединения извне
    port: 3000
  },
  modules: [
    '@nuxtjs/axios',
    'nuxt-buefy'
  ],
  axios: {
    baseURL: process.env.API_BASE_URL || 'http://localhost'
  },
  plugins: [
    '~/plugins/vee-validate.js'
  ],
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
    }
  }
}
