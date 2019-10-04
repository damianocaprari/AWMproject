<template>
  <div class="col-12 text-right mb-4">
    <div class="d-flex justify-content-between">
      <h1 class="text-white">Conditions</h1>
    </div>

    <div class="text-right">
      <p><nuxt-link to="/"> <v-btn >Back</v-btn> </nuxt-link></p>
    </div>

    <div>
      <li v-for="condition in conditions" :key="condition.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <condition-card :onDelete="deleteCondition" :condition="condition"></condition-card>
      </li>
    </div>
  </div>
</template>


<script>
    import ConditionCard from "~/components/ConditionCard.vue";

 export default {
  head() {
    return {
      title: "Conditions list"
    };
  },
  components: {
    ConditionCard
  },
  async asyncData({ $axios, params }) {
    try {
      let query = await $axios.$get(`/conditions/`);
      if (query.count > 0){
          return { conditions: query.results }
      }
      return { conditions: [] };
    } catch (e) {
      return { conditions: [] };
    }
  },
  data() {
    return {
      conditions: []
    };
  },
  methods: {
    async deleteCondition(condition_id) {
      try {
        await this.$axios.$delete(`/conditions/${condition_id}/`); // delete condition
        let newCondition = await this.$axios.$get("/conditions/"); // get new list of conditions
        this.conditions = newConditions; // update list of conditions
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style scoped>

</style>
