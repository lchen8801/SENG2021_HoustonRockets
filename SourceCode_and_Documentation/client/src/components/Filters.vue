<template>
  <div style="float:left; width:23%; padding-left: 20px" class="my-5">
    <h3> Filters </h3>
    <b-card header="Date">
      <b-list-group flush>
        <b-list-group-item button active> Any Day </b-list-group-item>
        <b-list-group-item>
            <b-form-datepicker></b-form-datepicker>
        </b-list-group-item>
        <b-list-group-item button> Today </b-list-group-item>
        <b-list-group-item button> Tomorrow </b-list-group-item>
        <b-list-group-item button> This week </b-list-group-item>
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
  },
  created() {
    this.getData();
  },
};
</script>
