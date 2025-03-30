import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import HealthOperatorSearch from '@/components/HealthOperatorSearch.vue' // Importe o componente

const app = createApp(App)
app.component('HealthOperatorSearch', HealthOperatorSearch)
app.mount('#app')