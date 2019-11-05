<template>
  <v-container>
    <spell-form v-if="canAdd()"
      :spell="spell"
      :spelltags="spelltags"
      :characterclasses="characterclasses"
      :alert="alert"
      :submit="submit"
    ></spell-form>

    <v-row justify="center" v-else>
      <v-col cols="12">
        <v-alert :type="alert.type">{{ alert.message }}</v-alert>
      </v-col>

      <v-col class="text-center">
        <v-btn class="accent onaccent--text" @click="returnToSpells">Back to spells</v-btn>
      </v-col>
    </v-row>
  </v-container>
  <!--
    <v-container fluid class="my-5">
        <v-container class="row">
            <v-container class="col-md-12 my-3">
                <h2 class="mb-3 text-uppercase">new Spell</h2>
            </v-container>

            <v-container>
                <v-form @submit.prevent="submit">
                    <v-text-field v-model="spell.name" label="Name"/>
                    <v-row>
                        <v-col>
                            <v-select v-model="spell.level" :items="levelList" label="Level"></v-select>
                        </v-col>
                        <v-col>
                            <v-select v-model="spell.school" :items="schoolList" label="School"></v-select>
                        </v-col>
                    </v-row>

                    <v-row>
                        <v-col cols="12" md="4">
                            <v-text-field v-model="spell.casting_time_amount" type="number"
                                          label="Casting time amount"></v-text-field>
                        </v-col>
                        <v-col cols="12" md="4">
                            <v-select v-model="spell.casting_time_unit" :items="castingTimeList"
                                      label="Casting time unit"></v-select>
                        </v-col>
                        <v-col cols="12" md="4">
                            <v-text-field v-model="spell.casting_time_description"
                                          label="Casting time description (opt)"/>
                        </v-col>
                    </v-row>

                    <v-row>
                        <v-col cols="12" md="3">
                            <v-select v-model="spell.component_verbal" :items="booleanList"
                                      label="Component verbal"></v-select>
                        </v-col>
                        <v-col cols="12" md="3">
                            <v-select v-model="spell.component_somatic" :items="booleanList"
                                      label="Component somatic"></v-select>
                        </v-col>
                        <v-col cols="12" md="3">
                            <v-select v-model="spell.component_material" :items="booleanList"
                                      label="Component material"></v-select>
                        </v-col>
                        <v-col cols="12" md="3">
                            <v-text-field v-model="spell.component_material_description"
                                          label="Component description (opt)"/>
                        </v-col>
                    </v-row>

                    <v-row>
                        <v-col cols="12" md="6">
                            <v-select v-model="spell.range_type" :items="rangeList" label="Range type"></v-select>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-text-field v-model="spell.range_distance" type="number"
                                          label="Range distance (opt)"/>
                        </v-col>
                    </v-row>

                    <v-row>
                        <v-col cols="12" md="4">
                            <v-select v-model="spell.duration_type" :items="durationList"
                                      label="Duration type"></v-select>
                        </v-col>
                        <v-col cols="12" md="4">
                            <v-text-field v-model="spell.duration_amount"
                                          type="number"
                                          label="Duration amount (opt)"/>
                        </v-col>
                        <v-col cols="12" md="4">
                            <v-select v-model="spell.duration_unit" :items="durationUnitList"
                                      label="Duration unit (opt)"></v-select>
                        </v-col>
                    </v-row>

                    <v-text-field v-model="spell.description" label="Description"/>

                    <v-row>
                        <v-col>
                            <v-select v-model="spell.ritual" :items="booleanList"
                                      label="Ritual"></v-select>
                        </v-col>
                        <v-col>
                            <v-select v-model="spell.higher_level" :items="booleanList"
                                      label="Higher level"></v-select>
                        </v-col>
                    </v-row>

                    <v-row>
                        <v-col>
                            <v-select v-model="spell.classes"
                                      :items="characterClassesList"
                                      label="Character classes"
                                      multiple
                                      ></v-select>

                        </v-col>
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
  -->
</template>

