<template>
  <el-row>
    <el-col :span="22" :offset="1">
      <div>
        <!-- <div class="head" >
          Main
        </div> -->
        <!-- 대시보드 -->
        <el-row id="dashboard">
          <el-col :span="6">

            <el-card :body-style="{ padding: '0px' }" id="dash" shadow="always" v-if="this.dashHw">
              <div style="padding: 14px; text-align:left; background-color:#EADDFF">
                <font-awesome-icon icon="clock" style="font-size:80px" />
                <span style="font-weight:bold; color:#21005D; font-size:20px">
                  곧 마감인 과제
                </span>
                <div class="bottom">
                  <el-button type="text" class="button" @click="drawerHW = true">{{this.dashHw.title}}</el-button>
                  <!-- <p>{{this.dashHw.content}}</p> -->
                  <div>
                    <time class="time">{{ this.dashHw.end.substring(0, 10) }}</time>
                  </div>
                </div>
              </div>
              <el-drawer v-model="drawerHW" direction="ttb" size="50%">
                <template #title>
                  <h1 style="font-size: 25px; color: black">{{this.dashHw.title}}</h1>
                </template>
                <h4>수업: {{ this.dashHw.className }}</h4>
                <h4>내용: {{ this.dashHw.content }}</h4>
                <h4>제출 기한: {{ this.dashHw.end }}</h4>
                <h4>첨부파일: {{ this.dashHw.fileName }}</h4>
              </el-drawer>
            </el-card>

            <el-card :body-style="{ padding: '0px' }" id="dash" shadow="always" v-else>
              <div style="padding: 14px; text-align:left; background-color:#EADDFF">
                <font-awesome-icon icon="clock" style="font-size:80px" />
                <span style="font-weight:bold; color:#21005D; font-size:20px">
                  곧 마감인 과제
                </span>
                <div class="bottom">
                  <p>등록된 과제가 없습니다</p>
                </div>
              </div>
            </el-card>

          </el-col>
          <el-col :span="6">
            <el-card :body-style="{ padding: '0px' }" id="dash" shadow="always" v-if="this.dashNotice">
              <div style="padding: 14px; text-align:left;background-color:#D9E7CB">
                <font-awesome-icon icon="bell" style="font-size:80px" />
                <span style="font-weight:bold; color:#273420; font-size:20px">
                  최신 공지
                </span>
                <div class="bottom">
                  <el-button type="text" class="button" @click="drawer = true">{{this.dashNotice.noticeTitle}}</el-button>
                  <!-- <p>{{this.dashNotice.noticeContent}}</p> -->
                  <div>
                    <time class="time">{{ this.dashNotice.noticePosted }}</time>
                  </div>
                </div>
              </div>
              <el-drawer v-model="drawer" direction="ttb" size="50%">
                <template #title>
                  <h1 style="font-size: 25px; color: black">{{this.dashNotice.noticeTitle}}</h1>
                </template>
                <h4>내용: {{ this.dashNotice.noticeContent }}</h4>
                <h4>제출 기한: {{ this.dashNotice.noticePosted }}</h4>
                <h4>첨부 파일: {{ this.dashNotice.noticeFile[0].fileOriginName }}</h4>
              </el-drawer>
            </el-card>
            <el-card :body-style="{ padding: '0px' }" id="dash" shadow="always" v-else>
              <div style="padding: 14px; text-align:left;background-color:#D9E7CB">
                <font-awesome-icon icon="bell" style="font-size:80px" />
                <span style="font-weight:bold; color:#273420; font-size:20px">
                  최신 공지
                </span>
                <div class="bottom">
                  <p>등록된 공지가 없습니다</p>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card :body-style="{ padding: '0px' }" id="dash" shadow="always">
              <div style="padding: 14px; text-align:left;background-color:#F9DEDC" class="">
                <font-awesome-icon icon="calendar-check" style="font-size:80px" />
                <span style="font-weight:bold; color:#410E08; font-size:20px">
                  출석 확인
                </span>
                <div class="bottom">
                  <el-button type="text" class="button">Operating</el-button>
                  <div>
                    <time class="time">{{ this.today }}</time>
                  </div>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card :body-style="{ padding: '0px' }" id="dash" shadow="always">
              <div style="padding: 14px; text-align:left;background-color:#FFD8E4" class="">
                <font-awesome-icon icon="chalkboard-teacher" style="font-size:80px" />
                <span style="font-weight:bold; color:#31111D; font-size:20px">
                  진행중인 수업
                </span>
                <div class="bottom">
                  <el-button type="text" class="button">{{ this.progresstitle }}</el-button>
                  <div>
                    <time class="time">~{{ this.progressend.substring(0, 16) }}</time>
                  </div>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <el-row >
        <!-- 달력 -->
          <el-col :span="17" style="margin-left: 1vh">
            <div class="calendar" style="margin-left: 10px">
              <vue-cal
                class="vuecal--blue-theme cal"
                :selected-date="this.today"
                :disable-views="['years', 'year']"
                active-view="month"
                events-on-month-view="short"
                overlaps-per-time-step
                :events="events"
                style="height: auto"
              >
              </vue-cal>
            </div>
          </el-col>
        <!-- 원형 그래프 -->
          <el-col :span="6" style="margin-left: 2vh">
            <div style="background-color: #1B2A57; margin-bottom: 4vh; margin-top: 1vh; text-color: #fff">
              <canvas id="myChart" style="padding-top: 10px; padding-bottom: 20px"></canvas>
              <div v-if="this.tchrOrNot" style="color: #fff">
                <h4 style="margin-top: 2px; padding-bottom: 15px;">출제한 과제 비율</h4>
              </div>
              <div v-else style="color: #fff">
                <h4 style="margin-top: 2px; padding-bottom: 15px;">HW Chart</h4>
              </div>
            </div>
            <div style="background-color: #1B2A57">
              <el-progress type="dashboard" :percentage="this.percentageHW" style="padding-top: 10px; margin-top: 3%">
                <template #default="{ percentage }">
                  <span class="percentage-value">{{ percentage }}%</span>
                  <span class="percentage-label">과제 제출률</span>
                </template>
              </el-progress>
              <h4 style="margin-top: 2px; padding-bottom: 15px; color: #fff">제출한 과제: {{ this.doneHW }}  /  미제출 과제: {{ this.notyetHW }}</h4>
            </div>
          </el-col>
        </el-row>
      </div>
    </el-col>
  </el-row>
