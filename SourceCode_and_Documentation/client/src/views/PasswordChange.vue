<template>
  <div>
    <navbar></navbar>
  <div class="center-screen">
  <div class="wrapper fadeInDown">
  <div id="formContent">
    <br>
    <form @submit.prevent="changepassword">
      <h1 class="h3 mb-3 font-weight-normal">Change Password</h1>
      <b-alert v-bind:show="showAlert" variant="danger">
        {{ alertMsg }}
      </b-alert>
      <input type="password" id="curr_password" class="form-control" placeholder="current password"
ref="curr_password" required>
      <input type="password" id="new_password" class="form-control" placeholder="new password"
required ref="new_password">
      <input type="password" id="conf_new_password" class="form-control"
placeholder="confirm new password" required ref="conf_new_password">
      <br>
      <button type="submit" class="btn btn-primary" @click="changepassword">Change password</button>
    </form>
  </div>
</div>
  </div>
</div>
</template>

<script>
import axios from 'axios';
import NavBar from '../components/NavBar.vue';

export default {
  name: 'PasswordChange',
  components: {
    navbar: NavBar,
  },
  data() {
    return {
      showAlert: false,
      alertMsg: '',
    };
  },
  methods: {
    changepassword() {
      const path = 'http://localhost:5000/changepassword';
      const currPassword = this.$refs.curr_password.value;
      const newPassword = this.$refs.new_password.value;
      const confNewPassword = this.$refs.conf_new_password.value;
      if (newPassword === confNewPassword) {
        axios
          .post(path, {
            currPassword,
            newPassword,
            confNewPassword,
          })
          .then((response) => {
            console.log(response);
            if (response.data.status === 'Fail') {
              this.alertMsg = response.data.msg;
              this.showAlert = true;
            } else {
              this.$router.push('/');
            }
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      } else {
        this.alertMsg = 'New passwords do not match.';
        this.showAlert = true;
      }
    },
  },
};
</script>

<style>
html {
  background-color: #56baed;
}
body {
  font-family: "Poppins", sans-serif;
  height: 100vh;
}
a {
  color: #92badd;
  display:inline-block;
  text-decoration: none;
  font-weight: 400;
}
h2 {
  text-align: center;
  font-size: 16px;
  font-weight: 600;
  text-transform: uppercase;
  display:inline-block;
  margin: 40px 8px 10px 8px;
  color: #cccccc;
}
/* STRUCTURE */
.wrapper {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  min-height: 100%;
  padding: 20px;
}
#formContent {
  -webkit-border-radius: 10px 10px 10px 10px;
  border-radius: 10px 10px 10px 10px;
  background: #fff;
  padding: 30px;
  width: 90%;
  max-width: 450px;
  position: relative;
  padding: 0px;
  -webkit-box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3);
  box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3);
  text-align: center;
}
#formFooter {
  background-color: #f6f6f6;
  border-top: 1px solid #dce8f1;
  padding: 25px;
  text-align: center;
  -webkit-border-radius: 0 0 10px 10px;
  border-radius: 0 0 10px 10px;
}
/* TABS */
h2.inactive {
  color: #cccccc;
}
h2.active {
  color: #0d0d0d;
  border-bottom: 2px solid #5fbae9;
}
/* FORM TYPOGRAPHY*/
input[type=text] {
  background-color: #f6f6f6;
  border: none;
  color: #0d0d0d;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 5px;
  width: 85%;
  border: 2px solid #f6f6f6;
  -webkit-transition: all 0.5s ease-in-out;
  -moz-transition: all 0.5s ease-in-out;
  -ms-transition: all 0.5s ease-in-out;
  -o-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
}
input[type=text]:focus {
  background-color: #fff;
  border-bottom: 2px solid #5fbae9;
}
input[type=text]:placeholder {
  color: #cccccc;
}
input[type=password] {
  background-color: #f6f6f6;
  border: none;
  color: #0d0d0d;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 5px;
  width: 85%;
  border: 2px solid #f6f6f6;
  -webkit-transition: all 0.5s ease-in-out;
  -moz-transition: all 0.5s ease-in-out;
  -ms-transition: all 0.5s ease-in-out;
  -o-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
}
input[type=password]:focus {
  background-color: #fff;
  border-bottom: 2px solid #5fbae9;
}
input[type=password]:placeholder {
  color: #cccccc;
}
button[type=submit] {
  margin-bottom: 20px;
  margin-top: 20px;
  padding: 0px 80px;
}
.underlineHover:after {
  display: block;
  left: 0;
  bottom: -10px;
  width: 0;
  height: 2px;
  background-color: #56baed;
  content: "";
  transition: width 0.2s;
}
.underlineHover:hover {
  color: #0d0d0d;
}
.underlineHover:hover:after{
  width: 100%;
}
.center-screen {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  min-height: 100vh;
}
/* OTHERS */
*:focus {
    outline: none;
}
#icon {
  width:60%;
}
</style>
