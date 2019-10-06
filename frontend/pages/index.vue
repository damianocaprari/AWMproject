<template>
  <header>
    <div class="text-box">
      <h1>DnD 5.0</h1>
      <p class="mt-3">A simple wiki of the best rpg ever! </p>

      <v-col class="text-center" cols="">
        <div style="margin-bottom: 10px;"> <v-btn to="/conditions" block>View Conditions</v-btn> </div>
        <div style="margin-bottom: 10px;"> <v-btn to="/spells" block>View Spells</v-btn> </div>
      </v-col>

    </div>
  </header>
</template>


<script>
export default {
  head(){
      return {
          title: "Home page"
      };
  },
};
</script>


<style>
  header {
      min-height: 100vh;
      background-image: linear-gradient(
        to right,
        rgba(0, 0, 0, 0.9),
        rgba(0, 0, 0, 0.4)
      ),
      url("/images/dndWallpaper.jpg");
      background-position: center;
      background-size: cover;
      position: relative;
  }
  .text-box{
    position: absolute;
    top: 50%;
    left: 10%;
    transform: translateY(-50%);
    color: #fff;
  }

  .text-box h1 {
    font-family: cursive;
    font-size: 5rem;
  }
  .text-box p {
  font-size: 2rem;
  font-weight: lighter;
  }
</style>
