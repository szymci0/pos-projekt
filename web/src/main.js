import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import {ClientTable} from 'v-tables-3';

const app = createApp(App)
app.use(router)
app.mount('#app')

app.use(ClientTable)
