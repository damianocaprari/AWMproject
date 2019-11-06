<template>
  <v-container>
    <v-row>
      <v-col class="d-sm-none">
        <h2>Monsters</h2>
      </v-col>
      <!-- for screen >= 600 px -->
      <v-col class="d-none d-sm-block">
        <h1>Monsters</h1>
      </v-col>

      <!-- for screen < 600 px -->
      <template v-if="isLogged()">
        <v-col class="d-sm-none" align="right">
          <v-btn right color="primary" to="/monsters/add" x-small>Add monster</v-btn>
        </v-col>
        <!-- for screen >= 600 px -->
        <v-col class="d-none d-sm-block" align="right">
          <v-btn right color="primary" to="/monsters/add">Add monster</v-btn>
        </v-col>
      </template>
    </v-row>

    <monsters-table :monsters="monsters"></monsters-table>

  </v-container>
</template>


<script>
    import MonstersTable from "../../components/MonstersTable";

    export default {
        head(){
            return {
                title: `AWM Project - Monsters`
            };
        },

        components: {MonstersTable},

        async asyncData({$axios, params}) {
            let retval = {monsters: []}
            try {
                let query_monster = await $axios.$get(`/monsters/`);
                if (query_monster.count > 0) {
                    retval.monsters = query_monster.results

                    retval.monsters.forEach(monster => {
                        let armor_class_total = "" + monster.armor_class
                        if (monster.armor_class_notes) {
                            armor_class_total = armor_class_total + " (" + monster.armor_class_notes + ")"
                        }
                        monster['armor_class_total'] = armor_class_total
                    })
                }


            } catch (e) {
                console.log(e);
            }
            return retval
        },

        data() {
            return {
                monsters: [],

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
            };
        },

        methods: {
            // -- Filter for name
            nameFilter(value) {
                if (!this.monsterFilterValue) {
                    return true;
                }
                return value.toLowerCase().includes(this.monsterFilterValue.toLowerCase());
            }
            ,

            // -- Filter for challenge rating
            crFilter(value) {
                if (!this.CRFilterValue) {
                    return true;
                }
                return value == this.CRFilterValue;
            }
            ,

            // -- Filter for ALIGNMENT
            alignmentFilter(value) {
                if (!this.AlignmentFilterValue) {
                    return true;
                }
                return value.toLowerCase().includes(this.AlignmentFilterValue.toLowerCase())
            }
            ,

            // -- Filter for SIZE
            sizeFilter(value) {
                if (!this.SizeFilterValue) {
                    return true;
                }
                return value.toLowerCase().includes(this.SizeFilterValue.toLowerCase())
            }
            ,


            // go to single page
            goToSinglePage(item) {
                let number = item.id
                let link = "/monsters/" + item.id
                this.$router.push((`/monsters/${item.id}/edit`))
            },

            deleteItem(item) {
                const index = this.monsters.indexOf(item)
                confirm('Delete this monster?') && this.monsters.splice(index, 1)
            },

            isLogged() {
                try {
                    let user = this.$store.state.auth.user
                    if (!!user) {
                        return true
                    }
                } catch (e) {
                    console.log('monsters/add isLogged() .catch e:', e)
                }
                return false
            },


        }
        ,


    };
</script>

<style scoped>

</style>
