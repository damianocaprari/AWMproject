<template>
  <v-list-item>
    <v-list-item-content>
      <v-container fluid>
        <v-row dense>
          <template v-if="isLoggedIn">
            <v-col cols="6">
              <v-btn
                text
                color="onprimary"
                @click="logOut"
              >
                Sign Out
              </v-btn>
            </v-col>
            <v-col cols="6">
              <v-btn
                outlined
                color="onprimary"
                to="/account"
              >
                Profile
              </v-btn>
            </v-col>
          </template>

          <template v-else>
            <v-col cols="6">
              <v-btn
                text
                color="onprimary"
                to="/account/login"
              >
                Sign In
              </v-btn>
            </v-col>
            <v-col cols="6">
              <v-btn
                outlined
                color="onprimary"
                to="/account/register">
                Register
              </v-btn>
            </v-col>
          </template>

        </v-row>
      </v-container>
    </v-list-item-content>
  </v-list-item>
</template>

<script>
export default {
  name: "HeaderAccount",
  props: [ "isLoggedIn", ],
  methods: {
    logOut () {
      this.$store.dispatch('auth/reset').then(() => {
        this.$router.push('/')
      })
    }
  }
}
</script>

<style scoped>
  .v-btn:before {
    background-color: unset;
  }
</style>
