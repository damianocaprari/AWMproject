export default function ({ $axios, redirect }) {
  //console.log('plugins/axios.js')
  $axios.defaults.headers.common['Accept'] = 'application/json'
}
