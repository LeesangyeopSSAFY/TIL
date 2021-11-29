<template>
  <div id="listItem">
    <span
      @click="updateListStatus(toWatch)"
      :class="{'is-watched': toWatch.isWatched }"
    >{{ toWatch.title }}</span>
    <b-button @click="deleteList" size="sm" variant="danger">❌</b-button>

  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'MyListItem',
  props: {
    toWatch: {
      type: Object
    }
  },
  methods: {
    ...mapActions([
      'updateListStatus'
    ]),
    deleteList: function () {
      this.$store.dispatch('deleteList', this.toWatch)
    }
  }
}
</script>

<style>
.is-watched {
  text-decoration: line-through;
}
#listItem {
  margin: 5px;
}
</style>