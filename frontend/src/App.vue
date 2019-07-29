<template>
  <v-app id="app">
    <Header/>
    <v-content>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
    <Footer/>
  </v-app>
</template>

<script>
  import Header from "@/components/Header";
  import Footer from "@/components/Footer";

  export default {
    name: "App",
    components: {
      Header,
      Footer
    }
  };
</script>
