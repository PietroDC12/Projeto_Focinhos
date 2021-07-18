<template>
  <div class="container">
    <h1> Adicionar Cachorro </h1>
      <ul>
        <li> </li>
      </ul>

    <input v-model="newFicha" type="text" />
    <button @click="addFicha">Adicionar</button>
  </div>
</template>
 
<script>
import axios from "axios"

export default {
  name: "AddFicha",
  data(){
    return {
      newFicha: "",
      fichas: [],
    }
  },

  methods: {
    addFicha() {
      axios.put("", { nome_cachorro: this.newFicha })
      this.InfoGet()
    },
  }
  
};
</script>