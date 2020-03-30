<template>
  <b-card
    v-bind:title="name"
    v-bind:img-src="img_src"
    img-top
    bg-variant="light"
    class="mt-3">
    <b-card-text>{{ category }}</b-card-text>
  </b-card>
</template>

<script>
export default {
  name: 'EventCard',
  props: ['name', 'category', 'img_src'],
};
</script>
