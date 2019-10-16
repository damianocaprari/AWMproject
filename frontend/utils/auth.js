import axios from 'axios'
import cookies from 'js-cookie'

export function setAuthToken (token) {
  console.log('utils/auth.js setAuthToken() token', token)
  axios.defaults.headers.common['Authorization'] = 'JWT '.concat(token)
}

export function resetAuthToken () {
  console.log('utils/auth.js resetAuthToken()')
  delete axios.defaults.headers.common['Authorization']
}

export function setAuthCookie (token) {
  console.log('utils/auth.js setAuthCookie() token', token)
  cookies.set('Authorization', token)
}

export function resetAuthCookie () {
  console.log('utils/auth.js resetAuthCookie()')
  cookies.remove('Authorization')
}
