<template>
  <v-container>
    <spell-form v-if="canEdit()"
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
</template>

<script>
    import SpellForm from "~/components/SpellForm";
    export default {
        components: {
            SpellForm,
        },
        data () {
            return {
                alert: null,
                spell: {},
                spelltags: [],
                characterclasses: [],
            }
        },

        async asyncData({$axios, params}) {
            try {
                let query_spell = await $axios.$get(`/spells/${params.id}`)
                let query_characterclasses = await $axios.$get(`/characterclasses/`)
                let query_spelltags = await $axios.$get(`/spelltags/`)

                if (!query_spell || query_spell.id != params.id) {
                    return {
                        alert: {
                            type: 'error',
                            message: 'Selected spell does not exist'
                        }
                    }
                }

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
                    spell: query_spell,
                    characterclasses: query_characterclasses.results,
                    spelltags: query_spelltags.results || {},
                }
            }
            catch (e) {
                if (e.response) {
                    console.log('spells/_id/edit.vue asyncData() .catch e.response:', e.response)
                    if (e.response.status == 404)
                        return {
                            alert: {
                                type: 'error',
                                message: 'Requested spell not found'
                            }
                        }
                }
                console.log('spells/_id/edit.vue asyncData() .catch e:', e)
                return {
                    alert: {
                        type: 'error',
                        message: 'An error occurred while retrieving information'
                    }
                }
            }
        },

        methods: {
            canEdit() {
                try {
                    let user = this.$store.state.auth.user
                    if (!user) {
                        this.alert = {
                            type: 'error',
                            message: 'Sign In to edit this spell'
                        }
                        return false
                    }
                    if (this.spell && this.spell.author) {
                        let spellAuthorId = this.$store.app.getResourceId(this.spell.author)
                        if (user.id == spellAuthorId)
                            return true
                    }
                }
                catch (e) {
                    console.log('spells/_id/edit.vue canEdit() .catch e:', e)
                }
                this.alert = {
                    type: 'error',
                    message: 'You do not have the permission to edit this spell'
                }
                return false
            },

            returnToSpells() {
                this.$router.push(`/spells`)
            },

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

                this.$axios.$put(`/spells/${this.$route.params.id}/`, form)
                .then(data => {
                    console.log("tutto ok")
                })
                .catch(e => {
                    if (e.response)
                        console.log(e.response)
                    else
                        console.log(e)
                })

                if(!!this.form_data_avatar_file && !!this.spell.spell_additional_info && !!this.spell.spell_additional_info.id) {
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
        }

    }
</script>

<style scoped>

</style>
