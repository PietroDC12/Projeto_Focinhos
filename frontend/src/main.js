//import { createApp } from 'vue'
import App from './App.vue'
import Vue from 'vue'
import VueRouter from 'vue-router'
import router from '@/router'
import 'bootstrap/dist/css/bootstrap.css'

Vue.use(VueRouter)

new Vue({
    render: h => h(App),
    router
}).$mount('#app')