# -*- coding: utf-8 -*-
import MySQLdb

class DatabaseOperation():
    def openconnect(self):
        conn = MySQLdb.connect(host='114.115.208.238', port=3306, user='saas3_owner', passwd='C0Bg9y#qAgq7', db='saas3',charset='UTF8',)
        cur = conn.cursor()
        return conn,cur


if __name__ == '__main__':
    con=DatabaseOperation()
    con.openconnect()