<template>
<div id="eachMovie">
  <b-card
    :title="movieCard.title"
    :img-src="poster"
    img-alt="Image"
    img-top
    tag="article"
    style="width: 20rem;"
    class="m-2 text-center h-100"
    align="center"
    border-variant="dark"
  >
    <b-card-text>
      {{ movieCard.overview }}
    </b-card-text>
  </b-card>
</div>
</template>

<script>
const baseurl = 'https://image.tmdb.org/t/p/original/'
export default {
  name: 'MovieCard',
  props: {
    movieCard: Object
  },
  computed:{
    poster:function(){ 
      return baseurl + this.movieCard.poster_path
    }
  }
}
</script>

<style>

</style>