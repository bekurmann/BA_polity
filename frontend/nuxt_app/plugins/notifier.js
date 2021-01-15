// registrered as plugin in nuxt.config.js
// -> global Snackbar; 
// -> see: https://dev.to/stephannv/how-to-create-a-global-snackbar-using-nuxt-vuetify-and-vuex-1bda

export default ({ app, store }, inject) => {
    inject('notifier', {
      showSnackbar ({ content = '', color = '' }) {
        store.commit('snackbar/showSnackbar', { content, color })
      }
    })
  }