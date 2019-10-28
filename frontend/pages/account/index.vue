<template>
  <v-container fluid>
    <v-row wrap>
      <v-col>
        <v-card
          max-width="768"
          class="mx-auto"
        >
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">{{ user.username }}</v-list-item-title>
              <v-list-item-subtitle>Created: {{ parseDate(user.date_joined) }}</v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-avatar
              tile
              size="100"
              color="grey"
            >
              <v-img :src="user.profile.avatar || ''"></v-img>
            </v-list-item-avatar>
          </v-list-item>

          <v-card-text>
            Email: {{ user.email || "..." }}<br>
            First name: {{ user.first_name || "..."  }}<br>
            Last name: {{ user.last_name || "..."  }}<br>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    async asyncData(context) {
      try {
        let userId = context.store.state.auth.user.id
        let user = await context.$axios.$get(`/users/${userId}`);
        if (user != undefined){
          //console.log("/account/index asyncData() user", user)
          return {
            user: user,
          }
        }
      } catch (e) {
        context.redirect('/account/login')
      }
    },
    data: () => ({
      lorem: `Lorem ipsum dolor sit amet, mel at clita quando. Te sit oratio vituperatoribus, ..`,
      user: {},
    }),
    methods: {
        parseDate(dateTimeString) {
        try {
            let date = new Date(dateTimeString)
            return `${date.getDate()}-${date.getMonth() + 1}-${date.getFullYear()}`
        }
        catch (e1) {
          try {
            let date = dateTimeString.split("T")[0]
            let dateparams = date.split("-")
            return `${dateparams[2]}-${dateparams[1]}-${dateparams[0]}`
          }
          catch (e2) {
            return ""
          }
        }
      }
    },
  }
</script>

<style scoped>

</style>
