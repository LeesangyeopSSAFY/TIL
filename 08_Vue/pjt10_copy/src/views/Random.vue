<template>
  <div>
    <h3 style="font-weight: bold;">🔸랜덤영화 추천🔸</h3>
    <div v-if="randomMovie" class="d-flex justify-content-center align-items-center">   
      <b-card
      :title="randomMovie.title"
      :img-src="poster"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem;"
      class="mb-2"
      border-variant="dark"
      >
      <!-- <b-card-text>
        {{ randomMovie.overview }}
      </b-card-text> -->
        </b-card>
    </div>
    <div>
      <b-button @click="randomPick" variant="outline-primary">Pick</b-button>

    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapState } from 'vuex'

const baseurl = 'https://image.tmdb.org/t/p/original/'
export default {
  name: 'Random',
  data: function () {
    return {
      randomMovie: null
    }
  },
  methods: {
    randomPick: function () {
      let idx   = _.random(this.$store.state.movieCards.length-1)
      this.randomMovie = this.$store.state.movieCards[idx]
      console.log(this.randomMovie)
    }
  },
  created () {
    this.$store.dispatch('LoadMovieCards')
    this.randomPick()
  },
  computed: {
    ...mapState ([
      'movieCards'
    ]),
    poster:function(){ 
      return baseurl + this.randomMovie.poster_path
    }
  },
}
</script>

<style>

</style>