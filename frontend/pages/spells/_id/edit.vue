<template>
    <v-container fluid>
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
                spelltags: {},
                characterclasses: {},
            }
        },

        async asyncData({$axios, params}) {
            try {
                let query_spell = await $axios.$get(`/spells/${params.id}`)
                let query_characterclasses = await $axios.$get(`/characterclasses/`)
                let query_spelltags = await $axios.$get(`/spelltags/`)

                if (!query_spell) {
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
                console.log(e)
                return {
                    alert: {
                        type: 'error',
                        message: 'An error occurred while retrieving information',
                    }
                }
            }
        },

    }
</script>

<style scoped>

</style>
