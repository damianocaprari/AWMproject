<template>
  <v-container fluid>
    <dice-roller></dice-roller>
    <v-divider vertical></v-divider>
    <initiative-tracker></initiative-tracker>
    <v-divider vertical></v-divider>
    <npc-generator></npc-generator>
  </v-container>
</template>

<script>
    import DiceRoller from "~/components/DiceRoller"
    import InitiativeTracker from "~/components/InitiativeTracker"
    import NpcGenerator from "~/components/NpcGenerator";
    export default {
        components: {
            DiceRoller,
            InitiativeTracker,
            NpcGenerator,
        },
    }
</script>

<style scoped>

</style>
