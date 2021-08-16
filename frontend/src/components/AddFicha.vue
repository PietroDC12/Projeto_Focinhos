<template>

  <div class="container">
    <div class="wrapper fadeInDown">
      <div id="formContent">
        <h1>Cadastro</h1>

        <form>
          <p>
            <label for="nome_cachorro"></label>
            <input
              placeholder="Nome cachorro"
              type="text"
              id="nome_cachorro"
              v-model="cadastro.nome_cachorro"
              class="fadeIn second"
              name="cadastro"
            />
          </p>

         <p>
            <label for="idade"></label>
            <input
              placeholder="Idade"
              type="text"
              id="idade"
              v-model="cadastro.idade"
              class="fadeIn second"
              name="cadastro"
            />
          </p>

          <p>
            <label for="escolha_sexo"></label>
            <input
              placeholder="Sexo"
              type="text"
              id="escolha_sexo"
              v-model="cadastro.escolha_sexo"
              class="fadeIn second"
              name="cadastro"
            />
          </p>

          <p>
            <label for="tamanho_cachorro"></label>
            <input
              placeholder="Tamanho cachorro"
              type="text"
              id="tamanho_cachorro"
              v-model="cadastro.tamanho_cachorro"
              class="fadeIn third"
              name="cadastro"
            />
          </p>

          <p>
            <label for="raca"></label>
            <input
              placeholder="Raça"
              type="text"
              id="raca"
              v-model="cadastro.raca"
              class="fadeIn third"
              name="cadastro"
            />
          </p>

          <p>
            <label for="cor_pelagem"></label>
            <input
              placeholder="Cor da pelagem"
              type="text"
              id="cor_pelagem"
              v-model="cadastro.cor_pelagem"
              class="fadeIn third"
              name="cadastro"
            />
          </p>

          <p>
            <label for="nome_dono"></label>
            <input
              placeholder="Nome do dono"
              type="text"
              id="nome_dono"
              v-model="cadastro.nome_dono"
              class="fadeIn third"
              name="cadastro"
            />
          </p>

          <p>
            <label for="endereco"></label>
            <input
              placeholder="Endereço"
              type="text"
              id="endereco"
              v-model="cadastro.endereco"
              class="fadeIn third"
              name="cadastro"
            />
          </p>

            <p>
            <label for="email"></label>
            <input
              placeholder="Email"
              type="email"
              id="email"
              v-model="cadastro.email"
              class="fadeIn third"
              name="cadastro"
            />
          </p>

          <p>
            <label for="telefone"></label>
            <input
              placeholder="Telefone"
              type="text"
              id="telefone"
              v-model="cadastro.telefone"
              class="fadeIn third"
              name="cadastro"
            />
          </p>
          

          <input
            type="submit"
            class="fadeIn fourth"
            style="font-weight: bold"
            value="Cadastrar"
            v-on:click.prevent="addFicha()"
          />
        </form>
      </div>
    </div>
  </div>
</template>
 
<script>
import axios from "axios"

export default {
  name: "AddFicha",
  data() {
    return {
      dialog: false,
      cadastro: {},
      
    }
  },

  created(){
    //this.getFicha();
    //this.addFicha();
  },

  methods: {

    addFicha() {
      axios
        .post("http://127.0.0.1:8000/api/info/add/", this.cadastro,

        )
        .then((response) => {
          this.dialog = false;
          this.$emit("updateCadastro");
          this.log.console(response);
        });
    },
  },  
};
</script>