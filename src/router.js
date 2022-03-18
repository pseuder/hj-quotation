import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/login'
import Main from '@/components/main'
import BackSide from '@/components/backSide'

Vue.use(Router)

export default new Router({
  routes: [
    {//防止有人亂try結構
      path: '*',
      redirect: '/login',
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/main',
      name: 'main',
      component: Main
    },
    {
      path: '/backSide',
      name: 'backSide',
      component: BackSide
    },
  ]
})
