import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios'
import VueAxios from 'vue-axios'
import qs from  'qs'  

//配全局属性配置，在任意组件内可以使用this.$qs獲取qs对象 (axios.post需要)
Vue.prototype.$qs = qs

Vue.config.productionTip = false
Vue.use(VueAxios, axios)
axios.defaults.baseURL = '/api'//跨域問題
Vue.use(ElementUI);
Vue.config.devtools = true



router.beforeEach((to, from, next)=>{
    
    next();
 
});

const vue = new Vue({
  router,
  render: h => h(App)
})

vue.$mount('#app')