export const state = () => ({
  selectedParlament: []
})

export const getters = {
    getSelectedParlament(state) {
        return state.selectedParlament;
    }
}

export const mutations = {
    // mutations mutate the state
    setSelectedParlament(state, payload) {
        state.selectedParlament = payload;
    }
}

export const actions = {
    // through actions we commit mutations
    setSelectedParlament({commit}, parlament) {
        commit('setSelectedParlament', parlament)
    }
    
}