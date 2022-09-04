import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ContactsView from '../views/ContactsView.vue'
import ServicesView from '../views/ServicesView.vue'
import SkillsView from '../views/SkillsView.vue'
import TestimonialsView from '../views/TestimonialsView.vue'
import WorkView from '../views/WorkView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/contacts',
    name: 'contacts',
    component: ContactsView
  },
  {
    path: '/services',
    name: 'services',
    component: ServicesView
  },
  {
    path: '/skills',
    name: 'skills',
    component: SkillsView
  },
  {
    path: '/testimonials',
    name: 'testimonials',
    component: TestimonialsView
  },
  {
    path: '/work',
    name: 'work',
    component: WorkView
  },
 
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeResolve((to, from, next) => {
  // If this isn't an initial page load.
  if (to.name) {
    // Start the route progress bar.
    NProgress.start()
    NProgress.configure({ easing: 'ease', speed: 2000 , height:'4px' });
  }
  next()
})

router.afterEach((to, from) => {
  // Complete the animation of the route progress bar.
  NProgress.done()
})

export default router
