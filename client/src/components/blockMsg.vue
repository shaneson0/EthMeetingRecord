<template>
  <div>

    <div class="modal fade" id="blockList" tabindex="-1" role="dialog" aria-labelledby="blockList" aria-hidden="true">
      <div class="modal-dialog" style=" width: 80%;">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
            <h4 class="modal-title">blockList</h4>
          </div>
          <div class="modal-body">

            <div class="container" style="width: inherit">
              <div class="row">
                <div class="col-xs-12 col-sm-12" >
                  <div class="box">
                    <!-- /.box-header -->
                    <div class="box-body no-padding">
                      <table class="table table-striped">
                        <thead>
                        <tr>
                          <th>区块高度</th>
                          <th>交易数量</th>
                          <th>区块哈希</th>
                          <th>操作</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="(block, index) in BlocksInfo">
                          <td>{{block.number}}</td>
                          <td>{{block.transactionnum}}</td>
                          <td><a href="#">{{block.hash}}</a></td>
                          <td><a href="#" @click="getTransactions(index)">查看交易</a></td>
                        </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div><!-- /.modal-content -->
      </div><!-- /.modal -->
    </div>

    <div class="modal fade" id="transactionList" tabindex="-1" role="dialog" aria-labelledby="transactionList" aria-hidden="true">
      <div class="modal-dialog" style=" width: 80%;">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
            <h4 class="modal-title">模态框（Modal）标题</h4>
          </div>
          <div class="modal-body">

            <div class="col-xs-12 col-sm-12">
              <div class="box">
                <!-- /.box-header -->
                <div class="box-body no-padding">
                  <table class="table table-striped">
                    <thead>
                    <tr>
                      <th>交易ID</th>
                      <th>操作</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="x in transactions">
                      <td>{{x}}</td>
                      <td><a href="#"  v-on:click="getTransactionDetail(x)">查看详情</a></td>
                    </tr>
                    </tbody>

                  </table>
                </div>
                <!-- /.box-body -->
              </div>
            </div>

          </div>
          <div class="modal-footer">
            <button type='button' class='btn btn-primary previous-page' v-on:click="transactionPreStep()">
              上一步
            </button>
          </div>
        </div><!-- /.modal-content -->
      </div><!-- /.modal -->
    </div>


    <transaction-detail :Info="Info"></transaction-detail>
  </div>

</template>

<script>

  import * as API from '../api/index'
  import TransactionDetail from './transactionDetail.vue'

  export default {
      name: 'blockMsg',
      components: {TransactionDetail},
      created: function () {
          this.getBlockslist()
      },
      data () {
          return {
            BlocksInfo: [],
            transactions: [],
            transcationId: 0,
            Info: {
              hash: '',
              nonce: '',
              blockHash: '',
              blockNumber: '',
              transactionIndex: 0,
              from: '',
              to: '',
              value: '',
              gas: '',
              input: '',
              votingPromoter: '',
              votingFrom: '',
              votingTo: ''
            }
          }
      },
      methods: {
        getBlockslist: function () {
          const self = this
          const data = `pagesize=100`
          API.request('post', '/app/blocks/list', data).then(function (res) {
            if (res.data.code === 0) {
              self.BlocksInfo = res.data.data.list
              self.BlocksInfo.reverse()
            }
          })
        },
        flushTransaction: function (transcationId) {
          const self = this
          const data = `txhash=${transcationId}`
          API.request('post', '/app/transaction/info', data).then(function (res) {
            if ( res.data.code === 0 ) {
              console.log(res.data.data.info)
              self.Info = res.data.data.info
            }
          })
        },
        getTransactions: function (index) {
          this.transactions = this.BlocksInfo[index]['transactions']
          $('#blockList').modal('hide')
          $('#transactionList').modal('toggle')
        },
        getTransactionDetail: function (Txid) {
          this.transcationId = Txid
          this.flushTransaction(Txid)
          $('#transactionList').modal('hide')
          $('#transactionDetail').modal('toggle')
        },
        transactionPreStep: function () {
          $('#blockList').modal('toggle')
          $('#transactionList').modal('hide')
        }
      }
  }

</script>
