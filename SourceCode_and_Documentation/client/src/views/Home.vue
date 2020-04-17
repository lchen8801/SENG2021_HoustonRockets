<template>
  <div class="container">
    <navbar></navbar>
    <favourite v-if="signedIn"></favourite>
    <div style="padding-bottom: 50px">
      <h1>Upcoming Events</h1>
      <b-card-group deck>
        <eventcard
            v-for="event in events"
            v-bind:key="event.id"
            v-bind:name="event.name"
            v-bind:category="event.classifications[0].segment.name"
            v-bind:img_src="event.images[0].url"
            v-bind:id="event.id"
            v-bind:favourite="event.favourite"
            style="min-width: 25%; max-width: 35%"
        ></eventcard>
      </b-card-group>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import NavBar from '../components/NavBar.vue';
import EventCard from '../components/EventCard.vue';
import Favourites from '../components/Favourites.vue';

export default {
  name: 'Home',
  data() {
    return {
      events: '',
      signedIn: '',
    };
  },
  components: {
    navbar: NavBar,
    eventcard: EventCard,
    favourite: Favourites,
  },
  methods: {
    getEvents() {
      const path = 'http://localhost:5000/events';
      axios
        .get(path)
        .then((res) => {
          this.events = res.data;
          console.log(this.events);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    checkSigned() {
      const path = 'http://localhost:5000/check_signed';
      axios
        .get(path)
        .then((res) => {
          this.signedIn = res.data;
          console.log(this.signedIn);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getEvents();
    this.checkSigned();
  },
};
</script>
