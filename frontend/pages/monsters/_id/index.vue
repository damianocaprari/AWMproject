<template>
  <v-container>
    <v-row wrap>
      <v-alert v-if="!!alert" :type="alert.type">{{ alert.message }}</v-alert>
      <v-col>
        <v-card>
          <v-card-title class="secondary onsecondary--text">
            <v-row>
              <v-col><h3>
                {{ monster.name }}
              </h3></v-col>

              <template v-if="canEdit()">
                <v-col align="right">
                  <v-btn text color="onsecondary" @click="deleteMonster()" x-small>Delete</v-btn>
                  <v-btn outlined color="onsecondary" @click="goToEditPage" small>Edit</v-btn>
                  <v-btn class="ml-5 " text color="onsecondary" @click="returnToMonsters" small>Back</v-btn>
                </v-col>
              </template>
              <template v-else>
                <v-btn class="ml-5 " text color="onsecondary" @click="returnToMonsters" small>Back</v-btn>
              </template>

            </v-row>
          </v-card-title>

          <v-card-text>
            <v-row>
              <v-col cols="12" sm="4">
                <v-row justify="center">
                  <v-col align="center">
                    <v-avatar color="grey" tile size="160" class="mx-auto">
                      <v-img :src="monster.image"
                             v-if="(monster.image)"></v-img>
                    </v-avatar>


                    <v-form @submit.prevent="submit">
                      <div class="form-group">
                        <input type="file" name="file" @change="onFileChange">
                        <v-btn type="submit" outlined color="accent">Modify</v-btn>
                      </div>
                    </v-form>


                  </v-col>
                </v-row>
              </v-col>

              <v-col cols="12" sm="8">
                <v-row>
                  {{monster.size}} {{monster.type}}
                  <template v-if="monster.subtype"> ({{monster.subtype}})</template>
                  , {{monster.alignment}}
                </v-row>
                <v-row>
                  <br>
                  <v-divider></v-divider>
                  <br>
                </v-row>
                <v-row>
                  <span class="boldedname">Armor Class:</span> {{monster.armor_class}}
                  <template v-if="monster"> ({{monster.armor_class_notes}})</template>
                </v-row>
                <v-row>
                  <span class="boldedname">Hit points:</span> {{monster.hit_point }} ({{monster.hit_dice}})
                </v-row>
                <v-row v-if="monster.speeds"><span class="boldedname">Speed:</span> {{monster.speeds}}</v-row>
                <v-row>
                  <v-divider></v-divider>
                </v-row>
                <v-row>
                  <v-col cols="12" sm="2">
                    <v-row>STR</v-row>
                    <v-row>{{monster.ability_str}}</v-row>
                  </v-col>
                  <v-col cols="12" sm="2">
                    <v-row>DEX</v-row>
                    <v-row>{{monster.ability_dex}}</v-row>
                  </v-col>
                  <v-col cols="12" sm="2">
                    <v-row>CON</v-row>
                    <v-row>{{monster.ability_con}}</v-row>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" sm="2">
                    <v-row>INT</v-row>
                    <v-row>{{monster.ability_int}}</v-row>
                  </v-col>
                  <v-col cols="12" sm="2">
                    <v-row>WIS</v-row>
                    <v-row>{{monster.ability_wis}}</v-row>
                  </v-col>
                  <v-col cols="12" sm="2">
                    <v-row>CHA</v-row>
                    <v-row>{{monster.ability_cha}}</v-row>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>

            <v-row>
              <v-divider></v-divider>
            </v-row>

            <v-row v-if="monster.skills"><span class="boldedname">Skills:</span> {{monster.skills}}</v-row>
            <v-row v-if="monster.senses"><span class="boldedname">Senses:</span> {{monster.senses}}</v-row>
            <v-row v-if="monster.languages"><span class="boldedname">Languages:</span> {{monster.languages}}</v-row>
            <v-row><span class="boldedname">Challenge rating:</span> {{monster.challenge_rating}}</v-row>

            <v-row v-if="monster.damage_vulnerabilities"><span class="boldedname">Damage Vulnerabilities:</span>
              {{monster.damage_vulnerabilities}}
            </v-row>
            <v-row v-if="monster.damage_resistances"><span class="boldedname">Damage Resistances:</span>
              {{monster.damage_resistances}}
            </v-row>
            <v-row v-if="monster.condition_immunities"><span class="boldedname">Condition Immunities:</span>
              {{monster.condition_immunities}}
            </v-row>
            <v-row v-if="monster.damage_immunities"><span class="boldedname">Damage Immunities:</span>
              {{monster.damage_immunities}}
            </v-row>

            <template v-if="monster.traits">
              <v-row>
                <v-divider></v-divider>
              </v-row>
              <v-row class="text-justify" v-html="monster.traits"/>
            </template>

            <template v-if="monster.actions">
              <v-row>
                <v-divider></v-divider>
              </v-row>
              <v-row><h3>Actions</h3></v-row>
              <v-row class="text-justify" v-html="monster.actions"/>
            </template>

            <template v-if="monster.special_abilities">
              <v-row>
                <v-divider></v-divider>
              </v-row>
              <v-row><h3>Special abilities</h3></v-row>
              <v-row class="text-justify" v-html="monster.special_abilities"/>
            </template>

            <template v-if="monster.legendary_actions">
              <v-row>
                <v-divider></v-divider>
              </v-row>
              <v-row><h3>Legendary Actions</h3></v-row>
              <v-row class="text-justify" v-html="monster.legendary_actions"/>
            </template>

          </v-card-text>

        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
    export default {
        head() {
            return {
                title: "View Monster"
            };
        },
        async asyncData({$axios, params}) {
            try {
                let monster = await $axios.$get(`/monsters/${params.id}`);
                if (!monster) {
                    return {
                        alert: {
                            type: 'error',
                            message: 'Selected monster does not exist'
                        }
                    }
                }
                return {monster};
            } catch (e) {
                return {
                    alert: {
                        type: 'error',
                        message: 'An error occurred while retrieving information'
                    }
                }
            }
        },
        data() {
            return {
                monster: {},
                alert: null,
            };
        },
        methods: {
            deleteMonster() {
                if (this.canEdit()) {
                    this.$axios.$delete(`/monsters/${this.$route.params.id}`)
                }
                this.returnToMonsters()
            },

            goToEditPage() {
                this.$router.push(`/monsters/${this.$route.params.id}/edit`)
            },

            canEdit() {
                try {
                    let userId = this.$store.state.auth.user.id
                    if (this.monster && this.monster.author) {
                        let monsterAuthorId = this.$store.app.getResourceId(this.monster.author)
                        if (userId == monsterAuthorId)
                            return true
                    }
                } catch (e) {
                    console.log('monsters/_id/edit.vue canEdit() .catch e:', e)
                    return false
                }
                return false
            },

            returnToMonsters() {
                this.$router.push(`/monsters`)
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

            submit() {
                console.log("AAAAAAAAAAAAAAAA", this.monster.image)

                if (!!this.monster.image) {
                    let form_data = new FormData();
                    form_data.append('image', this.monster.image)
                    this.$axios.$put(`/monsters/${this.monster.id}/`,
                        form_data, {headers: {'Content-Type': 'multipart/form-data'}})
                        .then(data => {
                            console.log(data)
                        })
                        .catch(e => {
                            console.log(e.response)
                        })
                }

                //this.$axios.$put(`monsters/${this.monster.id}/`, this.monster)
                /*
                api.updateMonster(this.$axios, this.monster.id, this.form_data)
                    .then(result => {
                        console.log('/account/edit.vue .then() result', result)
                        this.alert = {type: 'success', message: result.message || 'Success'}
                        this.loading = false
                        this.isEditing = false

                        this.monster.name = this.form_data.name
                        //this.monster.image = this.form_data.image
                        this.monster.size = this.form_data.size

                        this.monster.type = this.form_data.type
                        this.monster.subtype = this.form_data.subtype
                        this.monster.alignment = this.form_data.alignment
                        this.monster.armor_class = this.form_data.armor_class
                        this.monster.armor_class_notes = this.form_data.armor_class_notes

                        this.monster.hit_point = this.form_data.hit_point
                        this.monster.hit_dice = this.form_data.hit_dice
                        this.monster.ability_str = this.form_data.ability_str
                        this.monster.ability_dex = this.form_data.ability_dex
                        this.monster.ability_con = this.form_data.ability_con
                        this.monster.ability_int = this.form_data.ability_int
                        this.monster.ability_wis = this.form_data.ability_wis
                        this.monster.ability_cha = this.form_data.ability_cha
                        this.monster.challenge_rating = this.form_data.challenge_rating

                        this.monster.traits = this.form_data.traits
                        this.monster.speeds = this.form_data.speeds
                        this.monster.saves = this.form_data.saves
                        this.monster.skills = this.form_data.skills
                        this.monster.damage_vulnerabilities = this.form_data.damage_vulnerabilities
                        this.monster.damage_resistances = this.form_data.damage_resistances
                        this.monster.condition_immunities = this.form_data.condition_immunities
                        this.monster.damage_immunities = this.form_data.damage_immunities
                        this.monster.senses = this.form_data.senses
                        this.monster.languages = this.form_data.languages
                        this.monster.special_abilities = this.form_data.special_abilities
                        this.monster.actions = this.form_data.actions
                        this.monster.legendary_actions = this.form_data.legendary_actions

                        //this.user.last_name = this.form_data.last_name
                        //this.user.email = this.form_data.email
                    })
                    .catch(error => {
                        console.log('/account/edit.vue .catch() error', error)
                        console.log('/account/edit.vue .catch() error.response', error.response)
                        this.loading = false
                        if (error.response && error.response.data) {
                            this.alert = {
                                type: 'error',
                                message: error.response.data || 'Error'
                            }
                        }
                    })

                 */
                this.$router.push('/monsters')

            },
        },
    }
    ;

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