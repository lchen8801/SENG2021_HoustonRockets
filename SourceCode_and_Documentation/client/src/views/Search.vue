<template>
  <div>
    <navbar @changedSearch="getEvents($event)"></navbar>
    <filters float:left></filters>
    <div class="my-5" float:right style="width: 50%">
      <h1 style="padding-top: 30px">{{ searchTerm }}</h1>
      <b-card-group deck class="mx-5">
        <eventcard
            v-for="event in events"
            v-bind:key="event.id"
            v-bind:name="event.name"
            v-bind:category="event.category"
            v-bind:img_src="event.img"
            v-bind:id="event.id"
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
import Filters from '../components/Filters.vue';

export default {
  name: 'Search',
  data() {
    return {
      events: '',
      searchTerm: '',
    };
  },
  components: {
    navbar: NavBar,
    eventcard: EventCard,
    filters: Filters,
  },
  methods: {
    getEvents(searchVal) {
      const path = 'http://localhost:5000/search';
      let getParams = { searchTerm: this.$route.params.searchTerm };
      this.searchTerm = this.$route.params.searchTerm;
      if (searchVal != null) {
        getParams = { searchTerm: searchVal };
        this.searchTerm = searchVal;
      }
      console.log(getParams);
      axios
        .get(path, { params: { getParams } })
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
