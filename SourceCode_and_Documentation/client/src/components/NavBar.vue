<template>
  <div>
    <b-navbar type="light" variant="light" fixed="top">
      <b-navbar-brand href="/">
        <img src="../assets/logo.png" />
      </b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item-dropdown v-for="header in navBarHeaders"
        v-bind:key="header.id" v-bind:text="header.title">
          <b-dropdown-item v-for="item in header.items" v-bind:key="item.id"
          @click="headerSearch(item)">
              {{ item }}
          </b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-form>
          <b-form-input ref="searchBar" placeholder="Search" class="ml-5"
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
          <b-dropdown-item href="/passwordchange"> Change Password </b-dropdown-item>
          <b-dropdown-item @click="logout" href="#"> Logout </b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
      <div class = "fixed-bottom" v-if="temp === true">
        <div class = "alert alert-primary" role = "alert" style = "margin-bottom: 0px;">
          Hey, it looks like you signed in with a temporary password. Click
          <a href="/passwordchange"> here </a> to change it.
        </div>
      </div>
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
      temp: '',
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
            this.temp = res.data.temp;
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
    headerSearch(category) {
      this.$emit('headerSelect', category);
      this.$router.push({ name: 'Search', params: { searchTerm: `category: ${category}` } }).catch((err) => { console.error(err); });
    },
  },
  created() {
    this.getData();
  },
};
</script>
