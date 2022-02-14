<template>
  <!-- login.vue -->
  <div @click="clickLogin">
    <!-- <img id="loginwall" :src="require(`@/assets/images/윈터.jpg`)"/> -->
    <img id="loginwall" :src="require(`@/assets/images/plain-blue-background.jpg`)"/>
  </div>
</template>
<style>
#loginwall{
  width: 100vw;
  height: 100vh;
}

.infinite-list {
  padding-left: 0;
  max-height: calc(100% - 35px);
}

@media (min-width: 701px) and (max-width: 1269px) {
  .infinite-list {
    min-width: 700px;
  }
}

@media (min-width: 1270px) {
  .infinite-list {
    min-width: 1021px;
  }
}

.infinite-list .infinite-list-item {
  min-width: 335px;
  max-width: 25%;
  display: inline-block;
  cursor: pointer;
}
</style>
<script>
import { reactive } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

export default {
  name: 'Login',

  setup(props, { emit }) {
    const store = useStore()
    const router = useRouter()

    const clickLogin = () => {
      emit('openLoginDialog')
    }

    const changeCollapse = () => {
      state.isCollapse = !state.isCollapse
    }

    return {clickLogin, changeCollapse}
  }
}
</script>
