import Vue from 'vue'
import Router from 'vue-router'
import FishUI from 'fish-ui'
import HelloWorld from '@/components/HelloWorld'
import login from '@/components/login'

Vue.use(FishUI)
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/main',
      name: 'main',
      component: HelloWorld
    },
    {
      path: '/login',
      name: 'login',
      component: login
    }
  ]
})
