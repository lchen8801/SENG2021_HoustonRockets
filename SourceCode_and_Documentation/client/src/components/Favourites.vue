<template>
  <div>
    <h1>Your Favourites</h1>
    <div style = "padding-bottom: 20px">
    </div>
    <div style = "padding-bottom: 20px">
    <h2 v-if="favourites.length === 0"> It doesn't look like you have any favourites :( </h2>
    </div>
    <b-card-group deck>
    <eventcard
        v-for="event in favourites"
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
</template>

<script>
import axios from 'axios';
import EventCard from './EventCard.vue';

export default {
  name: 'Favourites',
  data() {
    return {
      favourites: [],
    };
  },
  components: {
    eventcard: EventCard,
  },
  methods: {
    list_favourites() {
      const path = 'http://localhost:5000/get_favourites';
      axios
        .get(path)
        .then((res) => {
          this.favourites = res.data;
          console.log(this.favourites);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.list_favourites();
  },
};
</script>
