<template>
  <v-card class="condition-card ">
    <v-card-title>{{ condition.name }}</v-card-title>
    <v-card-text>{{ condition.description }}</v-card-text>
  </v-card>
</template>


<script>
  export default {
      props: ["condition", "onDelete"]
  }
</script>


<style>
  .condition-card {
    width: 100%;
  }
</style>
