<template>
  <v-data-table
      :headers="headers"
      :items="monsters"
      :items-per-page="5"
      sort-by="name"
      item-key="name"
      class="elevation-1"
      @click:row="goToSinglePage">

    <template v-slot:top>
      <v-container fluid>
        <v-row>
          <!-- filter for name -->
          <v-col cols="12" md="3">
            <v-row class="pa-3">
              <v-text-field
                  v-model="monsterFilterValue"
                  type="text"
                  label="Name"
              ></v-text-field>
            </v-row>
          </v-col>

          <!-- Filter for challenge rating -->
          <v-col cols="12" md="3">
            <v-row class="pa-3">
              <v-select
                  :items="CRList"
                  v-model="CRFilterValue"
                  label="Challenge rating"
              ></v-select>
            </v-row>
          </v-col>

          <!-- Filter for ALIGNMENT -->
          <v-col cols="12" md="3">
            <v-row class="pa-3">
              <v-select
                  :items="AlignmentList"
                  v-model="AlignmentFilterValue"
                  label="Alignment"
              ></v-select>
            </v-row>
          </v-col>

          <!-- Filter for SIZE -->
          <v-col cols="12" md="3">
            <v-row class="pa-3">
              <v-select
                  :items="SizeList"
                  v-model="SizeFilterValue"
                  label="Size"
              ></v-select>
            </v-row>
          </v-col>

        </v-row>
      </v-container>
    </template>

  </v-data-table>
</template>

<script>
    export default {
        props: ['monsters',],

        data() {
            return {
                // monsters: [],
                CRList: [
                    {text: "All", value: null},
                    {text: "1/8", value: "1/8"},
                    {text: "1/4", value: "1/4"},
                    {text: "1/2", value: "1/2"},
                    {text: "1", value: "1"},
                    {text: "2", value: "2"},
                    {text: "3", value: "3"},
                    {text: "4", value: "4"},
                    {text: "5", value: "5"},
                    {text: "6", value: "6"},
                    {text: "7", value: "7"},
                    {text: "8", value: "8"},
                    {text: "9", value: "9"},
                    {text: "10", value: "10"},
                    {text: "11", value: "11"},
                    {text: "12", value: "12"},
                    {text: "13", value: "13"},
                    {text: "14", value: "14"},
                    {text: "15", value: "15"},
                    {text: "16", value: "16"},
                    {text: "17", value: "17"},
                    {text: "18", value: "18"},
                    {text: "19", value: "19"},
                    {text: "20", value: "20"},
                    {text: "21", value: "21"},
                    {text: "22", value: "22"},
                    {text: "23", value: "23"},
                    {text: "24", value: "24"},
                    {text: "25", value: "25"},
                    {text: "26", value: "26"},
                    {text: "27", value: "27"},
                    {text: "28", value: "28"},
                    {text: "29", value: "29"},
                    {text: "30", value: "30"},
                ],
                AlignmentList: [
                    {text: "All", value: null},
                    {text: "Good", value: "Good"},
                    {text: "Neutral", value: "Neutral"},
                    {text: "Evil", value: "Evil"},
                    {text: "Lawful", value: "Lawful"},
                    {text: "Chaotic", value: "Chaotic"},
                ],
                SizeList: [
                    {text: "All", value: null},
                    {text: "Fine", value: "Fine"},
                    {text: "Diminutive", value: "Diminutive"},
                    {text: "Tiny", value: "Tiny"},
                    {text: "Small", value: "Small"},
                    {text: "Medium", value: "Medium"},

                    {text: "Large", value: "Large"},
                    {text: "Huge", value: "Huge"},
                    {text: "Gargantuan", value: "Gargantuan"},
                    {text: "Colossal", value: "Colossal"},
                ],

                // Filter models
                monsterFilterValue: '',
                CRFilterValue: '',
                AlignmentFilterValue: '',
                SizeFilterValue: '',

                // v-data-table
                headers: [
                    {text: 'NAME', value: 'name', align: 'left', filter: this.nameFilter},
                    {text: 'SIZE', value: 'size', align: 'center', filter: this.sizeFilter},
                    {text: 'CHALLENG RATING', value: 'challenge_rating', align: 'center', filter: this.crFilter},
                    {text: 'TYPE', value: 'type', align: 'center'},
                    {text: 'HIT POINTS', value: 'hit_point', align: 'center'},
                    //{text: 'ARMOR CLASS', value: 'armor_class_total', align: 'center'},
                    {text: 'ALIGNMENT', value: 'alignment', align: 'center', filter: this.alignmentFilter},
                ],
            }
        },

        methods: {
            // -- Filter for name
            nameFilter(value) {
                if (!this.monsterFilterValue) {
                    return true;
                }
                return value.toLowerCase().includes(this.monsterFilterValue.toLowerCase());
            },

            // -- Filter for challenge rating
            crFilter(value) {
                if (!this.CRFilterValue) {
                    return true;
                }
                return value == this.CRFilterValue;
            },

            // -- Filter for ALIGNMENT
            alignmentFilter(value) {
                if (!this.AlignmentFilterValue) {
                    return true;
                }
                return value.toLowerCase().includes(this.AlignmentFilterValue.toLowerCase())
            },

            // -- Filter for SIZE
            sizeFilter(value) {
                if (!this.SizeFilterValue) {
                    return true;
                }
                return value.toLowerCase().includes(this.SizeFilterValue.toLowerCase())
            },

            // go to single page
            goToSinglePage(item) {
                this.$router.push(`/monsters/${item.id}`)
            },
        },
    }
</script>

<style scoped>

</style>
