<template>
  <div>
    <tchr-nav @startvideo="start"></tchr-nav>
    <div class="demo-date-picker">
      <div class="block">
        <el-date-picker
        class = "datepick"
        v-model="state.studyDate"
        type="String"
        placeholder="수업일"
        format="YYYY-MM-DD"
        value-format="YYYY-MM-DD"
        >
        </el-date-picker>
        <el-button class = "datepickbtn" @click ="getConfAttData">조회</el-button>
        <div>
          <el-select v-model="value" class="m-2" placeholder="시간을 선택해주세요" @change="getConfSTrecord">
            <el-option
              v-for="con in state.STTimeRecord"
              :key="con.confId"
              :label="con.confStart.substr(0, 19)"
              :value="con"
            >
            </el-option>
          </el-select>
        </div>
      </div>
    </div>
    <table class= "recotable">
      <th>학생이름</th>
      <th>입장시간</th>
      <th>퇴장시간</th>
      <th>출결여부</th>
      <tr v-for="tr in state.conferList.attendances" :key ="tr.confId">
        <td>{{tr.stId}}</td>
        <td><p v-for="(Rin, index) in makereco(tr).rstart" :key="index">{{Rin}}</p></td>
        <td><p v-for="(Rin, index) in makereco(tr).rend" :key="index">{{Rin}}</p></td>
        <td v-if="is_passible(tr.attPass)" class="ipa">O</td>
        <td v-else class="inpa">X</td>
      </tr>
    </table>
    <start-video-dialog
      :open="state.videoDialogOpen"
      @closeVideoDialog="end"
    ></start-video-dialog>
  </div>
</template>
<script>
import { reactive, computed, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

import Tchr_nav from './tchr_nav.vue'
import StartVideoDialog from './startvideo-dialog.vue'

export default {
  name: 'daily_attend',
  setup() {
    const router = useRouter()
    const store = useStore()
    const state = reactive({
      studyDate : "",
      chooseConfer: "",
      videoDialogOpen : false,
      conferList: {},
      attreco:[],
      STTimeRecord:[
  {
    attendances: [
      {
        attId: 0,
        attPass: 0,
        attendanceRecords: [
          {
            attId: 0,
            confId: 0,
            recId: 0,
            recIn: "",
            recOut: "",
            stId: "수업을 선택해주세요"
          }
        ],
        confId: 0,
        stId: "수업을 선택해주세요"
      }
    ],
    confAtt: 0,
    confDes: "",
    confEnd: "",
    confId: 0,
    confInit: "",
    confStart: "",
    confTitle: "수업을 선택해주세요",
    studyId: 0,
    tchrId: "수업을 선택해주세요"
  }
],
    })
    const getConfAttData = function(){
      console.log("현재시간:", state.studyDate)
      store.dispatch("root/requestConfAttData",{
        studyId : parseInt(store.state.root.curClassId),
        tchrId : store.state.root.userid,
        targetDate: String(state.studyDate)
      })
      .then(res =>{
        state.STTimeRecord = res.data
      })
    }
    const getConfSTrecord = function(conf){
      state.conferList = conf
    }
    const makereco = function(data){
      var l_list = []
      var r_list = []
      for (var i =0; i<data.attendanceRecords.length; i++){
        if (data.attendanceRecords[i].recIn){
          l_list.push(data.attendanceRecords[i].recIn.substr(0, 19))
        } else {
          l_list.push("입장시간없음")
        }
        if (data.attendanceRecords[i].recOut){
          r_list.push(data.attendanceRecords[i].recOut.substr(0, 19))
        } else {
          r_list.push("퇴장시간없음")
        }
      }
      const tlist = {rstart : l_list, rend : r_list}
      return tlist
    }
    const is_passible= function(data){
      if (data){
        return true
      }else{
        return false
      }
    }
    const start = function(){
      console.log("열림")
      state.videoDialogOpen= true
    }
    const end = function(){
      state.videoDialogOpen= false
    }
    return { state, start, end, getConfAttData, getConfSTrecord, makereco, is_passible }
  },
  components: {
    "tchr-nav" : Tchr_nav,
    StartVideoDialog,
  },
}

</script>
<style scoped>
*, html, body {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
.topnav{
  background-color: #545c64;
  position: relative;
  color: #fff;
  display: flex;
  list-style:none;
  width: 100%;
}
.navitem{
  padding: 20px;
  border-bottom: solid 2px white;
  margin-right: 10px;
}
.navitem:hover{
  color: yellow;
  border-bottom: solid 2px yellow;
}
.lessonstr {
  right: 0;
  margin: 20px;
  position: absolute;
}
.demo-date-picker {
  display: flex;
  width: 100%;
  padding: 0;
  flex-wrap: wrap;
}
.demo-date-picker .block {
  padding: 30px 0;
  display: flex;
  text-align: center;
  margin: auto;
  border-right: solid 1px var(--el-border-color-base);
  align-items: center;
}
.datepickbtn{
  margin-right: 55vh;
  margin-left: 1vh;
  width: 50px;
  height: 30px;
  background-color: #6B3BE3;
  color:#fff;
  border-radius: 10px;
}
.demo-date-picker .block:last-child {
  border-right: none;
}
.recotable{
  width: 120vh;
  margin: auto;
  background-color: #fff;
  border-collapse: collapse;
}
.recotable>tr:nth-child(2n){
  background-color: #c8bfdf;
}
.recotable th{
  background-color: #6B3BE3;
  color:#fff;
  padding:12px;
}
.recotable p{
  margin: 8px;
}
.ipa{
  color: green;
}
.inpa{
  color: red;
}

</style>
