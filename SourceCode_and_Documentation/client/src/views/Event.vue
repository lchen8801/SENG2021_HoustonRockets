<template>
  <div>
    <navbar></navbar>
<div class="container">
<div class="row">
<div class="col">
    <h1> {{ eventdata.name }} </h1>
</div>
<div class="col">
<h2>Directions</h2>
</div>
</div>
<div class="row">
<div class="col">
<img v-bind:src="eventdata.img" style="width:100%;">
</div>
<div class="col">
<iframe style="width:100%;height:100%"
v-bind:src="'https://www.google.com/maps/embed/v1/directions?origin=UNSW&destination='
+ eventdata.location + '&key=AIzaSyCvKEl8IR2YcNzK5P80dQAZ5CI88nvX0nk'"
 allowfullscreen></iframe>
</div>
</div>
<div class="row" style="margin-top:5%">
<div class="col-8">
<p>{{ eventdata.desc }}</p>
</div>
<div class="col-4">
<div class="text-center"><h2>Event Date</h2></div>
<div class="text-center"><h2><span class="badge badge-secondary">23 OCT</span></h2>
</div>
</div>
</div>
</div>
</div>
</template>

<script>
import axios from 'axios';
import NavBar from '../components/NavBar.vue';

export default {
  name: 'Event',
  data() {
    return {
      eventdata: '',
      searchTerm: '',
    };
  },
  components: {
    navbar: NavBar,
  },
  methods: {
    getEvent() {
      const path = 'http://localhost:5000/event';
      const getParams = { id: this.$route.params.id };
      this.id = this.$route.params.id;
      console.log(getParams);
      axios
        .get(path, { params: { getParams } })
        .then((res) => {
          this.eventdata = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getEvent();
  },
};
</script>

<style>
body {
  padding-top: 65px;
}
</style>
