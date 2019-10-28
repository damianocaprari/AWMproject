<template>
  <v-app>
    <v-content class="bg-img">
      <nuxt/>
    </v-content>
  </v-app>
</template>

<script>
  export default {
    beforeCreate() {
      if (process.client)
        document
        .getElementsByTagName('html')[0]
        .setAttribute('style', 'overflow-y: hidden;')
    }
  }
</script>

<style>
  .bg-img {
      min-height: 100vh;
      background-image: linear-gradient(
        to right,
        rgba(0, 0, 0, 0.9),
        rgba(0, 0, 0, 0.4)
      ),
      url("/images/dndWallpaper.jpg");
      background-position: right;
      background-size: cover;
      position: relative;
  }
</style>
