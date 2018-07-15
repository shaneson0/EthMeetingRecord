# coding=utf-8

from DBUtils.PooledDB import PooledDB
import pymysql
import sys


class Conns:
    def __init__(self):
        self.connPool = None
        mysqlhost = '114.215.132.245'
        mysqlport = 3306
        mysqluser = 'root'
        mysqlpass = 'Xuan13924540343!'
        self.connPool = PooledDB(pymysql, mincached=15, host=mysqlhost, user=mysqluser, passwd=mysqlpass, db='meeting_record',
                                 port=mysqlport,
                                 charset="utf8", setsession=["SET AUTOCOMMIT = 1"], ping=2)


    def getConnByConnPool(self, connname=''):
        return self.connPool.connection()

    def getVoteDb(self):
        return self.getConnByConnPool("vote")

    def closeDB(self, conn):
        pass


__g_conn = Conns()

def getVoteDb():
    return __g_conn.getVoteDb()


def OpNewExecWrite(sql, args):
    db = getVoteDb()
    cursor = db.cursor()
    try:
        cursor.execute(sql, args)
        db.commit()
        return (True,"success")
    except : #Exception,e:
        db.rollback()
        import traceback
        traceback.print_exc()
        print(sql)
        sys.stdout.flush()
        return False, "exp"

def OpExecWrite(sql):
    db = getVoteDb()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        return (True,"success")
    except : #Exception,e:
        db.rollback()
        import traceback
        traceback.print_exc()
        print(sql)
        sys.stdout.flush()
        return False, "exp"

import traceback
def NewOpExecRead(sql, args):
    db = getVoteDb()
    cursor = db.cursor()
    try:
        cursor.execute(sql, args)
        results = cursor.fetchall()
        return results
    except:
        print(sql)
        return None



def OpExecRead(sql):
    db = getVoteDb()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except:
        print(sql)
        return None

