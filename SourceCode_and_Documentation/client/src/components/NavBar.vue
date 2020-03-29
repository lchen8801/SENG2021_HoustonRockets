<template>
  <div>
    <b-navbar type="light" variant="light" fixed="top">
      <b-navbar-brand href="#">
        <img src="../assets/logo.png" />
      </b-navbar-brand>
      <b-navbar-nav>
          <b-nav-item-dropdown v-for="header in navBarHeaders"
          v-bind:key="header.id" v-bind:text="header.title">
            <b-dropdown-item v-for="item in header.items" v-bind:key="item.id" href="#">
                {{ item }}
            </b-dropdown-item>
          </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'NavBar',
  data() {
    return {
      navBarHeaders: '',
    };
  },
  methods: {
    getHeaders() {
      const path = 'http://localhost:5000/';
      axios
        .get(path)
        .then((res) => {
          this.navBarHeaders = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getHeaders();
  },
};
</script>
