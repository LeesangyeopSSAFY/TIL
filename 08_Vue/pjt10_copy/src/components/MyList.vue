<template>
  <div>
    <my-list-item
      v-for="toWatch in toWatchs"
      :key="toWatch.date"
      :toWatch="toWatch"
    ></my-list-item>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import MyListItem from '@/components/MyListItem'

export default {
  name: 'MyList',
  components: {
    MyListItem
  },
  computed: {
    ...mapState([
      'toWatchs'
    ])
  }
}
</script>

<style>

</style>