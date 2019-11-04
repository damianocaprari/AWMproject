<template>
  <v-card>
    <v-card-title class="secondary onsecondary--text">
      <v-row no-gutters>
        <v-col>
         NPC Quick Generator
        </v-col>

        <!-- for screen < 600 px -->
        <v-col class="d-sm-none" align="right">
          <v-btn text color="onsecondary" @click="clearHistory" x-small>Clear</v-btn>
          <v-btn outlined color="onsecondary" @click="generateCharacter(form_data.class, form_data.race, form_data.sex)" small>Roll</v-btn>
        </v-col>

        <!-- for screen >= 600 px -->
        <v-col class="d-none d-sm-block" align="right">
          <v-btn text color="onsecondary" @click="clearHistory">Clear</v-btn>
          <v-btn outlined color="onsecondary" @click="generateCharacter(form_data.class, form_data.race, form_data.sex)">Roll</v-btn>
        </v-col>
      </v-row>
    </v-card-title>
    <v-card-text>
      <v-form @submit.prevent="generateCharacter(form_data.class, form_data.race, form_data.sex)" class="mt-5">
        <v-row>
          <v-col cols="12" sm="4">
            <v-select label="Class" v-model="form_data.class" :items="classes" return-object></v-select>
          </v-col>
          <v-col cols="12" sm="4">
            <v-select label="Race" v-model="form_data.race" :items="races" return-object
            ></v-select>
          </v-col>
          <v-col cols="12" sm="4">
            <v-select label="Sex" v-model="form_data.sex" :items="sexes" return-object
            ></v-select>
          </v-col>
        </v-row>
      </v-form>

      <v-row v-if="!!history">
        <v-list three-line>
          <template v-for="(h, idx) in history">
            <v-divider v-if="idx > 0"></v-divider>
            <v-list-item :key="idx">
              <v-list-item-content>
                <v-list-item-title><span class="font-weight-bold">{{ h.name.text }}</span>: {{ h.sex.text }} {{ h.race.text }} {{ h.class.text }}, {{ h.alignment.text}}.</v-list-item-title>
                <v-list-item-subtitle class="caption">Str {{ h.abilities.str }} | Con {{ h.abilities.con }} | Dex {{ h.abilities.dex }} | Int {{ h.abilities.int }} | Str {{ h.abilities.wis }} | Cha {{ h.abilities.cha }}</v-list-item-subtitle>
                {{ h.name.text }} {{ h.appearance.text }}. {{ h.sex.pronoun }} {{ h.equipment.text }}. {{ h.name.text }} {{ h.trivia.text }}.
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
      </v-row>

    </v-card-text>
  </v-card>
</template>

