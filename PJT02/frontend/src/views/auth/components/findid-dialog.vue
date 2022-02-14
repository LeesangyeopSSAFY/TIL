<template>
  <div>
    <el-dialog custom-class="findid-dialog" title="ID 찾기" v-model="state.dialogVisible" @close="handleClose" top="30vh">
      <el-form :model="state.form" :rules="state.rules" ref="loginForm" :label-position="state.form.align">
        <el-form-item prop="id" label="이메일" :label-width="state.formLabelWidth" >
          <el-input v-model="state.form.email" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item prop="password" label="이름" :label-width="state.formLabelWidth">
          <el-input v-model="state.form.name" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <el-row class="row-btn" style="margin-top: 40px">
          <el-button @click="clickFindid" style="width: 45%; border-radius: 15px">ID 찾기(학생)</el-button>
          <el-button @click="clickFindTchrid" style="width: 45%; border-radius: 15px">ID 찾기(교사)</el-button>
      </el-row>
    </el-dialog>
  </div>
</template>
<style>
.findid-dialog {
  width: 400px !important;
  height: auto;
  border-radius: 30px;
}
</style>
<script>
import { reactive, computed, ref, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

export default {
  name: 'findid-dialog',

  props: {
    open: {
      type: Boolean,
      default: false
    }
  },

  setup(props, { emit }) {
    const router = useRouter()
    const store = useStore()
    // 마운드 이후 바인딩 될 예정 - 컨텍스트에 노출시켜야함. <return>
    const loginForm = ref(null)

    /*
      // Element UI Validator
      // rules의 객체 키 값과 form의 객체 키 값이 같아야 매칭되어 적용됨
      //
    */
    const state = reactive({
      form: {
        email: '',
        name: '',
        align: 'left'
      },
      dialogVisible: computed(() => props.open),
      formLabelWidth: '120px'
    })

    onMounted(() => {
      // console.log(loginForm.value)
    })

    const handleClose = function () {
      state.form.email = ''
      state.form.name = ''
      emit('closeFindidDialog')
    }
    const clickLogin = () => {
      handleClose()
      emit('openLoginDialog')
    }
    const clickFindid = function () {
      store.dispatch('root/requestFindid', {stEmail: state.form.email, stName: state.form.name })
      .then(function (result) {
        alert('id 찾기(학생) 결과 : 성공')
        handleClose()
      })
      .catch(function (err) {
        alert(err)
      })
    }
    const clickFindTchrid = function () {
      store.dispatch('root/requestFindTchrid', {tchrEmail: state.form.email, tchrName: state.form.name })
      .then(function (result) {
        alert('id 찾기(교사) 결과 : 성공')
        handleClose()
      })
      .catch(function (err) {
        alert(err)
      })
    }


    return { loginForm, state, handleClose, clickFindid, clickFindTchrid, clickLogin }
  },

}
</script>
