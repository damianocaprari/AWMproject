
<!--
  TODO: Creare SpellCard con poche info.
  TODO: ritornare info di spell dalla API
  TODO: fai i filtri ricerca
  TODO: Creare pagina singola per la spell (recipes) o che si apra una tendina

  TODO DAMI: se metto NON RANGED io non dovrei mettere la distanza
-->

<template>
  <div class="col-12 text-right mb-4">
    <div class="d-flex justify-content-between">
      <h1>Spells</h1>
    </div>

    <!-- SEARCH AREA -->
    <v-container>
      <v-row>
        <v-text-field v-model="search"      label="Search spells for name" outlined dense></v-text-field>
        <v-text-field v-model="search_desc" label="Search spells for descriptions" outlined dense></v-text-field>
        <v-text-field v-model="search_lvl" label="Search spells for level" outlined dense></v-text-field>
      </v-row>
    </v-container>


    <v-container>

      <v-row >
        <v-col>LEVEL</v-col>
        <v-col>NAME</v-col>
        <v-col>CASTING TIME</v-col>
        <v-col>DURATION</v-col>
        <v-col>RANGE/AREA</v-col>
      </v-row>

      <v-expansion-panels multiple focusable>
        <v-expansion-panel v-for="spell in filteredSpells" :key="spell.id">
          <v-expansion-panel-header>
            <v-row >
              <v-col >{{spell.level}}</v-col>
              <v-col >{{spell.name}}</v-col>
              <v-col >{{ spell.casting_time_amount }} {{ spell.casting_time_unit.toLowerCase() }}</v-col>
              <v-col >{{ spell.duration_type.toLowerCase() }}</v-col>
              <v-col v-if="spell.range_type.match('RANGED')">
                {{ spell.range_type.toLowerCase() }} ({{ spell.range_distance}} ft)
              </v-col>
              <v-col v-else>{{ spell.range_type.toLowerCase() }}</v-col>
            </v-row>
          </v-expansion-panel-header>

          <v-expansion-panel-content>
            <v-container class="grey lighten-5">
              <v-row>


                <v-col class="bold text-center">LEVEL <v-col class="regular text-center">{{spell.level}}</v-col> </v-col>
                <v-col class="bold text-center">CASTING TIME <v-col class="regular text-center">{{spell.casting_time_amount}}  {{ spell.casting_time_unit.toLowerCase() }}</v-col> </v-col>
                <v-col class="bold text-center">RANGE/AREA
                  <v-col class="regular text-center" v-if="spell.range_type.match('RANGED')">
                    {{ spell.range_type.toLowerCase() }} ({{ spell.range_distance}} ft)
                  </v-col>
                </v-col>
                <v-col class="bold text-center">COMPONTENTS
                  <v-col class="regular text-center">
                    <span v-if="spell.component_verbal == true">V</span>
                    <span v-if="spell.component_somatic == true">S </span>
                    <span v-if="spell.component_material == true">M </span>
                  </v-col>
                </v-col>
              </v-row>
              <v-row>
                <v-col class="bold text-center">DURATION<v-col class="regular text-center">{{spell.casting_time_amount}}  {{ spell.casting_time_unit.toLowerCase() }}</v-col> </v-col>
                <v-col>Column</v-col>
                <div class="w-100"></div>
                <v-col>Column</v-col>
                <v-col>Column</v-col>
              </v-row>
            </v-container>
            <v-divider></v-divider>
            <v-container>
              {{ spell.description}}
            </v-container>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-container>


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
      title: "Spells list"
    };
  },
  components: {
    ConditionCard
  },
  async asyncData({ $axios, params }) {
    try {
      let query = await $axios.$get(`/spells/`);
      if (query.count > 0){
          return { spells: query.results }
      }
      return { spells: [] };
    } catch (e) {
      return { spells: [] };
    }
  },
  data() {
    return {
      spells: [],
      search: '',
      search_desc: '',
      search_lvl: '',
    };
  },
  methods: {
    async deleteSpell(spell_id) {
        try {
            await this.$axios.$delete(`/spells/${spell_id}/`); // delete spell
            let newSpell = await this.$axios.$get("/spells/"); // get new list of cspells
            this.spells = newSpells; // update list of spells
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
  filteredSpells: function(){
    return this.spells.filter((spell) => {
      if (this.search.length > 0)
        return spell.name.toLowerCase().match(this.search.toLowerCase())
      if(this.search_desc.length > 0) {
        return spell.description.toLowerCase().match(this.search_desc.toLowerCase())
      }
      if(this.search_lvl.length > 0)
        return spell.level == this.search_lvl
      else
        return this.spells
    });
  }
 }

};
</script>


<style scoped>
  ul {
    list-style-type:  none;
  }
  .bold { font-weight: bold;}
  .text-center {text-align: center;}
  .regular { font-weight: normal; }
</style>
