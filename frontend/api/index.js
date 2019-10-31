export default {
  auth: {
    me: ($axios, userId) => $axios.$get(`users/${userId}/`),
    login: ($axios, data) => $axios.$post('auth/', {
      username: data.username,
      password: data.password
    }),
    register: ($axios, data) => $axios.$post('users/', {
      username: data.username,
      password: data.password,
      email: data.email,
      first_name: data.first_name,
      last_name: data.last_name
    })
  },
  updateUserProfile: ($axios, userId, data) => $axios.$put(`users/${userId}/`, {
    email: data.email,
    first_name: data.first_name,
    last_name: data.last_name
  })
}
