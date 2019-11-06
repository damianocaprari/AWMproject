<template>
  <v-app>
    <v-container class="col-15">
      <v-container>
        <v-row>
          <v-col cols="12" md="6">
            <h1 class="mb-5 ml-3">Atmospheric musics</h1>

            <v-card width="320" class="mb-5 mr-5 d-sm-none">
              <h2 class="text-center"> Village</h2>
              <iframe width="320" height="180" src="https://www.youtube.com/embed/xu2pESvXcmM"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </v-card>

            <v-card max-width="320" class="mb-5 mr-5">
              <h2 class="text-center"> Tavern</h2>
              <iframe width="320" height="180" src="https://www.youtube.com/embed/4r_5A6K7gu0"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </v-card>

            <v-card max-width="320" class="mb-5 mr-5">
              <h2 class="text-center">City</h2>
              <iframe width="320" height="180" src="https://www.youtube.com/embed/ZiHtOVw8zsA"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </v-card>

            <v-card max-width="320" class="mb-5 mr-5">
              <h2 class="text-center">Castle</h2>
              <iframe width="320" height="180" src="https://www.youtube.com/embed/uIbAzScUwec"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </v-card>

            <v-card max-width="320" class="mb-5 mr-5">
              <h2 class="text-center">Holy place</h2>
              <iframe width="320" height="180" src="https://www.youtube.com/embed/RG1ydqEEa0c"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </v-card>

            <v-card max-width="320" class="mb-5 mr-5">
              <h2 class="text-center">Creepy</h2>
              <iframe width="320" height="180" src="https://www.youtube.com/embed/per3XrNT3QU"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </v-card>

            <v-card max-width="320" class="mb-5 mr-5">
              <h2 class="text-center">Wild</h2>
              <iframe width="320" height="180" src="https://www.youtube.com/embed/xHP2GgxYddY"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </v-card>


          </v-col>
          <v-col cols="12" md="6">
            <h1 class="mb-5 ml-10">Combat musics</h1>
            <v-card width="320" class="mb-5 mr-5">
              <h2 class="text-center"> Tribal</h2>
              <iframe width="320" height="180" src="https://www.youtube.com/embed/KoTku7qMZOM"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </v-card>

            <v-card width="320" class="mb-5 mr-5">
              <h2 class="text-center"> Tavern</h2>
              <iframe width="320" height="180" src="https://www.youtube.com/embed/0p79IBaksXU"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </v-card>


            <v-card width="320" class="mb-5 mr-5">
              <h2 class="text-center"> City</h2>
              <iframe width="320" height="180" src="https://www.youtube.com/embed/VaKVLWZrG-4"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </v-card>

            <v-card width="320" class="mb-5 mr-5">
              <h2 class="text-center"> Epic</h2>
              <iframe width="320" height="180" src="https://www.youtube.com/embed/1NhoXJrnNUM"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </v-card>


            <v-card width="320" class="mb-5 mr-5">
              <h2 class="text-center"> Dramatic</h2>
              <iframe width="320" height="180" src="https://www.youtube.com/embed/4uvqbpkowLA"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </v-card>

            <v-card width="320" class="mb-5 mr-5">
              <h2 class="text-center"> Celtic</h2>
              <iframe width="320" height="180" src="https://www.youtube.com/embed/jWObTfiovD8"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </v-card>

            <v-card width="320" class="mb-5 mr-5">
              <h2 class="text-center">Naval battle</h2>
              <iframe width="320" height="180" src="https://www.youtube.com/embed/_-ck4DAGtzs"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </v-card>

          </v-col>
        </v-row>

        <v-btn class="ma-2" v-scroll="onScroll" fab right bottom fixed color="primary" @click="toTop">
          <v-icon>mdi-arrow-up</v-icon>
        </v-btn>

      </v-container>
    </v-container>
  </v-app>
</template>


<script>
    export default {
        head() {
            return {
                title: `AWM Project - Musics`
            };
        },
        methods: {
            onScroll(e) {
                if (typeof window === 'undefined')
                    return
                const top = window.pageYOffset || e.target.scrollTop || 0
                this.fab = top > 20
            },
            toTop() {
                this.$vuetify.goTo(0)
            },

        }
    }
</script>


<style scoped>
  .subtitle {
    font-size: 30px;
    font-weight: bold;
  }


</style>
