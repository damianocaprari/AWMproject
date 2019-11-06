<template>
  <!-- TRY FILTERBY --
  https://front.id/en/articles/vuetify-achieve-multiple-filtering-data-table-component
  -->
  <v-data-table
    :headers="headers"
    :items="spells"
    :items-per-page="5"
    :expanded.sync="expanded"
    item-key="name"
    show-expand
    class="elevation-1"
    @click:row="expandRow"
  >

    <template v-slot:top>
      <!-- v-container, v-col and v-row are just for decoration purposes. -->
      <v-container fluid>
        <v-row>
          <!-- Filter for spell name -->
          <v-col cols="12" md="3">
            <v-row class="pa-3">
              <v-text-field
                v-model="spellFilterValue"
                type="text"
                label="Name"
              ></v-text-field>
            </v-row>
          </v-col>

          <!-- Filter for levels -->
          <v-col cols="12" md="3">
            <v-row class="pa-3">
              <v-select
                :items="levelsList"
                v-model="levelsFilterValue"
                label="Levels"
              ></v-select>
            </v-row>
          </v-col>

          <!-- Filter for tags -->
          <v-col cols="12" md="3">
            <v-row class="pa-3">
              <v-select
                :items="spelltags"
                v-model="spelltagsFilterValue"
                label="Spell tags"
              ></v-select>
            </v-row>
          </v-col>

          <!-- SEARCH FOR CLASSES con lista spuntata-->
          <v-col cols="12" md="3">
            <v-row class="pa-3">
              <v-select
                :items="characterclasses"
                v-model="characterclassesFilterValue"
                label="Character classes"
              ></v-select>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </template>

    <template v-slot:item.name="{ item }">
      <n-link :to="`/spells/${item.id}`">{{ item.name }}</n-link>&nbsp;<span class="mdi mdi-open-in-new"></span>
    </template>

    <!-- expand item -->
    <template v-slot:expanded-item="{ headers, item }">
      <td :colspan="headers.length">
        <v-row>
          <v-col class="bold text-center">LEVEL
            <v-col class="regular text-center">{{item.level}}</v-col>
          </v-col>
          <v-col class="bold text-center">CASTING TIME
            <v-col class="regular text-center">{{item.casting_time_amount}} {{
              item.casting_time_unit.toLowerCase() }}
            </v-col>
          </v-col>
          <v-col class="bold text-center">RANGE/AREA
            <v-col class="regular text-center" v-if="item.range_type.match('RANGED')">
              {{ item.range_type.toLowerCase() }} ({{ item.range_distance}} ft)
            </v-col>
          </v-col>
          <v-col class="bold text-center">COMPONTENTS
            <v-col class="regular text-center">
              <span v-if="item.component_verbal == true">V</span>
              <span v-if="item.component_somatic == true">S</span>
              <span v-if="item.component_material == true">M</span>
            </v-col>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="bold text-center">DURATION
            <v-col class="regular text-center" v-if="item.duration_type.match('TIME')">
              {{item.duration_amount}} {{item.duration_unit.toLowerCase()}}
            </v-col>
            <v-col class="regular text-center" v-else>{{item.duration_type.toLowerCase()}}</v-col>
          </v-col>

          <v-col class="bold text-center">SCHOOL
            <v-col class="regular text-center">{{item.school}}</v-col>
          </v-col>

          <v-col class="bold text-center">ATTACK/SAVE
            <v-col class="regular text-center" v-if="item.spell_additional_info != null &&
                                  item.spell_additional_info.save_type != null">
              {{item.spell_additional_info.save_type}}
            </v-col>
            <v-col class="regular text-center" v-else>-</v-col>
          </v-col>

          <v-col class="bold text-center">DAMAGE/EFFECT
            <v-col class="regular text-center"
                   v-if="item.spell_additional_info != null &&
                         item.spell_additional_info.tags != null "
            >
              <span v-for="tag in item.spell_additional_info.tags" :key="tag.id">{{tag.tag}} </span>
            </v-col>
            <v-col class="regular text-center" v-else>-</v-col>
          </v-col>
        </v-row>

        <v-divider></v-divider>

        <v-container>
          {{ item.description }}
        </v-container>
        <v-container>
          <v-row>Classes: {{ item.class_list }} </v-row>
          <v-row>Tags: {{ item.tag_list }} </v-row>

        </v-container>
      </td>
    </template>
  </v-data-table>
</template>

<script>
  export default {
    props: [ 'spells', 'spelltags', 'characterclasses',],

    data () {
      return {
        expanded: [],
        headers: [
          {text: 'LEVEL', value: 'level', align: 'left', filter: this.levelsFilter},
          {text: 'NAME', value: 'name', align: 'center', filter: this.nameFilter,},
          {text: 'SCHOOL', value: 'school', align: 'center', filter: this.schoolFilter,},
          {text: 'CASTING TIME', value: 'casting_time', align: 'center', sortable: false},
          {text: 'TAGS', value: 'tag_list', align: ' d-none', filter: this.spelltagsFilter},
          {text: 'CLASSES', value: 'class_list', align: ' d-none', filter: this.characterclassesFilter},
          {text: ' ', value: 'data-table-expand', align: 'left'}
        ],
        levelsList: [
          {text: "All", value: null},
          {text: "Cantrip", value: 0},
          {text: "1st", value: 1},
          {text: "2nd", value: 2},
          {text: "3rd", value: 3},
          {text: "4th", value: 4},
          {text: "5th", value: 5},
          {text: "6th", value: 6},
          {text: "7th", value: 7},
          {text: "8th", value: 8},
          {text: "9th", value: 9},
        ],
        // Filter models
        spellFilterValue: '',
        levelsFilterValue: null,
        spelltagsFilterValue: null,
        characterclassesFilterValue: null,
      }
    },
    methods: {
      // Expand row
      expandRow(item) {
          this.expanded = item == this.expanded[0] ? [] : [item]
      },

      // ----- NEW FILTERS -----
      // -- Filter for spell name col
      nameFilter(value) {
        if (!this.spellFilterValue) {
          return true
        }
        return value.toLowerCase().includes(this.spellFilterValue.toLowerCase())
      },

      // -- Filter for level col
      levelsFilter(value) {
        if (!this.levelsFilterValue) {
          return true
        }
        return value == this.levelsFilterValue
      },

      // -- Filter for spell tags col
      spelltagsFilter(value) {
        if (!this.spelltagsFilterValue) {
          return true
        }
        return value.toLowerCase().includes(this.spelltagsFilterValue.toLowerCase())
      },

      // -- Filter for character classes
      characterclassesFilter(value) {
        if (!this.characterclassesFilterValue) {
          return true
        }
        return value.toLowerCase().includes(this.characterclassesFilterValue.toLowerCase())
      },
    },
  }
</script>

<style scoped>

</style>
