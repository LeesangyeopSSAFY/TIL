<template>
  <div>
    <el-dialog custom-class="password-dialog" title="비밀번호 재설정" v-model="state.dialogVisible" @close="handleClose" top="30vh">
      <el-form :model="state.form" :rules="state.rules" ref="changePasswordForm" :label-position="state.form.align">
        <el-form-item prop="id" label="ID" :label-width="state.formLabelWidth" >
          <el-input v-model="state.form.id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item prop="newPassword" label="새 비밀번호" :label-width="state.formLabelWidth">
          <el-input v-model="state.form.newPassword" autocomplete="off" show-password></el-input>
        </el-form-item>

      </el-form>

      <el-row class="row-btn" style="margin-top: 40px">
        <el-button @click="clickChangeStPassword" style="width: 45%; border-radius: 15px">비밀번호 재설정(학생)</el-button>
        <el-button @click="clickChangeTchrPassword" style="width: 45%; border-radius: 15px">비밀번호 재설정(교사)</el-button>
      </el-row>
    </el-dialog>
  </div>
</template>
<style>
.password-dialog {
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
  name: 'changePassword-dialog',

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
    const changePasswordForm = ref(null)

    /*
      // Element UI Validator
      // rules의 객체 키 값과 form의 객체 키 값이 같아야 매칭되어 적용됨
      //
    */
    let reg = /(?!^(\d+|[a-zA-Z]+|[~!@#$%^&*?]+)$)^[\w~!@#$%^&*?]{8,15}$/
    const checkPasswordPattern = function(rule, value, callback) {
      if (!reg.test(value)) {
        callback(new Error('Password should be 8-15 Numbers, letters or characters'))
      } else {
        callback()
      }
    }

    const state = reactive({
      form: {
        id: '',
        newPassword: '',
        align: 'left'
      },
      rules: {
        newPassword: [
          { message: 'Please input password', trigger: 'blur'},
          { validator: checkPasswordPattern, trigger: 'blur'}
        ]
      },
      dialogVisible: computed(() => props.open),
      formLabelWidth: '120px'
    })

    onMounted(() => {
      // console.log(loginForm.value)
    })


    const handleClose = function () {
      state.form.id = ''
      state.form.newPassword = ''
      emit('closeChangePasswordDialog')
    }
    const clickChangeStPassword = function () {
      changePasswordForm.value.validate((valid) => {
        if (valid) {
          store.dispatch('root/requestChangeStPassword', {stId: state.form.id, stPassword: state.form.newPassword })
          .then(function (result) {
            alert('비밀번호 재설정(학생) : 성공')
            handleClose()
          })
          .catch(function (err) {
            alert(err)
          })
        }
      });
    }
    const clickChangeTchrPassword = function () {
      store.dispatch('root/requestChangeTchrPassword', {tchrId: state.form.id, tchrPassword: state.form.newPassword })
      .then(function (result) {
        alert('비밀번호 재설정(교사) : 성공')
        handleClose()
      })
      .catch(function (err) {
        alert(err)
      })
    }


    return { changePasswordForm, state, handleClose, clickChangeStPassword, clickChangeTchrPassword }
  },

}
</script>
