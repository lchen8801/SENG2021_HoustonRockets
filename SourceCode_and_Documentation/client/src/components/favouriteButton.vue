<template>
  <b-button pill variant="outline-warning" v-on:click.stop="favouriting" :pressed="favourite">
    <img src="../assets/star.png" width="20px" height="20px" />
  </b-button>
</template>

<script>
import axios from 'axios';

export default {
  name: 'favouriteButton',
  props: ['id', 'favourite'],
  methods: {
    favouriting() {
      if (this.$props.favourite) {
        this.$props.favourite = false;
      } else {
        this.$props.favourite = true;
      }
      const path = 'http://localhost:5000/favourite';
      const eid = this.$props.id;
      console.log(this.$props.id);
      const isFavourite = this.$props.favourite;
      axios
        .post(path, {
          eid,
          isFavourite,
        })
        .then((res) => {
          this.categories = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>
