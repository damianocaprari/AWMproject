import cookie from 'cookie'
import { setAuthToken, resetAuthToken } from '~/utils/auth'

export const actions = {
  nuxtServerInit ({ dispatch }, context) {
    return new Promise((resolve, reject) => {
      console.log('store/index.js nuxtServerInit()')
      const cookies = cookie.parse(context.req.headers.cookie || '')
      console.log('cookies.hasOwnProperty(Authorization): ', cookies.hasOwnProperty('Authorization'))
      console.log(cookies)
      if (cookies.hasOwnProperty('Authorization') &&
      cookies.hasOwnProperty('userId')) {
        setAuthToken(cookies['Authorization'])
        dispatch('auth/fetch', cookies['userId'])
          .then(result => {
            resolve(true)
          })
          .catch(error => {
            console.log('Provided token is invalid:', error.response)
            resetAuthToken()
            resolve(false)
          })
      } else {
        resetAuthToken()
        resolve(false)
      }
    })
  }
}
