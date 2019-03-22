#-*-encoding:utf-8 -*-
"""
@version:1
@author:刘雅
@file:Read_From_Mysql.py
@time:2019/1/1016:42
"""
import xlrd
# import xlwt
# from xlutils.copy import copy
import MySQLdb
class Read_From_Mysql():
    # 读取Excel值
    def read_excel(self,file_path,sheet_name,rows,cols):
        work_book=xlrd.open_workbook(file_path)
        table=work_book.sheet_by_name(sheet_name)
        cell_value=str(table.cell(rows,cols).value)
        return cell_value
    # 写入Excel值
    def write_excel(self,file_path,sheet_index,rows,cols,bl):
        books1=xlrd.open_workbook(file_path)
        books2=copy(books1)
        table=books2.get_sheet(sheet_index)
        table.write(rows,cols,bl)
        books2.save(file_path)
    # 从表中读取数据,单行数据
    def Select_Data_From_User(self,sql):
        # 打开数据库连接
        # fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
        # fetchall():接收全部的返回结果行.
        # rowcount: 这是一个只读属性，并返回执行execute()
        # 方法后影响的行数
        self.db = MySQLdb.connect("10.98.8.61", "ab", "ab", "postman", charset='utf8')
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
        # 使用execute方法执行SQL语句
        self.cursor.execute(sql)
        data=self.cursor.fetchone()[0]
        self.db.close()
        return data
        # 从表中读取数据,多行数据
    def Select_Datas_From_User(self, sql):
        # 打开数据库连接
        # fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
        # fetchall():接收全部的返回结果行.
        # rowcount: 这是一个只读属性，并返回执行execute()
        # 方法后影响的行数
        self.db = MySQLdb.connect("10.98.8.61", "ab", "ab", "postman", charset='utf8')
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
        # 使用execute方法执行SQL语句
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        self.db.close()
        return data
#     写入表数据
    def InsertOrUpdate_Data_To_bl(self,sql):

        # 打开数据库连接
        self.db = MySQLdb.connect("10.98.8.61", "ab", "ab", "postman", charset='utf8')
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

        try:
            # 使用execute方法执行SQL语句
            self.cursor.execute(sql)
            self.db.commit()
            print "sql:",sql
        except:
            # 发生错误时回滚
            self.db.rollback()
        self.db.close()
        # return data

    #从表中读取分页读取数据
    def select_datas_by_page(self,start, num):
        # 打开数据库连接
        self.db = MySQLdb.connect("10.98.8.61", "ab", "ab", "postman", charset='utf8')
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor( cursorclass = MySQLdb . cursors . DictCursor )
        results = ''
        sql = "select count(0) from execution_result "
        self.cursor.execute(sql)
        # total = self.cursor.fetchone()[0]
        total = self.cursor.fetchall()[0][u'count(0)']
        getsql = "select Identifi_field,platform_name,Execution_Count,Fail_Count,Pass_Count,id,date_format(Execution_date,'%Y-%m-%d %h:%i:%s') as Exec_date,Execution_date,exec_user,exec_state,serialnum from execution_result order by Execution_date desc limit {0},{1}".format(
            start, num)
        try:
            # 使用execute方法执行SQL语句
            self.cursor.execute(getsql)
            self.db.commit()

        except:
            self.db.rollback()
            print "Error: unable to fecth data"

        items = self.cursor.fetchall()
        # 关闭数据库连接
        self.db.close()
        result = {}
        result['items'] = items
        result['total'] = total
        print items
        return result

    #     写入表数据返回新数据id
    def InsertOrUpdate_Data_return_id(self, sql):

        # 打开数据库连接
        self.db = MySQLdb.connect("10.98.8.61", "ab", "ab", "postman", charset='utf8')
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
        newid = 0
        try:
            # 使用execute方法执行SQL语句
            self.cursor.execute(sql)
            self.db.commit()
            newid = int(self.cursor.lastrowid)
        except:
            # 发生错误时回滚
            self.db.rollback()
        self.db.close()
        return newid
    # 从表中读取数据,多行数据,字段名一起返回
    def Select_Datas_From_table(self,serialnum,start,num):
        # 打开数据库连接
        self.db = MySQLdb.connect("10.98.8.61", "ab", "ab", "postman", charset='utf8')
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor( cursorclass = MySQLdb . cursors . DictCursor )
        results = ''
        sql = "select count(0) from error_log where serialnum = '"+serialnum+"'"
        self.cursor.execute(sql)
        # total = self.cursor.fetchone()[0]
        total = self.cursor.fetchall()[0][u'count(0)']
        getsql = "select *,date_format(Execution_date,'%Y-%m-%d %h:%i:%s') as Exec_date from error_log where serialnum = '"+serialnum+"' limit {0},{1}".format(
            start, num)
        print sql
        print getsql
        try:
            # 使用execute方法执行SQL语句
            self.cursor.execute(getsql)
            self.db.commit()

        except:
            self.db.rollback()
            print "Error: unable to fecth data"

        items = self.cursor.fetchall()
        # 关闭数据库连接
        self.db.close()
        result = {}
        result['items'] = items
        result['total'] = total
        print items
        return result
if __name__ == '__main__':
    Read_From_Mysql().select_datas_by_page(1,10)
