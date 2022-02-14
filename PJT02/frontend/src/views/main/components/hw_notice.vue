<template>
  <el-row>
    <el-col :span="20" :offset="2">
      <div class="common-layout">
        <!-- 공지사항 -->
        <h1 style="font-size: 25px; height: 4vh">공지사항</h1>
        <el-container style="height: 38vh">
          <el-main style="background-color: #E7EDDE; line-height: 100px" v-if="state.notice.length >= 1">
            <el-row v-for="item in state.notice" :key="item.noticeId" style="background-color: #ecf0f1; border-radius: 20px">
              <el-col :span="3" style="border-radius: 20px">{{item.noticeId}}</el-col>
              <el-col :span="18">
                <div style="border-radius: 20px">
                  <el-popover
                    placement="bottom"
                    title="Title"
                    :width="200"
                    trigger="click"
                    content="item.noticeContent"
                  >
                    <template #reference>
                      <el-button type="text">{{item.noticeTitle}}</el-button>
                    </template>
                  </el-popover>

                </div>
              </el-col>
              <el-col :span="3">
                <div class ="li-item filebar">
                  첨부파일
                  <ul>
                    <!-- <li v-for="nf in notice.File" :key = "nf.id"></li> -->
                    <li>파일1</li>
                  </ul>
                </div>
              </el-col>

            </el-row>
          </el-main>
          <el-main v-else style="background-color: #E7EDDE">
            <h1 style="background-color: #E7EDDE">등록된 공지가 없습니다</h1>
          </el-main>
        </el-container>

        <!-- 과제 -->
        <h1 style="font-size: 25px; height: 4vh">과제목록</h1>
        <el-container style="height: 38vh">
          <el-main style="background-color: #E7EDDE; line-height: 100px" v-if="state.hw.length >= 1">
            <el-row v-for="item in state.hw" :key="item.id" style="background-color: #ecf0f1; border-radius: 20px">
              <el-col :span="7"><div>{{item.hwTitle}}</div></el-col>
              <el-col :span="7"><div>{{item.studyroom.studyName}}</div></el-col>
              <el-col :span="3">
                <div class ="li-item filebar">
                  첨부파일
                  <ul>
                    <!-- <li v-for="nf in notice.File" :key = "nf.id"></li> -->
                    <li>파일1</li>
                  </ul>
                </div>
              </el-col>
              <el-col :span="7">
                <el-button type="text" @click="onOpenHwDialog(item)">
                  제출하기
                </el-button>
                <el-button type="text" @click="delStHw(item.hwid)">
                  삭제하기
                </el-button>
              </el-col>

            </el-row>
          </el-main>
          <el-main v-else style="background-color: #E7EDDE">
            <h1 style="background-color: #E7EDDE">등록된 과제가 없습니다</h1>
          </el-main>
        </el-container>

        <!-- 과제 제출 -->
        <hw-dialog
          :open="state.hwDialogOpen"
          @closeHwDialog="onCloseHwDialog"
          v-bind:props_hw = state.props_hw
          style="box-shadow: 3px 3px 3px 3px gray;"
        />
      </div>
    </el-col>
  </el-row>
</template>

<script>
import { onMounted, reactive } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import HwDialog from './hw-dialog.vue'

export default {
  name: 'Lesson',
  components:{
    HwDialog
  },
  // data(){
  //   return{
  //     hwDialogOpen:false,
  //   }
  // },
  // methods: {
  //   onOpenHwDialog () {
  //     this.hwDialogOpen = true
  //   },
  //   onCloseHwDialog () {
  //     this.hwDialogOpen = false
  //   },
  // },
  setup () {
    const router = useRouter()
    const store = useStore()
    const state = reactive({
      notice:{},
      hw:{},
      props_hw:{},
      hwDialogOpen:false,
      notice : [],
      hw : [],
    })
    // function submitHw(){
    //   router.push({
    //     name:"Tchr_Lesson"
    //   })
    // }\

    // 페이지 진입시 불리는 훅
    const delStHw = function(hwid){
      store.dispatch('root/requestdelsthw' ,{
        "hwId": hwid,
        "stId": store.state.root.userid
      })
    }
    const onOpenHwDialog=function(item){
      state.props_hw = item
      state.hwDialogOpen = true
      console.log("열림", state.props_hw)
    }
    const onCloseHwDialog=function(){
      state.hwDialogOpen = false
      state.props_hw={}
    }
    onMounted (() => {
      store.commit('root/setMenuActiveMenuName', 'history')
      // 과제 불러오기
      store.dispatch('root/requestGetHW',{
        stId : store.state.root.userid
      })
      .then(function(result){
        // alert('과제 조회 성공')
        // console.log("homework", result.data)
        state.hw=result.data
      })
      .catch(function(err){
        alert(err)
      })
      // 공지사항 불러오기
      store.dispatch('root/requestGetSTNotice',{
        stId : store.state.root.userid
      })
      .then(function(result){
        console.log("notice",result.data)
        state.notice=result.data
      })
      .catch(function(err){
        alert(err)
      })
    })
    return {state, onOpenHwDialog, onCloseHwDialog, delStHw}
  },
  created:function(){
    const localvuex=JSON.parse(localStorage.getItem('vuex'))
    // this.userId = localvuex["root"]["userid"]
    // this.getNotice()
    // this.getHw()
  }
}
</script>
<style scoped>
  .filebar>ul {
    overflow: hidden;
    height: 0;
    position: absolute;
    top:60px;
    z-index: 10;
    min-width: 100px;
    background-color: blanchedalmond;
    transition: height;
    transition-duration: 0.5s;
  }
  .filebar:hover>ul {
    height: 150px;
  }
</style>
