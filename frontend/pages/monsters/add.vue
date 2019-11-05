<template>
  <v-container class="my-5">
    <v-container class="row">
      <v-container class="col-md-12 my-3">
        <h2 class="mb-3 text-uppercase">new Monster</h2>
      </v-container>


      <v-container>
        <v-form @submit.prevent="submit">
          <!--<v-alert v-if="alert" :type="alert.type">{{ alert.message }}</v-alert>-->
          <v-text-field v-model="monster.name" label="Name"/>
          <v-select v-model="monster.alignment" :items="alignmentList" label="Alignment"></v-select>
          <v-select v-model="monster.challenge_rating" :items="CRList" label="Challenge rating - CR"></v-select>
          <v-text-field v-model="monster.hit_point" type="number" label="Hit points"></v-text-field>
          <v-select v-model="monster.hit_dice" :items="hitDiceList" label="Hit Dice"></v-select>
          <v-text-field v-model="monster.armor_class" type="number" label="Armor Class"></v-text-field>
          <v-text-field v-model="monster.armor_class_notes" label="Armor Class Notes (opt)"></v-text-field>

          <v-row>
            <v-col>
              <v-select v-model="monster.size" :items="sizeList" label="Size"></v-select>
            </v-col>
            <v-col>
              <v-text-field v-model="monster.type" label="Type"></v-text-field>
            </v-col>
            <v-col>
              <v-text-field v-model="monster.subtype" label="Subtype"></v-text-field>
            </v-col>
          </v-row>

          <v-row>
            <v-col>
              <v-text-field v-model="monster.ability_str" type="number" label="STRENGTH"></v-text-field>
              <v-text-field v-model="monster.ability_dex" type="number" label="DEXTERITY"></v-text-field>
              <v-text-field v-model="monster.ability_con" type="number" label="CONSTITUTION"></v-text-field>
            </v-col>
            <v-col>
              <v-text-field v-model="monster.ability_int" type="number" label="INTELLIGENCE"></v-text-field>
              <v-text-field v-model="monster.ability_wis" type="number" label="WISDOM"></v-text-field>
              <v-text-field v-model="monster.ability_cha" type="number" label="CHARISMA"></v-text-field>
            </v-col>
          </v-row>

          <v-row>
            <v-textarea
                v-model="monster.traits"
                auto-grow
                outlined
                clearable
                name="input-7-4"
                label="Traits"
                value="No traits.."
            ></v-textarea>
          </v-row>

          <v-row>
            <v-col>
              <v-text-field v-model="monster.skills" label="Skills"/>
            </v-col>
            <v-col>
              <v-text-field v-model="monster.languages" label="Languages"/>
            </v-col>
          </v-row>

          <v-row>
            <v-col>
              <v-text-field v-model="monster.damage_vulnerabilities" label="Damage Vulnerabilities"/>
            </v-col>
            <v-col>
              <v-text-field v-model="monster.damage_resistances" label="Damage Resistances"/>
            </v-col>
          </v-row>

          <v-row>
            <v-col>
              <v-text-field v-model="monster.condition_immunities" label="Condition Immunities"/>
            </v-col>
            <v-col>
              <v-text-field v-model="monster.damage_immunities" label="Damage Immunities"/>
            </v-col>
          </v-row>


          <v-row>
            <v-text-field v-model="monster.senses" label="Senses"/>
          </v-row>

          <v-row>
            <v-textarea
                v-model="monster.actions"
                auto-grow
                outlined
                clearable
                name="input-7-4"
                label="Actions"
                value="No actions.."
            ></v-textarea>
          </v-row>

          <v-row>
            <v-textarea
                v-model="monster.special_abilities"
                auto-grow
                outlined
                clearable
                name="input-7-4"
                label="Special abilities"
                value="No special abilities.."
            ></v-textarea>
          </v-row>

          <v-row>
            <v-textarea
                v-model="monster.legendary_actions"
                auto-grow
                outlined
                clearable
                name="input-7-4"
                label="Legendary Actions"
                value="No legendary actions.."
            ></v-textarea>
          </v-row>

          <v-row justify="center">
            <v-col class="text-center">
              <v-btn type="submit" outlined color="accent">Save</v-btn>
            </v-col>
          </v-row>
        </v-form>

      </v-container>
    </v-container>
  </v-container>
</template>

<script>
    import api from '~/api'

    export default {

        head() {
            return {
                title: "Add Monster"
            };
        },
        data() {
            return {
                monster: {
                    name: "",
                    image: null,
                    version: "",
                    size: "",

                    type: "",
                    subtype: "",
                    alignment: "",
                    armor_class: null,
                    armor_class_notes: "",

                    hit_point: null,
                    hit_dice: "",
                    ability_str: 0,
                    ability_dex: 0,
                    ability_con: 0,
                    ability_int: 0,
                    ability_wis: 0,
                    ability_cha: 0,
                    challenge_rating: "",

                    creation_time: "",
                    last_modified: "",

                    traits: "",
                    speeds: "",
                    saves: "",
                    skills: "",
                    damage_vulnerabilities: "",
                    damage_resistances: "",
                    condition_immunities: "",
                    damage_immunities: "",
                    senses: "",
                    languages: "",
                    special_abilities: "",
                    actions: "",
                    legendary_actions: "",
                    custom_attributes: []
                },

                preview: "",

                CRList: [
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
                sizeList: [
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
                alignmentList: [
                    {text: 'Lawful Good', value: 'Lawful Good'},
                    {text: 'Neutral Good', value: 'Neutral Good'},
                    {text: 'Chaotic Good', value: 'Chaotic Good'},
                    {text: 'Lawful Neutral', value: 'Lawful Neutral'},
                    {text: 'True Neutral', value: 'True Neutral'},
                    {text: 'Chaotic Neutral', value: 'Chaotic Neutral'},
                    {text: 'Lawful Evil', value: 'Lawful Evil'},
                    {text: 'Neutral Evil', value: 'Neutral Evil'},
                    {text: 'Chaotic Evil', value: 'Chaotic Evil'},
                ],
                hitDiceList: [
                    {text: '1d3', value: '1d3'},
                    {text: '1d4', value: '1d4'},
                    {text: '1d6', value: '1d6'},
                    {text: '1d8', value: '1d8'},
                    {text: '1d10', value: '1d10'},
                    {text: '1d12', value: '1d12'},
                ]

            };
        },
        methods: {
            submit() {
                this.alert = null
                this.loading = true

                this.monster.armor_class = Number(this.monster.armor_class)

                this.monster.hit_point = Number(this.monster.hit_point)
                this.monster.ability_str = Number(this.monster.ability_str)
                this.monster.ability_dex = Number(this.monster.ability_dex)
                this.monster.ability_con = Number(this.monster.ability_con)
                this.monster.ability_int = Number(this.monster.ability_int)
                this.monster.ability_wis = Number(this.monster.ability_wis)
                this.monster.ability_cha = Number(this.monster.ability_cha)

                api.createMonster(this.$axios, this.monster)
                    .then(result => {
                        this.alert = {type: 'success', message: result.message || 'Success'}
                        this.loading = false
                    })
                    .catch(error => {
                        console.log('/monster/add.vue .catch() error', error)
                        console.log('/monster/add.vue .catch() error.response', error.response)
                        this.loading = false
                        if (error.response && error.response.data) {
                            this.alert = {
                                type: 'error',
                                message: error.response.data || 'Error'
                            }
                        }
                    })

                this.$router.push(`/monsters`)
            },
        }
    };

</script>


<style scoped>
</style>
