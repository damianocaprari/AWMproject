<template>
  <v-container>

    <v-card-text v-if="isEditing">
      <v-form @submit.prevent="submit">

        <v-row>
        <v-text-field class="title" label="Name" v-model="form_data.name" :readonly="!isEditing"/>
      </v-row>
      <v-row>

        <v-col>
          <v-row>
              <v-select outlined label="Size" :items="sizeList" v-model="form_data.size" :readonly="!isEditing"/>
              <v-text-field outlined label="Type" v-model="form_data.type" :readonly="!isEditing"/>
              <v-text-field outlined label="Subtype" v-model="form_data.subtype" :readonly="!isEditing"/>
          </v-row>
          <v-row>
            <v-select v-model="form_data.alignment" :items="alignmentList" label="Alignment" :readonly="!isEditing"></v-select>
          </v-row>

          <p></p>

          <v-row>
            <v-col cols="12" md="4">
              <v-text-field type="number" label="Armor class" v-model="form_data.armor_class" :readonly="!isEditing"/>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="form_data.hit_point" type="number" label="Hit points" :readonly="!isEditing"></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-select v-model="form_data.hit_dice" :items="hitDiceList" label="Hit Dice" :readonly="!isEditing"></v-select>
            </v-col>
          </v-row>

          <p></p>

          <v-row>
              <v-col cols="6" md="2">
                  <v-text-field v-model="monster.ability_str" type="number" label="STR"></v-text-field>
                  <v-text-field v-model="monster.ability_dex" type="number" label="DEX"></v-text-field>
                  <v-text-field v-model="monster.ability_con" type="number" label="CON"></v-text-field>
              </v-col>
              <v-col cols="6" md="2">
                  <v-text-field v-model="monster.ability_int" type="number" label="INT"></v-text-field>
                  <v-text-field v-model="monster.ability_wis" type="number" label="WIS"></v-text-field>
                  <v-text-field v-model="monster.ability_cha" type="number" label="CHA"></v-text-field>
              </v-col>
          </v-row>


          <p></p>
          <v-select v-model="form_data.challenge_rating" :items="CRList" label="Challenge rating - CR" :readonly="!isEditing"></v-select>


          <p></p>

          <v-row v-for="(speed, index) in form_data.speeds">
                      <v-text-field v-model="speed.value" label="Speeds" :readonly="!isEditing"/>
          </v-row>


        </v-col>
        <v-col v-if="monster.image != null">
          <v-img
              :src="monster.image"
              max-width="250">
          </v-img>
        </v-col>





      </v-row>





        <v-row justify="center">
          <v-col class="text-center">
            <v-btn type="submit" :loading="loading" :disabled="loading" outlined color="accent">Save</v-btn>
            <v-btn text color="accent" @click="resetFormData">Cancel</v-btn>
          </v-col>
        </v-row>
      </v-form>
    </v-card-text>
    <!-- ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd -->
    <v-card-text v-else>

      <v-row>
        <v-text-field class="title" label="Name" v-model="form_data.name" :readonly="!isEditing"/>
      </v-row>
      <v-row>

        <v-col>
          <v-row>
              <v-select outlined label="Size" :items="sizeList" v-model="form_data.size" :readonly="!isEditing"/>
              <v-text-field outlined label="Type" v-model="form_data.type" :readonly="!isEditing"/>
              <v-text-field outlined label="Subtype" v-model="form_data.subtype" :readonly="!isEditing"/>
          </v-row>
          <v-row>
            <v-select v-model="form_data.alignment" :items="alignmentList" label="Alignment" :readonly="!isEditing"></v-select>
          </v-row>

          <p></p>

          <v-row>
            <v-col cols="12" md="4">
              <v-text-field type="number" label="Armor class" v-model="form_data.armor_class" :readonly="!isEditing"/>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="form_data.hit_point" type="number" label="Hit points" :readonly="!isEditing"></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-select v-model="form_data.hit_dice" :items="hitDiceList" label="Hit Dice" :readonly="!isEditing"></v-select>
            </v-col>
          </v-row>

          <p></p>

          <v-row>
              <v-col cols="6" md="2">
                  <v-text-field v-model="monster.ability_str" type="number" label="STR"></v-text-field>
                  <v-text-field v-model="monster.ability_dex" type="number" label="DEX"></v-text-field>
                  <v-text-field v-model="monster.ability_con" type="number" label="CON"></v-text-field>
              </v-col>
              <v-col cols="6" md="2">
                  <v-text-field v-model="monster.ability_int" type="number" label="INT"></v-text-field>
                  <v-text-field v-model="monster.ability_wis" type="number" label="WIS"></v-text-field>
                  <v-text-field v-model="monster.ability_cha" type="number" label="CHA"></v-text-field>
              </v-col>
          </v-row>


          <p></p>
          <v-select v-model="form_data.challenge_rating" :items="CRList" label="Challenge rating - CR" :readonly="!isEditing"></v-select>


          <p></p>

          <v-row v-for="(speed, index) in form_data.speeds">
                      <v-text-field v-model="speed.value" label="Speeds" :readonly="!isEditing"/>
          </v-row>


        </v-col>
        <v-col v-if="monster.image != null">
          <v-img
              :src="monster.image"
              max-width="250">
          </v-img>
        </v-col>





      </v-row>



      <v-row justify="center">
        <v-col class="text-center">
          <v-btn type="" outlined color="accent" @click="isEditing = true">Edit</v-btn>
        </v-col>
      </v-row>


    </v-card-text>

  </v-container>
