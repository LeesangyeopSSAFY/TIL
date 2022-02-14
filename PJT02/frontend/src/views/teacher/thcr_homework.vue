<template>
  <div>
    <ModalView v-bind:isupdate= state.isupdate v-bind:pdata = state.props_data style="box-shadow: 3px 3px 3px 3px gray;" v-if ="state.isVisible" @close-modal="closemodal"></ModalView>
    <div style="text-align: right">
      <el-button style="background-color: #6B3BE3; color: #fff; width: 100px; height: 40px; border-radius: 15px" class="sub_btn" @click="state.isVisible = true">숙제 생성</el-button>
    </div>
    <div v-if="state.homeworks.length >= 1">
      <div v-for="(hw, index) in state.homeworks" :key = hw.hwId class ="el-item">
        <div class="li-left li-sec">
          <div class ="li-title li-item">{{hw.hwTitle}}</div>
          <div class ="li-lesson li-item">{{hw.hwContent}}</div>
          <!-- <div class ="li-lesson li-item">{{hw.hwFile}}</div> -->
        </div>
        <div class="li-right li-sec">
          <div class ="li-time li-item">{{hw.hwPosted.substring(0, 10)}}</div>
          <div class ="li-item filebar">
            첨부파일
            <ul>
              <h4>파일목록</h4>
              <div v-for="hf in hw.hwFile" :key=hf.fileId>
                <hr>
                <a class="filenamehover" @click="downHWFile(hf.fileName, hf.filePath, hf.fileOriginName)">💾 {{hf.fileOriginName}}</a>
              </div>
              <!-- <li v-for="nf in notice.File" :key = "nf.id"></li>
              <li>파일1</li> -->
            </ul>
          </div>
          <el-button type="text" class ="li-item" @click = "updatehomework(index)">수정</el-button>
          <el-button type="text" class ="li-item" @click = "delhomeworks(hw.hwId)" style="color: red">삭제</el-button>
        </div>
      </div>
    </div>
    <div v-else style="height: 80%; padding: 100px">
      <h1>등록된 과제가 없습니다</h1>
    </div>
  </div>
</template>

<script>
import ModalView from "./homework_modal"
import { reactive, computed, ref, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
export default {
  name: 'Tchr_homework',
  components:{
    ModalView,
  },
  setup() {
    const router = useRouter()
    const store = useStore()
    const state = reactive({
      isupdate : false,
      isVisible :false,
      homeworks:computed(() => store.getters['root/getTchrHomeworkList']),
      props_data:{}
    })
    const gethomeworksList = function(){
      store.dispatch('root/requestListHomework', {
            studyId: store.state.root.curClassId})
        .then(res =>{
          store.state.root.TchrHomeworkList = res.data
          state.homeworks = store.getters['root/getTchrHomeworkList']
        })
    }
    const delhomeworks = function(homwid){
      store.dispatch('root/requestDelHomework', {
            hwId: homwid,
            tchrId: store.state.root.userid})
        .then(res =>{
          gethomeworksList();
        })
    }
    const updatehomework = function(idx){
      state.props_data = state.homeworks[idx]
      state.isupdate = true
      console.log(state.homeworks[idx])
      state.isVisible = true
    }
    const closemodal = function(){
      gethomeworksList();
      state.isVisible = false
      state.isupdate = false
      state.props_data={}
    }
    const downHWFile = function(fileName, filePath, fileOriginName) {
      const fileurl = `http://localhost:8080/api/v1/homework/download-file?fileName=${fileName}&filePath=${filePath}`
      const anchor = document.createElement('a')
      anchor.href = fileurl
      anchor.download = fileOriginName
      document.body.appendChild(anchor)
      anchor.click()
      document.body.removeChild(anchor)
    }
    onMounted(()=>{
      gethomeworksList();
    })

    return {state, onMounted, closemodal, updatehomework, delhomeworks, gethomeworksList, downHWFile}
  },
};
</script>
<style scoped>
  *, html, body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  .el-item{
    display: flex;
    justify-content: space-between;
    /* border: solid 1px black; */
    background-color: #ecf0f1;
    align-items: center;
    border-radius: 20px;
    height: 80px;
    margin-bottom: 10px;
  }
  .li-sec{
    display: flex;
  }
  .li-item{
    margin: 20px;
  }
  .sub_btn{
    padding: 5px;
    margin: 20px;
  }
  .filebar>ul {
    overflow: hidden;
    height: 0;
    position: absolute;
    z-index: 10;
    min-width: 100px;
    background-color: #6B3BE3;
    transition: height;
    transition-duration: 0.5s;
    color: #fff;
    border-radius: 10px;
    margin-top: 5px;
  }
  .filebar:hover>ul {
    height: auto;
  }
  .filenamehover {
    cursor: pointer;
    padding: 10px;
  }
</style>
