<template>
  <div>
    <img src="https://kr.seaicons.com/wp-content/uploads/2015/11/Photo-Video-Film-2-icon.png" alt="movie icon" style="width: 50px;">
    <h1 style="font-weight: bold;">MyMovieList</h1>
    <my-list-form></my-list-form>
    <my-list></my-list>
  </div>
</template>

<script>
import MyListForm from '@/components/MyListForm'
import MyList from '@/components/MyList'

export default {
  name: 'MyMovieList',
  components: {
    MyListForm,
    MyList
  }
}
</script>

<style>

</style>