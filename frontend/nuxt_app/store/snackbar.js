export const state = () => ({
    content: '',
    color: ''
  })
  
  export const mutations = {
    showSnackbar (state, payload) {
      state.content = payload.content
      state.color = payload.color
    }
  }