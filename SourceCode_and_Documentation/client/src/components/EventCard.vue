<template>
  <b-card
    v-bind:title="name"
    v-bind:img-src="img_src"
    img-top
    bg-variant="light"
    class="mt-3"
    >
    <a v-bind:href="'/event/' + id"
style="position:absolute;top:0;left:0;height:70%;width:100%;">
    </a>
    <b-card-text>
      {{ category }} - {{ genre }}
      <p>{{ date }}</p>
    </b-card-text>
    <favourite-button v-bind:id="id" v-bind:favourite="favourite">
    </favourite-button>
  </b-card>
</template>

<script>
import FavouriteButton from './favouriteButton.vue';

export default {
  name: 'EventCard',
  props: ['name', 'category', 'genre', 'date', 'img_src', 'id', 'favourite'],
  components: {
    favouriteButton: FavouriteButton,
  },
};
</script>
