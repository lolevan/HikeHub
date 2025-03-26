export const state = () => ({
  auth: {
    loggedIn: false,
    token: null
  }
})

export const mutations = {
  setAuth(state, payload) {
    state.auth = payload
  }
}

export const actions = {
  async login({ commit }, credentials) {
    try {
      const data = await this.$axios.$post('/api/v1/private/users/login/', credentials)
      commit('setAuth', { loggedIn: true, token: data.access })
      // Сохраним токен в заголовках axios, чтобы он отправлялся
      this.$axios.setToken(data.access, 'Bearer')
    } catch (err) {
      throw err
    }
  },
  logout({ commit }) {
    commit('setAuth', { loggedIn: false, token: null })
    this.$axios.setToken(false)
  }
}
