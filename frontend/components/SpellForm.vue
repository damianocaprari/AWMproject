<template>
  <v-container flui>
    <v-row justify="center" v-if="alert || form_alert">
      <v-col cols="12" v-if="alert">
        <v-alert :type="alert.type">{{ alert.message }}</v-alert>
      </v-col>
      <v-col cols="12" v-if="form_alert">
        <v-alert :type="form_alert.type">{{ form_alert.message }}</v-alert>
      </v-col>
    </v-row>

    <v-form @submit.prevent="submit">
      <v-row>
        <v-col cols="12" sm="6">
          <v-row no-gutters>
            <v-col cols="12">
              <v-text-field v-model="spell.name" label="Name *" :rules="rules.required"/>
            </v-col>
            <v-col cols="6">
              <v-text-field v-model="spell.version" label="Version"/>
            </v-col>
          </v-row>
        </v-col>
        <v-spacer></v-spacer>
        <v-col align="center">
          <v-avatar tile size="160" class="mx-auto" color="grey">
            <v-hover v-slot:default="{ hover }">
              <v-img :src="spell_additional_info.avatar || '/images/image-placeholder.png'">
                <v-expand-transition>
                  <div v-if="hover" class="d-flex transition-fast-in-fast-out grey darken-2 v-card--reveal white--text" style="height: 100%;" @click="pickImage">
                    Change
                    <input type="file" style="display: none" ref="image" accept="image/*" @change="onImagePicked">
                  </div>
                </v-expand-transition>
              </v-img>
            </v-hover>
          </v-avatar>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" sm="6">
          <v-row>
            <v-col cols="6">
              <v-select v-model="spell.level" :items="levelList" label="Level *" :rules="rules.requiredN"></v-select>
            </v-col>
            <v-col cols="6">
              <v-select v-model="spell.school" :items="schoolList" label="School *" :rules="rules.required"></v-select>
            </v-col>

            <v-col cols="6">
              <v-text-field v-model="spell.casting_time_amount" type="number" label="Casting time amount *" :rules="rules.requiredN"></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-select v-model="spell.casting_time_unit" :items="castingTimeList" label="Casting time unit *" :rules="rules.required"></v-select>
            </v-col>
            <v-col cols="12" v-if="'REACTION' == spell.casting_time_unit">
              <v-text-field v-model="spell.casting_time_description" label="Reaction Description"></v-text-field>
            </v-col>

            <template v-if="spell.range_type == 'RANGED'">
              <v-col cols="5">
                <v-select v-model="spell.range_type" :items="rangeList" label="Range type *" :rules="rules.required"></v-select>
              </v-col>
              <v-col cols="7">
                <v-text-field v-model="spell.range_distance" type="number" label="Range distance (ft)"></v-text-field>
              </v-col>
            </template>
            <template v-else>
              <v-col cols="6">
                <v-select v-model="spell.range_type" :items="rangeList" label="Range type *" :rules="rules.required"></v-select>
              </v-col>
            </template>

            <template v-if="spell.duration_type == 'CONCENTRATION' || spell.duration_type == 'SPECIAL' || spell.duration_type == 'TIME'">
              <v-col cols="12">
                <v-select v-model="spell.duration_type" :items="durationList" label="Duration type *" :rules="rules.required"></v-select>
              </v-col>
              <v-col cols="6">
                <v-text-field v-model="spell.duration_amount" type="number" label="Duration amount"></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-select v-model="spell.duration_unit" :items="durationUnitList" label="Duration unit"></v-select>
              </v-col>
            </template>
            <template v-else>
              <v-col cols="12">
                <v-select v-model="spell.duration_type" :items="durationList" label="Duration type *" :rules="rules.required"></v-select>
              </v-col>
            </template>
          </v-row>

          <v-row no-gutters>
            <v-col cols="4">
              <v-checkbox v-model="spell.component_verbal" label="Verbal" dense></v-checkbox>
            </v-col>
            <v-col cols="4">
              <v-checkbox v-model="spell.component_somatic" label="Somatic" dense></v-checkbox>
            </v-col>
            <v-col cols="4">
              <v-checkbox v-model="spell.component_material" label="Material" dense></v-checkbox>
            </v-col>
            <v-col cols="12" v-if="spell.component_material">
              <v-text-field v-model="spell.component_material_description" label="Component description"></v-text-field>
            </v-col>
          </v-row>

          <v-row class="d-sm-none"> <!-- show only for screen <600 px -->
            <v-col cols="12">
              <v-textarea v-model="spell.description" label="Description *" :rules="rules.required" counter="8000" auto-grow ></v-textarea>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="12">
              <v-select v-model="spell.classes" :items="getCharacterclassesList()" label="Character classes *" :rules="rules.required" multiple></v-select>
            </v-col>
            <v-col cols="6">
              <v-checkbox v-model="spell.ritual" label="Ritual"></v-checkbox>
            </v-col>
            <v-col cols="6">
              <v-checkbox v-model="spell.higher_level" label="Higher level"></v-checkbox>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="6" sm="6" class="d-none d-sm-block"> <!-- show only for screen >=600 px -->
          <v-row>
            <v-col cols="12">
              <v-textarea v-model="spell.description" v-html="" label="Description *" counter="8000" auto-grow height="588" filled :rules="rules.required"></v-textarea>
            </v-col>
          </v-row>
        </v-col>
      </v-row>

      <v-row justify="center">
        <v-col class="text-center">
          <v-btn type="submit" outlined color="accent">Save</v-btn>
          <v-btn text color="accent" @click="goBack">Cancel</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>
    export default {
        props: ['spell', 'spelltags', 'characterclasses', 'alert', 'edit'],
        data () {
            return {
                rules: {
                    required: [
                        v => !!v || 'Field is required'
                    ],
                    requiredN: [
                        v => (''+v).length > 0 || 'Field is required'
                    ]
                },
                form_alert: null,
                form_data_avatar_file : null,
                levelList: [
                    {text: "Cantrip", value: 0},
                    {text: "1st", value: 1},
                    {text: "2nd", value: 2},
                    {text: "3rd", value: 3},
                    {text: "4th", value: 4},
                    {text: "5th", value: 5},
                    {text: "6th", value: 6},
                    {text: "7th", value: 7},
                    {text: "8th", value: 8},
                    {text: "9th", value: 9}
                ],
                schoolList: [
                    {text: 'Abjuration', value: 'Abjuration'},
                    {text: 'Conjuration', value: 'Conjuration'},
                    {text: 'Divination', value: 'Divination'},
                    {text: 'Enchantment', value: 'Enchantment'},
                    {text: 'Evocation', value: 'Evocation'},
                    {text: 'Illusion', value: 'Illusion'},
                    {text: 'Necromancy', value: 'Necromancy'},
                    {text: 'Transmutation', value: 'Transmutation'},
                ],
                castingTimeList: [
                    {text: 'Action', value: 'ACTION'},
                    {text: 'Bonus Action', value: 'BONUS_ACTION'},
                    {text: 'Hour', value: 'HOUR'},
                    {text: 'Minute', value: 'MINUTE'},
                    {text: 'No Action', value: 'NO_ACTION'},
                    {text: 'Reaction', value: 'REACTION'},
                    {text: 'Special', value: 'SPECIAL'},
                ],
                rangeList: [
                    {text: 'Self', value: 'SELF'},
                    {text: 'Touch', value: 'TOUCH'},
                    {text: 'Ranged', value: 'RANGED'},
                    {text: 'Sight', value: 'SIGHT'},
                    {text: 'Unlimited', value: 'UNLIMITED'},
                ],
                durationList: [
                    {text: 'Concentration', value: 'CONCENTRATION'},
                    {text: 'Instantaneous', value: 'INSTANTANEOUS'},
                    {text: 'Special', value: 'SPECIAL'},
                    {text: 'Time', value: 'TIME'},
                    {text: 'Until Dispelled', value: 'UNTIL_DISPELLED'},
                    {text: 'Until Dispelled or Triggered', value: 'UNTIL_DISPELLED_OR_TRIGGERED'},
                ],
                durationUnitList: [
                    {text: 'Round', value: 'ROUND'},
                    {text: 'Minute', value: 'MINUTE'},
                    {text: 'Hour', value: 'HOUR'},
                    {text: 'Day', value: 'DAY'},
                ],
            }
        },

        computed: {
            spell_additional_info() {
                if (this.spell) {
                    if (this.spell.spell_additional_info) {
                        return this.spell.spell_additional_info
                    }
                }
                return {}
            },
        },

        methods: {
            getCharacterclassesList() {
                //console.log(this.characterclasses)
                let classes = []
                if (!!this.characterclasses) {
                    this.characterclasses.forEach(clazz => {
                        classes.push({value: clazz.id, text: clazz.name})
                    })
                }
                return classes
            },

            getSpelltagsList() {
                let tags = []
                if (!!this.spelltags) {
                    this.spelltags.forEach(tag => {
                        tags.push({value: tag.id, text: tag.tag})
                    })
                }
                return tags
            },

            submitEdit() {
                // copia i valori, non il puntatore all'oggetto
                let form = JSON.parse(JSON.stringify(this.spell))
                delete form['author']
                delete form['creation_time']
                delete form['custom_attributes']
                delete form['id']
                delete form['last_modified']
                delete form['url']
                delete form['spell_additional_info']

                this.$axios.$put(`/spells/${this.$route.params.id}/`, form)
                .then(data => {
                    console.log('/spells/_id/edit.vue $axios->spell OK', data)
                    if(!!this.form_data_avatar_file && !!data.spell_additional_info && !!data.spell_additional_info.id) {
                        let form_data = new FormData();
                        form_data.append('avatar', this.form_data_avatar_file, this.form_data_avatar_file.name)
                        this.$axios.$put(`/spell_additional_info/${data.spell_additional_info.id}/`,
                            form_data, {headers: {'Content-Type': 'multipart/form-data'}})
                            .then(data => {
                                console.log('/spells/_id/edit.vue $axios->spell_additional_info OK')
                                this.form_alert = {
                                    type: 'success',
                                    message: 'Success'
                                }
                            })
                            .catch(e => {
                                console.log('/spells/_id/edit.vue $axios->spell_additional_info ERROR:', e.response || e)
                                if (e.response && e.response.data) {
                                    this.form_alert = {
                                        type: 'error',
                                        message: this.handleErrorMsg(e.response.data)
                                    }
                                }
                            })
                    }
                    else {
                        this.form_alert = {
                            type: 'success',
                            message: 'Success'
                        }
                    }
                })
                .catch(e => {
                    console.log('/spells/_id/edit.vue $axios->spell ERROR:', e.response || e)
                    if (e.response && e.response.data) {
                        this.form_alert = {
                            type: 'error',
                            message: this.handleErrorMsg(e.response.data)
                        }
                    }
                })
            },

            submitAdd() {
                console.log('spell', this.spell)

                // copia i valori, non il puntatore all'oggetto
                let form = JSON.parse(JSON.stringify(this.spell))
                delete form['author']
                delete form['creation_time']
                delete form['custom_attributes']
                delete form['id']
                delete form['last_modified']
                delete form['url']
                form['spell_additional_info'] = {}

                console.log(form)

                this.$axios.$post(`/spells/`, form)
                .then(new_spell => {
                    console.log('/spells/_id/edit.vue $axios->spell OK', new_spell)
                    if(!!this.form_data_avatar_file && !!new_spell.spell_additional_info && !!new_spell.spell_additional_info.id) {
                        let form_data = new FormData();
                        form_data.append('avatar', this.form_data_avatar_file, this.form_data_avatar_file.name)
                        this.$axios.$put(`/spell_additional_info/${new_spell.spell_additional_info.id}/`,
                            form_data, {headers: {'Content-Type': 'multipart/form-data'}})
                            .then(spai => {
                                console.log('/spells/_id/edit.vue $axios->spell_additional_info OK')
                                this.$router.push(`/spells/${new_spell.id}`)
                            })
                            .catch(e => {
                                console.log('/spells/_id/edit.vue $axios->spell_additional_info ERROR:', e.response || e)
                                if (e.response && e.response.data) {
                                    this.form_alert = {
                                        type: 'error',
                                        message: this.handleErrorMsg(e.response.data)
                                    }
                                }
                            })
                    }
                    else {
                        this.$router.push(`/spells/${new_spell.id}`)
                    }
                })
                .catch(e => {
                    console.log('/spells/_id/edit.vue $axios->spell ERROR:', e.response || e)
                    if (e.response && e.response.data) {
                        this.form_alert = {
                            type: 'error',
                            message: this.handleErrorMsg(e.response.data)
                        }
                    }
                })
            },

            handleErrorMsg(data) {
                if (data.name) return `Error with "name": ${data.name[0]}`
                if (data.level) return `Error with "level": ${data.level[0]}`
                if (data.school) return `Error with "school": ${data.school[0]}`
                if (data.casting_time_amount) return `Error with "casting_time_amount": ${data.casting_time_amount[0]}`
                if (data.casting_time_unit) return `Error with "casting_time_unit": ${data.casting_time_unit[0]}`
                if (data.range_type) return `Error with "range_type": ${data.range_type[0]}`
                if (data.duration_type) return `Error with "duration_type": ${data.duration_type[0]}`
                if (data.description) return `Error with "description": ${data.description[0]}`
                if (data.non_field_errors) return `Error: ${data.non_field_errors[0]}`
                return `Error`
            },

            submit() {
                if (this.edit) {
                    this.submitEdit()
                }
                else {
                    this.submitAdd()
                }
            },

            returnToSpell() {
                this.$router.push(`/spells/${this.$route.params.id}`)
            },

            returnToSpells() {
                this.$router.push(`/spells`)
            },

            goBack() {
                if (this.edit) {
                    this.returnToSpell()
                }
                else {
                    this.returnToSpells()
                }
            },

            pickImage() {
                this.$refs.image.click()
            },

            onImagePicked (e) {
                const files = e.target.files
                if(files[0] !== undefined) {
                    if(files[0].name.lastIndexOf('.') <= 0) {
                        console.log('/components/SpellForm.vue onImagePicked() files[0].name.lastIndexOf(\'.\') <= 0')
                        return
                    }
                    const fr = new FileReader ()
                    fr.readAsDataURL(files[0])
                    fr.addEventListener('load', () => {
                        this.form_data_avatar_file = files[0]
                        this.spell_additional_info.avatar = fr.result
                    })
                }
            },
        },
    }
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