<script>
    export default {
        data () {
            return {
                form_data: {
                    race: {value: 'random', text: 'Random'},
                    sex: {value: 'random', text: 'Random'},
                    class: {value: 'random', text: 'Random'},
                },
                history: [],
                races: [
                    {value: 'random', text: 'Random'},
                    {value: 'dragonborn', text: 'Dragonborn'},
                    {value: 'dwarf', text: 'Dwarf'},
                    {value: 'elf', text: 'Elf'},
                    {value: 'gnome', text: 'Gnome'},
                    {value: 'halfling', text: 'Halfling'},
                    {value: 'halfelf', text: 'Half-Elf'},
                    {value: 'halforc', text: 'Half-Orc'},
                    {value: 'human', text: 'Human'},
                    {value: 'tiefling', text: 'Tiefling'},
                ],
                sexes: [
                    {value: 'random', text: 'Random'},
                    {value: 'male', text: 'Male', pronoun: 'He'},
                    {value: 'female', text: 'Female', pronoun: 'She'},
                ],
                alignments: [
                    //{value: 'random', text: 'Random'},
                    {value: 'lg', text: 'LG'},
                    {value: 'ng', text: 'NG'},
                    {value: 'cg', text: 'CG'},
                    {value: 'ln', text: 'LN'},
                    {value: 'nn', text: 'NN'},
                    {value: 'cn', text: 'CN'},
                    {value: 'le', text: 'LE'},
                    {value: 'ne', text: 'NE'},
                    {value: 'ce', text: 'CE'},
                ],
                classes: [
                    {value: 'random', text: 'Random'},
                    {value: 'class', text: 'Adventurer Class'},
                    {value: 'npc', text: 'NPC Class'},
                ],
                npc_classes: [
                    {text: 'Servant'},
                    {text: 'Paesant'},
                    {text: 'Alchemist'},
                    {text: 'Scholar'},
                    {text: 'Professional'},
                    {text: 'Priest'},
                    {text: 'Mercenary'},
                    {text: 'Artist'},
                    {text: 'Merchant'},
                    {text: 'Aristocrat'},
                    {text: 'Entertainer'},
                    {text: 'Scofflaw'},
                    {text: 'Guard'},
                    {text: 'Farmer'},
                    {text: 'Vagabond'},
                ],
                adv_classes: [
                    {text: 'Barbarian'},
                    {text: 'Bard'},
                    {text: 'Cleric'},
                    {text: 'Druid'},
                    {text: 'Fighter'},
                    {text: 'Monk'},
                    {text: 'Paladin'},
                    {text: 'Ranger'},
                    {text: 'Rogue'},
                    {text: 'Sorcerer'},
                    {text: 'Wizard'},
                    {text: 'Warlock'},
                ],
                names: [
                    {text: 'Amisca'},{text: 'Anzis'},{text: 'Abdil'},{text: 'Arnies'},{text: 'Alstald'},{text: 'Alyn'},
                    {text: 'Biri'},{text: 'Brihtiua'},{text: 'Buacha'},{text: 'Bane'},{text: 'Balda'},{text: 'Baldo'},
                    {text: 'Codditu'},{text: 'Conian'},{text: 'Collen'},{text: 'Cece'},{text: 'Cily'},{text: 'Constie'},
                    {text: 'Darro'},{text: 'Dic'},{text: 'Dyley'},{text: 'Ditani'},{text: 'Dreder'},{text: 'Dainain'},
                    {text: 'Elior'},{text: 'Eren'},{text: 'Elean'},{text: 'Ernalbh'},{text: 'Ecil'},{text: 'Eanfled'},
                    {text: 'Fahima'},{text: 'Fastob'},{text: 'Finde'},{text: 'Fingoli'},{text: 'Fratur'},{text: 'Frazur'},
                    {text: 'Gothiuda'},{text: 'Gela'},{text: 'Gery'},{text: 'Giles'},{text: 'Gaga'},{text: 'Gefortis'},
                    {text: 'Henry'},{text: 'Hamfo'},{text: 'Hallda'},{text: 'Hallgidotr'},{text: 'Here'},{text: 'Humliva'},
                    {text: 'Isobella'},{text: 'Ioana'},{text: 'Isckel'},{text: 'Ilit'},{text: 'Ithrellas'},{text: 'Inel'},
                    {text: 'Javend'},{text: 'Jonton'},{text: 'Jordaye'},{text: 'Joycie'},{text: 'Jamund'},{text: 'Johny'},
                    {text: 'Kasim'},{text: 'Kenny'},{text: 'Kerre'},{text: 'Kentor'},{text: 'Kerde'},{text: 'Kater'},
                    {text: 'Lenenke'},{text: 'Lava'},{text: 'Lotie'},{text: 'Lica'},{text: 'Lothienye'},{text: 'Lala'},
                    {text: 'Marime'},{text: 'Morgan'},{text: 'Maera'},{text: 'Merca'},{text: 'Mira'},{text: 'Mithrielye'},
                    {text: 'Nontodi'},{text: 'Nane'},{text: 'Ninki'},{text: 'Nigero'},{text: 'Ningal'},{text: 'Nerwende'},
                    {text: 'Omald'},{text: 'Olitt'},{text: 'Ornstein'},{text: 'Ogomor'},{text: 'Otto'},{text: 'Orleig'},
                    {text: 'Precit'},{text: 'Prosse'},{text: 'Porter'},{text: 'Prosa'},{text: 'Phely'},{text: 'Pyley'},
                    {text: 'Qarm'},{text: 'Quott'},{text: 'Qelet'},{text: 'Quasim'},{text: 'Qelamur'},{text: 'Qasim'},
                    {text: 'Riffolk'},{text: 'Rancent'},{text: 'Rubbuck'},{text: 'Rimcio'},{text: 'Robert'},{text: 'Rine'},
                    {text: 'Sumadi'},{text: 'Sarica'},{text: 'Sifu'},{text: 'Syfla'},{text: 'Suntho'},{text: 'Sana'},
                    {text: 'Terica'},{text: 'Toridotr'},{text: 'Thiuda'},{text: 'Thelchilda'},{text: 'Thari'},{text: 'Thricannia'},
                    {text: 'Utterom'},{text: 'Uccom'},{text: 'Ualin'},{text: 'Ulis'},{text: 'Umul'},{text: 'Umrar'},
                    {text: 'Vicker'},{text: 'Vand'},{text: 'Vanda'},{text: 'Vaca'},{text: 'Vela'},{text: 'Valdamal'},
                    {text: 'Waphen'},{text: 'Winderli'},{text: 'Weren'},{text: 'Wynna'},{text: 'Wilguda'},{text: 'Wisym'},
                    {text: 'Xanu'},{text: 'Xettere'},{text: 'Xotl'},{text: 'Xantus'},{text: 'Xena'},{text: 'Xandril'},
                    {text: 'Yttr'},{text: 'Yago'},{text: 'Yeenu'},{text: 'Yasul'},{text: 'Yotus'},{text: 'Yatengo'},
                    {text: 'Zantos'},{text: 'Zultar'},{text: 'Zelene'},{text: 'Zika'},{text: 'Zolt'},{text: 'Zayne'},
                ],
                appearances: [
                    {text: 'is tall, with brown hair and dark amber eyes'},
                    {text: 'is rough in appearance, with brown hair and narrow brown eyes'},
                    {text: 'has a long face, with black hair and large gray eyes'},
                    {text: 'has blood red skin, with dark red hair and gold eyes'},
                    {text: 'is tall and thin, with straight auburn hair and amber eyes'},
                    {text: 'has copper hair and soft amber eyes'},
                    {text: 'is tall, with black hair and green eyes'},
                    {text: 'is common in appearance, with auburn hair and large gray eyes'},
                    {text: 'has an angular face, with black hair and large amber eyes'},
                    {text: 'is short and stout, with black hair and amber eyes'},
                    {text: 'has uneven red hair and brown eyes, and an unusual scar on his face'},
                    {text: 'is tall, with copper hair and sharp green eyes'},
                    {text: 'has a long face, with straight blonde hair and amber eyes'},
                    {text: 'is short and heavyset, with copper hair and light amber eyes'},
                    {text: 'is rugged in appearance, with brown hair and dark brown eyes'},
                    {text: 'has bronze scales and dark brown eyes, and wears glasses with electrum rims'},
                    {text: 'has blue scales and soft gray eyes'},
                    {text: 'has blonde hair and soft green eyes '},
                    {text: 'has thick golden hair and blue eyes'},
                    {text: 'is short and willowy, with dark red hair and red eyes'},
                    {text: 'has white hair and light amber eyes'},
                    {text: 'is tall, with short golden hair and blue eyes'},
                    {text: 'has matted white hair and bright blue eyes'},
                    {text: 'has white hair and green eyes'},
                    {text: 'is heavyset, with gray hair and blue eyes'},
                    {text: 'has auburn hair and amber eyes, and a flat nose'},
                    {text: 'has thin blonde hair and narrow green eyes'},
                    {text: 'is fair in appearance, with tangled auburn hair and brown eyes'},
                    {text: 'has silver hair and large green eyes, and a straight moustache'},
                    {text: 'has bronze scales and brown eyes'},
                ],
                equipments: [
                    {text: 'wears studded leather and wields a spear and dagger'},
                    {text: 'wears chain mail and wields a shortsword'},
                    {text: 'wears travel-stained clothing and wields a kanabo (mace)'},
                    {text: 'wears hide armor and wields a whip'},
                    {text: 'wears a breastplate and wields a longsword and shield'},
                    {text: 'wears leather armor and wields a maul'},
                    {text: 'wears studded leather and wields a handaxe and darts'},
                    {text: 'wears sturdy clothing and wields nunchaku (club) and shuriken (darts)'},
                    {text: 'wears hide armor and wields a shortsword and shield'},
                    {text: 'wears a breastplate and wields a warhammer'},
                    {text: 'wears studded leather and wields a handaxe and sickle'},
                    {text: 'wears leather armor and wields a mace and dagger'},
                    {text: 'wears studded leather and wields a greataxe'},
                    {text: 'wears leather armor and wields a maul'},
                    {text: 'wears tailored clothing and several pouches hang from his belt'},
                    {text: 'wears tailored clothing and a dragonscale cloak'},
                    {text: 'wears modest garments and carries a long knife'},
                    {text: 'wears plain clothing and several pouches hang from her belt'},
                    {text: 'wears modest garments and a feathered hat'},
                    {text: 'wears studded leather and wields a rapier and heavy crossbow'},
                    {text: 'wears leather armor and wields a greatsword'},
                    {text: 'wears well-made clothing and a leopard fur cape'},
                    {text: 'wears modest garments and a red cloak'},
                    {text: 'wears well-made garments and silk gloves'},
                    {text: 'wears well-made clothing and a dragonscale cloak'},
                    {text: 'wears expensive clothing and an amulet of luminous crystal'},
                    {text: 'wears well-made clothing and a sling of vials and potions'},
                    {text: 'wears leather armor and wields a trident and hand crossbow'},
                    {text: 'wears expensive clothing and a silver holy symbol'},
                    {text: 'wears modest garments and an iron amulet'},
                ],
                trivia: [
                    {text: 'is haunted by the ghost of someone he killed'},
                    {text: 'seeks to discover why she cannot remember anything from yesterday'},
                    {text: 'is hard-hearted and fiendish'},
                    {text: 'has a forest owl named Lida'},
                    {text: 'is barbaric and destructive'},
                    {text: 'has an animal companion, a tawny rat named Colli'},
                    {text: 'has an animal companion, a green firedrake named Asuidagne'},
                    {text: 'dislikes having people behind her'},
                    {text: 'has an animal companion, a black snake named Wyny'},
                    {text: 'is searching for the legendary Vaults of the Wraith Baroness'},
                    {text: 'has an animal companion, a black rat named Kater'},
                    {text: 'is selfish and slothful'},
                    {text: 'is searching for the lost elven kingdom of Helinde'},
                    {text: 'is corrupt and greedy'},
                    {text: 'has an animal companion, a black cat named Gundve'},
                    {text: 'is honest and merciless'},
                    {text: 'is painfully tone-deaf'},
                    {text: 'is fascinated by necromancy and the undead'},
                    {text: 'is searching for the legendary dwarven kingdom of Gunargund'},
                    {text: 'is searching for her lost brother'},
                    {text: 'seeks revenge against the sister who betrayed him'},
                    {text: 'suffers a traumatic fear of confined spaces'},
                    {text: 'is amoral and covetous'},
                    {text: 'suffers a paralyzing fear of open water'},
                    {text: 'seeks to free himself from an ancient curse'},
                    {text: 'is destructive and selfish'},
                    {text: 'is flamboyant and timid'},
                    {text: 'is lustful and greedy'},
                    {text: 'is searching for his missing daughter'},
                    {text: 'seeks only fame and glory'},
                ],
            }
        },
        methods: {
            rollAbilityScore() {
                return this.getRandomInt(1, 6+1) + this.getRandomInt(1, 6+1) + this.getRandomInt(1, 6+1)
            },
            getRandomInt(min_included, max_excluded) { //Il max è escluso e il min è incluso
                min_included = Math.ceil(min_included);
                max_excluded = Math.floor(max_excluded);
                return Math.floor(Math.random() * (max_excluded - min_included)) + min_included;
            },
            generateCharacter(class_choice, race_choice, sex_choice) {
                let name = this.names[this.getRandomInt(0, this.names.length)]
                let alignment = this.alignments[this.getRandomInt(0, this.alignments.length)]
                let appearance = this.appearances[this.getRandomInt(0, this.appearances.length)]
                let equipment = this.equipments[this.getRandomInt(0, this.equipments.length)]
                let trivia = this.trivia[this.getRandomInt(0, this.trivia.length)]
                let sex = sex_choice
                while (sex.value == 'random') {
                    sex = this.sexes[this.getRandomInt(0, this.sexes.length)]
                }
                let classes = []
                if (class_choice.value == 'random')
                    classes = this.adv_classes.concat(this.npc_classes)
                else if (class_choice.value == 'npc')
                    classes = this.npc_classes
                else
                    classes = this.adv_classes
                let clazz = classes[this.getRandomInt(0, classes.length)]
                let race = race_choice
                while (race.value == 'random') {
                    race = this.races[this.getRandomInt(0, this.races.length)]
                }
                let str = this.rollAbilityScore()
                let con = this.rollAbilityScore()
                let dex = this.rollAbilityScore()
                let int = this.rollAbilityScore()
                let wis = this.rollAbilityScore()
                let cha = this.rollAbilityScore()

                console.log(name)
                console.log(sex)
                console.log(race)
                console.log(clazz)
                console.log(alignment)
                console.log(appearance)
                console.log(equipment)
                console.log(trivia)

                let character = {
                    name: name,
                    sex: sex,
                    race: race,
                    class: clazz,
                    alignment: alignment,
                    abilities: { str: str, con: con, dex: dex, int: int, wis: wis, cha: cha },
                    appearance: appearance,
                    equipment: equipment,
                    trivia: trivia,
                }

                /*
                this.history.unshift(`${name.text}: ${sex.text} ${race.text} ${clazz.text}, ${alignment.text}.\n` +
                  `Str ${str} | Con ${con} | Dex ${dex} | Int ${int} | Wis ${wis} | Cha ${cha}\n` +
                  `${name.text} ${appearance.text} ${sex.pronoun} ${equipment.text} ${name.text} ${trivia.text}`)
                 */
                this.history.unshift(character)

                if (this.history.length > 10)
                    this.history.pop()
            },
            clearHistory() {
                this.history = []
                this.form_data = {
                    race: {value: 'random', text: 'Random'},
                    sex: {value: 'random', text: 'Random'},
                    class: {value: 'random', text: 'Random'},
                }
            }
        }
    }
</script>

<style scoped>

</style>
