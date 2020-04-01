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
    <div class="col">
      <div class="weathercard">
        <p>{{ eventdata.desc }}</p>
      </div>
    </div>
  <div class="col">
      <div class="text-center">
    <h2>Date and Weather</h2>
      <div class="weathercard">
        <h1>
04 APR 2020</h1><h5>Sunny</h5>
        <h1><i class="wi wi-day-sunny"></i>  {{ eventdata.weather.temperature }}°</h1>
      <p> Wind: {{ eventdata.weather.wind }}<br>
      Precipitation: {{ eventdata.weather.precipitation }}<br>
      Humidity: {{ eventdata.weather.humidity }}</p>
      </div>
      <h2 style="margin-top:20px;">Venue Information</h2>
      <iframe height="450" style="width:100%;"
      v-bind:src="'https://www.google.com/maps/embed/v1/place?q=' + eventdata.location
      + 'Hordern%20Pavillion&key=AIzaSyCvKEl8IR2YcNzK5P80dQAZ5CI88nvX0nk'"
      allowfullscreen></iframe>
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
@import './css/weather-icons.min.css';

body {
  padding-top: 65px;
  min-width:960px;
}
.weathercard {
    margin: 0 auto;
    margin-top: 5%;
    padding: 30px 30px;
    border-radius: 3px;
    background-color: #fff;
    box-shadow: 1px 2px 10px rgba(0, 0, 0, .2);
    text-align: center;
}


h1,
h2,
h3,
h4 {
    position: relative;
}

h1 {
    color: #666;
    font-weight: 300;
    font-size: 6.59375em;
    line-height: .2em;
}

h2 {
    font-weight: 300;
    font-size: 2.25em;
}

h3 {
    float: left;
    color: #777;
    font-weight: 400;
    font-size: 1em;
}

span {
    margin-left: 24px;
    color: #999;
    font-weight: 300;
}

span span {
    margin-left: 0;
}

.dot {
    font-size: .9em;
}
</style>