</template>

<script>
import VueCal from 'vue-cal'
import "vue-cal/dist/vuecal.css";

import Chart from 'chart.js'

export default {
  name: "Calendar",
  components: {
    VueCal,
    },

  data: () => ({
    events: [],
    today:new Date(),
    dashHw:undefined,
    dashNotice:undefined,
    drawerHW: false,
    drawer: false,
    doneHW: 0,
    notyetHW: 0,
    percentageHW: 0,
    myTchr: [],
    inProgressClass: [],
    progresstitle: '',
    progressend: ''
 }),
  methods: {
    setEventVal() {
      this.events = [
        {
          start: "2022-1-21 15:25",
          end: "2022-1-21 16:25",
          title: "john 1",
          content: 'Default',
          class: "health",
          split: 2
        }
      ];
    },
    getNotice(){
      this.$store.dispatch('root/requestGetSTNotice',this.userId)
      .then(result =>{
        this.notices=result.data
        this.dashNotice=this.notices[this.notices.length-1]
        if (result.data.length >= 1) {
            this.dashNotice.noticePosted=this.dashNotice.noticePosted.substring(0,10)
        }
      })
      .catch(function(err){
        alert(err)
      })
    },
    getNoticeTchr(){
      this.$store.dispatch('root/requestGetTchrNotice')
      .then(result => {
        this.notices=result.data
        this.dashNotice=this.notices[this.notices.length-1]
        if (result.data.length >= 1) {
            this.dashNotice.noticePosted=this.dashNotice.noticePosted.substring(0,10)
        }
      })
      .catch(function(err){
        alert(err)
      })
    },
    getHw(){
      this.$store.dispatch('root/requestGetHW',this.userId)
      .then(result =>{
        for (var j = 0; j < result.data.length; j++) {
          if (this.events.length >= 3) {
            break
          }
          var hw = result.data[j];
          if (hw.hwDeadline > this.today) {
            this.events.push({
              start: hw.hwPosted.substring(0, 16), //"2022-02-08 14:00"
              end: hw.hwDeadline.substring(0,16),
              //start: hw.hwPosted.substring(0,5)+hw.hwPosted.substring(6,16),//"2022-01-30 17:46:39.000000"
              //end: hw.hwDeadline.substring(0,5)+hw.hwDeadline.substring(6,16),//"2022-02-18 12:00:00"
              title: hw.hwTitle,
              className :hw.studyroom.studyName,
              content: hw.hwContent,
              teacher: hw.tchrId,
              fileName: hw.hwFile[0].fileOriginName,
              class: "health",
              split: 2
            });
          }
        }
        // const hws=[];
        // for (var j = 0; j < this.events.length; j++) {
        //   var hw = this.events[j];
        //   console.log("마감기한:"+hw.end)
        //   console.log("오늘:"+this.today)
        //   if (hw.end>=this.today){
        //     hws.push(hw);
        //   }
        // }

        // hws.sort(function(a, b) { // 오름차순
        //   return a["end"] - b["end"];
        // });
        // this.dashHw=hws[hws.length-1]
        this.dashHw=this.events[0]
        console.log('과제:', this.dashHw)
      })
      .catch(function(err){
        alert(err)
      })
    },
    getTchtHW(){
      this.$store.dispatch('root/requestTchrListHomework')
      .then(result =>{
        for (var j = 0; j < result.data.length; j++) {
          if (this.events.length >= 3) {
            break
          }
          var hw = result.data[j];
          if (hw.hwDeadline > this.today) {
            this.events.push({
              start: hw.hwPosted.substring(0, 16), //"2022-02-08 14:00"
              end: hw.hwDeadline.substring(0,16),
              title: hw.hwTitle,
              className :hw.studyroom.studyName,
              content: hw.hwContent,
              teacher: hw.tchrId,
              fileName: hw.hwFile[0].fileOriginName,
              class: "health",
              split: 2
            });
          }
        }
        this.dashHw=this.events[0]
        console.log('선생님 과제:', this.events)
      })
      .catch(function(err){
        alert(err)
      })
    },
    getProgress(){
      this.$store.dispatch('root/requestRateHW')
      .then(result => {
        console.log(result.data[0], '과제 제출률 콘솔')
        this.doneHW = result.data[0][0]
        this.notyetHW = result.data[0][1]
        if (this.doneHW == 0 && this.notyetHW == 0) {
          this.percentageHW = 0
        } else {
          this.percentageHW = Math.floor(100 * result.data[0][0] / (result.data[0][0] + result.data[0][1]))
        }
      })
    },
    getMyTchr(){
      this.$store.dispatch('root/requestGetClass')
      .then(result => {
        for (let j = 0; j < result.data.length; j++) {
          this.myTchr.push({
            studyId: result.data[j].studyId,
            tchrId: result.data[j].tchrId
          })
        }
        for (let i = 0; i < this.myTchr.length; i++) {
          this.$store.dispatch('root/requestConfAttData', {studyId: this.myTchr[i].studyId, targetDate: this.today, tchrId: this.myTchr[i].tchrId })
          .then(res => {
            const thishour = new Date().getHours()
            const thisminutes = new Date().getMinutes()
            let tmphour = ''
            let tmpmin = ''
            if (thishour < 10) {
              tmphour = '0' + thishour
            } else {
              tmphour = thishour
            }
            if (thisminutes < 10) {
              tmpmin = '0' + thisminutes
            } else {
              tmpmin = thisminutes
            }
            const thisTime = tmphour + ':' + tmpmin
            for (let k = 0; k < res.data.length; k++) {
              if (this.inProgressClass.length >= 1) {
                break
              }
              const tmpclass = res.data[k]
              if (res.data[k].confStart.substring(11, 16) < thisTime && res.data[k].confEnd.substring(11, 16) > thisTime) {
                this.inProgressClass.push(tmpclass)
                this.progresstitle = tmpclass.confTitle
                this.progressend = tmpclass.confEnd
              }
            }
          })
        }
      })
    },

  },
  created:function(){
    const localvuex=JSON.parse(localStorage.getItem('vuex'))
    this.userId = localvuex["root"]["userid"]
    this.tchrOrNot = localvuex["root"]["whetherTchr"]
    const nowyear = new Date().getFullYear()
    let nowmonth = new Date().getMonth()+1
    let nowday = new Date().getDate()
    if (nowmonth < 10){
      nowmonth = '0' + nowmonth
    }
    if (nowday < 10) {
      nowday = '0' + nowday
    }
    this.today=nowyear + '-' + nowmonth + '-' + nowday
    // this.setEventVal()
    if (this.tchrOrNot) {
      this.getNoticeTchr()
      this.getTchtHW()
    } else {
      this.getNotice()
      this.getHw()
      this.getMyTchr()
    }
    this.getProgress()
    console.log(this.inProgressClass, '진행중인 수업 테스트')
  },
  mounted() {
      // cdn chart.js
      let recaptchaScript = document.createElement('script')
      recaptchaScript.setAttribute('src', 'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.min.js')
      document.head.appendChild(recaptchaScript)

      let hwlabels = []
      let hwdata = []
      if (this.tchrOrNot) {
        this.$store.dispatch('root/requestTchrListHomework')
        .then(result => {
          let hwClass = {}
          for (var j = 0; j < result.data.length; j++) {
            if (result.data[j].studyroom.studyName in hwClass) {
              hwClass[result.data[j].studyroom.studyName] += 1
            } else {
              hwClass[result.data[j].studyroom.studyName] = 1
            }
          }
          hwlabels = Object.keys(hwClass)
          for (var key in hwClass) {
            hwdata.push(hwClass[key])
          }
          if (hwlabels.length == 0) {
            hwlabels = ['과제없음']
            hwdata = [0]
          }

          const ctx = document.getElementById('myChart');
            var myChart = new Chart(ctx, {
            type: 'doughnut',
              data: {
                labels: hwlabels,
                datasets: [{
                  data: hwdata,
                  backgroundColor: [
                    '#9DCEFF',
                    '#F2F3F6',
                    '#B3261E',
                    '#21005D',
                  ],
                  borderWidth: 0,
                  scaleBeginAtZero: true,
                }
              ]
            },
          });
        })
      } else {
        this.$store.dispatch('root/requestGetHW',this.userId)
        .then(result => {
          let hwClass = {}
          for (var j = 0; j < result.data.length; j++) {
            if (result.data[j].studyroom.studyName in hwClass) {
              hwClass[result.data[j].studyroom.studyName] += 1
            } else {
              hwClass[result.data[j].studyroom.studyName] = 1
            }
          }
          hwlabels = Object.keys(hwClass)
          for (var key in hwClass) {
            hwdata.push(hwClass[key])
          }
          if (hwlabels.length == 0) {
            hwlabels = ['과제없음']
            hwdata = [0]
          }

          const ctx = document.getElementById('myChart');
            var myChart = new Chart(ctx, {
            type: 'doughnut',
              data: {
                labels: hwlabels,
                datasets: [{
                  data: hwdata,
                  backgroundColor: [
                    '#9DCEFF',
                    '#F2F3F6',
                    '#B3261E',
                    '#21005D',
                  ],
                  borderWidth: 0,
                  scaleBeginAtZero: true,
                }
              ]
            },
          });
        })
      }
  },
};
</script>

