<template>
  <navbar></navbar>
</template>

<script>
// import axios from 'axios';
import NavBar from '../components/NavBar.vue';

export default {
  name: 'Home',
  //   data() {
  //     return {
  //       navBarHeaders: '',
  //     };
  //   },
  components: {
    navbar: NavBar,
  },
  //   methods: {
  //     getHeaders() {
  //       const path = 'http://localhost:5000/';
  //       axios
  //         .get(path)
  //         .then((res) => {
  //           this.navBarHeaders = res.data;
  //         })
  //         .catch((error) => {
  //           // eslint-disable-next-line
  //           console.error(error);
  //         });
  //     },
  //   },
  //   created() {
  //     this.getHeaders();
  //   },
};
</script>
