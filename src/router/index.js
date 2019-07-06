import Vue from 'vue'
import Router from 'vue-router'
import FishUI from 'fish-ui'
import HelloWorld from '@/components/HelloWorld'
import login from '@/components/login'
import admin from '@/components/admin'
import Notifications from 'vue-notification'

Vue.use(FishUI)
Vue.use(Router)
Vue.use(Notifications)

export default new Router({
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
    },
    {
      path: '/admin',
      name: 'admin',
      component: admin
    }
  ]
})