<style>
@import url('../../../../node_modules/vue-cal/dist/vuecal.css');
/* 수정 요함 */
canvas{
  width:100%!important;
  /* height: auto !important; */
}
p{
  margin: 5px;
}
.head{
  padding: 15px;
  font-size: 30px;
}
.bottom{
  clear:both;
}
.calendar{
  padding: 10px;
}
.cal{
  background-color: #C4C9BC;

}

#dashboard{
  display: flex;
  justify-content: space-between;
  align-content: center;
  padding: 10px
}

#dash {
  border-radius: 10px;
}

*.vuecal--month-view .vuecal__cell {
  height: 80px;
}

.vuecal--month-view .vuecal__cell-content {
  justify-content: flex-start;
  height: 100%;
  align-items: flex-end;
}

.vuecal--month-view .vuecal__cell-date {
  padding: 4px;
}
.vuecal--month-view .vuecal__no-event {
  display: none;
}

/* Different color for different event types. */
.vuecal__event.leisure {
  background-color: rgba(253, 156, 66, 0.9);
  border: 1px solid rgb(233, 136, 46);
  color: #fff;
}
.vuecal__event.sport {
  background-color: rgba(255, 102, 102, 0.9);
  border: 1px solid rgb(235, 82, 82);
  color: #fff;
}
.vuecal__event.health {
  /* background-color: rgba(164, 230, 210, 0.9); */
  /* background-color: #8D9287; */
  background-color: #EDCE5A;
  /* border: 1px solid rgb(144, 210, 190); */
  /* border: 1px solid #8D9287; */
  color: black;
}
.percentage-value {
  display: block;
  margin-top: 10px;
  font-size: 28px;
  color: #fff;
}

.percentage-label {
  display: block;
  margin-top: 10px;
  font-size: 12px;
  color: #fff;
}
</style>




