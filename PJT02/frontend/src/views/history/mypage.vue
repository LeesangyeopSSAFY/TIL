<template>
  <el-row :gutter="20">
    <el-col :span="12" :offset="6">
      <el-container style="border-style: solid; border-color: #b2bec3; border-radius: 50px; margin-top: 8vh; background-color: #fff">
        <el-form label-width="100px" label-position="left" style="width: 100%; padding: 20px; margin-top: 20px; margin-bottom: 20px">
          <span>
            <strong style="font-size: xx-large">프로필</strong>
          </span>
          <br><br><br>
          <el-row>
            <el-col :span="17">
              <el-form-item prop="name" label="이름" >
                <el-input v-model="state.form.name" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item prop="id" label="아이디" >
                <el-input v-model="state.form.id" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item prop="passwordCheck" label="이메일" >
                <el-input v-model="state.form.email" autocomplete="off"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="6" :offset="1" style="overflow-x: hidden">
              <el-avatar :size="80" :fit="cover" :src="state.imgpath" v-if="state.imgpath"></el-avatar>
              <el-avatar :size="80" :fit="cover" :src="require('@/assets/images/기본프로필.jpg')" v-else></el-avatar>
              <!--
                교사는 {tchrProfPath} + {tchrProfName}
                학생은 {stProfPath} + {stProfName}
                위치에서 이미지 불러오면됨!!!
                > 우리반 보기에서도 수정바람
              -->
              <form action="#" id="profileForm" method="post" enctype="multipart/form-data">
                <input type="file" accept="image/*" @change="updateProfileImage" style="margin-top: 15px">
              </form>
            </el-col>
          </el-row>
          <el-form-item prop="birthday" label="생년월일" >
            <el-date-picker
              v-model="state.form.birthday" type="date" placeholder="Pick your birthday" style="width: 100%" format="YYYY-MM-DD" value-format="YYYYMMDD"
            >
            </el-date-picker>
          </el-form-item>
          <el-form-item prop="department" label="학교" >
            <el-input v-model="state.form.school" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item prop="position" label="연락처" >
            <el-input v-model="state.form.contact" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item prop="password" label="비밀번호 확인">
            <el-input v-model="state.form.password" autocomplete="off" show-password></el-input>
          </el-form-item>
          <el-row :gutter="20">
            <el-col :span="4" :offset="20">
              <el-button type="text" @click="clickDelete" style="color: red">계정 탈퇴</el-button>
            </el-col>
          </el-row>
          <el-button
            style="background-color: #6B3BE3; color: white; width: 40%; height: 45px; margin-top: 20px; border-radius: 15px"
            @click="clickModify">정보수정</el-button>
        </el-form>
      </el-container>
    </el-col>
  </el-row>
</template>

<script>
import { onMounted,reactive,computed } from 'vue'
import { useStore } from 'vuex'
import $axios from 'axios'

