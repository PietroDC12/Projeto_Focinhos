import Vue from 'vue'
import VueRouter from 'vue-router';

import Index from '../components/Index.vue'
import AddFicha from '../components/AddFicha.vue'
import BuscaID from '../components/BuscaID.vue'
import BuscaImagem from '../components/BuscaImagem.vue'


//import { component } from 'vue/types/umd';

Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  hash: false,
  routes: [{
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/add-ficha',
      name: 'AddFicha',
      component: AddFicha
    },
    {
      path: '/busca-id',
      name: 'BuscaID',
      component: BuscaID
    },
    {
      path: '/busca-imagem',
      name: 'BuscaImagem',
      component: BuscaImagem
    },
    


  ]
})