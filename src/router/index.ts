import { createRouter, createWebHistory } from "vue-router";
import guestList from '@/mock/guestList.json';

const guestURLs = Object.keys(guestList);

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/admin',
      name: 'adminPage',
      component: () => import('@/pages/AdminPage.vue'),
    },
    {
      path: '/guests/:user',
      name: 'guestPage',
      component: () => import('@/pages/GuestPage.vue'),
      beforeEnter: (to) => {
        const user = to.params.user as string;
        if (!guestURLs.includes(user)) {
          return { name: 'NotFound' }
        }
      }
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: () => import('@/pages/ErrorPage.vue')
    }
  ],
});

export default router;