import axios from 'axios'

console.log('api/index.js')

export default {
  auth: {
    me: (userId) => axios.get(`api/users/${userId}/`),
    login: (data) => axios.post('auth/', {
      username: data.email,
      password: data.password
    })
  }
}
