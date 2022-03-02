<template>
  <div>
    <!-- <v-app id=""> -->
      <nav-bar ref="drawer" />
      <section id="content">
        <router-view></router-view>
      </section>
    <!-- </v-app> -->
  </div>
</template>
 
<script>
import NavBar from "./components/NavBar";


export default {
  name: "App",
  components: {
    NavBar,
  },
};
</script>