</template>

<script>
    import api from '~/api'

    import FormData from 'form-data'

    export default {
        head() {
            return {
                title: "View Monster"
            };
        },
        async asyncData({$axios, params}) {
            try {
                let monster = await $axios.$get(`/monsters/${params.id}`);
                let form_data = {
                    name: monster.name,
                    image: monster.image,
                    size: monster.size,
                    type: monster.type,
                    subtype: monster.subtype,
                    alignment: monster.alignment,
                    armor_class: monster.armor_class,
                    hit_point: monster.hit_point,
                    hit_dice: monster.hit_dice,
                    ability_str: monster.ability_str,
                    ability_dex: monster.ability_dex,
                    ability_con: monster.ability_con,
                    ability_int: monster.ability_int,
                    ability_wis: monster.ability_wis,
                    ability_cha: monster.ability_cha,
                    challenge_rating: monster.challenge_rating,

                    speeds: monster.speeds,

                };
                console.log("AAAAAAAAAA", typeof(form_data.speeds))

                return {monster, form_data};
            } catch (e) {
                return {monster: []};
            }
        },
        data() {
            return {
                monster: {},
                loading: false,

                form_data: {
                    name: '',
                    size: '',
                    type: '',
                    subtype: '',
                    alignment: '',
                    armor_class: '',
                    hit_point: '',
                    hit_dice: '',
                    ability_str: '',
                    ability_dex: '',
                    ability_con: '',
                    ability_int: '',
                    ability_wis: '',
                    ability_cha: '',
                    challeng_rating: '',

                    speeds:[]

                },

                alert: null,
                isEditing: false,

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
            resetFormData() {
                this.form_data = {
                    name: this.monster.name,
                    size: this.monster.size,
                    type: this.monster.type,
                    subtype: this.form_data.subtype,
                    alignment: this.form_data.alignment,
                    armor_class: this.form_data.armor_class,
                    hit_point: this.form_data.hit_point,
                    hit_dice: this.form_data.hit_dice,
                    ability_str: this.form_data.ability_str,
                    ability_dex: this.form_data.ability_dex,
                    ability_con: this.form_data.ability_con,
                    ability_int: this.form_data.ability_int,
                    ability_wis: this.form_data.ability_wis,
                    ability_cha: this.form_data.ability_cha,
                    challenge_rating: this.form_data.challenge_rating,

                    speeds: this.form_data.speeds


                    //first_name: this.user.first_name,
                    //last_name: this.user.last_name,
                }
                this.isEditing = false
            },
            submit() {
                if (this.isEditing == false) return
                this.alert = null
                this.loading = true
                api.updateMonster(this.$axios, this.monster.id, this.form_data)
                    .then(result => {
                        //console.log('/account/index.vue .then() result', result)
                        this.alert = {type: 'success', message: result.message || 'Success'}
                        this.loading = false
                        this.isEditing = false
                        this.monster.name = this.form_data.name
                        this.monster.size = this.form_data.size
                        this.monster.type = this.form_data.type
                        this.monster.subtype = this.form_data.subtype
                        this.monster.alignment = this.form_data.alignment
                        this.monster.this.monster.armor_class= this.form_data.armor_class
                        this.monster.hit_point= this.form_data.hit_point
                        this.monster.hit_dice= this.form_data.hit_dice
                        this.monster.ability_str = this.form_data.ability_str
                        this.monster.ability_dex= this.form_data.ability_dex
                        this.monster.ability_con= this.form_data.ability_con
                        this.monster.ability_int= this.form_data.ability_int
                        this.monster.ability_wis= this.form_data.ability_wis
                        this.monster.ability_cha= this.form_data.ability_cha
                        this.monster.challenge_rating= this.form_data.challenge_rating

                        this.monster.speeds = this.form_data.speeds




                        //this.user.last_name = this.form_data.last_name
                        //this.user.email = this.form_data.email
                    })
                    .catch(error => {
                        console.log('/account/index.vue .catch() error', error)
                        console.log('/account/index.vue .catch() error.response', error.response)
                        this.loading = false
                        if (error.response && error.response.data) {
                            this.alert = {
                                type: 'error',
                                message: error.response.data || 'Error'
                            }
                        }
                    })
            },
            onDelete(id) {
                console.log(id)
            }
        }
    };

</script>

<style scoped>
  .boldedname {
    font-weight: bold
  }

  span {
    margin-right: 3px
  }

  .subtitle {
    font-size: 30px;
    font-weight: bold;
  }

</style>
