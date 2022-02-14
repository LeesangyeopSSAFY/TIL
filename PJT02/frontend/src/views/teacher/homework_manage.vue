<template>
  <div>
    <tchr-nav @startvideo="start"></tchr-nav>
    <h1>과제 관리 페이지</h1>
    <el-tabs v-model="activeName" class="demo-tabs">
      <el-tab-pane label="User" name="first">User</el-tab-pane>
      <el-tab-pane v-for="Hw in Hws" :key="Hw" :label="Hw.hwTitle">
        <!-- {{Hw.studentHomeworks[0].stHwFile[0]}} -->
        <el-scrollbar height="400px">
          <el-row>
            <el-col :span="1"><div class="grid-content bg-head">번호</div></el-col>
            <el-col :span="3"><div class="grid-content bg-head">ID</div></el-col>
            <el-col :span="6"><div class="grid-content bg-head">내용</div></el-col>
            <el-col :span="14"><div class="grid-content bg-head">파일명</div></el-col>
          </el-row>
          <el-row v-for="(item,index) in Hw.studentHomeworks" :key="index" >
            <el-col :span="1"><div class="grid-content bg-content">{{index+1}}</div></el-col>
            <el-col :span="3"><div class="grid-content bg-content">{{item.stId}}</div></el-col>
            <el-col :span="6"><div class="grid-content bg-content">{{item.stHwcontent}}</div></el-col>
            <el-col :span="12">
              <div class="grid-content bg-content" v-if="item.stHwFile[0]">
                {{item.stHwFile[0].fileOriginName}}
              </div>
              <div class="grid-content bg-content" v-else>
                파일이 없습니다
              </div>
            </el-col>
            <el-col :span="1"><el-input class="grid-content bg-content"/></el-col>
            <el-col :span="1"><el-button @click="ent">D</el-button></el-col>
          </el-row>
        </el-scrollbar>
      </el-tab-pane>
    </el-tabs>

    <start-video-dialog
        :open="videoDialogOpen"
        @closeVideoDialog="end"
    ></start-video-dialog>
  </div>
</template>

<script>
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { ref, unref, reactive, computed, onMounted } from 'vue'

import Tchr_nav from './tchr_nav.vue'
import StartVideoDialog from './startvideo-dialog.vue'
export default {
  name: 'Tchr_HWManage',
  components: {
    "tchr-nav": Tchr_nav,
    StartVideoDialog,
  },
  data(props){
    return {
      videoDialogOpen: false,
    }
  },
  setup() {
    const store = useStore()
    const Hws = []
    const activeName = ref('')
    const getHw = function () {
      store.dispatch('root/requestTchrListHomework',this.userId)
      .then(result =>{
        this.Hws=result.data
        console.log(this.Hws)
      })
      .catch(function(err){
        alert(err)
      })
    }
    const ent = function(a){
      console.log(a)
    }
    return {Hws, activeName, getHw, ent}
  },
  methods:{
    start (){this.videoDialogOpen= true},
    end (){this.videoDialogOpen= false},
  },
  created: function(){
    const localvuex=JSON.parse(localStorage.getItem('vuex'))
    this.userId=localvuex["root"]["userid"]
    this.getHw()
  },

}
</script>

<style scoped>
.el-row {
  margin: 4px;
  /* border: solid;
  border-bottom-width: thick 2px;
  border-color: #3D6657; */

}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  padding: 2px;

  border-radius: 4px;
}
.bg-head {
  background: #3D6657;
  color: white;
}
.bg-content {
  background: #BFEDD9;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.scrollbar-demo-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  margin: 10px;
  text-align: center;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
}
</style>
