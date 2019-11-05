<template>
  <v-container v-if="canEdit()">
    <spell-form
      :spell="spell"
      :spelltags="spelltags"
      :characterclasses="characterclasses"
      :alert="alert"
    ></spell-form>
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
                    let userId = this.$store.state.auth.user.id
                    if (this.spell && this.spell.author) {
                        let spellAuthorId = this.$store.app.getResourceId(this.spell.author)
                        if (userId == spellAuthorId)
                            return true
                    }
                }
                catch (e) {
                    console.log('spells/_id/edit.vue canEdit() .catch e:', e)
                }
                this.$router.push('/')
            },
        }

    }
</script>

<style scoped>

</style>
