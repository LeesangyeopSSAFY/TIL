<template>
  <div class ="modal">
    <el-button type="text" class="overlay" @click="closeModal" style="margin-right: 5px">❌</el-button>
    <h2 style="margin-top: 4vh"><strong>공지 등록</strong></h2>
    <form action="#" id="noticeForm" method="post" enctype="multipart/form-data">
      <div style="margin-bottom: 1vh; height: 25px">
        <label for="noticeTitle" style="display: inline-block; width: 10%; text-align: start">제목:</label>
        <input v-model="state.form.noticeTitle"  name="noticeTitle" type="text" style="width: 60%">
      </div>
      <div style="margin-bottom: 1vh;">
        <label for="noticeContent" style="display: inline-block; width: 10%; text-align: start">내용: </label>
        <textarea v-model="state.form.noticeContent" name="noticeContent" id="" cols="41" rows="8" style="vertical-align: middle; resize: none;"></textarea>
      </div>
      <div style="margin-bottom: 1vh">
        <label for="noticeFile" style="display: inline-block; width: 10%; text-align: start">파일: </label>
        <input type="file" multiple="multiple" @change="addFile" ref="refNoticeFile" name="noticeFile" id="ntFile" style="width: 62%">
      </div>
      <div v-if="isupdate" @click="updatenotice" class="purplebtn">수정</div>
      <div v-else @click="addnotice" class="purplebtn">등록</div>
    </form>
  </div>
</template>

<script>
import { reactive, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
export default {
  name: 'ModalView',
  props: ["pdata", "isupdate"],
  setup(props, context) {
    const router = useRouter()
    const store = useStore()
    const state = reactive({
      form : {
        isupdate: props.isupdate,
        noticeTitle : props.pdata.noticeTitle,
        noticeContent : props.pdata.noticeContent,
        ntid : props.pdata.noticeId,
        noticeFile : null,
        studyId: store.state.root.curClassId,
        tchrId: store.state.root.userid
      }
    })
    const closeModal = function(){
      state.form.noticeTitle = null
      state.form.noticeContent = null
      state.form.isupdate = false
      state.form.ntid = null
      state.form.noticeFile = null
      context.emit('close-modal')
    }
    const showRequest = (request)=> {
      const reqObject = JSON.parse(JSON.stringify(request));
      console.log('request', reqObject);
      dataChange(reqObject);
    };
    const addnotice = function(){
      var noticeFormData = new FormData(document.querySelector('#noticeForm'))
      noticeFormData.append('studyId', state.form.studyId)
      noticeFormData.append('tchrId', state.form.tchrId)
      // noticeFormData.append('noticeTitle', state.form.noticeTitle)
      // noticeFormData.append('noticeContent', state.form.noticeContent)
      // noticeFormData.append('noticeFile', state.form.noticeFile)

      store.dispatch('root/requestAddNotice', noticeFormData)
      .then(res => {
        console.log(res)
        closeModal()
      })
    }
    const addFile = function(event) {
      var files = event.target.files
      var filesArr = Array.prototype.slice.call(files)
      state.form.noticeFile = filesArr
    }
    const updatenotice = function(){
      var noticeFormData = new FormData(document.querySelector('#noticeForm'))
      noticeFormData.append('noticeId', props.pdata.noticeId)
      // noticeFormData.append('noticeTitle', state.form.noticeTitle)
      // noticeFormData.append('noticeContent', state.form.noticeContent)
      // noticeFormData.append('noticeFile', state.form.noticeFile)
      store.dispatch('root/requestUpdateNotice', noticeFormData)
      .then(res => {
        closeModal()
      })
    }
    const dataChange = function(pdata){
      console.log("abab",pdata)
      state.form.noticeTitle = pdata.noticeTitle
      state.form.noticeContent = pdata.noticeContent
      state.form.ntid = pdata.noticeId
    }
    onMounted(()=>{
      console.log("안녕하세요", props.pdata, props.isupdate)

      showRequest(props.pdata);
    })
    return {state, onMounted, addnotice, closeModal, dataChange, updatenotice, updatenotice, addFile}
  },

};
</script>

<style scoped>
  .modal{
    width: 500px;
    height: auto;
    position: fixed;
    top: 50%;
    left: 50%;
    -webkit-transform: translate(-50%, -50%);
    -moz-transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    -o-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    /* border : solid 1px black; */
    border-radius: 20px;
    background-color: white;
  }
  .overlay{
    position: absolute;
    width : 20px;
    height : 20px;
    right: 10px;
    top: 10px;
  }
  .btn-div .el-button {
    width: 20%;
    background-color: #6B3BE3;
    border-radius: 12px;
    text-align: center;
    color: #fff;
    margin-top: 10px;
    margin-bottom: 2vh;
  }
  input {
    border-color: #f0f0f1;
    border-radius: 5px;
  }
  textarea {
    border-color: #dcdcde;
    border-radius: 5px;
  }
  .purplebtn {
    width: 20%;
    height: 30px;
    background-color: #6B3BE3;
    border: none;
    border-radius: 12px;
    text-align: center;
    color: #fff;
    margin: auto;
    margin-top: 10px;
    margin-bottom: 2vh;
    cursor: pointer;
  }
  .purplebtn:hover {background-color: #fff; color: #6B3BE3;}
</style>