<script>
    import api from '~/api'
    import SpellForm from "~/components/SpellForm";

    export default {

        head() {
            return {
                title: "Add Spell"
            };
        },

        components: {
            SpellForm,
        },

        data() {
            return {
                alert: null,
                spelltags: [],
                characterclasses: [],
                spell: {
                    name: "",
                    level: "",
                    school: "",
                    casting_time_amount: "",
                    casting_time_unit: "",
                    casting_time_description: null,
                    component_verbal: false,
                    component_somatic: false,
                    component_material: false,
                    component_material_description: null,
                    range_type: "",
                    range_distance: null,
                    duration_type: "",
                    duration_amount: null,
                    duration_unit: null,
                    description: "",
                    ritual: false,
                    higher_level: false,

                    classes: [],
                    spell_additional_info: {},
                },
            }
        },

        async asyncData({$axios, params}) {
            try {
                let query_characterclasses = await $axios.$get(`/characterclasses/`)
                let query_spelltags = await $axios.$get(`/spelltags/`)

                if (!query_characterclasses.count > 0) {
                    return {
                        alert: {
                            type: 'error',
                            message: 'An error occurred while retrieving information',
                        }
                    }
                }

                if (!query_spelltags.count > 0) {
                    return {
                        alert: {
                            type: 'error',
                            message: 'An error occurred while retrieving information',
                        }
                    }
                }

                return {
                    characterclasses: query_characterclasses.results,
                    spelltags: query_spelltags.results || {},
                }
            }
            catch (e) {
                if (e.response) {
                    console.log('spells/_id/edit.vue asyncData() .catch e.response:', e.response)
                }
                else {
                    console.log('spells/_id/edit.vue asyncData() .catch e:', e)
                }
                return {
                    alert: {
                        type: 'error',
                        message: 'An error occurred while retrieving information'
                    }
                }
            }
        },

        methods: {
            submit() {
                console.log('spell', this.spell)

                // copia i valori, non il puntatore all'oggetto
                let form = JSON.parse(JSON.stringify(this.spell))
                delete form['author']
                delete form['creation_time']
                delete form['custom_attributes']
                delete form['id']
                delete form['last_modified']
                delete form['url']
                delete form['spell_additional_info']

                let spell_id = null

                this.$axios.$post('/spells/', form)
                .then(data => {
                    console.log("tutto ok", data)
                    spai_id = data.spell_additional_info.id
                })
                .catch(e => {
                    if (e.response)
                        console.log(e.response)
                    else
                        console.log(e)
                })


                if(!!spell_id && !!this.form_data_avatar_file && !!this.spell.spell_additional_info && !!this.spell.spell_additional_info.id) {
                    let form_data = new FormData();
                    form_data.append('avatar', this.form_data_avatar_file, this.form_data_avatar_file.name)
                    this.$axios.$put(`/spell_additional_info/${this.spell.spell_additional_info.id}/`,
                        form_data, {headers: {'Content-Type': 'multipart/form-data'}})
                        .then(data => {
                            console.log(data)
                        })
                        .catch(e => {
                            console.log(e.response)
                        })
                }
            },

            /*
            submit() {
                this.alert = null
                this.loading = true
                console.log(this.spell)

                this.spell.casting_time_amount = Number(this.spell.casting_time_amount)
                this.spell.duration_amount = Number(this.spell.duration_amount)

                console.log(JSON.stringify(this.spell))

                api.createSpell(this.$axios, this.spell)
                    .then(result => {
                        //console.log('/account/edit.vue.OLD .then() result', result)
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
            },
             */

            canAdd() {
                try {
                    let user = this.$store.state.auth.user
                    if (!user) {
                        this.alert = {
                            type: 'error',
                            message: 'Sign In to create a spell'
                        }
                        return false
                    }
                    else {
                        return true
                    }
                }
                catch (e) {
                    console.log('spells/_id/edit.vue canEdit() .catch e:', e)
                }
                this.alert = {
                    type: 'error',
                    message: 'You do not have the permission create a spell'
                }
                return false
            },

            returnToSpells() {
                this.$router.push(`/spells`)
            },
        }
    };

</script>


<style scoped>
</style>
