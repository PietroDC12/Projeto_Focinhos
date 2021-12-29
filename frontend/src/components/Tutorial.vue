<template>
  <div class="container pt-5 pb-5 text-center">
    <img class="border p-3" :src="tutorial" :alt="descricao">
  </div>
</template>
 
<script>
  export default {
    name: "Tutorial",
    data () {
      return {
        tutorial :"/img/tutorial-focinho.jfif",
        descricao: "Folder-Tutorial"
      }
    }
  };
</script>

<style>
  .border {
    border-radius: 2rem;
  }
</style>
