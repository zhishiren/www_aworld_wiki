import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
// import { ElIcon } from 'element-plus'
// import { Loading } from '@element-plus/icons-vue'




const app = createApp(App).use(router)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}


app.use(ElementPlus)
app.mount('#app')

// // 以下代码是原始配置，以上是加入elementplus
// import { createApp } from 'vue';  
// import App from './App.vue'
// const app = createApp(App);  
// app.mount('#app');
// createApp(App).mount('#app')


