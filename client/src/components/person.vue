
<template>
  <div class="content-wrapper">
    <div class="row">
      <div class="col-sm-8"></div>
      <div class="col-sm-4" style="margin-top:10px">
        <!--<a v-bind:href="'person.html'">-->
        <button type="button" class="btn btn-success btn-group-sm" v-on:click="showAddPerson()"><span
          class="glyphicon glyphicon-plus"></span>
          添加一个人
        </button>
        <!-- 模态框（Modal） -->
        <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
             aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;
                </button>
                <h4 class="modal-title" id="myModalLabel">添加人员</h4>
              </div>
              <div class="modal-body">
                <form class="bs-example bs-example-form" role="form">
                  <div class="input-group input-group-lg">
                    <span class="input-group-addon">姓名</span>
                    <input id="name" type="text" class="form-control" placeholder="请输入姓名"
                           v-model="addName">
                  </div>
                </form>
                <br>
                <form class="bs-example bs-example-form" role="form">
                  <div class="input-group input-group-lg">
                    <span class="input-group-addon">年级</span>
                    <select id="grade" type="text" class="form-control" v-model="addGrade">
                      <option disabled value="" selected="selected">请选择</option>
                      <option>老师</option>
                      <option>博士</option>
                      <option>研三</option>
                      <option>研二</option>
                      <option>研一</option>
                      <option>研零</option>
                    </select>
                  </div>
                </form>
                <br>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                <button v-on:click="addPerson()" id="submit" type="button" class="btn btn-primary">提交
                </button>
              </div>
            </div><!-- /.modal-content -->
          </div><!-- /.modal -->
        </div>
        <!--</a>-->
      </div>
    </div>
    <!-- 模态框（Modal） -->
    <div class="modal fade" id="myEditModal" tabindex="-1" role="dialog" aria-labelledby="myEditModalLabel"
         aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
            <h4 class="modal-title" id="myEditModalLabel">修改人员信息</h4>
          </div>
          <div class="modal-body">
            <form class="bs-example bs-example-form" role="form">
              <div class="input-group input-group-lg">
                <span class="input-group-addon">姓名</span>
                <input id="editName" type="text" class="form-control" placeholder="请输入姓名"
                       v-model="updateName">
              </div>
            </form>
            <br>
            <form class="bs-example bs-example-form" role="form">
              <div class="input-group input-group-lg">
                <span class="input-group-addon">年级</span>
                <select id="editGrade" type="text" class="form-control" v-model="updateGrade">
                  <option disabled value="" selected="selected">请选择</option>
                  <option>老师</option>
                  <option>博士</option>
                  <option>研三</option>
                  <option>研二</option>
                  <option>研一</option>
                  <option>研零</option>
                </select>
              </div>
            </form>
            <br>
          </div>
          <div class="modal-footer">
            <button v-on:click="deletePerson()" type="button" class="btn btn-primary">删除此人</button>
            <button v-on:click="updatePerson()" type="button" class="btn btn-primary">提交</button>
          </div>
        </div><!-- /.modal-content -->
      </div><!-- /.modal -->
    </div>
    <div class="container">
      <section class="content">
        <div class="box box-success" v-if="ifshow('老师',items)">
          <div class="box-header with-border">
            <h2 class="box-title">老师</h2>
          </div>
          <div class="box-body">
            <div class="col-sm-2" v-for="item in items" v-if="item.grade=='老师'">
              <a v-on:click="transPerson(item)">
                <span v-text="item.username" style="font-size: 20px"></span>
                <span class="glyphicon glyphicon-edit"></span>
              </a>
            </div>
          </div>
        </div>
        <div class="box box-success" v-if="ifshow('博士',items)">
          <div class="box-header with-border">
            <h3 class="box-title">博士</h3>
          </div>
          <div class="box-body">
            <div class="col-sm-2" v-for="item in items" v-if="item.grade=='博士'">
              <a v-on:click="transPerson(item)">
                <span v-text="item.username" style="font-size: 20px"></span>
                <span class="glyphicon glyphicon-edit"></span>
              </a>
            </div>
          </div>
        </div>
        <div class="box box-success" v-if="ifshow('研三',items)">
          <div class="box-header with-border">
            <h3 class="box-title">研三</h3>
          </div>
          <div class="box-body">
            <div class="col-sm-2" v-for="item in items" v-if="item.grade=='研三'">
              <a v-on:click="transPerson(item)">
                <span v-text="item.username" style="font-size: 20px"></span>
                <span class="glyphicon glyphicon-edit"></span>
              </a>
            </div>
          </div>
        </div>
        <div class="box box-success" v-if="ifshow('研二',items)">
          <div class="box-header with-border">
            <h3 class="box-title">研二</h3>
          </div>
          <div class="box-body">
            <div class="col-sm-2" v-for="item in items" v-if="item.grade=='研二'">
              <a v-on:click="transPerson(item)">
                <span v-text="item.username" style="font-size: 20px"></span>
                <span class="glyphicon glyphicon-edit"></span>
              </a>
            </div>
          </div>
        </div>
        <div class="box box-success" v-if="ifshow('研一',items)">
          <div class="box-header with-border">
            <h3 class="box-title">研一</h3>
          </div>
          <div class="box-body">
            <div class="col-sm-2" v-for="item in items" v-if="item.grade=='研一'">
              <a v-on:click="transPerson(item)">
                <span v-text="item.username" style="font-size: 20px"></span>
                <span class="glyphicon glyphicon-edit"></span>
              </a>
            </div>
          </div>
        </div>
        <div class="box box-success" v-if="ifshow('研零',items)">
          <div class="box-header with-border">
            <h3 class="box-title">研零</h3>
          </div>
          <div class="box-body">
            <div class="col-sm-2" v-for="item in items" v-if="item.grade=='研零'">
              <a v-on:click="transPerson(item)">
                <span v-text="item.username" style="font-size: 20px"></span>
                <span class="glyphicon glyphicon-edit"></span>
              </a>
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
    name: 'person',
    created: function () {
        this.getAllPeople()
    },
    data () {
      return {
        items: {},
        updateName: "",
        updateGrade: "",
        addName: "",
        addGrade: "",
        curPerson: {}
      }
    },
    methods: {
      ifshow: function (name, obj) {
        if (JSON.stringify(obj).indexOf(name) !== -1) {
          return true
        }
        return false
      },
      showAddPerson: function () {
        $("#myModal").modal('toggle');
      },
      transPerson: function (person) {
        vm.curPerson = person;
        $("#myEditModal").modal('toggle');
        vm.updateName = vm.curPerson.name;
        vm.updateGrade = vm.curPerson.grade;
      },
      addPerson: function () {
        const self = this
        const data = `username=${this.addName}&grade=${this.addGrade}`
        API.request('post', '/app/user/add', data ).then(function (res) {
          console.log(res)
          if (res.data.code === 0) {
            self.getAllPeople()
            $("#myModal").modal('hide')
          }
        })
      },
      updatePerson: function () {
      },
      editPerson: function () {
      },
      getAllPeople: function () {
        const self = this
        API.request('post', '/app/user/list', null).then(function (res) {
          console.log(res)
          if (res.data.code === 0 ) {
              self.items = res.data.data.users
          }
        })
      },
      deletePerson: function () {
      }
    }
  }
</script>
