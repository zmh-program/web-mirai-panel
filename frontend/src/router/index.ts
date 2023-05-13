import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NotFoundView from '@/views/NotFoundView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/404',
      name: 'error',
      component: NotFoundView
    }
  ]
})

router.beforeEach((to, from, next) => (
  to.matched.length === 0 ? next('/404') : next()
));

export default router
