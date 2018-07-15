<template>
  <div id="app" class="wrapper">
      <header class="main-header">
        <nav class="navbar navbar-static-top">
          <div class="container">
            <div class="navbar-header">
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse pull-right" id="navbar-collapse">
              <ul class="nav navbar-nav">
                <li>
                  <router-link to="person">
                    <span class="glyphicon glyphicon-edit">人员编辑</span>
                  </router-link>
                </li>
                <li>
                  <a href="#">
                    <span class="glyphicon glyphicon-th-list" data-toggle="modal" data-target="#blockList">区块信息</span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
          <!-- /.container-fluid -->
        </nav>
      </header>
    <block-msg></block-msg>
      <router-view/>


  </div>


</template>



<script>

  import blockMsg from './components/blockMsg.vue'

  export default {
    components: {blockMsg},
    name: 'App'
  }
</script>
