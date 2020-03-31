<template>
  <div>
    <navbar></navbar>
  <div class="center-screen">
  <div class="wrapper fadeInDown">
  <div id="formContent">
    <br>
    <form action="/emailsent">
      <h1 class="h3 mb-3 font-weight-normal">Forgot username/password?</h1>
      <p align="justify" color="#A9A9A9" style="margin-left:10%;margin-right:10%">
Not to worry! Enter your email address below and we will send you an email with
recovery details shortly.</p>
      <input type="email" id="email" class="email" name="email" placeholder="email"
required>
      <br>
      <button type="submit" class="btn btn-primary" style="padding:0px 10px">
Send recovery email</button>
    </form>
  </div>
</div>
  </div>
</div>
</template>
<script>
// import axios from 'axios';
import NavBar from '../components/NavBar.vue';

export default {
  name: 'Login',
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
