
<!--
  TODO: Creare SpellCard con poche info.
  TODO: ritornare info di spell dalla API
  TODO: fai i filtri ricerca
  TODO: Creare pagina singola per la spell (recipes) o che si apra una tendina
-->

<template>
  <div class="col-12 text-right mb-4">
    <div class="d-flex justify-content-between">
      <h1>Spells</h1>
    </div>

    <!-- SEARCH AREA -->
    <div>
      <v-row>
        <v-text-field v-model="search"      label="Search spells for name" outlined dense></v-text-field>
        <v-text-field v-model="search_desc" label="Search spells for descriptions" outlined dense></v-text-field>
        <v-text-field v-model="search_desc" label="Search spells for level" outlined dense></v-text-field>
      </v-row>
    </div>



    <div>
      <v-list v-for="condition in filteredConditions" :key="condition.id" >
          <v-list-item>
            <condition-card :onDelete="deleteCondition" :condition="condition"></condition-card>
          </v-list-item>
      </v-list>
    </div>


    <v-btn class="ma-2" v-scroll="onScroll" fab right bottom fixed color="black" @click="toTop">
      <v-icon>mdi-arrow-up</v-icon>
    </v-btn>
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
      search: '',
      search_desc: ''
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
      if(this.search_desc.length > 0)
        return condition.description.toLowerCase().match(this.search_desc.toLowerCase())
      if(this.search.length > 0)
        return condition.name.toLowerCase().match(this.search.toLowerCase())
      else
        return this.conditions
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
