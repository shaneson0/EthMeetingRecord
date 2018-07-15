<template>

  <div class="content-wrapper">
    <div class="row">
      <div class="col-sm-8"></div>
      <div class="col-sm-4" style="margin-top:10px">

        <router-link to="meetingRecord">
          <button type="button" class="btn btn-success btn-group-sm">
            <span class="glyphicon glyphicon-plus"></span>
            添加一次会议记录
          </button>
        </router-link>

      </div>
    </div>
    <div class="container">
      <section class="content">
        <div>
          <div class="box box-default" v-for="record in records">
            <div class="box-header with-border">
              <router-link
                  :to="{name: 'showMeetingRecord', params: {id: record.id}}"
              ><h3 class="box-title" v-text="record.date"></h3></router-link>
            </div>
            <div class="box-body">
              <div class="col-sm-8">
                <span v-text="'参与人：'+record.attList"></span>
              </div>
              <div class="col-sm-4">
                <span v-text="'阅读量：'+record.readNum"></span>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>

</template>

<script>

import * as API from '../api/index'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      records: []
    }
  },
  created: function () {
    this.getRecords()
  },
  methods: {
    getRecords: function () {
      const self = this
      API.request('post', '/app/record/list', null).then(function (res) {
          if (res.data.code === 0 ) {
            self.records = res.data.data.records
          }
      })
    }
  }
}
</script>

