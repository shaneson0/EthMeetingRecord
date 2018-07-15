<template>
  <div class="content-wrapper">
    <div class="row">
      <h1 class="text-center">{{title}}</h1>
      <div class="row">
        <div class="container">
          <div class="row">
            <div class="col-sm-6">
              <div class="box box-default">
                <div class="box-header with-border">
                  <span style="font-size: 25px " class="box-title text-center"><b>会议时间</b></span>
                </div>
                <div style="font-size: 20px" class="box-body"><span v-text="date"></span>&nbsp;<span
                  v-text="time"></span></div>
              </div>
            </div>
            <div class="col-sm-6">
              <div class="box box-default">
                <div class="box-header with-border">
                  <span style="font-size: 25px " class="box-title text-center"><b>会议地点</b></span>
                </div>
                <div style="font-size: 20px" class="box-body"><span v-text="place"></span></div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class=" col-sm-12">
              <div class="box box-default">
                <div class="box-header with-border">
                  <span style="font-size: 25px " class="box-title text-center"><b>会议内容</b></span>
                </div>
                <div style="font-size: 20px" class="box-body">
                  <div v-html="content"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>


  </div>
</template>


<script>
  import * as API from '../api/index'

  import { Base64 } from 'js-base64';

  export default {
    name: 'showMeetingRecord',
    data () {
        return {
          recordId: "",
          items: {},
          date: "",
          time: "",
          place: "",
          recorder: "",
          content: "",
          verification: "",
          attachment: {},
          attPersons: {},
          nonAttPersons: {},
          nonAttCou: {},
          info: {},
          title: ''
        }
    },
    mounted: function () {
      this.recordId = this.$route.params.id
      console.log('recordId: ' + this.recordId)
      this.showRecord()
//      this.stasticNon()
    },
    methods: {
      showRecord: function () {
        const self = this
        const data = `recordid=${this.recordId}`
        API.request('post', '/app/record/info', data).then(function (res) {
            console.log(res)
            if (res.data.code === 0) {
                const info = res.data.data.info
                self.date = info.date
                self.time = info.time
                self.place = info.place
                self.recorder = '善轩'
                self.attPersons = JSON.parse(info.attList)
                self.content = Base64.decode(info.content)
                self.title = info.title
                console.log(info.content)
                console.log(self.content)
            }
        })
      },
      ifshow: function (name, obj) {
        if (JSON.stringify(obj).indexOf(name) !== -1) {
          return true
        }
        return false
      },
      ifExist: function (obj) {
        if (obj.toString() <= 4) {
          return false
        }
        return true
      },
      stasticNon: function () {
        $.ajax({
          type: "get",
          url: appname + "/nonAttendance/listNon",
          data: {id: getQueryString("id")},
          success: function (data) {
            console.log(data)
            vm.nonAttCou = data
            // 指定图表的配置项和数据
            var option = {
              title: {
                // text: '请假次数统计：'
              },
              tooltip: {},
              legend: {
                data: ['请假次数']
              },
              xAxis: {
                data: vm.nonAttCou.all.map(function (m) {
                  return m.name
                })
              },
              yAxis: {},
              series: [{
                name: '请假次数',
                type: 'bar',
                data: vm.nonAttCou.all.map(function (m) {
                  return m.number
                })
              }]
            };
            myChart.setOption(option);

          }
        });
      }
    }
  }

</script>
