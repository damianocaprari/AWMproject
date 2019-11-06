<template>
  <v-container>
    <spell-form v-if="canAdd()"
      :spell="spell"
      :spelltags="spelltags"
      :characterclasses="characterclasses"
      :alert="alert"
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
</template>

<script>
    import api from '~/api'
    import SpellForm from "~/components/SpellForm";

    export default {

        head() {
            return {
                title: "AWM Project - Add Spell"
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
                    version: "",

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
                console.log('spells/_id/edit.vue asyncData() .catch e.response:', e.response || e)
                return {
                    alert: {
                        type: 'error',
                        message: 'An error occurred while retrieving information'
                    }
                }
            }
        },

        methods: {
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
