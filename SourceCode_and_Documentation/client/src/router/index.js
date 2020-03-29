import Vue from 'vue';
import Router from 'vue-router';
import Test from '../components/Test.vue';
import NavBar from '../components/NavBar.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/test',
      name: 'Test',
      component: Test,
    },
    {
      path: '/',
      name: 'Home',
      component: NavBar,
    },
  ],
});
