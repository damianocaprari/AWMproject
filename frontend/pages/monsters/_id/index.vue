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

                    <v-row>
                      <v-avatar color="grey" tile size="160" class="mx-auto">
                        <v-img :src="monster.image"
                               v-if="(monster.image)"></v-img>
                      </v-avatar>
                    </v-row>
                    <template v-if="canEdit()">
                      <v-row>
                        <v-col align="center">
                          <v-form @submit.prevent="submit">
                            <div class="form-group">
                              <v-row>
                                <v-col>
                                  <v-row class="ml-1 mb-2"><input type="file" name="file" @change="onFileChange"></v-row>
                                  <v-row class="ml-1">
                                    <v-btn type="submit" outlined color="accent">Modify</v-btn>
                                  </v-row>
                                </v-col>
                              </v-row>
                            </div>
                          </v-form>
                        </v-col>
                      </v-row>
                    </template>
                  </v-col>
                </v-row>
              </v-col>

              <v-col cols="12" sm="8">
                <v-row>
                  <v-col>
                    {{monster.size}} {{monster.type}}
                    <template v-if="monster.subtype"> ({{monster.subtype}})</template>
                    , {{monster.alignment}}
                  </v-col>
                </v-row>

                <v-divider></v-divider>

                <v-col>
                  <v-row>
                    <span class="boldedname">Armor Class:</span> {{monster.armor_class}}
                    <template v-if="monster"> ({{monster.armor_class_notes}})</template>
                  </v-row>
                  <v-row>
                    <span class="boldedname">Hit points:</span> {{monster.hit_point }} ({{monster.hit_dice}})
                  </v-row>
                  <v-row v-if="monster.speeds"><span class="boldedname">Speed:</span> {{monster.speeds}}</v-row>
                </v-col>

                <v-divider></v-divider>

                <!-- for screen >= 600 px -->
                <v-col class="d-none d-sm-block" align="right">
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

                <!-- for screen < 600 px -->
                <v-col class="d-sm-none" align="right">
                  <v-row>
                    <v-col>
                      <v-row>STR</v-row>
                      <v-row class="mb-2">{{monster.ability_str}}</v-row>
                      <v-row>DEX</v-row>
                      <v-row class="mb-2">{{monster.ability_dex}}</v-row>
                      <v-row>CON</v-row>
                      <v-row>{{monster.ability_con}}</v-row>
                    </v-col>

                    <v-col>
                      <v-row>INT</v-row>
                      <v-row class="mb-2">{{monster.ability_int}}</v-row>
                      <v-row>WIS</v-row>
                      <v-row class="mb-2">{{monster.ability_wis}}</v-row>
                      <v-row>CHA</v-row>
                      <v-row>{{monster.ability_cha}}</v-row>
                    </v-col>
                  </v-row>
                </v-col>
              </v-col>
            </v-row>

            <v-divider></v-divider>

            <v-col>
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
                  <v-divider class=" mt-3 mb-3"></v-divider>
                </v-row>
                <v-row><h3>Traits</h3></v-row>
                <v-row class="text-justify" v-html="monster.traits"/>
              </template>

              <template v-if="monster.actions">
                <v-row>
                  <v-divider class=" mt-3 mb-3"></v-divider>
                </v-row>
                <v-row><h3>Actions</h3></v-row>
                <v-row class="text-justify" v-html="monster.actions"/>
              </template>

              <template v-if="monster.special_abilities">
                <v-row>
                  <v-divider class=" mt-3 mb-3"></v-divider>
                </v-row>
                <v-row><h3>Special abilities</h3></v-row>
                <v-row class="text-justify" v-html="monster.special_abilities"/>
              </template>

              <template v-if="monster.legendary_actions">
                <v-row>
                  <v-divider class=" mt-3 mb-3"></v-divider>
                </v-row>
                <v-row><h3>Legendary Actions</h3></v-row>
                <v-row class="text-justify" v-html="monster.legendary_actions"/>
              </template>
            </v-col>

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
                title: `AWM Project - ${this.monster.name}`
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
