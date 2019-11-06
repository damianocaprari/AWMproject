<template>
  <v-container>

    <v-row justify="center" v-if="alert">
      <v-col cols="12">
        <v-alert :type="alert.type">{{ alert.message }}</v-alert>
      </v-col>

      <v-col class="text-center">
        <v-btn class="accent onaccent--text" @click="returnToSpells">Back</v-btn>
      </v-col>
    </v-row>

    <v-row v-else>
      <v-col>
        <v-card>
          <v-card-title class="secondary onsecondary--text">
            <v-row no-gutters>
              <v-col>
                {{ spell.name }}
              </v-col>

              <template v-if="canEdit()">
                <!-- for screen < 600 px -->
                <v-col class="d-sm-none" align="right">
                  <v-btn text color="onsecondary" @click="deleteSpell" x-small>Delete</v-btn>
                  <v-btn outlined color="onsecondary" @click="editSpell" small>Edit</v-btn>
                </v-col>

                <!-- for screen >= 600 px -->
                <v-col class="d-none d-sm-block" align="right">
                  <v-btn text color="onsecondary" @click="deleteSpell">Delete</v-btn>
                  <v-btn outlined color="onsecondary" @click="editSpell">Edit</v-btn>
                </v-col>
              </template>
            </v-row>
          </v-card-title>

          <v-card-text>
            <v-row>
              <v-col cols="12" lg="3">
                <v-row justify="center">
                  <v-col align="center">
                    <v-avatar color="grey" tile size="160" class="mx-auto">
                      <v-img :src="spell.spell_additional_info.avatar" v-if="(spell.spell_additional_info && spell.spell_additional_info.avatar)"></v-img>
                    </v-avatar>
                  </v-col>
                </v-row>
              </v-col>
              <v-col cols="12" lg="9">
                <v-row>
                  <v-col cols="6" sm="4" lg="3">
                    <v-row no-gutters><v-col>LEVEL</v-col></v-row>
                    <v-row no-gutters><v-col>{{ spell.level }}</v-col></v-row>
                  </v-col>
                  <v-col cols="6" sm="4" lg="3">
                    <v-row no-gutters><v-col>CASTING TIME</v-col></v-row>
                    <v-row no-gutters><v-col>{{ spell.casting_time_amount }} <span class="text-capitalize">{{ spell.casting_time_unit }}</span></v-col></v-row>
                  </v-col>
                  <v-col cols="6" sm="4" lg="3">
                    <v-row no-gutters><v-col>RANGE/AREA</v-col></v-row>
                    <v-row no-gutters>
                      <v-col v-if="'RANGED'.match(spell.range_type)"><span class="text-capitalize">{{ spell.range_type }}</span> ({{ spell.range_distance }} ft)</v-col>
                      <v-col v-else><span class="text-capitalize">{{ spell.range_type }}</span></v-col>
                    </v-row>
                  </v-col>
                  <v-col cols="6" sm="4" lg="3">
                    <v-row no-gutters><v-col>COMPONENTS</v-col></v-row>
                    <v-row no-gutters><v-col>
                       <template v-if="spell.component_verbal">V</template>
                       <template v-if="spell.component_somatic">S</template>
                       <template v-if="spell.component_material">M ({{ spell.component_material_description }}</template>
                    </v-col></v-row>
                  </v-col>
                  <v-col cols="6" sm="4" lg="3">
                    <v-row no-gutters><v-col>DURATION</v-col></v-row>
                    <v-row no-gutters>
                      <v-col v-if="'TIME'.match(spell.duration_type) || 'CONCENTRATION'.match(spell.duration_type) || 'SPECIAL'.match(spell.duration_type)">
                        {{ spell.duration_amount }} <span class="text-capitalize">{{ spell.duration_unit }}</span> <span v-if="'CONCENTRATION'.match(spell.duration_type)" class="mdi mdi-alpha-c-circle"></span>
                      </v-col>
                      <v-col v-else><span class="text-capitalize">{{ spell.duration_type }}</span></v-col>
                    </v-row>
                  </v-col>
                  <v-col cols="6" sm="4" lg="3">
                    <v-row no-gutters><v-col>SCHOOL</v-col></v-row>
                    <v-row no-gutters><v-col>{{ spell.school }}</v-col></v-row>
                  </v-col>
                  <v-col cols="6" sm="4" lg="3">
                    <v-row no-gutters><v-col>ATTACK/SAVE</v-col></v-row>
                    <v-row no-gutters>
                      <v-col v-if="spell.spell_additional_info && spell.spell_additional_info.save_type">{{ item.spell_additional_info.save_type }}</v-col>
                      <v-col v-else>-</v-col>
                    </v-row>
                  </v-col>
                  <v-col cols="6" sm="4" lg="3">
                    <v-row no-gutters><v-col>DAMAGE/EFFECT</v-col></v-row>
                    <v-row no-gutters>
                      <v-col v-if="spell.spell_additional_info && spell.spell_additional_info.tags && spell.spell_additional_info.tags.length > 0">
                        {{ spell.spell_additional_info.tags[0].tag }}
                      </v-col>
                      <v-col v-else>-</v-col>
                    </v-row>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-row>
              <v-col>
                {{ spell.description }}
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-row>
              <v-col v-if="spell.classes">
                Classes:
                <template v-for="id in spell.classes">
                  <v-chip :key="id" v-if="getClassFromId(id)">{{ getClassFromId(id).name }}</v-chip>
                </template>
              </v-col>
            </v-row>
            <v-row>
              <v-col v-if="spell.spell_additional_info && spell.spell_additional_info.tags">
                Tags:
                <template v-for="tag in spell.spell_additional_info.tags">
                  <v-chip :key="tag.tag">{{ tag.tag }}</v-chip>
                </template>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
    export default {
        head(){
            return {
                title: `AWM Project - ${this.spell.name}`
            };
        },

        data () {
            return {
                spell: {},
                characterclasses: [],
                spelltags: [],
                alert: null,
            }
        },

        async asyncData ( {$axios, params }) {
            try {
                let retval = {spell: {}, characterclasses: [], spelltags: []}
                let query_spell = await $axios.$get(`/spells/${params.id}`)
                let query_characterclasses = await $axios.$get(`/characterclasses/`)
                let query_spelltags = await $axios.$get(`/spelltags/`)

                console.log(query_spell)

                if (!query_spell || query_spell.id != params.id) {
                    return {
                        alert: {
                            type: 'error',
                            message: 'Requested spell not found'
                        }
                    }
                }
                //console.log(query_spell)
                retval.spell = query_spell
                retval.characterclasses = query_characterclasses.results
                retval.spelltags = query_spelltags.results
                return retval
            } catch (e) {
                if (e.response) {
                    console.log('spells/_id/index.vue asyncData() .catch e.response:', e.response)
                    if (e.response.status == 404)
                        return {
                            alert: {
                                type: 'error',
                                message: 'Requested spell not found'
                            }
                        }
                }

                console.log('spells/_id/index.vue asyncData() .catch e:', e)
                return {
                    alert: {
                        type: 'error',
                        message: 'An error occurred while retrieving information'
                    }
                }
            }
        },

        methods: {
            getClassFromId(id) {
                for (let i = 0; i < this.characterclasses.length; i++) {
                    if (this.characterclasses[i].id == id) {
                        return this.characterclasses[i]
                    }
                }
                // ID not found
                return null
            },

            deleteSpell() {
                if (this.canEdit()) {
                    this.$axios.$delete(`/spells/${this.$route.params.id}`)
                }
                this.returnToSpells()
            },

            editSpell() {
               this.$router.push(`/spells/${this.$route.params.id}/edit`)
            },

            canEdit() {
                try {
                    let userId = this.$store.state.auth.user.id
                    if (this.spell && this.spell.author) {
                        let spellAuthorId = this.$store.app.getResourceId(this.spell.author)
                        return (userId == spellAuthorId)
                    }
                }
                catch (e) {
                    console.log('spells/_id/index.vue canEdit() .catch e:', e)
                    return false
                }
                return false
            },

            returnToSpells () {
                this.$router.push(`/spells`)
            }

        }
    }
</script>

<style scoped>

</style>
