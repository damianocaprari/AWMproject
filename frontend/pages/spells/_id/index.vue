<template>
  <v-container fluid>
    <v-row wrap>
      <v-alert v-if="!!alert" :type="alert.type">{{ alert.message }}</v-alert>
      <!-- qua i pulsanti -->
      <v-col>
        <v-card>
          <v-card-title class="secondary onsecondary--text"><h3>{{ spell.name }}</h3></v-card-title>
          <v-card-text>
            <v-row justify="center">
              <v-col align="center">
                <v-avatar color="grey" tile size="160" class="mx-auto">
                  <v-img :src="spell.spell_additional_info.avatar" v-if="(spell.spell_additional_info && spell.spell_additional_info.avatar)"></v-img>
                </v-avatar>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="6" sm="4" lg="3">
                <v-row no-gutters><v-col>LEVEL</v-col></v-row>
                <v-row no-gutters><v-col>{{ spell.level }}</v-col></v-row>
              </v-col>
              <v-col cols="6" sm="4" lg="3">
                <v-row no-gutters><v-col>CASTING TIME</v-col></v-row>
                <v-row no-gutters><v-col>{{ spell.casting_time_amount }} {{ spell.casting_time_unit.toLowerCase() }}</v-col></v-row>
              </v-col>
              <v-col cols="6" sm="4" lg="3">
                <v-row no-gutters><v-col>RANGE/AREA</v-col></v-row>
                <v-row no-gutters>
                  <v-col v-if="'RANGED'.match(spell.range_type)">{{ spell.range_type.toLowerCase() }} ({{ spell.range_distance }} ft)</v-col>
                  <v-col v-else>{{ spell.range_type.toLowerCase() }}</v-col>
                </v-row>
              </v-col>
              <v-col cols="6" sm="4" lg="3">
                <v-row no-gutters><v-col>COMPONENTS</v-col></v-row>
                <v-row no-gutters><v-col>
                   <template v-if="spell.component_verbal">V</template>
                   <template v-if="spell.component_somatic">S</template>
                   <template v-if="spell.component_material">M ({{ spell.component_material_description }}</template>
                </v-col></v-row>
              </v-col>
              <v-col cols="6" sm="4" lg="3">
                <v-row no-gutters><v-col>DURATION</v-col></v-row>
                <v-row no-gutters>
                  <v-col v-if="'TIME'.match(spell.duration_type) || 'CONCENTRATION'.match(spell.duration_type) || 'SPECIAL'.match(spell.duration_type)">
                    {{ spell.duration_amount }} {{ spell.duration_unit.toLowerCase() }} <span v-if="'CONCENTRATION'.match(spell.duration_type)" class="mdi mdi-alpha-c-circle"></span>
                  </v-col>
                  <v-col v-else>{{ spell.duration_type.toLowerCase() }}</v-col>
                </v-row>
              </v-col>
              <v-col cols="6" sm="4" lg="3">
                <v-row no-gutters><v-col>SCHOOL</v-col></v-row>
                <v-row no-gutters><v-col>{{ spell.school }}</v-col></v-row>
              </v-col>
              <v-col cols="6" sm="4" lg="3">
                <v-row no-gutters><v-col>ATTACK/SAVE</v-col></v-row>
                <v-row no-gutters>
                  <v-col v-if="spell.spell_additional_info && spell.spell_additional_info.save_type">{{ item.spell_additional_info.save_type }}</v-col>
                  <v-col v-else>-</v-col>
                </v-row>
              </v-col>
              <v-col cols="6" sm="4" lg="3">
                <v-row no-gutters><v-col>DAMAGE/EFFECT</v-col></v-row>
                <v-row no-gutters>
                  <v-col v-if="spell.spell_additional_info && spell.spell_additional_info.tags && spell.spell_additional_info.tags.length > 0">
                    {{ spell.spell_additional_info.tags[0].tag }}
                  </v-col>
                  <v-col v-else>-</v-col>
                </v-row>
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-row>
              <v-col>
                {{ spell.description }}
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-row>
              <v-col v-if="spell.classes">
                Classes:
                <template v-for="id in spell.classes">
                  <v-chip :key="id" v-if="getClassFromId(id)">{{ getClassFromId(id).name }}</v-chip>
                </template>
              </v-col>
            </v-row>
            <v-row>
              <v-col v-if="spell.spell_additional_info && spell.spell_additional_info.tags">
                Tags:
                <template v-for="tag in spell.spell_additional_info.tags">
                  <v-chip :key="tag.tag">{{ tag.tag }}</v-chip>
                </template>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
        <h2></h2>
      </v-col>
<!--
      <v-col>
        <v-form @submit.prevent="submit">
          <v-alert v-if="alert" :type="alert.type">{{ alert.message }}</v-alert>
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
              <v-btn text color="accent" @click="resetFormData">Cancel</v-btn>
            </v-col>
          </v-row>
        </v-form>

      </v-col>
      -->
    </v-row>
  </v-container>
</template>

<script>
    export default {
        data () {
            return {
                spell: {},
                characterclasses: [],
                spelltags: [],
                alert: null,
            }
        },

        async asyncData ( {$axios, params }) {
            try {
                let retval = {spell: {}, characterclasses: [], spelltags: []}
                let query_spell = await $axios.$get(`/spells/${params.id}`);
                let query_characterclasses = await $axios.$get(`/characterclasses/`);
                let query_spelltags = await $axios.$get(`/spelltags/`);

                if (!query_spell) {
                    return {
                        alert: {
                            type: 'error',
                            message: 'Selected spell does not exist'
                        }
                    }
                }
                //console.log(query_spell)
                retval.spell = query_spell
                retval.characterclasses = query_characterclasses.results
                retval.spelltags = query_spelltags.results
                return retval
            } catch (e) {
                return {
                    alert: {
                        type: 'error',
                        message: 'An error occurred while retrieving information'
                    }
                }
            }
        },

        methods: {
            getClassFromId(id) {
                for (let i = 0; i < this.characterclasses.length; i++) {
                    if (this.characterclasses[i].id == id) {
                        return this.characterclasses[i]
                    }
                }
                // ID not found
                return null
            },
        }
    }
</script>

<style scoped>

</style>
