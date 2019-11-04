<template>
  <v-row>
    <!-- for screen < 600px -->
    <v-col class="d-sm-none">
      <v-data-table
        dense
        :headers="headers_xs"
        :items="characters"
        :expanded.sync="expanded"
        @click:row="expandRow"
        item-key="key"
        show-expand
        sort-by="initiative"
        class="elevation-1"
        disable-sort disable-filtering disable-pagination
        hide-default-footer hide-default-header
      >
        <template v-slot:top>
          <v-toolbar flat class="secondary onsecondary--text">
            <v-toolbar-title>Initiative Tracker</v-toolbar-title>
            <!--<v-divider class="mx-4" inset vertical ></v-divider>-->
            <v-spacer></v-spacer>
            <v-dialog v-model="dialog" max-width="500px">
              <template v-slot:activator="{ on }">
                <v-btn color="onsecondary" outlined v-on="on" small>Add</v-btn>
                <v-btn text color="onsecondary" @click="initialize" x-small>Clear</v-btn>
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
                        <v-text-field v-model="editedItem.init" label="Initiative"></v-text-field>
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

        <template flat v-slot:expanded-item="{ headers, item }">
          <v-container class="body-2">
            <v-row dense>
              <v-col cols="6">
                <span class="font-weight-bold">HP</span>&nbsp;{{ item.hp }}
              </v-col>
              <v-col cols="6">
                <v-divider vertical></v-divider>
                <span class="font-weight-bold">AC</span>&nbsp;{{ item.ac }}
              </v-col>
              <v-col cols="4">
                <span class="font-weight-bold">Str</span>&nbsp;{{ item.str }}&nbsp;{{getModifier(item.str)}}
              </v-col>
              <v-col cols="4">
                <v-divider vertical></v-divider>
                <span class="font-weight-bold">Con</span>&nbsp;{{ item.con }}&nbsp;{{getModifier(item.con)}}
              </v-col>
              <v-col cols="4">
                <v-divider vertical></v-divider>
                <span class="font-weight-bold">Dex</span>&nbsp;{{ item.dex }}&nbsp;{{getModifier(item.dex)}}
              </v-col>
              <v-col cols="4">
                <span class="font-weight-bold">Int</span>&nbsp;{{ item.int }}&nbsp;{{getModifier(item.int)}}
              </v-col>
              <v-col cols="4">
                <v-divider vertical></v-divider>
                <span class="font-weight-bold">Wis</span>&nbsp;{{ item.wis }}&nbsp;{{getModifier(item.wis)}}
              </v-col>
              <v-col cols="4">
                <v-divider vertical></v-divider>
                <span class="font-weight-bold">Cha</span>&nbsp;{{ item.cha }}&nbsp;{{getModifier(item.cha)}}
              </v-col>
            </v-row>
          </v-container>
        </template>

        <template v-slot:no-data>
          Start adding characters!
        </template>
      </v-data-table>
    </v-col>

    <!-- for screen >= 600px -->
    <v-col class="d-none d-sm-block">
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
                <v-btn color="onsecondary" outlined v-on="on">Add</v-btn>
                <v-btn text color="onsecondary" @click="initialize">Clear</v-btn>
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
                        <v-text-field v-model="editedItem.init" label="Initiative"></v-text-field>
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

        <template v-slot:no-data>
          Start adding characters!
        </template>
      </v-data-table>
    </v-col>

  </v-row>
</template>

<script>
    export default {
        data: () => ({
            dialog: false,
            expanded: [],
            headers: [
                { text: 'Name', value: 'name', sortable: false, },
                { text: 'Initiative', value: 'init', sortable: false, },
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
            headers_xs: [
                { text: 'Name', value: 'name', sortable: false, },
                { text: 'Initiative', value: 'init', sortable: false, },
                { text: 'Actions', value: 'action', sortable: false },
            ],
            key: 0,
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
                return this.editedIndex === -1 ? 'Add character' : 'Edit character'
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
            getModifier(n) {
                if (!n) return ''
                n = Math.floor(n/2 -5)
                if (n >= 0) return `(+${n})`
                else return `(${n})`
            },
            expandRow(item) {
                let idx = this.expanded.indexOf(item)
                if (idx > -1)
                    this.expanded.splice(idx, 1)
                else
                    this.expanded.push(item)
            },
            initialize () {
                this.characters = []
                this.expanded = []
                this.key = 0
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
                    this.editedItem['key'] = ++this.key
                    this.characters.push(this.editedItem)
                }
                this.close()
            },
        },
    }
</script>

<style>
.v-data-table tbody tr.v-data-table__expanded__content {
  box-shadow: none;
  background-color: rgba(0, 0, 0, 0.03);
}
</style>
