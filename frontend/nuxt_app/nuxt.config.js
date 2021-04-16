import colors from 'vuetify/es5/util/colors'

export default {
  // disable ssr
  ssr: false,
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    titleTemplate: '%s - polity',
    title: 'polity',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  
  loading: { 
    color: '#005bad', height: '5px',throttle: 0 
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
  ],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
    '~/plugins/notifier.js',
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
  ],
  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    'cookie-universal-nuxt', // for redirect fix
    'nuxt-leaflet',
  ],
  axios: {
    baseURL: 'http://0.0.0.0:8000/api/v1/', // dev
    //baseURL_ 'https://dev.polity.ch/api/v1/', !!
    //baseURL: 'http://0.0.0.0/api/v1/', // prod -> don't forget to change
    credentials: false, // this says that in the request the httponly cookie should be sent
  },
  auth: {
    strategies: {
      local: {
        scheme: 'refresh',
        token: {
          property: 'access_token',
          maxAge: 10,
          type: 'Bearer'
        },
        refreshToken: {
          property: 'refresh_token',
          data: 'refresh',
          maxAge: 60 * 60 * 24 * 30// one day
        },
        cookie: {
          prefix: 'auth.', // Default token prefix used in building a key for token storage in the browser's localStorage.
          options: {
              path: '/', // Path where the cookie is visible. Default is '/'.
              expires: 5 // Can be used to specify cookie lifetime in Number of days or specific Date. Default is session only.
                  // domain: '', // Domain (and by extension subdomain/s) where the cookie is visible. Default is domain and all subdomains.
                  // secure: false, // Sets whether the cookie requires a secure protocol (https). Default is false, should be set to true if possible.
          }
        },
        watchLoggedIn: false,
        user: {
          property: false,
         // autoFetch: true
        },
        endpoints: {
          login: { url: '/auth/login/', method: 'post' },
          refresh: { url: 'auth/token/refresh/', method: 'post' },
          logout: { url: '/auth/logout/', method: 'post' },
          user: { url: '/auth/user/', method: 'get' },

        },
      }
    },
    redirect: {
      login: '/login',
      logout: '/',
      home: '/start'
    }
  },
  
  // Vuetify module configuration (https://go.nuxtjs.dev/config-vuetify)
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      light: true,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        },
        light: {
          primary: '#005bad',
          secondary: '#424242',
          accent: '#82B1FF',
          error: '#FF5252',
          info: '#2196F3',
          success: '#4CAF50',
          warning: '#FFC107',
        }
      }
    }
  },

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {

  },
}
