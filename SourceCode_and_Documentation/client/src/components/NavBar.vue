<template>
  <div>
    <b-navbar type="light" variant="light" fixed="top">
      <b-navbar-brand href="/">
        <img src="../assets/logo.png" />
      </b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item-dropdown v-for="header in navBarHeaders"
        v-bind:key="header.id" v-bind:text="header.title">
          <b-dropdown-item v-for="item in header.items" v-bind:key="item.id" href="#">
              {{ item }}
          </b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-form>
          <b-form-input ref="searchBar" placeholder="Search"
            style="background-color:white;border-color:#CCCCCC;">
          </b-form-input>
          <b-button variant="outline-primary" @click="search">
            <img src="../assets/search_icon.png" width="20px" height="20px"/>
          </b-button>
        </b-nav-form>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto">
        <b-button variant="outline-primary" v-if="signedIn === false" href="/signin">
          <img src="../assets/user_icon.png" width="20px" height="20px"/>
          Sign In/Register
        </b-button>
        <b-nav-item-dropdown v-else v-bind:text="user" right>
          <b-dropdown-item href="#"> Account Details </b-dropdown-item>
          <b-dropdown-item @click="logout" href="#"> Logout </b-dropdown-item>
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
      signedIn: '',
      user: '',
    };
  },
  methods: {
    getData() {
      const path = 'http://localhost:5000/nav';
      axios
        .get(path)
        .then((res) => {
          this.navBarHeaders = res.data.navBarHeaders;
          this.signedIn = res.data.signedIn;
          if (this.signedIn) {
            this.user = res.data.user;
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    logout() {
      const path = 'http://localhost:5000/logout';
      axios
        .post(path)
        .then((response) => {
          console.log(response);
          this.$router.go();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    search() {
      const searchVal = this.$refs.searchBar.vModelValue;
      this.$emit('changedSearch', searchVal);
      this.$router.push({ name: 'Search', params: { searchTerm: searchVal } }).catch((err) => { console.error(err); });
    },
  },
  created() {
    this.getData();
  },
};
</script>
