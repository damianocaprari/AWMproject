<template>
    <v-container class="my-5">
        <v-container class="row">
            <v-container class="col-md-12 my-3">
                <h2 class="mb-3 text-uppercase">new Spell</h2>
            </v-container>

            <v-container>
                <v-form @submit.prevent="submit">
                    <!--<v-alert v-if="alert" :type="alert.type">{{ alert.message }}</v-alert>-->
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
                            <!--<v-btn text color="accent" @click="resetFormData">Cancel</v-btn>-->
                        </v-col>
                    </v-row>
                </v-form>

            </v-container>
        </v-container>
    </v-container>
</template>

<script>
    import api from '~/api'

    export default {

        head() {
            return {
                title: "Add Spell"
            };
        },
        data() {
            return {
                spell: {
                    name: "",
                    version: null,
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
                    spell_additional_info: null,

                },

                preview: "",

                levelList: [
                    {text: "Cantrip", value: 0},
                    {text: "1", value: 1},
                    {text: "2", value: 2},
                    {text: "3", value: 3},
                    {text: "4", value: 4},
                    {text: "5", value: 5},
                    {text: "6", value: 6},
                    {text: "7", value: 7},
                    {text: "8", value: 8},
                    {text: "9", value: 9}
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
                booleanList: [
                    {text: 'True', value: 'true'},
                    {text: 'False', value: 'false'}
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
                characterClassesList: [
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
                ],

            };
        },
        methods: {
            submit() {
                this.alert = null
                this.loading = true
                console.log(this.spell)

                this.spell.casting_time_amount = Number(this.spell.casting_time_amount)
                this.spell.duration_amount = Number(this.spell.duration_amount)

                console.log(JSON.stringify(this.spell))

                api.createSpell(this.$axios, this.spell)
                    .then(result => {
                        //console.log('/account/index.vue .then() result', result)
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
        }
    };

</script>


<style scoped>
</style>
