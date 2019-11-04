<template>
    <v-form @submit.prevent="submit">
      <v-row>
        <v-col>
          <v-alert v-if="alert" :type="alert.type">{{ alert.message }}</v-alert>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" sm="6">
          <v-text-field v-model="spell.name" label="Name"/>
        </v-col>
        <v-spacer></v-spacer>
        <v-col align="center">
          <v-avatar tile size="160" class="mx-auto" color="grey">
            <v-hover v-slot:default="{ hover }">
              <v-img
                :src="spell_additional_info.avatar || '/images/image-placeholder.png'"
              >
                <v-expand-transition>
                  <div
                    v-if="hover"
                    class="d-flex transition-fast-in-fast-out grey darken-2 v-card--reveal white--text"
                    style="height: 100%;"
                    @click="pickImage"
                  >
                    Change
                    <input
                      type="file"
                      style="display: none"
                      ref="image"
                      accept="image/*"
                      @change="onImagePicked"
                    >
                  </div>
                </v-expand-transition>
              </v-img>
            </v-hover>
          </v-avatar>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="6">
          <v-select v-model="spell.level" :items="levelList" label="Level"></v-select>
        </v-col>
        <v-col cols="6">
          <v-select v-model="spell.school" :items="schoolList" label="School"></v-select>
        </v-col>

        <v-col cols="6">
          <v-text-field v-model="spell.casting_time_amount"
                        type="number"
                        label="Casting time amount"
          ></v-text-field>
        </v-col>
        <v-col cols="6">
          <v-select v-model="spell.casting_time_unit"
                    :items="castingTimeList"
                    label="Casting time unit"
          ></v-select>
        </v-col>
        <v-col cols="12" v-if="'REACTION' == spell.casting_time_unit">
          <v-text-field v-model="spell.casting_time_description"
                        label="Reaction Description"
          ></v-text-field>
        </v-col>

        <template v-if="spell.range_type == 'RANGED'">
          <v-col cols="6">
            <v-select v-model="spell.range_type"
                      :items="rangeList"
                      label="Range type"
            ></v-select>
          </v-col>
          <v-col cols="6" >
            <v-text-field v-model="spell.range_distance"
                          type="number"
                          label="Range distance (opt)"
            ></v-text-field>
          </v-col>
        </template>
        <template v-else>
          <v-col cols="12">
            <v-select v-model="spell.range_type"
                      :items="rangeList"
                      label="Range type"
            ></v-select>
          </v-col>
        </template>

        <template v-if="spell.duration_type == 'CONCENTRATION'
            || spell.duration_type == 'SPECIAL' || spell.duration_type == 'TIME'"
        >
          <v-col cols="12">
            <v-select v-model="spell.duration_type"
                      :items="durationList"
                      label="Duration type"
            ></v-select>
          </v-col>
          <v-col cols="6">
            <v-text-field v-model="spell.duration_amount"
                          type="number"
                          label="Duration amount (opt)"
            ></v-text-field>
          </v-col>
          <v-col cols="6">
            <v-select v-model="spell.duration_unit"
                      :items="durationUnitList"
                      label="Duration unit (opt)"
            ></v-select>
          </v-col>
        </template>
        <template v-else>
          <v-col cols="12">
            <v-select v-model="spell.duration_type"
                      :items="durationList"
                      label="Duration type"
            ></v-select>
          </v-col>
        </template>
      </v-row>

      <v-row no-gutters>
        <v-col cols="12" md="3">
          <v-checkbox v-model="spell.component_verbal" label="Component verbal"></v-checkbox>
        </v-col>
        <v-col cols="12" md="3">
          <v-checkbox v-model="spell.component_somatic" label="Component somatic"></v-checkbox>
        </v-col>
        <v-col cols="12" md="3">
          <v-checkbox v-model="spell.component_material" label="Component material"></v-checkbox>
        </v-col>
        <v-col cols="12" md="3" v-if="spell.component_material">
          <v-text-field v-model="spell.component_material_description"
          label="Component description"
          ></v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col>
          <v-text-field v-model="spell.description" label="Description" ></v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col>
          <v-select v-model="spell.classes"
                    :items="getCharacterclassesList()"
                    label="Character classes"
                    multiple
          ></v-select>
        </v-col>
      </v-row>

      <v-row>
        <v-col>
          <v-checkbox v-model="spell.ritual" label="Ritual"></v-checkbox>
        </v-col>
        <v-col>
          <v-checkbox v-model="spell.higher_level" label="Higher level"></v-checkbox>
        </v-col>
      </v-row>


      <v-row justify="center">
        <v-col class="text-center">
          <v-btn type="submit" outlined color="accent">Save</v-btn>
          <v-btn text color="accent" @click="returnToSpell">Cancel</v-btn>
        </v-col>
      </v-row>
    </v-form>
</template>

<script>
    export default {
        props: ['spell', 'spelltags', 'characterclasses'],
        data () {
            return {
                alert: null,
                spell_avatar_form_data : {},
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
                /*characterClassesList: [
                    {text: "Barbarian", value: 1},
                    {text: "Bard", value: 2},
                    {text: "Cleric", value: 3},
                    {text: "Druid", value: 4},
                    {text: "Fighter", value: 5},
                    {text: "Monk", value: 6},
                    {text: "Paladin", value: 7},
                    {text: "Ranger", value: 8},
                    {text: "Rogue", value: 9},
                    {text: "Sorcerer", value: 10},
                    {text: "Warlock", value: 11},
                    {text: "Wizard", value: 12}
                ],*/
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

            submit() {
                console.log(this.spell)

                // TODO ricorda this.spell_additional_info.avatar
            },

            returnToSpell() {
                this.$router.push(`/spells/${this.$route.params.id}`)
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
                        let form_data = new FormData()
                        form_data.append('avatar', files[0], files[0].name)

                        this.spell_avatar_form_data = {
                            form_data: form_data,
                            config: { headers: {'Content-Type': 'multipart/form-data'}}
                        }

                        console.log("Preparato spell_avatar_form_data da inviare con la form al submit")
                        console.log(this.spell_avatar_form_data)

                        this.spell_additional_info.avatar = fr.result
                    })
                } else {
                    this.spell_additional_info.avatar = '/images/image-placeholder.png'
                }
            }
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
