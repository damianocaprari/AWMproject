<!--
  TODO: Creare SpellCard con poche info.
  TODO: ritornare info di spell dalla API
  TODO: fai i filtri ricerca
  TODO: Creare pagina singola per la spell (recipes) o che si apra una tendina

  TODO DAMI: se metto NON RANGED io non dovrei mettere la distanza
-->
<template>
    <v-container>
        <v-container class="col-15">
            <v-container class="justify-content-between">
                <h1>Spells</h1>
            </v-container>

            <!-- TRY FILTERBY --
            https://front.id/en/articles/vuetify-achieve-multiple-filtering-data-table-component
            -->
            <v-data-table
                    :headers="headers"
                    :items="spells"
                    :items-per-page="5"

                    :expanded.sync="expanded"
                    item-key="name"
                    show-expand
                    class="elevation-1"
                    @click:row="expandRow"
            >

                <template v-slot:top>
                    <!-- v-container, v-col and v-row are just for decoration purposes. -->
                    <v-container fluid>
                        <v-row>
                            <!-- Filter for spell name -->
                            <v-col cols="12" md="4">
                                <v-row class="pa-3">
                                    <v-text-field
                                            v-model="spellFilterValue"
                                            type="text"
                                            label="Name"
                                    ></v-text-field>
                                </v-row>
                            </v-col>

                            <!-- Filter for levels -->
                            <v-col cols="12" md="4">
                                <v-row class="pa-3">
                                    <v-select
                                            :items="levelsList"
                                            v-model="levelsFilterValue"
                                            label="Levels"
                                    ></v-select>
                                </v-row>
                            </v-col>

                            <!-- Filter for tags -->
                            <v-col cols="12" md="4">
                                <v-row class="pa-3">
                                    <v-select
                                            :items="spelltags"
                                            v-model="spelltagsFilterValue"
                                            label="Spell tags"
                                    ></v-select>
                                </v-row>
                            </v-col>

                            <!-- FAI SEARCH FOR CLASSES con lista spuntata-->


                        </v-row>
                    </v-container>
                </template>

                <!-- expand item -->
                <template v-slot:expanded-item="{ headers, item }">
                    <td :colspan="headers.length">
                        <v-row>
                            <v-col class="bold text-center">LEVEL
                                <v-col class="regular text-center">{{item.level}}</v-col>
                            </v-col>
                            <v-col class="bold text-center">CASTING TIME
                                <v-col class="regular text-center">{{item.casting_time_amount}} {{
                                    item.casting_time_unit.toLowerCase() }}
                                </v-col>
                            </v-col>
                            <v-col class="bold text-center">RANGE/AREA
                                <v-col class="regular text-center" v-if="item.range_type.match('RANGED')">
                                    {{ item.range_type.toLowerCase() }} ({{ item.range_distance}} ft)
                                </v-col>
                            </v-col>
                            <v-col class="bold text-center">COMPONTENTS
                                <v-col class="regular text-center">
                                    <span v-if="item.component_verbal == true">V</span>
                                    <span v-if="item.component_somatic == true">S </span>
                                    <span v-if="item.component_material == true">M </span>
                                </v-col>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col class="bold text-center">DURATION
                                <v-col class="regular text-center" v-if="item.duration_type.match('TIME')">
                                    {{item.duration_amount}} {{item.duration_unit.toLowerCase()}}
                                </v-col>
                                <v-col class="regular text-center" v-else>{{item.duration_type.toLowerCase()}}</v-col>
                            </v-col>

                            <v-col class="bold text-center">SCHOOL
                                <v-col class="regular text-center">{{item.school}}</v-col>
                            </v-col>

                            <v-col class="bold text-center">ATTACK/SAVE
                                <v-col class="regular text-center" v-if="item.spell_additional_info != null &&
                                        item.spell_additional_info.save_type != null">
                                    {{item.spell_additional_info.save_type}}
                                </v-col>
                                <v-col class="regular text-center" v-else>-</v-col>
                            </v-col>

                            <v-col class="bold text-center">DAMAGE/EFFECT
                                <v-col class="regular text-center"
                                       v-if="item.spell_additional_info != null &&
                                        item.spell_additional_info.tags != null ">
                                    <span v-for="tag in item.spell_additional_info.tags"
                                          :key="tag.id">{{tag.tag}} </span>
                                </v-col>
                                <v-col class="regular text-center" v-else>-</v-col>
                            </v-col>
                        </v-row>

                        <v-divider></v-divider>

                        <v-container>
                            {{ item.description}}
                        </v-container>
                        <v-container>
                            Classes: {{item.class_list}}
                        </v-container>
                    </td>

                </template>

            </v-data-table>
            <!-- ................................. -->


            <!-- FILTER AREA from CHARACTER CLASS -->
            <!--
            <v-container>
                <v-col align="center" class="text-center">
                    <v-col>
                        <v-btn class="ma-2" v-for="characterclass in characterclasses" :key="characterclass.id"
                               @click="filterSpells">
                            {{characterclass.name}}
                        </v-btn>
                    </v-col>
                </v-col>
            </v-container>
            -->

            <!-- SEARCH AREA -->
            <!--
            <v-container>
                <v-row>
                    <v-text-field v-model="search" label="Search spells for name" outlined dense></v-text-field>
                    <v-text-field v-model="search_desc" label="Search spells for descriptions" outlined
                                  dense></v-text-field>
                    <v-text-field v-model="search_lvl" label="Search spells for level" outlined dense></v-text-field>
                    <v-text-field v-model="search_class" label="Search spells for class" outlined dense></v-text-field>
                </v-row>
            </v-container>
            -->

            <!--
            -- VECCHIA TABELLA --
            <v-container>
                <v-row>
                    <v-col>LEVEL</v-col>
                    <v-col>NAME</v-col>
                    <v-col>CASTING TIME</v-col>
                    <v-col>DURATION</v-col>
                    <v-col>RANGE/AREA</v-col>
                </v-row>

                <v-expansion-panels multiple focusable>
                    <v-expansion-panel v-for="spell in filteredSpells" :key="spell.id">
                        <v-expansion-panel-header>
                            <v-row>
                                <v-col>{{spell.level}}</v-col>
                                <v-col>{{spell.name}}</v-col>
                                <v-col>{{ spell.casting_time_amount }} {{ spell.casting_time_unit.toLowerCase() }}
                                </v-col>
                                <v-col>{{ spell.duration_type.toLowerCase() }}</v-col>
                                <v-col v-if="spell.range_type.match('RANGED')">
                                    {{ spell.range_type.toLowerCase() }} ({{ spell.range_distance}} ft)
                                </v-col>
                                <v-col v-else>{{ spell.range_type.toLowerCase() }}</v-col>
                            </v-row>
                        </v-expansion-panel-header>

                        <v-expansion-panel-content>
                            <v-container class="grey lighten-5">
                                <v-row>
                                    <v-col class="bold text-center">LEVEL
                                        <v-col class="regular text-center">{{spell.level}}</v-col>
                                    </v-col>
                                    <v-col class="bold text-center">CASTING TIME
                                        <v-col class="regular text-center">{{spell.casting_time_amount}} {{
                                            spell.casting_time_unit.toLowerCase() }}
                                        </v-col>
                                    </v-col>
                                    <v-col class="bold text-center">RANGE/AREA
                                        <v-col class="regular text-center" v-if="spell.range_type.match('RANGED')">
                                            {{ spell.range_type.toLowerCase() }} ({{ spell.range_distance}} ft)
                                        </v-col>
                                    </v-col>
                                    <v-col class="bold text-center">COMPONTENTS
                                        <v-col class="regular text-center">
                                            <span v-if="spell.component_verbal == true">V</span>
                                            <span v-if="spell.component_somatic == true">S </span>
                                            <span v-if="spell.component_material == true">M </span>
                                        </v-col>
                                    </v-col>
                                </v-row>
                                <v-row>
                                    <v-col class="bold text-center">DURATION
                                        <v-col class="regular text-center">{{spell.casting_time_amount}} {{
                                            spell.casting_time_unit.toLowerCase() }}
                                        </v-col>
                                    </v-col>
                                    <v-col class="bold text-center">SCHOOL
                                        <v-col class="regular text-center">{{spell.school}}</v-col>
                                    </v-col>
                                    <v-col class="bold text-center">ATTACK/SAVE
                                        <v-col class="regular text-center" v-if="spell.spell_additional_info != null">
                                            {{spell.spell_additional_info.save_type}}
                                        </v-col>
                                    </v-col>
                                    <v-col class="bold text-center">DAMAGE/EFFECT
                                        <v-col class="regular text-center">{{spell['tag']}}</v-col>
                                    </v-col>
                                </v-row>
                            </v-container>
                            <v-divider></v-divider>
                            <v-container>
                                {{ spell.description}}
                            </v-container>
                        </v-expansion-panel-content>
                    </v-expansion-panel>
                </v-expansion-panels>
            </v-container>
            -->

            <v-btn class="ma-2" v-scroll="onScroll" fab right bottom fixed color="primary" @click="toTop">
                <v-icon>mdi-arrow-up</v-icon>
            </v-btn>
        </v-container>

    </v-container>
