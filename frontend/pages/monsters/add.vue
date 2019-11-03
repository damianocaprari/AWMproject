<template>
    <v-container class="my-5">
        <v-container class="row">
            <v-container class="col-md-12 my-3">
                <h2 class="mb-3 text-uppercase">new Monster</h2>
            </v-container>


            <v-container>
                <v-form @submit.prevent="submit">
                    <!--<v-alert v-if="alert" :type="alert.type">{{ alert.message }}</v-alert>-->
                    <v-text-field v-model="monster.name" label="Name"/>
                    <v-select v-model="monster.size" :items="sizeList" label="Size"></v-select>
                    <v-select v-model="monster.alignment" :items="alignmentList" label="Alignment"></v-select>
                    <v-text-field v-model="monster.armor_class" type="number" label="Armor Class"></v-text-field>
                    <v-select v-model="monster.challenge_rating" :items="CRList" label="Challenge rating - CR"></v-select>
                    <v-text-field v-model="monster.hit_point" type="number" label="Hit points"></v-text-field>
                    <v-select v-model="monster.hit_dice" :items="hitDiceList" label="Hit Dice"></v-select>

                    <v-row>
                        <v-col>
                            <v-text-field v-model="monster.ability_str" type="number" label="STRENGTH"></v-text-field>
                            <v-text-field v-model="monster.ability_dex" type="number" label="DEXTERITY"></v-text-field>
                            <v-text-field v-model="monster.ability_con" type="number" label="CONSTITUTION"></v-text-field>
                        </v-col>
                        <v-col>
                            <v-text-field v-model="monster.ability_int" type="number" label="INTELLIGENCE"></v-text-field>
                            <v-text-field v-model="monster.ability_wis" type="number" label="WISDOM"></v-text-field>
                            <v-text-field v-model="monster.ability_cha" type="number" label="CHARISMA"></v-text-field>
                        </v-col>
                    </v-row>

                    <!--
                    <v-container class="form-group">
                        <v-row>Monster image</v-row>
                        <input type="file" name="file" @change="onFileChange">
                    </v-container>
                    -->


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
                title: "Add Monster"
            };
        },
        data() {
            return {
                monster: {
                    name: "",
                    image: null,
                    version: "",
                    size: "",
                    type: "",
                    subtype: "",
                    alignment: "",
                    armor_class: null,
                    armor_class_notes: "",
                    hit_point: null,
                    hit_dice: "",
                    ability_str: 0,
                    ability_dex: 0,
                    ability_con: 0,
                    ability_int: 0,
                    ability_wis: 0,
                    ability_cha: 0,
                    challenge_rating: "",
                    creation_time: "",
                    last_modified: "",
                    actions: [],
                    speeds: [],
                    saves: [],
                    skills: [],
                    damage_vulnerabilities: [],
                    damage_resistances: [],
                    condition_immunities: [],
                    damage_immunities: [],
                    languages: [],
                    reactions: [],
                    senses: [],
                    special_abilities: [],
                    traits: [],
                    legendary_actions: [],
                    custom_attributes: []
                },

                preview: "",

                CRList: [
                    {text: "All", value: null},
                    {text: "1/8", value: "1/8"},
                    {text: "1/4", value: "1/4"},
                    {text: "1/2", value: "1/2"},
                    {text: "1", value: "1"},
                    {text: "2", value: "2"},
                    {text: "3", value: "3"},
                    {text: "4", value: "4"},
                    {text: "5", value: "5"},
                    {text: "6", value: "6"},
                    {text: "7", value: "7"},
                    {text: "8", value: "8"},
                    {text: "9", value: "9"},
                    {text: "10", value: "10"},
                    {text: "11", value: "11"},
                    {text: "12", value: "12"},
                    {text: "13", value: "13"},
                    {text: "14", value: "14"},
                    {text: "15", value: "15"},
                    {text: "16", value: "16"},
                    {text: "17", value: "17"},
                    {text: "18", value: "18"},
                    {text: "19", value: "19"},
                    {text: "20", value: "20"},
                ],
                sizeList: [
                    {text: "Fine", value: "Fine"},
                    {text: "Diminutive", value: "Diminutive"},
                    {text: "Tiny", value: "Tiny"},
                    {text: "Small", value: "Small"},
                    {text: "Medium", value: "Medium"},
                    {text: "Large", value: "Large"},
                    {text: "Huge", value: "Huge"},
                    {text: "Gargantuan", value: "Gargantuan"},
                    {text: "Colossal", value: "Colossal"},
                ],
                alignmentList: [
                    {text: 'Lawful Good', value: 'Lawful Good'},
                    {text: 'Neutral Good', value: 'Neutral Good'},
                    {text: 'Chaotic Good', value: 'Chaotic Good'},
                    {text: 'Lawful Neutral', value: 'Lawful Neutral'},
                    {text: 'True Neutral', value: 'True Neutral'},
                    {text: 'Chaotic Neutral', value: 'Chaotic Neutral'},
                    {text: 'Lawful Evil', value: 'Lawful Evil'},
                    {text: 'Neutral Evil', value: 'Neutral Evil'},
                    {text: 'Chaotic Evil', value: 'Chaotic Evil'},
                ],
                hitDiceList: [
                    {text: '1d3', value: '1d3'},
                    {text: '1d4', value: '1d4'},
                    {text: '1d6', value: '1d6'},
                    {text: '1d8', value: '1d8'},
                    {text: '1d10', value: '1d10'},
                    {text: '1d12', value: '1d12'},
                ]

            };
        },
        methods: {
            submit() {
                this.alert = null
                this.loading = true
                console.log(this.monster)

                this.monster.armor_class = Number(this.monster.armor_class)
                console.log(this.monster.armor_class)

                this.monster.hit_point = Number(this.monster.hit_point)
                this.monster.ability_str = Number(this.monster.ability_str)
                this.monster.ability_dex = Number(this.monster.ability_dex)
                this.monster.ability_con = Number(this.monster.ability_con)
                this.monster.ability_int = Number(this.monster.ability_int)
                this.monster.ability_wis = Number(this.monster.ability_wis)
                this.monster.ability_cha = Number(this.monster.ability_cha)

                console.log(JSON.stringify(this.monster))

                api.createMonster(this.$axios, this.monster)
                    .then(result => {
                        //console.log('/account/index.vue.OLD .then() result', result)
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

            /*
            onFileChange(e) {
                let files = e.target.files || e.dataTransfer.files;
                if (!files.length) {
                    return;
                }
                this.recipe.image = files[0];
                this.createImage(files[0]);
            },
            createImage(file) {
                // let image = new Image();
                let reader = new FileReader();
                let vm = this;
                reader.onload = e => {
                    vm.preview = e.target.result;
                };
                reader.readAsDataURL(file);
            },
            async submitRecipe() {
                const config = {
                    headers: {"content-type": "multipart/form-data"}
                };
                let formData = new FormData();
                for (let data in this.recipe) {
                    formData.append(data, this.recipe[data]);
                }
                try {
                    let response = await this.$axios.$post("/recipes/", formData, config);
                    this.$router.push("/recipes/");
                } catch (e) {
                    console.log(e);
                }

            }
            */
        }
    };

</script>


<style scoped>
</style>
