<template>
  <b-button pill variant="outline-warning" v-on:click.stop="favouriting" :pressed="isFavourite">
    <img src="../assets/star.png" width="20px" height="20px" />
  </b-button>
</template>

<script>
import axios from 'axios';

export default {
  name: 'favouriteButton',
  props: ['id', 'favourite'],
  data() {
    return {
      isFavourite: this.$props.favourite,
    };
  },
  methods: {
    favouriting() {
      let path = 'http://localhost:5000/check_signed';
      axios
        .get(path)
        .then((res) => {
          console.log(res.data);
          if (res.data) {
            if (this.$props.favourite) {
              this.isFavourite = false;
            } else {
              this.isFavourite = true;
            }
            path = 'http://localhost:5000/favourite';
            const eid = this.$props.id;
            const isFavourite = this.$props.favourite;
            axios
              .post(path, {
                eid,
                isFavourite,
              })
              .then((response) => {
                console.log(response);
              })
              .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
              });
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>
