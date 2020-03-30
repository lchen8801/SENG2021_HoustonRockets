<template>
  <div>
    <div>
      <navbar></navbar>
    </div>
    <div class="my-5">
      <b-card-group deck class="mx-5">
        <eventcard
            v-for="event in events"
            v-bind:key="event.id"
            v-bind:name="event.name"
            v-bind:category="event.category"
            v-bind:img_src="event.img"
            style="min-width: 26.5rem; max-width: 26.5rem"
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
