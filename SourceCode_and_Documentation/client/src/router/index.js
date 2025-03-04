import Vue from 'vue';
import Router from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Signup from '../views/Signup.vue';
import Reset from '../views/Reset.vue';
import EmailSent from '../views/EmailSent.vue';
import Search from '../views/Search.vue';
import Event from '../views/Event.vue';
import PasswordChange from '../views/PasswordChange.vue';

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
    {
      path: '/search/:searchTerm',
      name: 'Search',
      component: Search,
    },
    {
      path: '/event/:id',
      name: 'Event',
      component: Event,
    },
    {
      path: '/passwordchange',
      name: 'PasswordChange',
      component: PasswordChange,
    },
  ],
});
