<template>


  <div class="content-wrapper">
    <div class="row">

      <h1 class="text-center" >添加会议记录</h1>
      <div class="container">
        <div class="row ">
          <div class=" col-sm-4" style="margin-top: 10px">
            <form class="bs-example bs-example-form " role="form">
              <div class="input-group input-group-lg">
                <span class="input-group-addon">会&nbsp;议&nbsp;日&nbsp;期</span>
                <input type="text" id="date" class="form-control">
              </div>
            </form>
          </div>
          <div class=" col-sm-4" style="margin-top: 10px">
            <form class="bs-example bs-example-form " role="form">
              <div class="input-group input-group-lg">
                <span class="input-group-addon">会&nbsp;议&nbsp;题&nbsp;目</span>
                <input type="text" id="title" class="form-control" value="19:30">
              </div>
            </form>
          </div>

          <div class=" col-sm-4" style="margin-top: 10px">
            <form class="bs-example bs-example-form " role="form">
              <div class="input-group input-group-lg">
                <span class="input-group-addon">会&nbsp;议&nbsp;地&nbsp;点</span>
                <input type="text" id="place" class="form-control" value="会议室332">
              </div>
            </form>
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <br>
          <div class="box box-success chuxi">
            <div class="box-header ui-sortable-handle" style="cursor: move;">
              <div class="col-sm-2">
              </div>
              <div class="row col-sm-8" style="margin-bottom: 5px;">
                <h4 class="text-center">出席人员
                  <small>请选出出席人员</small>
                </h4>
              </div>
              <div class="col-sm-2">
                <button type="button" class="btn btn-block btn-default" v-on:click="swapCheck">全选/取消全选</button>
              </div>
            </div>
            <div class="box-body font-size-18" id>
              <div>
                <!--<div class="col-sm-12 divcss5-bottom"> </div>-->
                <!--<div class="col-sm-11 divcss5-bottom"></div>-->
                <!--<div class="col-sm-12 divcss5-bottom"> </div>-->
                <!--<div class="col-sm-11 divcss5-bottom"></div>-->


                <div class="row">
                  <div class="col-sm-1 divcss5-bottom">老师</div>
                  <div class="col-sm-11 divcss5-bottom">
                    <div class=" col-sm-2" v-for="item in items" v-if="item.grade=='老师'">
                      <label>
                        <input type="checkbox" v-bind:name="item.username"><span class="label label-default" v-text="item.username"></span></input>
                      </label>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col-sm-1 divcss5-bottom">博士</div>
                  <div class="col-sm-11 divcss5-bottom">
                    <div class=" col-sm-2" v-for="item in items" v-if="item.grade=='博士'">
                      <label><input type="checkbox" v-bind:name="item.username"> <span class="label label-default"
                                                                                       v-text="item.username"></span></input>
                      </label>
                    </div>
                  </div>
                </div>


                <div class="row">

                  <div class="col-sm-1 divcss5-bottom">研三</div>
                  <div class="col-sm-11 divcss5-bottom">
                    <div class=" col-sm-2" v-for="item in items" v-if="item.grade=='研三'">
                      <label><input type="checkbox" v-bind:name="item.username"> <span class="label label-default"
                                                                                       v-text="item.username"></span></input>
                      </label>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col-sm-1 divcss5-bottom">研二</div>
                  <div class="col-sm-11 divcss5-bottom">
                    <div class=" col-sm-2" v-for="item in items" v-if="item.grade=='研二'">
                      <label><input type="checkbox" v-bind:name="item.username"> <span class="label label-default"
                                                                                       v-text="item.username"></span></input>
                      </label>
                    </div>
                  </div>
                </div>


                <div class="row">
                  <div class="col-sm-1 divcss5-bottom">研一</div>
                  <div class="col-sm-11 divcss5-bottom">
                    <div class=" col-sm-2" v-for="item in items" v-if="item.grade=='研一'">
                      <label><input type="checkbox" v-bind:name="item.username"> <span class="label label-default"
                                                                                       v-text="item.username"></span></input>
                      </label>
                    </div>
                  </div>
                </div>


                <div class="row">
                  <div class="col-sm-1">研零</div>
                  <div class="col-sm-11">
                    <div class=" col-sm-2" v-for="item in items" v-if="item.grade=='研零'">
                      <label><input type="checkbox" v-bind:name="item.username"> <span class="label label-default"
                                                                                       v-text="item.username"></span></input>
                      </label>
                    </div>
                  </div>
                </div>

              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <div class="col-sm-12 divcss5-bottom">
            <div id="edit" style="background-color: white"></div>
          </div>

        </div>
      </div>
      <div class="container">
        <div class="row">
          <p style="text-align: center">
            <!--<button  type="button"  class="btn btn-default btn-lg"></button>-->
            <button type="button" id="save" class="btn  btn-primary btn-lg" v-on:click="saveT">保存</button>
          </p>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
  import * as API from '../api/index'
  import { Base64 } from 'js-base64';

  export default {
    name: 'meetingRecord',
    mounted: function () {
      this.init()
      this.newOrEdit()
      this.getAllPeople()
    },
    data () {
      return {
        items: {},
        recordId: "",
        id: "",
        title: "",
        recoderid: "",
        record_text: "",
        nonAttend_items: new Array(),
        nonAttend_one: null,
        sucAttachments: new Array(),
        fileName: "",
        newOrUpdate: "",
        date: '2017-09-08 09:00:00',
        time: "",
        place: "",
        recorder: "",
        content: "",
        verification: "",
        attPersons: {},
      }
    },
    methods: {
      getQueryString: function () {
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i")
        var r = window.location.search.substr(1).match(reg)
        if (r != null) return unescape(r[2])
        return null
      },
      newOrEdit: function () {
        if (this.getQueryString("id") === null) {
          this.newOrUpdate = "new";
          //执行一个laydate实例
          laydate.render({
            elem: '#date',
            value: new Date()
          });
        }
        else {
          this.newOrUpdate = "update";
          this.recordId = getQueryString("id");
          this.getRecord();
        }
      },
      getRecord: function () {
        $.ajax({
          type: "get",
          url: appname + "/record/showOne",
          data: {id: vm.recordId},
          success: function (data) {
            vm.date = data.date
            $('#date').val(vm.date)
            //执行一个laydate实例
            laydate.render({
              elem: '#date',
              value: new Date(vm.date)
            });
            vm.time = data.time
            $('#time').val(vm.time)
            vm.place = data.place
            $('#place').val(vm.place)
            vm.recorder = data.recorder
            $('#recorder').val(vm.recorder)
            vm.verification = data.verification
            vm.sucAttachments = data.attachment
            vm.attPersons = data.attPersons
            for (index in vm.attPersons) {
              $("input[name='" + vm.attPersons[index].name + "']").attr("checked", 'true');
            }
            vm.nonAttend_items = data.nonAttPersons
            $('#edit > div.froala-element').html(data.content);
          }
        });
      },
      autoComplete: function (subjects) {
        $('#recorder').typeahead({
          // source: subjects,
          source: function (query, process) {
            process(subjects);
          },
          displayText: function (item) {//要匹配的东西，根据这个来搜索
            console.log(item.username)
            return item.username
          },
          updater: function (item) {  //显示的东西
            vm.recoderid = item.id;
            return item.username; //这里一定要return，否则选中不显示
          },
          items: 8, //显示8条
          delay: 50 //延迟时间
        });
      }
      ,
      autoComplete2: function (subjects) {
        $('#nonAttender').typeahead({
          // source: subjects,
          source: function (query, process) {
            process(subjects);
          },
          displayText: function (item) {//要匹配的东西，根据这个来搜索
            return item.username
          },
          updater: function (item) {  //显示的东西
            vm.nonAttend_one = item;
            return item.username; //这里一定要return，否则选中不显示
          },
          items: 8, //显示8条
          delay: 50 //延迟时间
        });
      }
      ,
      getAllPeople: function () {
        const self = this
        API.request('post', '/app/user/list', null).then(function (res) {
            if (res.data.code === 0) {
              self.items = res.data.data.users
              self.autoComplete(self.items)
              self.autoComplete2(self.items)
            }
        })
      },
      swapCheck: function () {
        if (isCheckAll) {
          $("input[type='checkbox']").each(function () {
            this.checked = false;
          });
          isCheckAll = false;
        } else {
          $("input[type='checkbox']").each(function () {
            this.checked = true;
          });
          isCheckAll = true;
        }
      },
      appendNonAttender: function () {
        if (vm.nonAttend_one == null) {
          alert('请先在输入框中选择已经存在的人名' + "\n\n （提示：先输入姓氏，然后点击提示框中的人名）")
          return
        }
        if ($('#nonAttender').val() == "" && $('#nonAttend_reason').val() == "") {
          alert("没有内容不能提交！")
          return
        }
        else if ($('#nonAttender').val() == "") {
          alert("请输入请假人！")
          return
        }
        else if ($('#nonAttend_reason').val() == "") {
          alert("不能无缘无故请假！")
          return
        }
        else {
          vm.nonAttend_one['personName'] = $('#nonAttender').val()
          vm.nonAttend_one['reason'] = $('#nonAttend_reason').val()
          vm.nonAttend_items.push(vm.nonAttend_one)
          vm.nonAttend_one = null
          $('#nonAttender').val("")
          $('#nonAttend_reason').val("")
        }
      },
      deleteNonAttender: function (it) {
        vm.nonAttend_items.splice($.inArray(it, vm.nonAttend_items), 1)
      },
      saveT: function () {
        if (this.newOrUpdate == "new") {
          var attend_persons = new Array();
          for (var index in this.items) {
            if ($("input[name=" + this.items[index].username + "]").is(':checked')) {
              attend_persons.push(this.items[index].username)
            }
          }
          const dateVar = $('#date').val()
          const timeVar = ''
          const title = $('#title').val()
          const placeVar = $('#place').val()
          const rawcontent = $('#edit > div.froala-element').html()
          const content = Base64.encodeURI(rawcontent)
          const attList = JSON.stringify(attend_persons)

          const self = this
          const data = `date=${dateVar}&time=${timeVar}&place=${placeVar}&content=${content}&attList=${attList}&title=${title}`
          console.log(rawcontent)
          console.log(content)
          console.log(Base64.decode(content))
          console.log(data)
          API.request('post', '/app/record/add', data).then(function (res) {
            if (res.data.code === 0) {
              self.$router.push("/")
            }
          })
        }
      },
      deleteAtt: function (it) {
        console.log(it)
        $.ajax({
          type: "post",
          url: appname + "/record/deleteAttach",
          data: {
            fileName: it.timeStamp + it.fileName,
          },
          success: function (data) {
            if (data.code == 200) {
              alert("删除成功！");
              vm.sucAttachments.splice($.inArray(it, vm.sucAttachments), 1)
            }
            else {
              alert("删除失败")
            }
          }
        });
      },
      init: function () {
        $(function () {
          $('#edit').editable(
            {
              inlineMode: false,
              theme: 'royal',
              height: '400px', //高度,
              language: "zh_cn",
            }
          )
        });
        $(function () {
          $("#btnsubmit").click(function () {
            if ($("input[name='attachment']").val() == "") {
              alert("no Att")
              return
            }
            $("#form1").ajaxSubmit({
              success: function (data) {
                vm.sucAttachments.push(data)
              },
              error: function (error) {
                console.log(error)
              },
              url: '/record/addAttach', /*设置post提交到的页面*/
              type: "post", /*设置表单以post方法提交*/
              dataType: "json" /*设置返回值类型为文本*/
            });
          });
        });
      }
    }
  }
</script>
