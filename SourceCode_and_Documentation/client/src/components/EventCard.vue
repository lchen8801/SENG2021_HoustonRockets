<template>
  <b-card
    v-bind:title="name"
    v-bind:img-src="img_src"
    img-top
    bg-variant="light"
    class="mt-3">
    <a v-bind:href="'/event/' + id"
style="position:absolute;top:0;left:0;height:100%;width:100%;">
    </a><b-card-text>{{ category }}</b-card-text>
  </b-card>
</template>

<script>
export default {
  name: 'EventCard',
  props: ['name', 'category', 'img_src', 'id'],
};
</script>
