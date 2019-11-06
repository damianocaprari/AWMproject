<template>
  <v-container class="my-5">

    <v-container class="col-md-12 my-3">
      <h2 class="mb-3 text-uppercase">new Monster</h2>
    </v-container>


    <v-container v-if="canAdd()">
      <v-form @submit.prevent="submit">
        <!--<v-alert v-if="alert" :type="alert.type">{{ alert.message }}</v-alert>-->
        <v-row>
          <v-col cols="12" sm="6">
            <v-text-field v-model="monster.name" label="Name*"/>
            <v-select v-model="monster.alignment" :items="alignmentList" label="Alignment*"></v-select>
            <v-select v-model="monster.challenge_rating" :items="CRList" label="Challenge rating*"></v-select>
            <v-text-field v-model="monster.hit_point" type="number" label="Hit points*"></v-text-field>
            <v-select v-model="monster.hit_dice" :items="hitDiceList" label="Hit Dice*"></v-select>
            <v-text-field v-model="monster.armor_class" type="number" label="Armor Class*"></v-text-field>
            <v-text-field v-model="monster.armor_class_notes" label="Armor Class Notes"></v-text-field>
          </v-col>

          <v-col cols="12" sm="6">
            <div class="form-group mt-6">
              <label for>Monster picture</label>
              <input type="file" name="file" @change="onFileChange">
            </div>

            <v-row class="mt-1">
              <v-col>
                <v-text-field v-model="monster.ability_str" type="number" label="STRENGTH*"></v-text-field>
                <v-text-field v-model="monster.ability_dex" type="number" label="DEXTERITY*"></v-text-field>
                <v-text-field v-model="monster.ability_con" type="number" label="CONSTITUTION*"></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="monster.ability_int" type="number" label="INTELLIGENCE*"></v-text-field>
                <v-text-field v-model="monster.ability_wis" type="number" label="WISDOM*"></v-text-field>
                <v-text-field v-model="monster.ability_cha" type="number" label="CHARISMA*"></v-text-field>
              </v-col>
            </v-row>

          </v-col>
        </v-row>


        <v-row>
          <v-col>
            <v-select v-model="monster.size" :items="sizeList" label="Size*"></v-select>
          </v-col>
          <v-col>
            <v-text-field v-model="monster.type" label="Type*"></v-text-field>
          </v-col>
          <v-col>
            <v-text-field v-model="monster.subtype" label="Subtype"></v-text-field>
          </v-col>
        </v-row>


        <v-row>
          <v-col>
          <v-textarea
              v-model="monster.traits"
              auto-grow
              outlined
              clearable
              name="input-7-4"
              label="Traits"
              value="No traits.."
          ></v-textarea>
          </v-col>
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
          <v-col>
            <v-text-field v-model="monster.senses" label="Senses"/>
          </v-col>
        </v-row>

        <v-row>
          <v-col>
            <v-textarea
                v-model="monster.actions"
                auto-grow
                outlined
                clearable
                name="input-7-4"
                label="Actions"
                value="No actions.."
            ></v-textarea>
          </v-col>
        </v-row>

        <v-row>
          <v-col>

            <v-textarea
                v-model="monster.special_abilities"
                auto-grow
                outlined
                clearable
                name="input-7-4"
                label="Special abilities"
                value="No special abilities.."
            ></v-textarea>
          </v-col>
        </v-row>

        <v-row>
          <v-col>

            <v-textarea
                v-model="monster.legendary_actions"
                auto-grow
                outlined
                clearable
                name="input-7-4"
                label="Legendary Actions"
                value="No legendary actions.."
            ></v-textarea>
          </v-col>
        </v-row>

        <v-row justify="center">
          <v-col class="text-center">
            <v-btn type="submit" outlined color="accent">Save</v-btn>
          </v-col>
        </v-row>
      </v-form>

    </v-container>

    <v-row justify="center" v-else>
      <v-col cols="12">
        <v-alert :type="alert.type">{{ alert.message }}</v-alert>
      </v-col>

      <v-col class="text-center">
        <v-btn class="accent onaccent--text" @click="returnToMonsters">Back to monsters</v-btn>
      </v-col>
    </v-row>


  </v-container>
