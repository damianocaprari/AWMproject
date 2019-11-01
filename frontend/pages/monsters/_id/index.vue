<template>
    <v-container>
        <h1>{{ monster.name }}</h1>

        <!-- TODO: add image-->
        <!-- TODO: togli virgole nei for -->

        <v-container>
            <v-row>
                <span>{{monster.size}} </span>
                <span v-if="monster.type != null">, {{monster.type}}</span>
                <span v-if="monster.subtype != null">, {{monster.subtype}}</span>
            </v-row>

            <v-divider></v-divider>

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
                <span v-for="item in monster.speeds" :key="item.id">{{item.speed}}, </span>
            </v-row>

            <v-divider></v-divider>

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

            <v-divider></v-divider>

            <v-row v-if="monster.saves.length > 0">
                <span class="boldedname">Saving throws: </span>
                <span v-for="item in monster.saves" :key="item.id">{{item.name}} +{{item.modifier}}, </span>
            </v-row>

            <v-row v-if="monster.skills.length > 0">
                <span class="boldedname">Skills: </span>
                <span v-for="item in monster.skills" :key="item.id">{{item.name}} +{{item.modifier}}, </span>
            </v-row>

            <v-row v-if="monster.senses.length > 0">
                <span class="boldedname">Senses: </span>
                <span v-for="item in monster.senses" :key="item.id">{{item.sense}} , </span>
            </v-row>

            <v-row v-if="monster.languages.length > 0">
                <span class="boldedname">Languages: </span>
                <span v-for="item in monster.languages" :key="item.id">{{item.language}} , </span>
            </v-row>

            <v-row>
                <span class="boldedname">Challenge Rating: </span>
                <span>{{monster.challenge_rating}}</span>
            </v-row>

            <v-divider></v-divider>

        </v-container>

        <v-container v-if="monster.traits.length > 0">
            <v-row class="subtitle">Traits</v-row>
            <v-row v-for="item in monster.traits" :key="item.id">
                <v-col>
                <v-row class="boldedname inline">{{item.name}} </v-row>
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

        <v-container v-if="monster.legendary_actions.length > 0">
            <v-row class="subtitle">Legendary Actions</v-row>
            <v-row class="mb-3" v-for="item in monster.legendary_actions" :key="item.id">
                <v-col>
                    <v-row class="boldedname">{{item.name}}</v-row>
                    <v-row class="text-justify">{{item.content}}</v-row>
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
        margin-right: 4px
    }
    
    .subtitle {
        font-size: 30px;
        font-weight: bold;
    }
</style>