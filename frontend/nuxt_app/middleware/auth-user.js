export default async function ({ app, redirect }) {
    // https://github.com/nuxt-community/auth-module/issues/478
    // the following look directly for the cookie created by nuxtjs/auth
    // instead of using $auth.loggedIn
    const user = await app.$cookies.get('auth._token.local')
    if (user) {
      // let the user see the page
    } else {
      // redirect to login page
      redirect('/login')
    }
  }