<template>
  <v-container>
    <div class="hp-text-box hp-header">
      <h1>DnD 5.0</h1>
      <p class="mt-3">A simple wiki of the best rpg ever! </p>

      <v-col class="text-center" cols="">
        <div style="margin-bottom: 10px;"> <v-btn to="/conditions" block>View Conditions</v-btn> </div>
        <div style="margin-bottom: 10px;"> <v-btn to="/spells" block>View Spells</v-btn> </div>
        <div style="margin-bottom: 10px;"> <v-btn to="/monsters" block>View Monsters</v-btn> </div>
        <div style="margin-bottom: 10px;"> <v-btn to="/musics" block>View Musics links</v-btn> </div>

      </v-col>

    </div>
  </v-container>
</template>


<script>
export default {
  layout: 'homepage',
  head(){
      return {
          title: "AWM Project"
      };
  },
};
</script>


<style>
  .hp-text-box{
    position: absolute;
    top: 50%;
    left: 10%;
    transform: translateY(-50%);
    color: #fff;
  }
  .hp-text-box h1 {
    font-family: cursive;
    font-size: 5rem;
  }
  .hp-text-box p {
  font-size: 2rem;
  font-weight: lighter;
  }
</style>
