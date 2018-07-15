# coding=utf-8

import sys
sys.path.append("..")


from db import opDBP

def insertUserlib(username, grade):
    sql = "insert into user(username,grade) VALUES ('%s', '%s')"%(username, grade)
    ret,msg = opDBP.OpExecWrite(sql)
    return ret


def selectUsers():
    queryfiles = ['username', 'grade']
    sql = "select username, grade from user "
    res = opDBP.OpExecRead(sql)
    r = [dict(zip(queryfiles, re)) for re in res]
    return r





