<template>
  <div style="height: 100%;">
    <el-row style="height: 100%">
      <el-col :span="24" style="heght: 100%">
        <el-menu
          default-active="0"
          active-text-color="#ffd04b"
          background-color="#4267D6"
          text-color="#fff"
          style="height: 100%; position: fixed; border-color: #4267D6; width: 240px"
          class="el-menu-vertical-demo"
          @select="menuSelect">
          <el-container class="profile-card">
            <el-card style="text-align: center; width: 220px; margin: 5px; background-color: #1B2A57; color: white; border-radius: 20px">
              <p>
                <el-avatar :size="80" fit=cover :src="state.imgpath" v-if="state.imgpath"></el-avatar>
                <el-avatar :size="80" fit=cover :src="require('@/assets/images/기본프로필.jpg')" v-else></el-avatar>
              </p>
              <div>
                <span><strong>{{ username }}</strong></span>
              </div>
              <el-button
                color="#626aef"
                style="margin-top: 5px; background-color: #6B3BE3; color: white; border-color: #6B3BE3"
                @click="goMypage"
                >마이페이지
              </el-button>
            </el-card>
          </el-container>

          <el-menu-item v-for="(item, index) in state.menuItems" :key="index" :index="index.toString()">
            <span>{{ item.title }}</span>
          </el-menu-item>

          <div v-if="whetherTchr">
            <el-menu-item v-for="(val, idx) in state.tchr_scha" :key=idx @click="MoveLesson(val[0], val[1])">
                <span>{{ val[1] }}</span>
            </el-menu-item>
            <el-menu-item @click="state.isVisible=true">
              <span>수업개설</span>
            </el-menu-item>
            <ModalView class="li_zindex" v-if ="state.isVisible" @close-modal="closeModal"></ModalView>
          </div>

          <el-menu-item class="mt-auto" style="bottom: 0; width: 240px; position : fixed" @click="logout">
            <span >로그아웃</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
  </div>
</template>
<style scoped>
.profile-card {
  padding: auto;
  justify-content: center;
}
.main-sidebar .el-menu {
  margin-top: 0;
  padding-left: 0;
}
.main-sidebar .hide-on-small {
  height: 100%;
}
.main-sidebar .hide-on-small .el-menu {
  height: 100%;
}
.main-sidebar .el-menu .el-menu-item {
  cursor: pointer;
  border-right: none;
}
.main-sidebar .el-menu .el-menu-item .ic {
  margin-right: 5px;
}
.li_zindex{
  z-index: 1000;
  box-shadow: 3px 3px 3px 3px gray;
}
.studyList{
  border-radius: 10px;
  list-style: none;
  padding: 10px;
  margin: 5px;
}
.studyList>li{
  margin : 10px;
  cursor: pointer;
}
.studyBtn{
  width: 50px;
  height: 50px;
  border-radius: 25px;
  border: solid 1px #e5e9f2;
  text-align: center;
  cursor: pointer;
}
</style>
<script>
import ModalView from "../../teacher/tchr_create_lesson"
import { reactive, computed, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import $axios from 'axios'

export default {
  name: 'main-header',
  components:{
    ModalView
  },
  props: {
    width: {
      type: String,
      default: '240px'
    }
  },
  setup(props, { emit }) {
    const store = useStore()
    const router = useRouter()

    const username = store.state.root.userid
    const whetherTchr = store.state.root.whetherTchr

    const state = reactive({
      isVisible: false,
      isteacher :false,
      tchr_scha: computed(() => store.getters['root/getStudy']),
      searchValue: null,
      menuItems: computed(() => {
        const MenuItems = store.getters['root/getMenus']
        let keys = Object.keys(MenuItems)
        let menuArray = []
        for (let i = 0; i < keys.length; ++i) {
          let menuObject = {}
          menuObject.icon = MenuItems[keys[i]].icon
          menuObject.title = MenuItems[keys[i]].name
          menuArray.push(menuObject)
        }
        return menuArray
      }),
      activeIndex: computed(() => store.getters['root/getActiveMenuIndex']),
      imgpath: ''
    })

    if (state.activeIndex === -1) {
      state.activeIndex = 0
      store.commit('root/setMenuActive', 0)
    }

    const menuSelect = function (index) {
      store.commit('root/setMenuActive', index)
      const MenuItems = store.getters['root/getMenus']
      let keys = Object.keys(MenuItems)
      router.push({
        name: keys[index]
      })
    }

    const goMypage = function(){
      router.push({
        name: 'Mypage'
      })
    }

    const logout = function(){
      emit('logout1')
    }
    const MoveLesson = function(idx, name){
      store.commit('root/changeClassName', name)
      store.commit('root/changeClassId', idx)
      router.push({
        name: 'Tchr_main',
      })
    }
    const getClass = function(){
      store.dispatch('root/requestGetTchrClass', {
            tchrId: store.state.root.userid})
        .then(res =>{
          store.state.root.classList = res.data
          state.tchr_scha = res.data
        })
    }
    const closeModal = function(){
      getClass();
      state.isVisible = false
    }
    onMounted(()=>{
      if (store.state.root.whetherTchr){
        $axios.get(`/teacher/${store.state.root.userid}?tchrId=` + store.state.root.userid )
        .then(res => {
          if (res.data.tchrProfName) {
            state.imgpath = require('@/assets/images/' + res.data.tchrProfPath + res.data.tchrProfName)
          }
          getClass();
        })
        .catch(err => {
          console.log(err)
        })
      } else {
        $axios.get(`/student/${store.state.root.userid}?stId=` + store.state.root.userid )
        .then(res => {
          if (res.data.stProfName) {
            state.imgpath = require('@/assets/images/' + res.data.stProfPath + res.data.stProfName)
          }
          getClass();
        })
      }
    })

    return { state, username, whetherTchr, onMounted, MoveLesson, menuSelect, logout, goMypage, getClass, closeModal}
  }
}
</script>