</template>

<script>
    import api from '~/api'

    export default {

        head() {
            return {
                title: `AWM Project - Add Monster`
            };
        },
        data() {
            return {
                form_data_avatar_file: null,
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
                console.log(this.monster)
                if (this.monster.image == null)
                    console.log("ADD BASIC IMAGE")
                console.log(this.monster.image)
                this.monster.armor_class = Number(this.monster.armor_class)
                this.monster.hit_point = Number(this.monster.hit_point)
                this.monster.ability_str = Number(this.monster.ability_str)
                this.monster.ability_dex = Number(this.monster.ability_dex)
                this.monster.ability_con = Number(this.monster.ability_con)
                this.monster.ability_int = Number(this.monster.ability_int)
                this.monster.ability_wis = Number(this.monster.ability_wis)
                this.monster.ability_cha = Number(this.monster.ability_cha)

                const config = {
                    headers: {"content-type": "multipart/form-data"}
                };
                let formData = new FormData();
                for (let data in this.monster) {
                    formData.append(data, this.monster[data]);
                }
                console.log(formData)
                try {
                    let response = this.$axios.$post("/monsters/", formData, config);
                    this.$router.push("/monsters/");
                } catch (e) {
                    console.log(e);
                }

            },
            submitCORRECT() {
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
                        let form_data = new FormData()
                        if (!!this.form_data_avatar_file) {
                            form_data.append('image', this.form_data_avatar_file, this.form_data_avatar_file.name)
                            this.$axios.put(`/monsters/${result.id}/`, form_data, {headers: {"Content-type": "multipart/form-data"}})
                                .then(data => {
                                        console.log("Add image")
                                    }
                                ).catch(e => {
                                console.log(e.response)
                            })
                        }

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

            pickImage() {
                this.$refs.image.click()
            },
            onImagePicked(e) {
                const files = e.target.files
                if (files[0] !== undefined) {
                    if (files[0].name.lastIndexOf('.') <= 0) {
                        //console.log('/components/SpellForm.vue onImagePicked() files[0].name.lastIndexOf(\'.\') <= 0')
                        console.log('/monsters/add.vue  onImagePicked() files[0].name.lastIndexOf(\'.\') <= 0')
                        return
                    }
                    const fr = new FileReader()
                    fr.readAsDataURL(files[0])
                    fr.addEventListener('load', () => {
                        //let form_data = new FormData()
                        //form_data.append('avatar', files[0], files[0].name)
                        this.form_data_avatar_file = files[0]
                        //alert("Preparato spell_avatar_form_data da inviare con la form al submit, vedi console.log()")
                        //console.log(this.spell_avatar_form_data)

                        //this.spell_additional_info.avatar = fr.result
                        this.monster.image = fr.result
                    })
                }
            },

            //------------------
            //------------------
            onFileChange(e) {
                let files = e.target.files || e.dataTransfer.files;
                if (!files.length) {
                    return;
                }
                this.monster.image = files[0];
                this.createImage(files[0]);
            },
            createImage(file) {
                // let image = new Image();
                let reader = new FileReader();
                let vm = this;
                reader.onload = e => {
                    vm.preview = e.target.result;
                };
                reader.readAsDataURL(file);
            },

            canAdd() {
                try {
                    let user = this.$store.state.auth.user
                    if (!user) {
                        this.alert = {
                            type: 'error',
                            message: 'Sign In to create a monster'
                        }
                        return false
                    } else {
                        return true
                    }
                } catch (e) {
                    console.log('monsters/_id/edit.vue canEdit() .catch e:', e)
                }
                this.alert = {
                    type: 'error',
                    message: 'You do not have the permission create a monster'
                }
                return false
            },
            returnToMonsters() {
                this.$router.push(`/monsters`)
            },
        }
    };

</script>


<style scoped>
  .v-card--reveal {
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .75;
    position: absolute;
    width: 100%;
  }
</style>
