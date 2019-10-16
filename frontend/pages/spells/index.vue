
<!--
  TODO: Creare SpellCard con poche info.
  TODO: ritornare info di spell dalla API
  TODO: fai i filtri ricerca
  TODO: Creare pagina singola per la spell (recipes) o che si apra una tendina

  TODO DAMI: se metto NON RANGED io non dovrei mettere la distanza
-->

<template>
  <v-container class="col-15">
    <v-container class="justify-content-between">
      <h1>Spells</h1>
    </v-container>

    <!-- FILTER AREA from CHARACTER CLASS -->
    <v-container>
      <v-col align="center" class="text-center">
          <v-col>
            <v-btn class="ma-2" v-for="characterclass in characterclasses" :key="characterclass.id" @click="filterSpells">
              {{characterclass.name}}
            </v-btn>
          </v-col>
      </v-col>
    </v-container>

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
                <v-col class="bold text-center">SCHOOL<v-col class="regular text-center">{{spell.school}}</v-col></v-col>
                <v-col class="bold text-center">ATTACK/SAVE
                  <v-col class="regular text-center" v-if="spell.spell_additional_info != null">
                    {{spell.spell_additional_info.save_type}}
                  </v-col>
                </v-col>
                <v-col class="bold text-center">DAMAGE/EFFECT<v-col class="regular text-center">{{spell['tag']}}</v-col></v-col>
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


    <v-btn class="ma-2" v-scroll="onScroll" fab right bottom fixed color="primary" @click="toTop">
      <v-icon>mdi-arrow-up</v-icon>
    </v-btn>
  </v-container>
</template>


<script>
 export default {
  head() {
    return {
      title: "Spells list"
    };
  },

  components: {

  },

  async asyncData({ $axios, params }) {
    let retval = { spells: [], characterclasses: []}
    try {
      let query_spell = await $axios.$get(`/spells/`);
      let query_characterclasses = await $axios.$get(`/characterclasses/`);

      if (query_spell.count > 0) {
          retval.spells = query_spell.results
      }
      if (query_characterclasses.count > 0) {
          retval.characterclasses = query_characterclasses.results
      }
    } catch (e) {
      console.log(e);
    }
    return retval
  },

  data() {
    return {
      spells: [],
      search: '',
      search_desc: '',
      search_lvl: '',
      characterclasses: [],
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
    },

    filterSpells () {
      return this.spells.filter((spell) => {
      if (this.search.length > 0)
        return spell.name.toLowerCase().match(this.search.toLowerCase())
      if(this.search_desc.length > 0)
        return spell.description.toLowerCase().match(this.search_desc.toLowerCase())
      if(this.search_lvl.length > 0)
        return spell.level == this.search_lvl
      else
        return this.spells
      })
    }
  },

 computed: {
  filteredSpells: function(){
    return this.filterSpells()
  }
 },

};
</script>


<style scoped>
  ul {
    list-style-type:  none;
  }
  /*
  .bold { font-weight: bold;}
  .text-center {text-align: center;}
  .regular { font-weight: normal; }
   */
</style>
