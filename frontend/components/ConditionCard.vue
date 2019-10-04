<template>
  <v-card max-width="344" class="mx-auto condition-card">
    <v-card-title>{{ condition.name }}</v-card-title>
    <v-card-text>{{ condition.description }}</v-card-text>
    <div class="action-buttons">
        <nuxt-link :to="`/conditions/${condition.id}/`" class="btn btn-sm btn-success"> View </nuxt-link>
        <nuxt-link :to="`/conditions/${condition.id}/edit/`" class="btn btn-sm btn-primary"> Edit </nuxt-link>
        <button @click="onDelete(condition.id)"  class="btn btn-sm btn-danger">Delete</button>
      </div>
  </v-card>
</template>

<script>
  export default {
      props: ["condition", "onDelete"]
  }
</script>


<style>
  .condition-card {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
  }
</style>
