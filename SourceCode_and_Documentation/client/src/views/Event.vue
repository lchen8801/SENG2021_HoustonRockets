<template>
  <div>
    <navbar></navbar>
<div class="container">
  <div class="row">
    <div class="col-3">
      <h1> {{ eventdata.name }} </h1>
    </div>
    <div class="col-1">
      <favourite-button v-bind:id="eventdata.id" v-bind:favourite="eventdata.favourite">
      </favourite-button>
    </div>
    <div class="col-2">
      <b-button v-bind:href="eventdata.url" target="_blank"> Buy Tickets </b-button>
    </div>
    <div class="col">
      <div class="text-center">
        <h2>Directions</h2>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col">
      <img v-bind:src="eventdata.images[0].url" style="width:100%;">
    </div>
    <div class="col">
      <iframe style="width:100%;height:100%"
      v-bind:src="'https://www.google.com/maps/embed/v1/directions?origin=' + latitude
      + ',' + longitude + '&destination='
      + eventdata._embedded.venues[0].name + '&key=AIzaSyCvKEl8IR2YcNzK5P80dQAZ5CI88nvX0nk'"
      allowfullscreen></iframe>
    </div>
  </div>
  <div class="row" style="margin-top:5%">
    <div class="col">
      <div class="weathercard">
        <!-- <p>{{ eventdata.desc }}</p> -->
        <p> testing </p>
      </div>
    </div>
  <div class="col">
      <div class="text-center">
    <h2>Date and Weather</h2>
      <div class="weathercard">
        <h1>{{ eventdate.toDateString() }}</h1>
        <div v-if="eventdata.weather != null">
          <h4>{{ eventdata.weather.weather[0].main }}</h4>
          <h1><img v-bind:src="'http://openweathermap.org/img/wn/' + eventdata.weather.weather[0].icon + '@2x.png'">
          {{ eventdata.weather.main.temp }}°C</h1>
          <p> Wind: {{ eventdata.weather.wind.speed }}m/s<br>
          Humidity: {{ eventdata.weather.main.humidity }}%</p>
        </div>
        <div v-if="eventdata.weather == null">
          <p>Weather data is currently unavailable for this event. Please check
          again closer to the event date.</p>
        </div>
      </div>
      <h2 style="margin-top:20px;">Venue Information</h2>
      <iframe height="450" style="width:100%;"
      v-bind:src="'https://www.google.com/maps/embed/v1/place?q=' + eventdata._embedded.venues[0].name
      + '&key=AIzaSyCvKEl8IR2YcNzK5P80dQAZ5CI88nvX0nk'"
      allowfullscreen></iframe>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col" style="margin-bottom:20px; margin-top:20px;">
      <h2>External Links</h2><br>
      <a v-for="item in eventdata._embedded.attractions[0].externalLinks" :key="item[0].url"
         v-bind:href="item[0].url">
        <img v-bind:src="item[0].imageLink" onerror="this.onerror=null;
                                                     this.src='/assets/default.png'"
         style="margin-right:20px;">
      </a>
    </div>
  </div>
</div>
</div>
</template>

<script>
import axios from 'axios';
import NavBar from '../components/NavBar.vue';
import FavouriteButton from '../components/favouriteButton.vue';

export default {
  name: 'Event',
  data() {
    return {
      eventdata: '',
      latitude: '',
      longitude: '',
      eventdate: '',
    };
  },
  components: {
    navbar: NavBar,
    favouriteButton: FavouriteButton,
  },
  methods: {
    getEvent() {
      const path = 'http://localhost:5000/event';
      const getParams = { id: this.$route.params.id };
      this.id = this.$route.params.id;
      axios
        .get(path, { params: { getParams } })
        .then((res) => {
          this.eventdata = res.data;
          console.log(this.eventdata);
          this.eventdate = new Date(this.eventdata.date * 1000);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getEvent();
    if ('geolocation' in navigator) {
      navigator.geolocation.getCurrentPosition((pos) => {
        this.gettingLocation = false;
        this.latitude = pos.coords.latitude;
        this.longitude = pos.coords.longitude;
      }).catch((error) => {
        console.error(error);
      });
    }
  },
};
</script>

<style>

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
