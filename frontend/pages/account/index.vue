<template>
  <v-container fluid>

    <!-- PROFILE -->
    <v-row wrap>
      <v-col>
        <v-card
          max-width="768"
          class="mx-auto"
        >
          <v-card-title class="secondary onsecondary--text"><h3>My Profile</h3></v-card-title>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">{{ user.username }}</v-list-item-title>
              <v-list-item-subtitle>Created: {{ parseDate(user.date_joined) }}</v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-avatar
              size="120"
              color="grey"
            >
              <v-hover v-slot:default="{ hover }">
                <v-img
                  sizes="100"
                  :src="avatar || '/images/image-placeholder.png'"
                >
                  <v-expand-transition>
                    <div
                      v-if="hover"
                      class="d-flex transition-fast-in-fast-out grey darken-2 v-card--reveal white--text"
                      style="height: 100%;"
                      @click="pickImage"
                    >
                      Change
                      <input
                        type="file"
                        style="display: none"
                        ref="image"
                        accept="image/*"
                        @change="onImagePicked"
                      >
                    </div>
                  </v-expand-transition>
                </v-img>
              </v-hover>
            </v-list-item-avatar>
          </v-list-item>

          <v-card-text v-if="isEditing">
            <v-form @submit.prevent="submit">
              <v-alert v-if="alert" :type="alert.type">{{ alert.message }}</v-alert>
              <v-text-field label="Email" v-model="form_data.email" :rules="emailRules" :readonly="!isEditing"/>
              <v-text-field label="FirstName" v-model="form_data.first_name" :readonly="!isEditing"/>
              <v-text-field label="LastName" v-model="form_data.last_name" :readonly="!isEditing"/>
              <v-row justify="center">
                <v-col class="text-center">
                  <v-btn type="submit" :loading="loading" :disabled="loading" outlined color="accent">Save</v-btn>
                  <v-btn text color="accent" @click="resetFormData">Cancel</v-btn>
                </v-col>
              </v-row>
            </v-form>
          </v-card-text>
          <v-card-text v-else>
            <v-text-field label="Email" v-model="form_data.email" :rules="emailRules" :readonly="!isEditing"/>
            <v-text-field label="FirstName" v-model="form_data.first_name" :readonly="!isEditing"/>
            <v-text-field label="LastName" v-model="form_data.last_name" :readonly="!isEditing"/>
            <v-row justify="center">
              <v-col class="text-center">
                <v-btn type="" outlined color="accent" @click="isEditing = true">Edit</v-btn>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <!-- EO PROFILE -->

    <!-- CREATED SPELLS --
    <v-row wrap>
      <v-col>
        <v-card
          max-width="768"
          class="mx-auto"
        >
          <v-card-title class="secondary onsecondary--text"><h3>My Spells</h3></v-card-title>
          <v-card-text>
            <v-list>
              <v-list-group
                v-for="item in spells"
                :key="item.title"
                v-model="item.active"
                :prepend-icon="item.action"
                no-action
              >
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title v-text="item.title"></v-list-item-title>
                  </v-list-item-content>
                </template>

                <v-list-item
                  v-for="subItem in item.items"
                  :key="subItem.title"
                  @click=""
                >
                  <v-list-item-content>
                    <v-list-item-title v-text="subItem.title"></v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-group>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    !-- EO CREATED SPELLS -->

  </v-container>
</template>

