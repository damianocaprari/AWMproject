<template>
  <v-card>
    <v-card-title class="secondary onsecondary--text">
      <v-row no-gutters>
        <v-col>
          Dice Roller&nbsp;<span class="mdi mdi-dice-d20"></span>
        </v-col>

        <!-- for screen < 600 px -->
        <v-col class="d-sm-none" align="right">
          <v-btn text color="onsecondary" @click="clearHistory" x-small>Clear</v-btn>
          <v-btn outlined color="onsecondary" @click="rollDice" small>Roll</v-btn>
        </v-col>

        <!-- for screen >= 600 px -->
        <v-col class="d-none d-sm-block" align="right">
          <v-btn text color="onsecondary" @click="clearHistory">Clear</v-btn>
          <v-btn outlined color="onsecondary" @click="rollDice">Roll</v-btn>
        </v-col>
      </v-row>
    </v-card-title>
    <v-card-text>
      <v-form @submit.prevent="rollDice" class="mt-5">
        <v-text-field label="Dice to roll" v-model="diceExpr" :rules="diceRules" placeholder="2d6 +5"/>
      </v-form>

      <v-divider class="mt-5"
        v-if="history.length > 0"
      ></v-divider>

      <v-row>
        <v-expansion-panels
          accordion
          multiple
          style="z-index: unset;"
        >
          <v-expansion-panel
            v-for="(entry, idx) in history"
            :key="idx"
          >
            <v-expansion-panel-header>
              {{ entry.expr }}:&nbsp;&nbsp;<span class="font-weight-bold">{{ entry.total }}</span>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              Rolls:&nbsp;{{ entry.rolls }}
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-row>

    </v-card-text>
  </v-card>
</template>

<script>
    export default {
        props: [],
        data () {
            return {
                diceExpr : '',
                diceRules: [
                    //v => !!v || 'Required field',
                    v => (!v || /^[1-9]{1}\d*d\d+((\+|\-)\d+)?$/.test(v.replace(/\s/g, ""))) || 'Expression must follow this format: N d# [+/-M]',
                    v => (!v || /d(4|6|8|10|12|20){1}/.test(v.replace(/\s/g, ""))) || 'Only d4, d6, d8, 10, d12 or d20 are allowed',
                ],
                history: [],
            }
        },
        methods : {
            getRandomInt(min_included, max_excluded) { //Il max è escluso e il min è incluso
                min_included = Math.ceil(min_included);
                max_excluded = Math.floor(max_excluded);
                return Math.floor(Math.random() * (max_excluded - min_included)) + min_included;
            },
            calculateRoll(expr) {
                /* assumes diceExpr has valid format 'N dX [+/-M]' */
                if (!expr || expr == '') return null
                expr = expr.replace(/\s/g, '')
                let n = Number(expr.substring(0, expr.indexOf('d')))
                let size = 0
                let bonus = 0
                if (expr.indexOf('+') > 0) {
                    size = Number(expr.substring(expr.indexOf('d') + 1, expr.indexOf('+')))
                    bonus = Number(expr.substring(expr.indexOf('+') + 1, expr.length))
                }
                else if (expr.indexOf('-') > 0) {
                    size = Number(expr.substring(expr.indexOf('d') + 1, expr.indexOf('-')))
                    bonus = -Number(expr.substring(expr.indexOf('-') + 1, expr.length))
                }
                else {
                    size = Number(expr.substring(expr.indexOf('d') + 1, expr.length))
                    bonus = 0
                }

                let sum = 0
                let rolls = []
                for (let i = 0; i < n; i++) {
                    let roll = this.getRandomInt(1, size + 1)
                    rolls.push(roll)
                    sum += roll
                }

                return { total: sum + bonus, rolls: rolls }
            },
            rollDice() {
                if (!this.diceExpr || !/^[1-9]{1}\d*d(4|6|8|10|12|20){1}((\+|\-)\d+)?$/.test(this.diceExpr.replace(/\s/g, ""))) return
                let roll = this.calculateRoll(this.diceExpr)
                if (!!roll) {
                    this.history.unshift({expr: this.diceExpr.replace(/\s/g, ''), total: roll.total, rolls: roll.rolls}) // unshift puts element into first position
                    //this.diceExpr = ''
                    if (this.history.length > 10)
                        this.history.pop()
                    //console.log(this.history)
                }
            },
            clearHistory() {
                this.diceExpr = ''
                this.history = []
            }
        }
    }
</script>

<style scoped>

</style>
