# coding=utf8
from flask import Flask, request, jsonify, make_response
import sys

app = Flask(__name__)

from service import userservice, blockchainservice, recordservice
import traceback


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/app/user/add", methods=['post', 'get'])
def addUser():
    username = request.values.get("username")
    grade = request.values.get("grade")
    ret = userservice.insertUserlib(username, grade)
    if ret:
        return finalMakeResponse(0, {}, 200)
    else:
        return finalMakeResponse(1, {}, 500)

@app.route("/app/user/list", methods=['post', 'get'])
def listUser():
    users = userservice.selectUsers()
    return finalMakeResponse(0, {'users': users}, 200)


@app.route('/app/record/add', methods=['post', 'get'])
def addRecord():
    try:
        date = request.values.get("date")
        time = request.values.get("time")
        place = request.values.get("place")
        content = request.values.get("content")
        attList = request.values.get("attList")
        title = request.values.get("title")
        ret = blockchainservice.makeRecord(date, time, place, content, attList, title)
        if ret:
            return finalMakeResponse(0, {}, 200)
        else:
            return finalMakeResponse(1, {}, 500)
    except:
        traceback.print_exc()
        return finalMakeResponse(1, {}, 500)

@app.route('/app/record/list', methods=['post', 'get'])
def getRecords():
    recordList = recordservice.selectRecords()
    return finalMakeResponse(0, {'records': recordList}, 200)


@app.route('/app/record/info', methods=['post', 'get'])
def getRecordInfo():
    try:
        recordid = request.values.get("recordid")
        info = recordservice.selectRecordInfo(recordid)
        recordservice.addReadNumber(recordid)
        return finalMakeResponse(0, {'info': info}, 200)
    except:
        traceback.print_exc()
        return finalMakeResponse(1, {}, 500)

@app.route("/app/blocks/list", methods=['post', 'get'])
def getBlocks():
    try:
        pagesize = int(request.values.get("pagesize", 10))
        currentpage = int(request.values.get("currentpage", 1))
        res, blockslist = blockchainservice.getBlocks(pagesize, currentpage)
        if res:
            return finalMakeResponse(0, {'list': blockslist}, 200)
            # return make_response(jsonify({'code': 0, 'data': {'list': blockslist}, 'msg': ''}), 200)
        else:
            return finalMakeResponse(1,  {'list': blockslist}, 200)
    except:
        traceback.print_exc()
        return finalMakeResponse(1, {}, 200)

@app.route("/app/transaction/info", methods=['post', 'get'])
def getTransactionInfo():
    try:
        tx_hash = request.values.get("txhash", '')
        info = blockchainservice.getTransactionInfo(tx_hash)
        return finalMakeResponse(0, {'info': info}, 200)
    except:
        traceback.print_exc()
        return finalMakeResponse(1, {}, 500)


def finalMakeResponse(code, data, ResCode):
    response = make_response(jsonify({'code': code, 'data': data, 'msg': ''}), ResCode)
    return response



if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=5001, debug=True)



