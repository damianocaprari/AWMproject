<template>
  <v-container fluid class="primary onprimary--text pa-0 pt-1" v-if="!dense">
    <v-row justify="center">
      <v-col align="center" v-for="link in links" :key="link.href" cols="3" sm="2">
        <a :href="link.href">
          <v-btn small color="white" text>
            <span style="white-space: normal;">{{ link.text }}</span>
          </v-btn>
        </a>
      </v-col>
    </v-row>
    <v-row justify="center" class="grey darken-1 onprimary--text">
      <v-col align="center">
        {{ new Date().getFullYear() }} - AWMproject
      </v-col>
    </v-row>
  </v-container>

  <v-container fluid class="primary onprimary--text pa-0 pt-1" v-else="!dense">
    <v-row justify="center" no-gutters>
      <v-col align="center" v-for="link in links" :key="link.href" cols="3" sm="2">
        <a :href="link.href">
          <v-btn small color="white" text>
            <span style="white-space: normal;">{{ link.text }}</span>
          </v-btn>
        </a>
      </v-col>
    </v-row>
    <v-row justify="center" no-gutters class="grey darken-1 onprimary--text">
      <v-col align="center">
        {{ new Date().getFullYear() }} - AWMproject
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
    export default {
        props: ['dense',],
        data () {
            return {
                links: [
                    { href: 'https://github.com/damianocaprari/AWMproject', text: 'GITHUB', },
                    { href: 'https://github.com/damianocaprari', text: 'Caprari', },
                    { href: 'https://github.com/matteopulega', text: 'Pulega', },
                ]
            }
        }
    }
</script>

<style scoped>

</style>