export default {
  name: 'History',
  setup (props, { emit }) {
    const state = reactive({
      form: {
        id: '',
        email: '',
        school: '',
        contact: '',
        name: '',
        birthday: '',
        password: '',
        align: 'left',
        filename: '',
      },
      rules: {
        id: [
          { required: true, message: 'Please input ID', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Please input password', trigger: 'blur' }
        ]
      },
      dialogVisible: computed(() => props.open),
      formLabelWidth: '120px',
      imgpath: '',
    })
    const store = useStore()
    const username = store.state.root.userid

    const clickModify = function () {
      if (store.state.root.whetherTchr) {
        store.dispatch('root/requestModifyTeacher', {
            tchr_contact: state.form.contact,
            tchr_email: state.form.email,
            tchr_id: state.form.id,
            tchr_name: state.form.name,
            tchr_school: state.form.school,
            tchr_birthday: state.form.birthday,
            tchr_password: state.form.password
        })
        .then(function (result) {
          alert('정보 수정(교사) 성공')
          $axios.get(`/teacher/${store.state.root.userid}?tchrId=` + store.state.root.userid )
          .then(res => {
            console.log(res.data)
            state.form.id = res.data.tchrId
            state.form.email = res.data.tchrEmail
            state.form.contact = res.data.tchrConcat
            state.form.school = res.data.tchrSchool
            state.form.birthday = res.data.tchrBirthday
            state.form.name = res.data.tchrName
            state.form.password = ''
          })
        })
        .catch(function (err) {
          alert(err)
        })
      } else {
        store.dispatch('root/requestModifyStudent', {
            st_contact: state.form.contact,
            st_email: state.form.email,
            st_id: state.form.id,
            st_name: state.form.name,
            st_school: state.form.school,
            st_birthday: state.form.birthday,
            st_password: state.form.password
        })
        .then(function (result) {
          alert('정보 수정(학생) 성공')
          $axios.get(`/student/${store.state.root.userid}?stId=` + store.state.root.userid )
          .then(res => {
            console.log(res.data)
            state.form.id = res.data.stId
            state.form.email = res.data.stEmail
            state.form.contact = res.data.stConcat
            state.form.school = res.data.stSchool
            state.form.birthday = res.data.stBirthday
            state.form.name = res.data.stName
            state.form.password = ''
          })
        })
        .catch(function (err) {
          alert(err)
        })
      }
    }

    const clickDelete = function () {
      if (store.state.root.whetherTchr) {
        store.dispatch('root/requestDeleteTeacher', username)
        .then(function (result) {
          alert('정보 수정 성공')
          state.form.id = ''
          state.form.email = ''
          state.form.contact = ''
          state.form.school = ''
          state.form.birthday = ''
          emit('deleteId')
        })
        .catch(function (err) {
          alert(err)
        })
      } else {
        store.dispatch('root/requestDeleteStudent', username)
        .then(function (result) {
          alert('정보 수정 성공')
          state.form.id = ''
          state.form.email = ''
          state.form.contact = ''
          state.form.school = ''
          state.form.birthday = ''
          emit('deleteId')
        })
        .catch(function (err) {
          alert(err)
        })
      }
    }

    const updateProfileImage = function (event) {
      var files = event.target.files
      var filesArr = Array.prototype.slice.call(files)[0]
      var profileImg = new FormData(document.querySelector('#profileForm'))
      if (store.state.root.whetherTchr) {
        console.log(state.form.id)
        profileImg.append('tchrId', state.form.id)
        console.log(filesArr)
        profileImg.append('tchrProfFile', filesArr)
        store.dispatch('root/requestUpdateTchrProfImg', profileImg)
      } else {
        profileImg.append('stId', state.form.id)
        profileImg.append('stProfFile', filesArr)
        store.dispatch('root/requestUpdateStProfImg', profileImg)
      }
    }


      // 페이지 진입시 불리는 훅
    onMounted (() => {
      store.commit('root/setMenuActiveMenuName', 'history')
      console.log(store.state.root.userid, store.state.root.whetherTchr)
      if (store.state.root.whetherTchr) {
        $axios.get(`/teacher/${store.state.root.userid}?tchrId=` + store.state.root.userid )
        .then(res => {
          console.log(res.data)
          state.form.id = res.data.tchrId
          state.form.email = res.data.tchrEmail
          state.form.contact = res.data.tchrConcat
          state.form.school = res.data.tchrSchool
          state.form.birthday = res.data.tchrBirthday
          state.form.name = res.data.tchrName
          if (res.data.tchrProfName) {
            state.imgpath = require('@/assets/images/' + res.data.tchrProfPath + res.data.tchrProfName)
          }
        })
        .catch(err => {
          console.log(err.data)
        })
      } else {
        $axios.get(`/student/${store.state.root.userid}?stId=` + store.state.root.userid )
        .then(res => {
          console.log(res.data)
          state.form.id = res.data.stId
          state.form.email = res.data.stEmail
          state.form.contact = res.data.stConcat
          state.form.school = res.data.stSchool
          state.form.birthday = res.data.stBirthday
          state.form.name = res.data.stName
          if (res.data.stProfName) {
            state.imgpath = require('@/assets/images/' + res.data.stProfPath + res.data.stProfName)
          }
        })
      }
    })

    return {state,clickModify,clickDelete, username, updateProfileImage}
  },
}
</script>
