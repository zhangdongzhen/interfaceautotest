#-*-encoding:utf-8 -*-
"""
@version:1
@author:刘雅
@file:sql_config.py
@time:2019/1/1615:53
"""
import time
# 获取common表中的url
def common_url(type,Identifi_field):
    return "select url from Common where Identifi_field ='"+Identifi_field+"' and platform_name ='"+type+"'"
# 获取各个平台的后台登录账户
def get_value_from_common_config(type,Identifi_field):
    return "select Variable_value from common_config where Variable_name ='"+Identifi_field+"' and platform_name='"+type+"'"
# 从Common_savebl表中判断该变量值是否已经存在
def get_True_From_Common_savebl(type,Variable_name):
    return "select Variable_value from Common_savebl where platform_name='"+type+"' and Variable_name ='"+Variable_name+"';"
# 获取表中成功的条数
def set_count_total_successful():
    return "select successful from count_total;"
# 将count_total表中的succ字段加1
def set_count_total_successful_and_one(successful):
    return "update count_total set successful ="+str(successful+1)+";"
# 获取表中失败的条数
def set_count_total_fail():
    return "select fail from count_total;"
# 将count_total表中的fail字段加1
def set_count_total_fail_and_one(fail):
    return "update count_total set fail ="+str(fail+1)+";"
# 将count_total表进行初始化
def set_count_total():
    return "update count_total set successful=0 ,fail=0;"
# 获取count_total表中的成功和失败数
def get_count_from_count_total():
    return "select successful,fail from count_total;"
# 将结果保存在execution_result表中
def write_to_execution_result(platform_name,Pass_Count,Fail_Count,Identifi_field):
    createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return "insert into execution_result(platform_name,Execution_date,Execution_Count,Pass_Count,Fail_Count,Identifi_field) values('"+platform_name+"','"+createTime+"',"+str(Pass_Count+Fail_Count)+","+str(Pass_Count)+","+str(Fail_Count)+",'"+Identifi_field+"')"
#按序列号和平台名称查询报错日志
def get_loginfo(platform_name,serialnum):
    return "select fail_inter_name,request_body,response_body from Error_Log where serialnum = '"+serialnum+"' and platform_name = '"+platform_name+"'"
#获取所有执行结果
def get_execution_result(start, num):
    sql = "select * from execution_result order by Execution_date desc limit {0},{1}".format(
        start, num)
    sql = sql + ';'
    return sql
# 页面执行结果保存在execution_result表中
def write_to_execution_result_page(platform_name,Execution_Count,Identifi_field,exec_user):
    createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    exec_state = u'正在执行'
    return "insert into execution_result(platform_name,Execution_date,Execution_Count,Identifi_field,exec_user,exec_state) values('"+platform_name+"','"+createTime+"',"+str(Execution_Count)+",'"+Identifi_field+"','"+exec_user+"','"+exec_state+"')"
#更新页面执行结果
def update_execution_result_page(id,successful,fail,serialnum):
    exec_state = u'已完成'
    return "update execution_result set Pass_Count ="+str(successful)+","+"Fail_Count = "+str(fail)+",serialnum = "+serialnum+",exec_state = '"+exec_state+"' where id = "+str(id)+";"
# 获取count_total表中的成功和失败数
def get_errorlog_from_error_log(serialnum):
    sql = "select * from error_log where serialnum = '"+serialnum+"';"
    print sql
    return "select *,date_format(Execution_date,'%Y-%m-%d %h:%i:%s') as Exec_date from error_log where serialnum = '"+serialnum+"';"