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
          <!--
          <v-divider></v-divider>

          <v-container>
            <v-row>

              <v-col>
                <v-row>
                  <span>{{monster.size}} </span>
                  <span v-if="monster.type != null">, {{monster.type}}</span>
                  <span v-if="monster.subtype != null">, {{monster.subtype}}</span>
                </v-row>


                <v-row>
                  <span class="boldedname">Armor Class:</span>
                  <span>{{monster.armor_class}}</span>
                  <span v-if="monster.armor_class_notes != null"> ({{monster.armor_class_notes}})</span>
                </v-row>

                <v-row>
                  <span class="boldedname">Hit Points:</span>
                  <span>{{monster.hit_point}} ({{monster.hit_dice}})</span>
                </v-row>


                <v-row v-if="monster.speeds.length > 0">
                  <span class="boldedname">Speed:</span>
                  <span v-for="(item, index) in monster.speeds" :key="item.id">
                            {{item.value}}
                            <span v-if="index+1 < monster.speeds.length">,</span>
                         </span>
                </v-row>

                <v-row>
                  <v-col>
                    <v-row>STR</v-row>
                    <v-row>{{monster.ability_str}}</v-row>
                  </v-col>
                  <v-col>
                    <v-row>DEX</v-row>
                    <v-row>{{monster.ability_dex}}</v-row>
                  </v-col>
                  <v-col>
                    <v-row>CON</v-row>
                    <v-row>{{monster.ability_con}}</v-row>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-row>INT</v-row>
                    <v-row>{{monster.ability_int}}</v-row>
                  </v-col>
                  <v-col>
                    <v-row>WIS</v-row>
                    <v-row>{{monster.ability_wis}}</v-row>
                  </v-col>
                  <v-col>
                    <v-row>CHA</v-row>
                    <v-row>{{monster.ability_cha}}</v-row>
                  </v-col>
                </v-row>
              </v-col>

              <v-col v-if="monster.image != null">
                <v-img
                    :src="monster.image"
                    max-width="250">
                </v-img>
              </v-col>
            </v-row>

            <v-divider></v-divider>

            <v-row v-if="monster.saves.length > 0">
              <span class="boldedname">Saving throws: </span>
              <span v-for="(item, index) in monster.saves" :key="item.id">
                    {{item.name}} +{{item.modifier}}
                    <span v-if="index+1 < monster.saves.length">,</span>
                </span>
            </v-row>

            <v-row v-if="monster.skills.length > 0">
              <span class="boldedname">Skills: </span>
              <span v-for="(item, index) in monster.skills" :key="item.id">
                    {{item.name}} +{{item.modifier}}
                    <span v-if="index+1 < monster.skills.length">,</span>
                </span>
            </v-row>

            <v-row v-if="monster.senses.length > 0">
              <span class="boldedname">Senses: </span>
              <span v-for="(item, index) in monster.senses" :key="item.id">
                    {{item.sense}}
                    <span v-if="index+1 < monster.senses.length">,</span>
                    </span>
            </v-row>

            <v-row v-if="monster.languages.length > 0">
              <span class="boldedname">Languages: </span>
              <span v-for="(item, index) in monster.languages" :key="item.id">
                    {{item.language}}
                    <span v-if="index+1 < monster.languages.length">,</span>
                </span>
            </v-row>

            <v-row>
              <span class="boldedname">Challenge Rating: </span>
              <span>{{monster.challenge_rating}}</span>
            </v-row>


            <v-row v-if="monster.damage_vulnerabilities.length > 0">
              <span class="boldedname">Damage Vulnerabilities: </span>
              <span v-for="(item, index) in monster.damage_vulnerabilities" :key="item.id">
                    {{item.damage_vulnerability}}
                    <span v-if="index+1 < monster.damage_vulnerabilities.length">,</span>
                </span>
            </v-row>
            <v-row v-if="monster.damage_resistances.length > 0">
              <span class="boldedname">Damage Resistances: </span>
              <span v-for="(item, index) in monster.damage_resistances" :key="item.id">
                    {{item.damage_resistance}}
                    <span v-if="index+1 < monster.damage_resistances.length">,</span>
                </span>
            </v-row>
            <v-row v-if="monster.condition_immunities.length > 0">
              <span class="boldedname">Condition Immunities: </span>
              <span v-for="(item, index) in monster.condition_immunities" :key="item.id">
                    {{item.condition_immunity}}
                    <span v-if="index+1 < monster.condition_immunities.length">,</span>
                </span>
            </v-row>
            <v-row v-if="monster.damage_immunities.length > 0">
              <span class="boldedname">Damage Immunities: </span>
              <span v-for="(item, index) in monster.damage_immunities" :key="item.id">
                    {{item.damage_immunity}}
                    <span v-if="index+1 < monster.damage_immunities.length">,</span>
                </span>
            </v-row>
            <v-divider></v-divider>
          </v-container>

          <v-container v-if="monster.traits.length > 0">
            <v-row class="subtitle">Traits</v-row>
            <v-row v-for="item in monster.traits" :key="item.id">
              <v-col>
                <v-row class="boldedname inline">{{item.name}}</v-row>
                <v-row class="text-justify">{{item.content}}</v-row>
              </v-col>
            </v-row>
          </v-container>

          <v-container v-if="monster.actions.length > 0">
            <v-row class="subtitle">Actions</v-row>
            <v-row class="mb-3" v-for="item in monster.actions" :key="item.id">
              <v-col>
                <v-row class="boldedname">{{item.name}}</v-row>
                <v-row class="text-justify">{{item.desc}}</v-row>
              </v-col>
            </v-row>
          </v-container>

          <v-container v-if="monster.reactions.length > 0">
            <v-row class="subtitle">Reactions</v-row>
            <v-row class="mb-3" v-for="item in monster.reactions" :key="item.id">
              <v-col>
                <v-row class="boldedname">{{item.name}}</v-row>
                <v-row class="text-justify">{{item.content}}</v-row>
              </v-col>
            </v-row>
          </v-container>

          <v-container v-if="monster.special_abilities.length > 0">
            <v-row class="subtitle">Special Abilities</v-row>
            <v-row class="mb-3" v-for="item in monster.special_abilities" :key="item.id">
              <v-col>
                <v-row class="boldedname">{{item.name}}</v-row>
                <v-row class="text-justify">{{item.desc}}</v-row>
              </v-col>
            </v-row>
          </v-container>

          <v-container v-if="monster.legendary_actions.length > 0">
            <v-row class="subtitle">Legendary Actions</v-row>
            <v-row class="mb-3" v-for="item in monster.legendary_actions" :key="item.id">
              <v-col>
                <v-row class="boldedname">{{item.name}}</v-row>
                <v-row class="text-justify">{{item.content}}</v-row>
              </v-col>
            </v-row>
          </v-container>

          <v-container v-if="monster.custom_attributes.length > 0">
            <v-row class="subtitle">Custom Attributes</v-row>
            <v-row class="mb-3" v-for="item in monster.custom_attributes" :key="item.id">
              <v-col>
                <v-row class="boldedname">{{item.name}}</v-row>
                <v-row class="text-justify">{{item.value}}</v-row>
              </v-col>
            </v-row>
          </v-container>
      -->

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
                console.log(monster.author)
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
                // TODO: FAI IN MODO CHE REFRESHI LA PAGINA QUANDO TORNA INDIETRO
            }
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