<template>
    <v-data-table
    :headers="headers"
    :items="characters"
    sort-by="initiative"
    class="elevation-1"
    disable-sort disable-filtering disable-pagination
    hide-default-footer

  >
    <template v-slot:top>
      <v-toolbar flat class="secondary onsecondary--text">
        <v-toolbar-title>Initiative Tracker</v-toolbar-title>
        <!--<v-divider class="mx-4" inset vertical ></v-divider>-->
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on }">
            <v-btn color="onsecondary" outlined v-on="on">Add character</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="12" class="pa-1">
                    <v-text-field v-model="editedItem.name" label="Name"></v-text-field>
                  </v-col>
                  <v-col cols="4" sm="4" class="pa-1">
                    <v-text-field v-model="editedItem.init" label="Init"></v-text-field>
                  </v-col>
                  <v-col cols="4" sm="4" class="pa-1">
                    <v-text-field v-model="editedItem.hp" label="HP"></v-text-field>
                  </v-col>
                  <v-col cols="4" sm="4" class="pa-1">
                    <v-text-field v-model="editedItem.ac" label="AC"></v-text-field>
                  </v-col>
                  <v-col cols="4" sm="2" class="pa-1">
                    <v-text-field v-model="editedItem.str" label="Str"></v-text-field>
                  </v-col>
                  <v-col cols="4" sm="2" class="pa-1">
                    <v-text-field v-model="editedItem.con" label="Con"></v-text-field>
                  </v-col>
                  <v-col cols="4" sm="2" class="pa-1">
                    <v-text-field v-model="editedItem.dex" label="Dex"></v-text-field>
                  </v-col>
                  <v-col cols="4" sm="2" class="pa-1">
                    <v-text-field v-model="editedItem.int" label="Int"></v-text-field>
                  </v-col>
                  <v-col cols="4" sm="2" class="pa-1">
                    <v-text-field v-model="editedItem.wis" label="Wis"></v-text-field>
                  </v-col>
                  <v-col cols="4" sm="2" class="pa-1">
                    <v-text-field v-model="editedItem.cha" label="Cha"></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="accent" text @click="close">Cancel</v-btn>
              <v-btn color="accent" text @click="save">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.action="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
      <!--
    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize">Reset</v-btn>
    </template>
      -->
    <template v-slot:no-data>
      Start adding characters!
    </template>
  </v-data-table>
</template>

<script>
    export default {
        data: () => ({
            dialog: false,
            headers: [
                { text: 'Name', value: 'name', sortable: false, },
                { text: 'Init', value: 'init', sortable: false, },
                { text: 'HP', value: 'hp', sortable: false, },
                { text: 'AC', value: 'ac', sortable: false, },
                { text: 'Str', value: 'str', sortable: false, },
                { text: 'Con', value: 'con', sortable: false, },
                { text: 'Dex', value: 'dex', sortable: false, },
                { text: 'Int', value: 'int', sortable: false, },
                { text: 'Wis', value: 'wis', sortable: false, },
                { text: 'Cha', value: 'cha', sortable: false, },
                { text: 'Actions', value: 'action', sortable: false },
            ],
            characters: [],
            editedIndex: -1,
            editedItem: {
                name: '',
                initiative: 0,
                hp: '',
                ac: '',
                str: '',
                con: '',
                dex: '',
                int: '',
                wis: '',
                cha: '',
            },
            defaultItem: {
                name: '',
                initiative: 0,
                hp: '',
                ac: '',
                str: '',
                con: '',
                dex: '',
                int: '',
                wis: '',
                cha: '',
            },
        }),

        computed: {
            formTitle () {
                return this.editedIndex === -1 ? 'New character' : 'Edit character'
            },
        },

        watch: {
            dialog (val) {
                val || this.close()
            },
        },

        created () {
            this.initialize()
        },

        methods: {
            initialize () {
                this.characters = [

                ]
            },

            editItem (item) {
                this.editedIndex = this.characters.indexOf(item)
                this.editedItem = Object.assign({}, item)
                this.dialog = true
            },

            deleteItem (item) {
                const index = this.characters.indexOf(item)
                confirm('Are you sure you want to delete this item?') && this.characters.splice(index, 1)
            },

            close () {
                this.dialog = false
                setTimeout(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                }, 300)
            },

            save () {
                if (this.editedIndex > -1) {
                    Object.assign(this.characters[this.editedIndex], this.editedItem)
                } else {
                    this.characters.push(this.editedItem)
                }
                this.close()
            },
        },
    }
</script>

<style scoped>

</style>