<script>
  import api from '~/api'
  import FormData from 'form-data'
  export default {
    async asyncData(context) {
      try {
        let userId = context.store.state.auth.user.id
        let user = await context.$axios.$get(`/users/${userId}`);
        if (user != undefined){
          console.log("/account/index asyncData() user", user)
          return {
            user: user,
            avatar: user.profile.avatar,
            form_data: {
              email: user.email,
              first_name: user.first_name,
              last_name: user.last_name,
            },

              spells: [
          {
            action: 'local_activity',
            title: 'Attractions',
            items: [
              { title: 'List Item' },
            ],
          },
          {
            action: 'restaurant',
            title: 'Dining',
            active: true,
            items: [
              { title: 'Breakfast & brunch' },
              { title: 'New American' },
              { title: 'Sushi' },
            ],
          },
          {
            action: 'school',
            title: 'Education',
            items: [
              { title: 'List Item' },
            ],
          },
          {
            action: 'directions_run',
            title: 'Family',
            items: [
              { title: 'List Item' },
            ],
          },
          {
            action: 'healing',
            title: 'Health',
            items: [
              { title: 'List Item' },
            ],
          },
          {
            action: 'content_cut',
            title: 'Office',
            items: [
              { title: 'List Item' },
            ],
          },
          {
            action: 'local_offer',
            title: 'Promotions',
            items: [
              { title: 'List Item' },
            ],
          },
        ],


          }
        }
      } catch (e) {
        context.redirect('/account/login')
      }
    },
    data: () => ({
      isEditing: false,
      user: {},
      avatar: '/images/image-placeholder.png',
      form_data: {
          email: '',
          first_name: '',
          last_name: ''
      },
      emailRules: [
        v => (!v || /.+@.+\..+/.test(v))  || 'Email must be valid',
      ],
      alert: null,
      loading: false
    }),
    methods: {
      resetFormData() {
        this.form_data = {
          email: this.user.email,
          first_name: this.user.first_name,
          last_name: this.user.last_name,
        }
        this.isEditing = false
      },
      parseDate(dateTimeString) {
        try {
            let date = new Date(dateTimeString)
            return `${date.getDate()}-${date.getMonth() + 1}-${date.getFullYear()}`
        }
        catch (e1) {
          try {
            let date = dateTimeString.split("T")[0]
            let dateparams = date.split("-")
            return `${dateparams[2]}-${dateparams[1]}-${dateparams[0]}`
          }
          catch (e2) {
            return ""
          }
        }
      },
      submit () {
        if (this.isEditing == false) return
        this.alert = null
        this.loading = true
        api.updateUserProfile(this.$axios, this.user.id, this.form_data)
          .then(result => {
            //console.log('/account/index.vue .then() result', result)
            this.alert = {type: 'success', message: result.message || 'Success'}
            this.loading = false
            this.isEditing = false
            this.user.first_name = this.form_data.first_name
            this.user.last_name = this.form_data.last_name
            this.user.email = this.form_data.email
          })
        .catch(error => {
          console.log('/account/index.vue .catch() error', error)
          console.log('/account/index.vue .catch() error.response', error.response)
          this.loading = false
          if (error.response && error.response.data) {
            this.alert = {
              type: 'error',
              message: error.response.data || 'Error'
            }
          }
        })
      },
      pickImage() {
        this.$refs.image.click()
      },
      onImagePicked (e) {
        console.clear()
        const files = e.target.files
        if(files[0] !== undefined) {
          if(files[0].name.lastIndexOf('.') <= 0) {
            console.log('/account/index.vue onImagePicked() files[0].name.lastIndexOf(\'.\') <= 0')
            return
          }
          const fr = new FileReader ()
          fr.readAsDataURL(files[0])
          fr.addEventListener('load', () => {
            let form_data = new FormData()
            form_data.append('avatar', files[0], files[0].name)
            this.$axios.$put(`profiles/${this.user.profile.id}/`,
                             form_data,
                             { headers: {'Content-Type': 'multipart/form-data'}})
              .then(data => {
                console.log('then data', data)
              })
              .catch(error => {
                console.log('/account/index.vue onImagePicked() .catch error', error)
                console.log('/account/index.vue onImagePicked() .catch error.response', error.response)
              })
            this.avatar = fr.result
          })
        } else {
          this.avatar = '/images/image-placeholder.png'
        }
      }
    },
  }
</script>

<style scoped>
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: .75;
  position: absolute;
  width: 100%;
}
</style>
