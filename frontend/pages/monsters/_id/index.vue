<template>
    <v-container>
        <h1>{{ monster.name }}</h1>

        <v-divider></v-divider>

        <v-container>
            <v-row>

                <v-col>
                    <v-row>
                        <span>{{monster.size}} </span>
                        <span v-if="monster.type != null">, {{monster.type}}</span>
                        <span v-if="monster.subtype != null">, {{monster.subtype}}</span>
                    </v-row>

                    <v-row>
                        <span class="boldedname">Armor Class:</span>
                        <span>{{monster.armor_class}}</span>
                        <span v-if="monster.armor_class_notes != null"> ({{monster.armor_class_notes}})</span>
                    </v-row>

                    <v-row>
                        <span class="boldedname">Hit Points:</span>
                        <span>{{monster.hit_point}} ({{monster.hit_dice}})</span>
                    </v-row>


                    <v-row v-if="monster.speeds.length > 0">
                        <span class="boldedname">Speed:</span>
                        <span v-for="(item, index) in monster.speeds" :key="item.id">
                            {{item.value}}
                            <span v-if="index+1 < monster.speeds.length">,</span>
                         </span>
                    </v-row>

                    <v-row>
                        <v-col>
                            <v-row>STR</v-row>
                            <v-row>{{monster.ability_str}}</v-row>
                        </v-col>
                        <v-col>
                            <v-row>DEX</v-row>
                            <v-row>{{monster.ability_dex}}</v-row>
                        </v-col>
                        <v-col>
                            <v-row>CON</v-row>
                            <v-row>{{monster.ability_con}}</v-row>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col>
                            <v-row>INT</v-row>
                            <v-row>{{monster.ability_int}}</v-row>
                        </v-col>
                        <v-col>
                            <v-row>WIS</v-row>
                            <v-row>{{monster.ability_wis}}</v-row>
                        </v-col>
                        <v-col>
                            <v-row>CHA</v-row>
                            <v-row>{{monster.ability_cha}}</v-row>
                        </v-col>
                    </v-row>
                </v-col>

                <v-col v-if="monster.image != null">
                    <v-img
                            :src="monster.image"
                            max-width="250">
                    </v-img>
                </v-col>


            </v-row>


            <v-divider></v-divider>

            <v-row v-if="monster.saves.length > 0">
                <span class="boldedname">Saving throws: </span>
                <span v-for="(item, index) in monster.saves" :key="item.id">
                    {{item.name}} +{{item.modifier}}
                    <span v-if="index+1 < monster.saves.length">,</span>
                </span>
            </v-row>

            <v-row v-if="monster.skills.length > 0">
                <span class="boldedname">Skills: </span>
                <span v-for="(item, index) in monster.skills" :key="item.id">
                    {{item.name}} +{{item.modifier}}
                    <span v-if="index+1 < monster.skills.length">,</span>
                </span>
            </v-row>

            <v-row v-if="monster.senses.length > 0">
                <span class="boldedname">Senses: </span>
                <span v-for="(item, index) in monster.senses" :key="item.id">
                    {{item.sense}}
                    <span v-if="index+1 < monster.senses.length">,</span>
                    </span>
            </v-row>

            <v-row v-if="monster.languages.length > 0">
                <span class="boldedname">Languages: </span>
                <span v-for="(item, index) in monster.languages" :key="item.id">
                    {{item.language}}
                    <span v-if="index+1 < monster.languages.length">,</span>
                </span>
            </v-row>

            <v-row>
                <span class="boldedname">Challenge Rating: </span>
                <span>{{monster.challenge_rating}}</span>
            </v-row>


            <v-row v-if="monster.damage_vulnerabilities.length > 0">
                <span class="boldedname">Damage Vulnerabilities: </span>
                <span v-for="(item, index) in monster.damage_vulnerabilities" :key="item.id">
                    {{item.damage_vulnerability}}
                    <span v-if="index+1 < monster.damage_vulnerabilities.length">,</span>
                </span>
            </v-row>
            <v-row v-if="monster.damage_resistances.length > 0">
                <span class="boldedname">Damage Resistances: </span>
                <span v-for="(item, index) in monster.damage_resistances" :key="item.id">
                    {{item.damage_resistance}}
                    <span v-if="index+1 < monster.damage_resistances.length">,</span>
                </span>
            </v-row>
            <v-row v-if="monster.condition_immunities.length > 0">
                <span class="boldedname">Condition Immunities: </span>
                <span v-for="(item, index) in monster.condition_immunities" :key="item.id">
                    {{item.condition_immunity}}
                    <span v-if="index+1 < monster.condition_immunities.length">,</span>
                </span>
            </v-row>
            <v-row v-if="monster.damage_immunities.length > 0">
                <span class="boldedname">Damage Immunities: </span>
                <span v-for="(item, index) in monster.damage_immunities" :key="item.id">
                    {{item.damage_immunity}}
                    <span v-if="index+1 < monster.damage_immunities.length">,</span>
                </span>
            </v-row>
            <v-divider></v-divider>
        </v-container>

        <v-container v-if="monster.traits.length > 0">
            <v-row class="subtitle">Traits</v-row>
            <v-row v-for="item in monster.traits" :key="item.id">
                <v-col>
                    <v-row class="boldedname inline">{{item.name}}</v-row>
                    <v-row class="text-justify">{{item.content}}</v-row>
                </v-col>
            </v-row>
        </v-container>

        <v-container v-if="monster.actions.length > 0">
            <v-row class="subtitle">Actions</v-row>
            <v-row class="mb-3" v-for="item in monster.actions" :key="item.id">
                <v-col>
                    <v-row class="boldedname">{{item.name}}</v-row>
                    <v-row class="text-justify">{{item.desc}}</v-row>
                </v-col>
            </v-row>
        </v-container>

        <v-container v-if="monster.reactions.length > 0">
            <v-row class="subtitle">Reactions</v-row>
            <v-row class="mb-3" v-for="item in monster.reactions" :key="item.id">
                <v-col>
                    <v-row class="boldedname">{{item.name}}</v-row>
                    <v-row class="text-justify">{{item.content}}</v-row>
                </v-col>
            </v-row>
        </v-container>

        <v-container v-if="monster.special_abilities.length > 0">
            <v-row class="subtitle">Special Abilities</v-row>
            <v-row class="mb-3" v-for="item in monster.special_abilities" :key="item.id">
                <v-col>
                    <v-row class="boldedname">{{item.name}}</v-row>
                    <v-row class="text-justify">{{item.desc}}</v-row>
                </v-col>
            </v-row>
        </v-container>

        <v-container v-if="monster.legendary_actions.length > 0">
            <v-row class="subtitle">Legendary Actions</v-row>
            <v-row class="mb-3" v-for="item in monster.legendary_actions" :key="item.id">
                <v-col>
                    <v-row class="boldedname">{{item.name}}</v-row>
                    <v-row class="text-justify">{{item.content}}</v-row>
                </v-col>
            </v-row>
        </v-container>

        <v-container v-if="monster.custom_attributes.length > 0">
            <v-row class="subtitle">Custom Attributes</v-row>
            <v-row class="mb-3" v-for="item in monster.custom_attributes" :key="item.id">
                <v-col>
                    <v-row class="boldedname">{{item.name}}</v-row>
                    <v-row class="text-justify">{{item.value}}</v-row>
                </v-col>
            </v-row>
        </v-container>

    </v-container>

</template>


<script>
    export default {
        head() {
            return {
                title: "View Monster"
            };
        },
        async asyncData({$axios, params}) {
            try {
                let monster = await $axios.$get(`/monsters/${params.id}`);
                return {monster};
            } catch (e) {
                return {monster: []};
            }
        },
        data() {
            return {
                monster: {}
            };
        }
    };

</script>

<style scoped>
    .boldedname {
        font-weight: bold
    }

    span {
        margin-right: 3px
    }

    .subtitle {
        font-size: 30px;
        font-weight: bold;
    }

</style>