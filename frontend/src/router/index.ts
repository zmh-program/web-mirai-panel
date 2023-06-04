import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { isAuthenticated } from '@/assets/script/config'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: () => import("../views/LoginView.vue")
    },
    {
      path: '/404',
      name: 'error',
      component: () => import("../views/NotFoundView.vue")
    },
    {
      path: '/config',
      name: 'config',
      component: () => import("../views/ConfigView.vue")
    },
    {
      path: '/term',
      name: 'term',
      component: () => import("../views/TermView.vue")
    },
    {
      path: '/upload',
      name: 'upload',
      component: () => import("../views/FileUploadView.vue")
    },
    {
      path: '/setting',
      name: 'setting',
      component: () => import("../views/SettingView.vue")
    }
  ],
  scrollBehavior(to) {
    return to.hash ? { selector: to.hash } : { left: 0, right: 0 };
  }
})

router.beforeEach((to, from, next) => {
  if (!["login", "error"].includes(<string>to.name) && !isAuthenticated.value) {
    next({ name: "login" });
    return
  } else {
    if (to.name === "login" && isAuthenticated.value) {
      next({ name: "home" });
      return
    }
  }
  if (to.matched.length === 0) {
    next('/404');
    return
  }
  next();
});

export default router
