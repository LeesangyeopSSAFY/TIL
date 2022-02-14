<template>
  <div>
    <tchr-nav @startvideo="start"></tchr-nav>
    <el-row :gutter="20">
      <el-col :span="20" style="margin-left: 15vh">
          <h1 style="text-align:center; margin-top: 1vh; font-size: 30px">{{ state.classId }}반의 수업 {{ state.classtitle }}</h1>
          <homework></homework>
          <notice></notice>
          <el-button class="sub_btn" @click ="delClass">수업 삭제</el-button>
      </el-col>
    </el-row>
    <start-video-dialog
      :open="state.videoDialogOpen"
      @closeVideoDialog="end"
    ></start-video-dialog>
  </div>
</template>
<script>
import { reactive, computed } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

import Tchr_notice from './tchr_notice.vue'
import Tchr_homework from './thcr_homework.vue'
import Tchr_nav from './tchr_nav.vue'
import StartVideoDialog from './startvideo-dialog.vue'

export default {
  name: 'Tchr_contents',
  components: {
    "homework" : Tchr_homework,
    "notice" : Tchr_notice,
    "tchr-nav" : Tchr_nav,
    StartVideoDialog
  },
  data(){
    return {
      videoDialogOpen:false,
    }
  },
  setup() {
    const router = useRouter()
    const store = useStore()
    const state = reactive({
      classtitle: computed(() => store.getters['root/getStudyName']),
      classId : computed(() => store.getters['root/getStudyId']),
      id: store.state.root.userid
    })
    const delClass = function(){
      console.log(state.id ,state.classtitle)
      store.dispatch('root/requestDeleteClass', {
          studyName: state.classtitle,
          tchrId: state.id
          })
      .then(function (result) {
        store.dispatch('root/requestGetTchrClass', {
            tchrId: store.state.root.userid})
        .then(res =>{
          store.state.root.classList = res.data
        })
        router.push({
          name: 'Main_calendar',
        })
      })
      .catch(function (err) {
        alert(err)
      })
    }
    return {state, delClass}
  },
  methods:{
    start (){
      this.videoDialogOpen= true
      console.log("열림")
    },
    end (){
      this.videoDialogOpen= false
    }
  }

}
</script>
<style scoped>
*, html, body {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
.topnav{
  background-color: #545c64;
  position: relative;
  color: #fff;
  display: flex;
  list-style:none;
  width: 100%;
}
.navitem{
  padding: 20px;
  border-bottom: solid 2px white;
  margin-right: 10px;
}
.navitem:hover{
  color: yellow;
  border-bottom: solid 2px yellow;
}
.lessonstr {
  right: 0;
  margin: 20px;
  position: absolute;
}
.sub_btn{
  padding: 5px;
  margin: 20px;
  background-color: #6B3BE3;
  border-radius: 15px;
  width: 30%;
  height: 50px;
  text-align: center;
  color: #fff;
}
</style>
