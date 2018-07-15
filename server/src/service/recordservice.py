# coding=utf-8

import base64
import sys
sys.path.append("..")


from db import opDBP

def insertRecordlib(date,time,place, content, attList,title, address):
    sql = "insert into record(`date`,`time`,place, content, attList, title, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    args = (date, time, place, base64.b64encode(content.encode()), attList, title, address)
    ret,msg = opDBP.OpNewExecWrite(sql, args)
    return ret

def selectRecords():
    queryfiles = ['id', 'date', 'time', 'place', 'content', 'attList', 'readNum']
    sql = "select id, `date`, `time`, place, content, attList, readNum from record "
    res = opDBP.OpExecRead(sql)
    r = [dict(zip(queryfiles, re)) for re in res]
    return r

def selectRecordInfo(recordId):
    queryfiles = ['date', 'time', 'place', 'content', 'attList', 'readNum', 'title']
    sql = "select `date`, `time`, place, content, attList, readNum, title from record where id = %s"%(recordId)
    res = opDBP.OpExecRead(sql)
    r = [dict(zip(queryfiles, re)) for re in res]
    info = r[0]
    info['content'] = base64.b64decode(info['content']).decode()
    return info


def addReadNumber(recordId):
    sql = "update record set readNum = readNum + 1 where id = %s"%(recordId)
    ret, msg = opDBP.OpExecWrite(sql)
    return ret