</template>


<script>
    export default {
        head() {
            return {
                title: "Spells list",
            };
        },

        components: {},

        async asyncData({$axios, params}) {
            let retval = {spells: [], characterclasses: [], spelltags: []}
            try {
                let query_spell = await $axios.$get(`/spells/`);
                let query_characterclasses = await $axios.$get(`/characterclasses/`);
                let query_spelltags = await $axios.$get(`/spelltags/`);

                if (query_characterclasses.count > 0) {
                    retval.characterclasses = query_characterclasses.results
                }

                if (query_spell.count > 0) {
                    retval.spells = query_spell.results
                    // -- Add casting_time value
                    retval.spells.forEach(spell => {
                        let casting_time = "" + spell.casting_time_amount + " " + spell.casting_time_unit.toLowerCase()
                        spell['casting_time'] = casting_time
                    })

                    // -- Add tags
                    retval.spells.forEach(spell => {
                        if (spell.spell_additional_info != null) {
                            if (spell.spell_additional_info.tags != null) {
                                // let tag_list = "" + spell.spell_additional_info.tags[0].tag
                                let tag_list = ""
                                for (var cnt in spell.spell_additional_info.tags) {
                                    tag_list = tag_list.concat(spell.spell_additional_info.tags[cnt].tag)
                                    tag_list = tag_list.concat(" ")
                                }
                                spell['tag_list'] = tag_list
                            } else
                                spell['tag_list'] = '-'
                        } else {
                            spell['tag_list'] = '-'
                        }
                    })

                    // -- Add classes name
                    retval.spells.forEach(spell => {
                        if (spell.classes != null) {
                            let class_list = ""
                            for (var cnt in spell.classes) {
                                for (var cl in query_characterclasses.results) {
                                    var a = query_characterclasses.results[cl].url
                                    if (a.match(spell.classes[cnt])) {
                                        class_list = class_list.concat(query_characterclasses.results[cl].name)
                                        class_list = class_list.concat(" ")
                                    }
                                }
                            }
                            spell['class_list'] = class_list
                        }
                    })


                }


                if (query_spelltags.count > 0) {
                    let v = {text: "All", value: null}
                    retval.spelltags.push(v)
                    for (var i = 0; i < query_spelltags.count; i++) {
                        let v = {text: query_spelltags.results[i].tag, value: query_spelltags.results[i].tag}
                        retval.spelltags.push(v)
                    }
                }
            } catch (e) {
                console.log(e);
            }
            return retval
        },

        data() {
            return {
                spells: [],
                search: '',
                search_desc: '',
                search_lvl: '',
                search_class: '',
                characterclasses: [],

                levelsList: [
                    {text: "All", value: null},
                    {text: "Cantrip", value: 0},
                    {text: "1st", value: 1},
                    {text: "2nd", value: 2},
                    {text: "3th", value: 3},
                    {text: "4th", value: 4},
                    {text: "5th", value: 5},
                    {text: "6th", value: 6},
                    {text: "7th", value: 7},
                    {text: "8th", value: 8},
                    {text: "9th", value: 9},
                ],

                // Filter models
                spellFilterValue: '',
                levelsFilterValue: null,
                spelltagsFilterValue: null,

                // v-data-table
                headers: [
                    {text: 'LEVEL', value: 'level', align: 'left', filter: this.levelsFilter},
                    {text: 'NAME', value: 'name', align: 'center', filter: this.nameFilter,},
                    {text: 'CASTING TIME', value: 'casting_time', align: 'center', sortable: false},
                    {text: 'TAGS', value: 'tag_list', align: 'center', filter: this.spelltagsFilter},
                    {text: ' ', value: 'data-table-expand', align: 'left'}
                ],
                expanded: [],
                spelltags: []       // For tags


            };
        },

        methods: {
            async deleteSpell(spell_id) {
                try {
                    await this.$axios.$delete(`/spells/${spell_id}/`); // delete spell
                    let newSpell = await this.$axios.$get("/spells/"); // get new list of cspells
                    this.spells = newSpells; // update list of spells
                } catch (e) {
                    console.log(e);
                }
            },

            onScroll(e) {
                if (typeof window === 'undefined')
                    return
                const top = window.pageYOffset || e.target.scrollTop || 0
                this.fab = top > 20
            },
            toTop() {
                this.$vuetify.goTo(0)
            },

            /*
            VECCHIA TABELLA
            filterSpells() {
                return this.spells.filter((spell) => {
                    if (this.search.length > 0)
                        return spell.name.toLowerCase().match(this.search.toLowerCase())
                    if (this.search_desc.length > 0)
                        return spell.description.toLowerCase().match(this.search_desc.toLowerCase())
                    if (this.search_lvl.length > 0)
                        return spell.level == this.search_lvl


                    if (this.search_class.length > 0) {
                        console.log(spell.classes[0, 0].length)

                        //console.log(this.characterclasses)
                    }
                    //return spell........description.toLowerCase().match(this.search_class.toLowerCase())
                    else
                        return this.spells
                })
            },
            */

            // ----- NEW FILTER -----
            // -- Filter for spell name col
            nameFilter(value) {
                if (!this.spellFilterValue) {
                    return true;
                }
                return value.toLowerCase().includes(this.spellFilterValue.toLowerCase());
            },

            // -- Filter for level col
            levelsFilter(value) {
                if (!this.levelsFilterValue) {
                    return true;
                }
                return value == this.levelsFilterValue;
            },

            // -- Filter for spell tags col
            spelltagsFilter(value) {
                if (!this.spelltagsFilterValue) {
                    return true;
                }
                return value.toLowerCase().includes(this.spelltagsFilterValue.toLowerCase());
            },

            // Expand row
            expandRow(item) {
                this.expanded = item == this.expanded[0] ? [] : [item]
            },


        },

        computed: {
            /*
            VECCHIA TABELLA
            filteredSpells: function () {
                return this.filterSpells()
            },
            */


        },

    };
</script>


<style scoped>
    ul {
        list-style-type: none;
    }
</style>
