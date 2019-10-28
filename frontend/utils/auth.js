import cookies from 'js-cookie'

export function setAuthToken ($axios, token) {
  let JWTtoken = 'JWT '.concat(token)
  //console.log('utils/auth.js setAuthToken() token', JWTtoken)
  $axios.defaults.headers.common['Authorization'] = JWTtoken
}

export function resetAuthToken ($axios) {
  //console.log('utils/auth.js resetAuthToken()')
  delete $axios.defaults.headers.common['Authorization']
}

export function setAuthCookie (token) {
  //console.log('utils/auth.js setAuthCookie() token', token)
  cookies.set('Authorization', token)
}

export function resetAuthCookie () {
  //console.log('utils/auth.js resetAuthCookie()')
  cookies.remove('Authorization')
}
