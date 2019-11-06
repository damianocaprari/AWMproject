<template>
  <v-container fill-height>
    <v-row justify="center" align="center">
      <v-col cols="12" sm="9" md="6" lg="4">
        <v-card class="elevation-10">
          <v-card-title class="headline primary onprimary--text">Register</v-card-title>
          <v-card-text>
            <v-form @submit.prevent="submit">
              <v-alert v-if="alert" :type="alert.type">{{ alert.message }}</v-alert>
              <v-text-field label="Username" v-model="username" :rules="usernameRules"/>
              <v-text-field label="Password" v-model="password" type="password" :rules="passwordRules"/>
              <v-text-field label="Email" v-model="email" :rules="emailRules"/>
              <v-text-field label="FirstName" v-model="first_name"/>
              <v-text-field label="LastName" v-model="last_name"/>
              <v-row justify="center">
                <v-col class="text-center">
                  <v-btn type="submit" :loading="loading" :disabled="loading" class="accent onaccent--text">Register</v-btn>
                </v-col>
                <v-col class="text-center">
                  <v-btn text to="/account/login" class="secondary--text">Sign In</v-btn>
                </v-col>
              </v-row>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    head(){
      return {
        title: `AWM Project - Register`
      };
    },
    layout: 'fullscreen',
    data () {
      return {
        username: '',
        usernameRules: [
          v => !!v || 'Username is required',
          v => (v && v.length <= 25) || 'Username must be less than 25 characters',
          v => /^[a-zA-Z0-9@.+_-]+$/.test(v) || 'Username can contain letters, digits and @.+-_ only'
        ],
        password: '',
        passwordRules: [
          v => !!v || 'Password is required',
          v => (v && v.length >= 8) || 'Password must be at least 8 characters',
        ],
        email: '',
        emailRules: [
          v => /.+@.+\..+/.test(v) || 'Email must be valid',
        ],
        first_name: '',
        last_name: '',
        alert: null,
        loading: false
      }
    },
    methods: {
      submit () {
        this.alert = null
        this.loading = true
        this.$store.dispatch('auth/register', {
          username: this.username,
          password: this.password,
          email: this.email,
          first_name: this.first_name,
          last_name: this.last_name
        }).then(result => {
          //console.log('/account/register.vue .then() result', result)
          this.alert = { type: 'success', message: result.message || 'Success' }
          this.loading = false
          this.$router.push(`/account`)
        }).catch(error => {
          console.log('/account/register.vue .catch() error', error)
          console.log('/account/register.vue .catch() error.response', error.response)
          this.loading = false
          if (error.response && error.response.data) {
            this.alert = {
              type: 'error',
              message: error.response.data.username[0] || error.response.data.password[0] || 'Error'
            }
          }
        })
      }
    }
  }
</script>

<style scoped>

</style>
