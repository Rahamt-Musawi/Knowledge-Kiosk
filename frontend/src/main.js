import { createApp } from 'vue'
import App from './App.vue'
import io from 'socket.io-client'
import "./index.css"

const socket = io('http://localhost:5000') // Replace with your backend server URL
const app = createApp(App)
app.config.globalProperties.$socket = socket

app.mount('#app')
