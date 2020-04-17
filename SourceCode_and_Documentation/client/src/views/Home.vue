<template>
  <div class="container">
    <navbar></navbar>
    <div style="padding-bottom: 50px">
      <b-card-group deck>
        <eventcard
            v-for="event in events"
            v-bind:key="event.id"
            v-bind:name="event.name"
            v-bind:category="event.classifications[0].segment.name"
            v-bind:genre="event.classifications[0].genre.name"
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

export default {
  name: 'Home',
  data() {
    return {
      events: '',
    };
  },
  components: {
    navbar: NavBar,
    eventcard: EventCard,
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
  },
  created() {
    this.getEvents();
  },
};
</script>
