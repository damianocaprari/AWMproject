<template>
  <v-container fill-height>
    <v-row justify="center" align="center">
      <v-col cols="12" sm="9" md="6" lg="4">
        <v-card class="elevation-10">
          <v-card-title class="headline primary onprimary--text">Sign In</v-card-title>
          <v-card-text>
            <v-form @submit.prevent="submit">
              <v-alert v-if="alert" :type="alert.type">{{ alert.message }}</v-alert>
              <v-text-field label="Username" v-model="username"/>
              <v-text-field label="Password" v-model="password" type="password"/>
              <v-row justify="center">
                <v-col class="text-center">
                  <v-btn type="submit" :loading="loading" :disabled="loading" class="accent onaccent--text">Sign In</v-btn>
                </v-col>
                <v-col class="text-center">
                  <v-btn text to="/account/register" class="accent--text">Register</v-btn>
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
    layout: 'fullscreen',
    data () {
      return {
        username: '',
        password: '',
        alert: null,
        loading: false
      }
    },
    methods: {
      submit () {
        this.alert = null
        this.loading = true
        this.$store.dispatch('auth/login', {
          username: this.username,
          password: this.password
        }).then(result => {
          //console.log('login.vue .then() result', result)
          this.alert = { type: 'success', message: result.message || 'Success' }
          this.loading = false
          this.$router.push(`/account`)
        }).catch(error => {
          console.log('login.vue .catch() error.response', error)
          this.loading = false
          if (error.response && error.response.data) {
            this.alert = {
              type: 'error',
              message: error.response.data.non_field_errors[0] || 'Error'
            }
          }
        })
      }
    }
  }
</script>

<style scoped>
</style>
