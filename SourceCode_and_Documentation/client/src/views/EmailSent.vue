<template>
  <div>
    <navbar></navbar>
    <p style="margin-left:1%">Your recovery email has been sent.<br>Follow the
instructions provided to regain access to your account.</p>
  </div>
</template>
<script>
// import axios from 'axios';
import NavBar from '../components/NavBar.vue';

export default {
  name: 'EmailSent',
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

<style>
body {
  padding-top: 65px;
}
</style>
