<template>
  <div>
    <h1 class="d-flex justify-content-center" style="font-weight: bold;">Home</h1>
    <div class="d-flex flex-wrap justify-content-center m-5">
        <movie-card
          v-for="movieCard in movieCards"
          :key="movieCard.id"
          :movieCard="movieCard"
        ></movie-card>
        
      
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import MovieCard from '@/components/MovieCard'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },
  computed: {
    ...mapState(['movieCards'])
  }
}
</script>
