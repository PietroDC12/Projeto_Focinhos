<template>
  <div class="container">
        <h1> Busca cachorro</h1>
      <ul>
        <li v-for="info in cadastro" :key="info.cachorro_id"> {{ info.nome_cachorro }}</li>
      </ul>
    <button @click="getFicha">Busca</button>
    </div>
    </div>
</template>
 
<script>
import axios from "axios"

export default {
  name: "BuscaID",
  data(){
    return {
      newFicha: "",
      fichas: [],
    }
  },

  methods: {
    getFicha(){
      axios.get("http://127.0.0.1:8000/api/info/").then((res) => {
        console.log(res.data),
        this.info = res.data
      })
    },
  }
  
};
</script>