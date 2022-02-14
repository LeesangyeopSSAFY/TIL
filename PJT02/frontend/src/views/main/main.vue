<template>
<!-- main.vue -->
  <el-container class="main-wrapper" style="padding: 0">
    <el-container class="main-container">
      <el-aside class="hide-on-small" width="240px">
        <main-sidebar
          :width="`240px`"
          style="height : 100vh; position: relatve;"
          @logout1="logout2"
          />
      </el-aside>
      <el-main style="padding: 0">
        <!-- <el-row> -->
          <!-- <el-col :span="20" :offset="2"> -->
          <router-view @deleteId="deleteId1" ></router-view>
          <!-- </el-col> -->
        <!-- </el-row> -->
      </el-main>
    </el-container>
  </el-container>

</template>
<style>
  @import "https://unpkg.com/element-plus/theme-chalk/index.css";
  @import './main.css';
  @import '../../common/css/common.css';
  @import '../../common/css/element-plus.css';
.main-wrapper{
  /* background-color: #E0E4D7; */
  background-color: #E7EDDE;

}
</style>
<script>
import MainSidebar from './components/main-sidebar'
import MainFooter from './components/main-footer'
import Calendar from './components/calendar.vue'

export default {
  name: 'Main',
  components: {
    // MainHeader,
    MainSidebar,
    MainFooter,
    Calendar,
  },
  setup(props, { emit }) {
    const logout2 = function(){
      emit('logout3')
    }
    const deleteId1 = function(){
      emit('deleteId2')
    }
    return {logout2, deleteId1 }
  },

}
</script>
