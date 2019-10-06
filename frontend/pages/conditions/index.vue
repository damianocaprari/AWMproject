<template>
  <div class="col-12 text-right mb-4">
    <div class="d-flex justify-content-between">
      <h1 class="text-white">Conditions</h1>
    </div>

    <div>
      <!--
      <input type="text" v-model="search" placeholder="search conditions"/>
      -->
      <v-text-field v-model="search" label="Search conditions" outlined dense></v-text-field>
    </div>

    <div>
      <v-list v-for="condition in filteredConditions" :key="condition.id" >
          <v-list-item>
            <condition-card :onDelete="deleteCondition" :condition="condition"></condition-card>
          </v-list-item>
      </v-list>
    </div>

    <v-btn class="ma-2" v-scroll="onScroll" absolute right fab bottom fixed color="black" @click="toTop">
      <v-icon>mdi-arrow-up</v-icon>
    </v-btn>
    <!--
    <v-btn v-scroll="onScroll" v-show="fab" fab dark fixed bottom right color="primary"
            @click="toTop">
          <v-icon>keyboard_arrow_up</v-icon>
    </v-btn>
    -->
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
      conditions: [],
      search: ''
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
    },
    onScroll (e) {
      if (typeof window === 'undefined')
          return
      const top = window.pageYOffset ||   e.target.scrollTop || 0
      this.fab = top > 20
    },
    toTop () {
      this.$vuetify.goTo(0)
    }
  },

 computed: {
  filteredConditions: function(){
    return this.conditions.filter((condition) => {
      return condition.name.toLowerCase().match(this.search.toLowerCase())
    });
  }
 }

};
</script>


<style scoped>
  ul {
    list-style-type:  none;
  }

</style>
