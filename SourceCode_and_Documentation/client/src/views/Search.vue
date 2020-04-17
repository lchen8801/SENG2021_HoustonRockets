<template>
  <div class="container-fluid">
    <navbar @changedSearch="getEvents($event, '', '', '', '')"></navbar>
    <div class="row">
      <div class="col-3">
        <filters @categoryFilter="getEvents(searchTerm, '', '', $event, '')"
        @genreFilter="getEvents(searchTerm, '', '', '',$event)"
        @dateFilter="getEvents(searchTerm, $event, '', '', '')"
        v-bind:searchTerm="updated_searchTerm" v-bind:key="searchTerm"></filters>
      </div>
      <div class="col-9" style="padding-bottom: 50px">
        <h6 style="color: grey"> Showing events for </h6>
        <h1>{{ searchTerm }}</h1>
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
            style="min-width: 30%; max-width: 30%"
          ></eventcard>
        </b-card-group>
      </div>
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
      date: '',
      location: '',
      category: '',
      genre: '',
    };
  },
  computed: {
    updated_searchTerm() {
      return this.searchTerm;
    },
  },
  components: {
    navbar: NavBar,
    eventcard: EventCard,
    filters: Filters,
  },
  methods: {
    getEvents(searchVal, dateFilter, locationFilter, categoryFilter, genreFilter) {
      const path = 'http://localhost:5000/search';
      const getParams = {
        searchTerm: this.$route.params.searchTerm,
        date: this.date,
        location: this.location,
        category: this.category,
        genre: this.genre,
      };
      this.searchTerm = this.$route.params.searchTerm;
      if (searchVal != null) {
        getParams.searchTerm = searchVal;
        this.searchTerm = searchVal;
        this.date = dateFilter === '' ? this.date : dateFilter;
        this.location = locationFilter === '' ? this.location : locationFilter;
        this.category = categoryFilter === '' ? this.category : categoryFilter;
        this.genre = genreFilter === '' ? this.genre : genreFilter;
        getParams.date = this.date;
        getParams.location = this.location;
        getParams.category = this.category;
        getParams.genre = this.genre;
      }
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
    this.getEvents(undefined, undefined);
  },
};
</script>
