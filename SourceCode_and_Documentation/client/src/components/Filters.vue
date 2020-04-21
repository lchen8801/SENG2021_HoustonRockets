<template>
  <div>
    <h2> Filters </h2>
    <b-card header="Date">
      <b-list-group flush>
        <b-list-group-item button @click="changeDate('Any date')"
        :active="dateButton === 'Any date'">
          Any Date
        </b-list-group-item>
        <b-list-group-item button @click="changeDate('Today')"
        :active="dateButton === 'Today'">
          Today
        </b-list-group-item>
        <b-list-group-item button @click="changeDate('Tomorrow')"
        :active="dateButton === 'Tomorrow'">
          Tomorrow
        </b-list-group-item>
        <b-list-group-item button @click="changeDate('This week')"
        :active="dateButton === 'This week'">
          This week
        </b-list-group-item>
        <b-list-group-item button @click="changeDate('Select Date')"
        :active="dateButton === 'Select Date'">
            <b-form-datepicker dropup no-flip v-model="datePicker">
            </b-form-datepicker>
        </b-list-group-item>
      </b-list-group>
    </b-card>
    <b-card header="Location">
      <b-list-group flush>
        <b-list-group-item button @click="changeLocation('Any location')"
        :active="locationButton === 'Any location'">
          Any location
        </b-list-group-item>
        <b-list-group-item button @click="changeLocation('Enter location')"
        :active="locationButton === 'Enter location'">
          <b-form-input placeholder="Enter location" v-model="location"
          @change="changeLocation('Enter location')">
          </b-form-input>
        </b-list-group-item>
      </b-list-group>
    </b-card>
    <b-card header="Category">
      <b-list-group flush>
        <b-list-group-item button @click="changeCategory('Any category')"
        :active="categoryButton === 'Any category'">
          Any category
        </b-list-group-item>
        <b-list-group-item button v-for="category in categories" v-bind:key="category.id"
        @click="changeCategory(category)" :active="categoryButton === category">
            {{ category }}
        </b-list-group-item>
      </b-list-group>
    </b-card>
        <b-card header="Genre">
      <b-list-group flush>
        <b-list-group-item button @click="changeGenre('Any genre')"
        :active="genreButton === 'Any genre'">
          Any genre
        </b-list-group-item>
        <b-list-group-item button v-for="genre in genres" v-bind:key="genre.id"
        @click="changeGenre(genre)" :active="genreButton === genre">
            {{ genre }}
        </b-list-group-item>
      </b-list-group>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Filters',
  props: ['searchTerm'],
  data() {
    return {
      categories: '',
      categoryButton: 'Any category',
      genres: '',
      genreButton: 'Any genre',
      dateButton: 'Any date',
      datePicker: '',
      locationButton: 'Any location',
      location: '',
    };
  },
  methods: {
    getData() {
      const path = 'http://localhost:5000/categories';
      const getParams = { searchTerm: this.$props.searchTerm };
      axios
        .get(path, { params: { getParams } })
        .then((res) => {
          this.categories = res.data.categories;
          this.genres = res.data.genres;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    changeCategory(category) {
      this.categoryButton = category;
      this.$emit('categoryFilter', category);
    },
    changeGenre(genre) {
      this.genreButton = genre;
      this.$emit('genreFilter', genre);
    },
    changeDate(date) {
      this.dateButton = date;
      if (date === 'Select Date') {
        this.$emit('dateFilter', this.datePicker);
        console.log(this.datePicker);
      } else {
        this.$emit('dateFilter', date);
      }
    },
    changeLocation(location) {
      let emitLocation = location;
      this.locationButton = location;
      if (location === 'Enter location') {
        emitLocation = this.location;
      }
      this.$emit('locationFilter', emitLocation);
    },
  },
  created() {
    this.getData();
  },
};
</script>
