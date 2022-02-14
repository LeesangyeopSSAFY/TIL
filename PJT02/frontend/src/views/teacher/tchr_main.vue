<template>
</template>
<script>
import { onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

export default {
  name: 'tchr_main',

  setup() {
    const router = useRouter()
    onMounted(()=>{
      router.push({
        name: 'Tchr_contents',
      })
    })

    return {onMounted}
  },
}
</script>
