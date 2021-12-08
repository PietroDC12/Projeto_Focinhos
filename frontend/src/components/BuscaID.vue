<template>
  <div class="container">

   <h1> Busca cachorro</h1>

        <div class="row">
                <div class="col-12">
                    <form action="d">
                        <input type="text" name="buscar" placeholder="O que está procurando...">
                        <button type="submit"><i class="fa fa-search" aria-hidden="true"></i></button>
                    </form>
                </div>
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