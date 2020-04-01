<template>
  <div>
    <h2> Filters </h2>
    <b-card header="Date">
      <b-list-group flush>
        <b-list-group-item ref='any day' button active @click="changeActive('any day')">
          Any Day
        </b-list-group-item>
        <b-list-group-item ref='datepicker' button @click="changeActive('datepicker')">
            <b-form-datepicker></b-form-datepicker>
        </b-list-group-item>
        <b-list-group-item ref='today' button @click="changeActive('today')">
          Today
        </b-list-group-item>
        <b-list-group-item ref='tomorrow' button @click="changeActive('tomorrow')">
          Tomorrow
        </b-list-group-item>
        <b-list-group-item ref='this week' button @click="changeActive('this week')">
          This week
        </b-list-group-item>
      </b-list-group>
    </b-card>
    <b-card header="Location">
       <b-form-input placeholder="Enter Location"></b-form-input>
    </b-card>
    <b-card header="Category/Genre">
      <b-list-group flush>
        <b-list-group-item button active> Any category </b-list-group-item>
        <b-list-group-item button v-for="category in categories" v-bind:key="category.id">
            {{ category }}
        </b-list-group-item>
      </b-list-group>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Filters',
  data() {
    return {
      categories: '',
    };
  },
  methods: {
    getData() {
      const path = 'http://localhost:5000/categories';
      axios
        .get(path)
        .then((res) => {
          this.categories = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    changeActive(buttonRef) {
      // this.$refs.buttonRef.active = true
      console.log(buttonRef);
    },
  },
  created() {
    this.getData();
  },
};
</script>
