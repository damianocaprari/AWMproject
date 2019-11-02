<template>
  <v-container fluid>
    <dice-roller></dice-roller>
    <v-divider vertical></v-divider>
    <initiative-tracker></initiative-tracker>
  </v-container>
</template>

<script>
    import DiceRoller from "~/components/DiceRoller"
    import InitiativeTracker from "~/components/InitiativeTracker"
    export default {
        components: {
            DiceRoller,
            InitiativeTracker,
        },
    }
</script>

<style scoped>

</style>
