import api from '~/api'
import { setAuthToken, resetAuthToken, setAuthCookie, resetAuthCookie } from '~/utils/auth'
import cookies from 'js-cookie'

export const state = () => ({
  user: null
})

export const mutations = {
  set_user (store, data) {
    console.log('store/auth.js mutations set_user() data', data)
    store.user = data
  },
  reset_user (store) {
    console.log('store/auth.js mutations reset_user()')
    store.user = null
  }
}

export const actions = {
  fetch ({ commit }, userId) {
    console.log('store/auth.js fetch()')
    return api.auth.me(userId)
      .then(response => {
        console.log('store/auth.js fetch() .then response'/*, response */)
        commit('set_user', response.data)
        return response
      })
      .catch(error => {
        console.log('store/auth.js fetch() .catch error')
        console.log(error.response)
        commit('reset_user')
        return error
      })
  },
  login ({ commit }, data) {
    console.log('store/auth.js login() data', data)
    return api.auth.login(data)
      .then(response => {
        console.log('store/auth.js login() .then response', response)
        commit('set_user', response.data.user)
        setAuthToken(response.data.token)
        setAuthCookie(response.data.token)
        cookies.set('userId', response.data.user.id)
        // cookies.set('Authorization', response.data.token, { expires: 0 })
        return response
      })
  },
  reset ({ commit }) {
    console.log('store/auth.js reset()')
    commit('reset_user')
    resetAuthToken()
    resetAuthCookie()
    cookies.remove('userId')
    // cookies.remove('Authorization')
    return Promise.resolve()
  }
}
