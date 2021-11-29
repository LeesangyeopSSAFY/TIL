<template>
  <div>
    <input 
      type="text"
      v-model.trim="movieTitle"
      @keyup.enter="createWishList"
    >
    <b-button variant="primary" @click="createWishList" size="sm" class="m-1">✔</b-button>
    
  </div>
</template>

<script>
export default {
  name: 'MyListForm',
  data: function () {
    return {
      movieTitle: null,
    }
  },
  methods: {
    createWishList: function () {
      const wishMovie = {
        title: this.movieTitle,
        isWatched: false,
        date: new Date().getTime(),
      }
      if (wishMovie.title) {
        this.$store.dispatch('createWishList', wishMovie)
      }
      this.movieTitle = null
    }
  }
}
</script>

<style>

</style>