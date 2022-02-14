<template>
  <div class ="modal">
    <el-button type="text" class="overlay" @click="closeModal" style="margin-right: 5px">❌</el-button>
    <h2 style="margin-top: 4vh"><strong>수업 개설</strong></h2>
    <el-row>
      <el-col :span="20" :offset="2">
        <el-form>
          <el-form-item label="제목:">
            <el-input v-model="state.form.title"></el-input>
          </el-form-item>
          <el-form-item label="내용:">
            <el-input v-model="state.form.content" resize = none type="textarea"></el-input>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
    <!-- <div><label for="title">제목</label><input v-model="state.form.title" name="title" type="text"></div>
    <div><label for="content">내용</label><textarea v-model="state.form.content" name="content" id="" cols="30" rows="10"></textarea></div> -->
    <el-button class="addbtn" @click="addclass">등록</el-button>
  </div>
</template>

<script>
import { reactive } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
export default {
  name: 'ModalView',
  setup(props, context) {
    const router = useRouter()
    const store = useStore()
    const state = reactive({
      form:{
        title:"",
        content:"",
      }
    })
    const closeModal = function(){
      state.form=
      {
        title:"",
        content:"",
      }
      context.emit('close-modal')
    }
    const addclass = function(){
      store.dispatch('root/requestTchrCreateClass', {
          studyDesc : state.form.content,
          studyName: state.form.title,
          tchrId: store.state.root.userid})
      .then(res=>{
        closeModal();
      })
    }
    return {state, addclass, closeModal}
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
    text-align: center;
  }
  .overlay{
    position: absolute;
    width : 20px;
    height : 20px;
    right: 10px;
    top: 10px;
  }
  .addbtn {
    width: 20%;
    background-color: #6B3BE3;
    border-radius: 12px;
    text-align: center;
    color: #fff;
    margin-top: 10px;
    margin-bottom: 2vh;
  }
</style>
