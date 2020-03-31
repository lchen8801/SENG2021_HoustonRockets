import Vue from 'vue';
import Router from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Signup from '../views/Signup.vue';
import Reset from '../views/Reset.vue';
import EmailSent from '../views/EmailSent.vue';

Vue.use(Router);
export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/signin',
      name: 'Login',
      component: Login,
    },
    {
      path: '/register',
      name: 'Signup',
      component: Signup,
    },
    {
      path: '/reset',
      name: 'Reset',
      component: Reset,
    },
    {
      path: '/emailsent',
      name: 'EmailSent',
      component: EmailSent,
    },
  ],
});
