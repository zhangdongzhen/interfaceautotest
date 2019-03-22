#-*-encoding:utf-8 -*-
"""
@version:1
@author:刘雅
@file:api_common_all.py
@time:2019/1/1015:44
"""
from pages.common_pages.base import BasePage
# import xlwt
# import xlrd
import time
from common.common_function.Read_From_Mysql import Read_From_Mysql
from pages.common_pages import config
global nows,cols
from pages.api import apicommon
import MySQLdb
from common.common_function import sql_config
from common.common_function import Bl_value
class Api_Common_All():
    def __init__(self):
        self.nows, self.cols = config.get_row_col_one()
    def run_all_common_inter(self,type):
        self.get_login_account_url(type)
        # self.get_menber_login_url(type)
    # 判断变量表中是否存在该变量值，存在则更新，不存在则新增
    def Insert_Or_Update_Common_savebl(self,type,bl_name,bl_value,Variable_name):
        print "27"
        sql_Is = sql_config.get_True_From_Common_savebl(type, bl_name)
        data1 = Read_From_Mysql().Select_Datas_From_User(sql_Is)
        createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print "data1:", data1
        if len(data1) == 0:
            print 38
            SQL2 = "INSERT INTO Common_savebl(Variable_name,Variable_value,platform_name,createTime,updateTime) values ('"+Variable_name+"','" + bl_value + "','" + type + "','" + createTime + "','" + createTime + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(SQL2)
        else:
            print 42
            # SQL2 = "INSERT INTO Common_savebl(Variable_name,Variable_value,platform_name,createTime,updateTime) values ('"+Variable_name+"','" + bl_value + "','" + type + "','" + createTime + "','" + createTime + "')"
            sql3 = "update Common_savebl set Variable_value='" + bl_value + "',updateTime='" + createTime + "' where platform_name='" + type + "' and Variable_name = '"+Variable_name+"'"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql3)
    # 获取登录管理后台
    def get_login_account_url(self,type):
        # 获取登录时需要的SQL
        sql=sql_config.common_url(type,Bl_value.get_Identifi_file_account_login())
        sql_email=sql_config.get_value_from_common_config(type,Bl_value.get_Identifi_file_email())
        sql_password =sql_config.get_value_from_common_config(type,Bl_value.get_Identifi_file_password())
        # 获取登录时需要的参数值
        login_account_url=Read_From_Mysql().Select_Data_From_User(sql)
        login_account_email = Read_From_Mysql().Select_Data_From_User(sql_email)
        login_account_password = Read_From_Mysql().Select_Data_From_User(sql_password)
        # 获取需要写入配置表的参数以及参数值
        flag,bakSess=apicommon.get_bakSess(login_account_url,login_account_email,login_account_password,Bl_value.get_Identifi_file_account_login(),type)
        if flag=="0":
            self.Insert_Or_Update_Common_savebl(type,Bl_value.get_Bak_name(),bakSess,"bakSess")
    # 前台登录接口
    def get_menber_login_url(self,type):
        # 获取登录时需要的SQL
        sql=sql_config.common_url(type,Bl_value.get_member_login())
        sql_tenantId=sql_config.get_value_from_common_config(type,Bl_value.get_dentifi_file_tenantId())
        sql_schemaId =sql_config.get_value_from_common_config(type,Bl_value.get_dentifi_file_schemaId())
        sql_memberFormId = sql_config.get_value_from_common_config(type, Bl_value.get_dentifi_file_memberFormId())
        sql_memberSchemaId = sql_config.get_value_from_common_config(type, Bl_value.get_dentifi_file_memberSchemaId())
        sql_unique = sql_config.get_value_from_common_config(type, Bl_value.get_dentifi_file_unique())
        sql_password = sql_config.get_value_from_common_config(type, Bl_value.get_member_login_password())
        print "sql_password:",sql_password
        # 获取登录时需要的参数值
        login_account_url = Read_From_Mysql().Select_Data_From_User(sql)
        tenantId = Read_From_Mysql().Select_Data_From_User(sql_tenantId)
        schemaId = Read_From_Mysql().Select_Data_From_User(sql_schemaId)
        memberFormId = Read_From_Mysql().Select_Data_From_User(sql_memberFormId)
        memberSchemaId = Read_From_Mysql().Select_Data_From_User(sql_memberSchemaId)
        unique = Read_From_Mysql().Select_Data_From_User(sql_unique)
        password = Read_From_Mysql().Select_Data_From_User(sql_password)
        flag,loginSess,memberId=apicommon.get_loginSess(login_account_url,tenantId,schemaId,memberFormId,memberSchemaId,unique,password,Bl_value.get_member_login(),type)
        print "flag:",flag
        print "loginSess:",loginSess
        print "memberID:",memberId
        if flag==0:
            print "79"
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_login_name(), loginSess,Bl_value.get_login_name())
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_memberId(), memberId, Bl_value.get_memberId())
    # 获取global_topicId接口,微讨论id
    def get_global_topicId(self,type):
        # 需要获取bakSess，tenantId，nodeId
        # sql_tenantId = sql_config.get_value_from_common_config(type, Bl_value.get_dentifi_file_tenantId())
        sql_tenantId=self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        print "tenantId:",tenantId
        sql_nodeId = self.get_sql_nodeId(type)
        nodeId =self.get_nodeId_value(sql_nodeId)
        print "nodeId:",nodeId
        bakSess_url=self.get_bakSess_url(type)
        bakSess = self.get_bakSess(bakSess_url)
        print "bakSess_url:",bakSess_url
        print "bakSess:",bakSess
        sql =self.get_sql_common(type,Bl_value.get_global_topicId())
        url_global_topicId=self.get_bl_value(sql)
        print "url_global_topicId:",url_global_topicId
        flag, loginSess =apicommon.get_global_topicId(type,url_global_topicId,tenantId,nodeId,bakSess,Bl_value.get_global_topicId())
        if flag=="0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_global_topicId(), loginSess,Bl_value.get_global_topicId())
    # 获取sql_tenantId值
    def get_sql_tenantId_value(self,type):
        return sql_config.get_value_from_common_config(type, Bl_value.get_dentifi_file_tenantId())
    # 获取tenantId值
    def get_tenantId_value(self,sql_tenantId):
        return Read_From_Mysql().Select_Data_From_User(sql_tenantId)
    # 获取sql_nodeId
    def get_sql_nodeId(self,type):
        return sql_config.get_value_from_common_config(type, Bl_value.get_nodeId())
    # 获取nodeId
    def get_nodeId_value(self,sql_nodeId):
        return Read_From_Mysql().Select_Data_From_User(sql_nodeId)
    # 获取后台session_url
    def get_bakSess_url(self,type):
        return sql_config.get_True_From_Common_savebl(type,Bl_value.get_Bak_name())
    # 获取后台session_url
    def get_bakSess(self, bakSess_url):
        return Read_From_Mysql().Select_Data_From_User(bakSess_url)
    # 获取公用的sql
    def get_sql_common(self,type,common_value):
        return sql_config.common_url(type,common_value)
    # 获取针对每个接口的变量值
    def get_bl_value(self,bl_sql):
        return Read_From_Mysql().Select_Data_From_User(bl_sql)
    # 从变量表中读取数据
    def get_value_from_bl(self,type,Variable_name):
        return sql_config.get_True_From_Common_savebl(type,Variable_name)
    # 从common_config表中读取数据
    def get_value_from_common_config(self,type,Variable_name):
        return sql_config.get_value_from_common_config(type,Variable_name)
    # 获取微讨论子版Id-sectionId
    def get_sectionId(self,type):
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取nodeId值
        sql_nodeId = self.get_sql_nodeId(type)
        nodeId = self.get_nodeId_value(sql_nodeId)
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取global_topicId值
        sql_global_topicId=self.get_value_from_bl(type,Bl_value.get_global_topicId())
        global_topicId=self.get_bl_value(sql_global_topicId)
        # 获取sectionId的url
        url_sectionId=self.get_sql_common(type,Bl_value.get_sectionId())
        url_sectionId=self.get_bl_value(url_sectionId)
        print "url:",url_sectionId
        flag,sectionId= apicommon.get_sectionId(type, url_sectionId, tenantId, nodeId, bakSess,Bl_value.get_sectionId(),global_topicId)
        if flag=="0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_sectionId(), str(sectionId),Bl_value.get_sectionId())
    # 获取topicId
    def get_topicId(self,type):
        # 获取tenantId值
        sql_tenantId=self.get_sql_tenantId_value(type)
        tenantId=self.get_tenantId_value(sql_tenantId)
        # 获取nodeId值
        sql_nodeId=self.get_sql_nodeId(type)
        nodeId=self.get_nodeId_value(sql_nodeId)
        # 获取bakSess值
        sql_bakSess=self.get_bakSess_url(type)
        bakSess=self.get_bakSess(sql_bakSess)
        # 获取请求得到url
        topicId_SQL=self.get_sql_common(type,Bl_value.get_topicId())
        topicId_URL=self.get_bl_value(topicId_SQL)
        flag, topicId =apicommon.get_topicId(type, topicId_URL, tenantId, nodeId, bakSess, Bl_value.get_topicId())
        if flag=="0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_topicId(), topicId,Bl_value.get_topicId())
    # 获取seminarid和instanceid
    def get_seminarid_And_instanceid(self,type):
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取nodeId值
        sql_nodeId = self.get_sql_nodeId(type)
        nodeId = self.get_nodeId_value(sql_nodeId)
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取请求得到url
        seminarId_SQL = self.get_sql_common(type, Bl_value.get_create_seminarId())
        seminarId_URL = self.get_bl_value(seminarId_SQL)
        # 获取memberFormId
        memberFormId_SQL = self.get_value_from_common_config(type, Bl_value.get_memberFormId())
        print "memberFormId_SQL:",memberFormId_SQL
        memberFormId= self.get_bl_value(memberFormId_SQL)
        # 获取memberFormName
        memberFormName_SQL = self.get_value_from_common_config(type, Bl_value.get_memberFormName())
        memberFormName= self.get_bl_value(memberFormName_SQL)
        print "memberFormName:",memberFormName
        print "url；",seminarId_URL
        flag,seminarId,instanceId=apicommon.get_seminarId(type,seminarId_URL,tenantId,bakSess,Bl_value.get_create_seminarId(),memberFormId,memberFormName)
        if flag==0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_seminarId(), str(seminarId), Bl_value.get_seminarId())
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_seminarId_instanceId(), str(instanceId),Bl_value.get_seminarId_instanceId())
    # 线下会开启大屏管理
    def semain_setModule(self,type):
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取nodeId值
        # sql_nodeId = self.get_sql_nodeId(type)
        # nodeId = self.get_nodeId_value(sql_nodeId)
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取semainId值
        seminarId_sql=self.get_value_from_bl(type,Bl_value.get_seminarId())
        seminarId=self.get_bl_value(seminarId_sql)
        # 获取请求得到url
        seminarId_SQL = self.get_sql_common(type, Bl_value.semainr_setModule())
        seminarId_URL = self.get_bl_value(seminarId_SQL)
        # 获取memberFormId
        # memberFormId_SQL = self.get_value_from_common_config(type, Bl_value.get_memberFormId())
        # print "memberFormId_SQL:",memberFormId_SQL
        # memberFormId= self.get_bl_value(memberFormId_SQL)
        # # 获取memberFormName
        # memberFormName_SQL = self.get_value_from_common_config(type, Bl_value.get_memberFormName())
        # memberFormName= self.get_bl_value(memberFormName_SQL)
        # print "memberFormName:",memberFormName
        # print "url；",seminarId_URL
        flag,seminarId,instanceId=apicommon.seminarId_setModule(type,seminarId_URL,tenantId,bakSess,Bl_value.get_create_seminarId(),seminarId)
        if flag==0 and instanceId==200:
           print seminarId
    # 获取线下会通道id
    def get_passageId(self,type):
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取seminarId值
        seminarId_SQL=self.get_value_from_bl(type,Bl_value.get_seminarId())
        seminarId=self.get_bl_value(seminarId_SQL)
        # 获取seminar_instanceId值
        seminarId_instanceId_SQL = self.get_value_from_bl(type, Bl_value.get_seminarId_instanceId())
        seminarId_instanceId = self.get_bl_value(seminarId_instanceId_SQL)
        # 获取url
        url_seminarId = self.get_sql_common(type, Bl_value.get_passageId())
        url_seminarId=self.get_bl_value(url_seminarId)
        flag,passageId=apicommon.get_seminarId_passageId(type,url_seminarId,tenantId,bakSess,seminarId_instanceId,seminarId,Bl_value.get_passageId())
        if flag==0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_passageId(), passageId,Bl_value.get_passageId())
    # 获取luckyDrawId
    def get_luckyDrawId(self,type):
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取url
        url_luckyDrawId = self.get_sql_common(type, Bl_value.get_luckyDrawId())
        url_luckyDrawId=self.get_bl_value(url_luckyDrawId)
        flag,luckyDrawId=apicommon.get_luckDrawid(type,url_luckyDrawId,tenantId,bakSess,Bl_value.get_luckyDrawId())
        if flag==0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_luckyDrawId(), str(luckyDrawId),Bl_value.get_luckyDrawId())
    # 给抽奖设置奖项
    def set_luckyDraw_Items(self,type):
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取luckyDrawId值
        seminarId_instanceId_SQL = self.get_value_from_bl(type, Bl_value.get_luckyDrawId())
        seminarId_instanceId = self.get_bl_value(seminarId_instanceId_SQL)
        # 获取url
        url_luckyDrawId = self.get_sql_common(type, Bl_value.get_luckDrawsetItem())
        url_luckyDrawId = self.get_bl_value(url_luckyDrawId)
        flag, luckyDrawId ,CODE= apicommon.set_luckDraw_Items(type, url_luckyDrawId, bakSess,seminarId_instanceId,tenantId)
        if flag==0 and CODE==200:
            print luckyDrawId
    # 获取签到点id
    def get_signingPointId(self,type):
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取seminarId值
        seminarId_SQL = self.get_value_from_bl(type, Bl_value.get_seminarId())
        seminarId = self.get_bl_value(seminarId_SQL)
        # 获取seminar_instanceId值
        seminarId_instanceId_SQL = self.get_value_from_bl(type, Bl_value.get_seminarId_instanceId())
        seminarId_instanceId = self.get_bl_value(seminarId_instanceId_SQL)
        # 获取url
        url_seminarId = self.get_sql_common(type, Bl_value.get_passageId())
        url_seminarId=self.get_bl_value(url_seminarId)
        flag, signingPointId = apicommon.get_seminarId_signingPointId(type, url_seminarId, tenantId, bakSess,seminarId_instanceId, seminarId, Bl_value.get_signingPointId())
        if flag ==0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_signingPointId(), signingPointId,Bl_value.get_signingPointId())
    # 获取签到大屏模板id
    def get_bigScreen_templateId(self,type):
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取seminar_instanceId值
        seminarId_instanceId_SQL = self.get_value_from_bl(type, Bl_value.get_seminarId_instanceId())
        seminarId_instanceId = self.get_bl_value(seminarId_instanceId_SQL)
        # 获取nodeId值
        sql_nodeId = self.get_sql_nodeId(type)
        nodeId = self.get_nodeId_value(sql_nodeId)
        # 获取url
        url_seminarId = self.get_sql_common(type, Bl_value.get_bigScreen_templateId())
        url_seminarId=self.get_bl_value(url_seminarId)
        flag, bigScreen_templateId = apicommon.get_bigScreen_templateId(type, url_seminarId,bakSess,seminarId_instanceId,nodeId,tenantId,Bl_value.get_bigScreen_templateId())
        if flag == 0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_bigScreen_templateId(), bigScreen_templateId,Bl_value.get_bigScreen_templateId())
    # 获取大屏configId
    def get_bigScreen_configId(self,type):
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取bigScreen_templateId值
        sql_bigScreen_templateId=self.get_value_from_bl(type,Bl_value.get_bigScreen_templateId())
        bigScreen_templateId=self.get_bl_value(sql_bigScreen_templateId)
        # 获取url
        url_configId=self.get_sql_common(type,Bl_value.get_bigScreen_configId())
        url_configId=self.get_bl_value(url_configId)
        flag, configId =apicommon.get_bigScreen_configId(type,url_configId,bakSess,tenantId,bigScreen_templateId,Bl_value.get_bigScreen_configId())
        if flag==0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_bigScreen_configId(), str(configId),Bl_value.get_bigScreen_configId())
    # 获取可多次签到的签到点id
    def get_signingPointIds(self,type):
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取seminarId值
        seminarId_SQL = self.get_value_from_bl(type, Bl_value.get_seminarId())
        seminarId = self.get_bl_value(seminarId_SQL)
        # 获取seminar_instanceId值
        seminarId_instanceId_SQL = self.get_value_from_bl(type, Bl_value.get_seminarId_instanceId())
        seminarId_instanceId = self.get_bl_value(seminarId_instanceId_SQL)
        # 获取url
        url_signingPointIds=self.get_sql_common(type,Bl_value.get_signingPointIds())
        url_signingPointIds=self.get_bl_value(url_signingPointIds)
        flag, signingPointIds =apicommon.get_signingPointIds(type,url_signingPointIds,bakSess,tenantId,seminarId,seminarId_instanceId,Bl_value.get_signingPointIds())
        print "falg:",flag
        print "signingPointIds:",signingPointIds
        if flag=="0":

            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_signingPointIds(), signingPointIds,Bl_value.get_signingPointIds())
    # 获取大屏id,此大屏允许同一用户多次签到
    def get_bigScreenId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取seminarId值
        seminarId_SQL = self.get_value_from_bl(type, Bl_value.get_seminarId())
        seminarId = self.get_bl_value(seminarId_SQL)
        # 获取signingPointIds
        signingPointIds_SQL = self.get_value_from_bl(type, Bl_value.get_signingPointIds())
        signingPointIds = self.get_bl_value(signingPointIds_SQL)
        # 获取configId
        bigScreen_configId_SQL = self.get_value_from_bl(type, Bl_value.get_bigScreen_configId())
        bigScreen_configId = self.get_bl_value(bigScreen_configId_SQL)
        # 获取url
        url_bigScreenId=self.get_sql_common(type,Bl_value.get_bigScreenId())
        url_bigScreenId=self.get_bl_value(url_bigScreenId)
        print "url_bigScreenId"
        flag, bigScreenId =apicommon.get_bigScreenId(type,url_bigScreenId,bakSess,seminarId,signingPointIds,bigScreen_configId,Bl_value.get_bigScreenId())
        if flag==0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_bigScreenId(), str(bigScreenId),Bl_value.get_bigScreenId())
    # 获取productLine
    def get_productLine(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        url_productLine=self.get_sql_common(type,Bl_value.get_productLine())
        url_productLine=self.get_bl_value(url_productLine)
        flag, productLine =apicommon.get_productLine(type,url_productLine,bakSess,tenantId,Bl_value.get_productLine())
        if flag=="0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_productLine(), str(productLine),Bl_value.get_productLine())
    # 获取webinarId和webinar_instanceid
    def get_webinarId_and_instanceid(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取memberFormId值
        memberFormId_url=self.get_value_from_common_config(type,Bl_value.get_memberFormId())
        memberFormId=self.get_bl_value(memberFormId_url)
        # 获取schemaId值
        schemaId_url = self.get_value_from_common_config(type, Bl_value.get_dentifi_file_schemaId())
        schemaId = self.get_bl_value(schemaId_url)
        print schemaId
        # 获取url
        webinar_url=self.get_sql_common(type,Bl_value.get_webinar_instanceId())
        webinar_url=self.get_bl_value(webinar_url)
        print webinar_url
        flag,webinarId,instanceId=apicommon.get_webinarId_and_instanceId(type,webinar_url,bakSess,tenantId,memberFormId,schemaId,Bl_value.get_webinar_instanceId())
        if flag==0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_webinarId(), str(webinarId),Bl_value.get_webinarId())
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_webinarId_instanceId(), str(instanceId), Bl_value.get_webinarId_instanceId())
    # 获取customFormId
    def get_customFormId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取seminarId
        seminarId=self.get_value_from_bl(type,Bl_value.get_seminarId())
        seminarId = self.get_bl_value(seminarId)
        # 获取url
        customFormId_url=self.get_sql_common(type,Bl_value.get_customFormId())
        customFormId_url=self.get_bl_value(customFormId_url)
        flag,customFormId=apicommon.get_customFormId(type,customFormId_url,bakSess,tenantId,seminarId,Bl_value.get_customFormId())
        if flag==0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_customFormId_bl(), str(customFormId), Bl_value.get_customFormId_bl())
    # 线下会开启报名表单
    def get_open_offline_meetingthe_form(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取seminar_instanceId值
        seminarId_instanceId_SQL = self.get_value_from_bl(type, Bl_value.get_seminarId_instanceId())
        seminarId_instanceId = self.get_bl_value(seminarId_instanceId_SQL)
        # 获取customFormId值
        customFormId_SQL = self.get_value_from_bl(type, Bl_value.get_customFormId_bl())
        customFormId = self.get_bl_value(customFormId_SQL)
        # 获取url
        openform_url = self.get_sql_common(type, Bl_value.get_open_offline_meetingthe_form())
        openform_url = self.get_bl_value(openform_url)
        flag,openform_url,code = apicommon.get_open_offline_meetingthe_form(type, openform_url, bakSess, tenantId, seminarId_instanceId, customFormId, Bl_value.get_open_offline_meetingthe_form())
        if flag==0 and openform_url=="successful" and code==200:
            print "successful"
    # 获取问卷ID,questionid—wj
    def get_questionid(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        questionid_url = self.get_sql_common(type, Bl_value.get_questionid())
        questionid_url= self.get_bl_value(questionid_url)
        flag, questionid = apicommon.get_questionid(type, questionid_url, bakSess, tenantId,Bl_value.get_questionid())
        if flag == "0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_questionid(),str(questionid), Bl_value.get_questionid())
    # 获取guestId
    def get_guestId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        print "bakSess:",bakSess
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        guestId_url = self.get_sql_common(type, Bl_value.get_guestId())
        guestId_url = self.get_bl_value(guestId_url)
        flag, guestId = apicommon. get_guestId(type, guestId_url, bakSess, tenantId, Bl_value.get_guestId())
        if flag == "0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_guestId(), str(guestId),Bl_value.get_guestId())
    # 获取productLineId
    def get_productLineId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        productLineId_url = self.get_sql_common(type, Bl_value.get_productLineId())
        productLineId_url = self.get_bl_value(productLineId_url)
        flag, productLineId = apicommon.get_productLineId(type, productLineId_url, bakSess, tenantId, Bl_value.get_productLineId())
        if flag == "0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_productLineId(), str(productLineId), Bl_value.get_productLineId())
    # 获取webinarId_DianBo和webinar_instanceId_DianBo
    def get_webinarId_DianBo_and_webinar_instanceId_DianBo(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取schemaId值
        schemaId_url = self.get_value_from_common_config(type, Bl_value.get_dentifi_file_schemaId())
        schemaId = self.get_bl_value(schemaId_url)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        webinar_DianBo_url = self.get_sql_common(type, Bl_value.webinarId_DianBo())
        webinar_DianBo_url = self.get_bl_value(webinar_DianBo_url)
        print webinar_DianBo_url
        flag, webinarId_DianBo,webinar_instanceId_DianBo = apicommon.get_webinarId_DianBo_and_webinar_instanceId_DianBo(type, webinar_DianBo_url, bakSess, tenantId,schemaId,Bl_value.webinarId_DianBo())
        print "1:",webinarId_DianBo
        print "2:",webinar_instanceId_DianBo
        if flag == 0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.webinarId_DianBo(), str(webinarId_DianBo),Bl_value.webinarId_DianBo())
            self.Insert_Or_Update_Common_savebl(type, Bl_value.webinar_instanceId_DianBo(), str(webinar_instanceId_DianBo),Bl_value.webinar_instanceId_DianBo())
    # 线下会日程创建获取agendaId
    def get_agendaId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取seminarId
        seminarId = self.get_value_from_bl(type, Bl_value.get_seminarId())
        seminarId = self.get_bl_value(seminarId)
        # 获取url
        agendaId_url = self.get_sql_common(type, Bl_value.get_agendaId())
        agendaId_url = self.get_bl_value(agendaId_url)
        flag, agendaId = apicommon.get_agendaId(type, agendaId_url, bakSess, seminarId,Bl_value.get_agendaId())
        if flag == 0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_agendaId(), str(agendaId),Bl_value.get_agendaId())
    # 获取栏目ID,categoryId
    def get_categoryId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取nodeId值
        sql_nodeId = self.get_sql_nodeId(type)
        nodeId = self.get_nodeId_value(sql_nodeId)
        # 获取url
        categoryId_url = self.get_sql_common(type, Bl_value.get_categoryId())
        categoryId_url = self.get_bl_value(categoryId_url)
        flag, categoryId = apicommon.get_categoryId(type, categoryId_url, bakSess, tenantId, nodeId, Bl_value.get_categoryId())
        if flag == "0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_categoryId(), str(categoryId),Bl_value.get_categoryId())
    # 获取文件夹id，rootFileId
    def get_rootFileId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        fileId_url = self.get_sql_common(type, Bl_value.get_rootFileId())
        fileId_url = self.get_bl_value(fileId_url)
        flag, fileId = apicommon.get_rootFileId(type, fileId_url, bakSess, tenantId, Bl_value.get_rootFileId())
        if flag == "0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_rootFileId(), str(fileId), Bl_value.get_rootFileId())
    # 获取文件夹id，FolderId
    def get_FolderId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取rootFileId值
        rootFileId_sql=self.get_value_from_bl(type,Bl_value.get_rootFileId())
        rootFileId=self.get_bl_value(rootFileId_sql)
        # 获取FolderId的url
        FolderId_sql=self.get_sql_common(type,Bl_value.get_createFolderiD())
        FolderId_url=self.get_bl_value(FolderId_sql)
        flag,FolderId=apicommon.get_FolderId(type,FolderId_url,bakSess,tenantId,rootFileId,Bl_value.get_FolderId())
        if flag=="0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_FolderId(), str(FolderId), Bl_value.get_FolderId())
    # 获取pollId值
    def get_pollId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取pollId的url
        pollId_url=self.get_sql_common(type,Bl_value.get_pollId())
        pollId_url=self.get_bl_value(pollId_url)
        flag,pollId=apicommon.get_pollId(type,pollId_url,bakSess,tenantId,Bl_value.get_pollId())
        if flag=="0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_pollId(), str(pollId), Bl_value.get_pollId())
    # 获取邮件id,taskId
    def get_taskId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取nodeId值
        sql_nodeId = self.get_sql_nodeId(type)
        nodeId = self.get_nodeId_value(sql_nodeId)
        # 获取邮件任务的id
        taskId_SQL=self.get_sql_common(type,Bl_value.get_taskId())
        taskId_url=self.get_bl_value(taskId_SQL)
        flag,taskId=apicommon.get_taskId(type,taskId_url,bakSess,nodeId,Bl_value.get_taskId())
        if flag=="0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_taskId(), str(taskId), Bl_value.get_taskId())
    # 邮件填写内容
    def get_task_content(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取taskId
        taskId_SQL=self.get_value_from_bl(type,Bl_value.get_taskId())
        taskId=self.get_bl_value(taskId_SQL)
        # 获取url
        task_updateContent_sql=self.get_sql_common(type,Bl_value.get_task_updateContent())
        task_updateContent_url=self.get_bl_value(task_updateContent_sql)
        flag,succ=apicommon.get_task_content(type,task_updateContent_url,bakSess,taskId,Bl_value.get_task_updateContent())
        if flag=="0":
            print succ
    # 获取自定义通用表单id
    def get_registerFormId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        registerFormId_sql=self.get_sql_common(type,Bl_value.get_registerFormId())
        registerFormId_url=self.get_bl_value(registerFormId_sql)
        flag,registerFormId=apicommon.get_registerFormId(type,registerFormId_url,bakSess,tenantId,Bl_value.get_registerFormId())
        if flag=="0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_registerFormId(), str(registerFormId), Bl_value.get_registerFormId())
    # 获取随机试卷id
    def get_question_sjsj(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取随机试卷的url
        questionid_sjsj_sql=self.get_sql_common(type,Bl_value.get_questionid_sjsj())
        questionid_sjsj_utl=self.get_bl_value(questionid_sjsj_sql)
        flag,questionid_sjsj,code=apicommon.get_questionid_sjsj(type,questionid_sjsj_utl,bakSess,tenantId,Bl_value.get_questionid_sjsj())
        if flag==0 and code==200:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_questionid_sjsj(), str(questionid_sjsj),Bl_value.get_questionid_sjsj())
    # 线下会报名表单开启按钮
    def get_seminar_customForm_start(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取seminar_instanceId
        seminarId_instanceId_sql=self.get_value_from_bl(type,Bl_value.get_seminarId_instanceId())
        seminarId_instanceId=self.get_bl_value(seminarId_instanceId_sql)
        print "seminarId_instanceId：",seminarId_instanceId
        # 获取customFormId
        customFormId_sql=self.get_value_from_bl(type,Bl_value.get_customFormId_bl())
        customFormId=self.get_bl_value(customFormId_sql)
        # 获取url
        customForm_sql=self.get_sql_common(type,Bl_value.get_seminar_customForm_start())
        customForm_url=self.get_bl_value(customForm_sql)
        flag,secc,code=apicommon.get_seminar_customForm_start(type,customForm_url,bakSess,tenantId,seminarId_instanceId,customFormId,Bl_value.get_seminar_customForm_start())
        if flag==0 and code==200:
            print secc
    # 线下会报名接口
    def get_customForm_action(self, type):
        # 获取loginSess
        sql_loginSess = self.get_value_from_bl(type, Bl_value.get_login_name())
        loginSess = self.get_bl_value(sql_loginSess)
        # 获取customFormId
        customFormId_sql = self.get_value_from_bl(type, Bl_value.get_customFormId_bl())
        customFormId = self.get_bl_value(customFormId_sql)
        # 获取seminar_instanceId值
        seminarId_instanceId_SQL = self.get_value_from_bl(type, Bl_value.get_seminarId_instanceId())
        seminarId_instanceId = self.get_bl_value(seminarId_instanceId_SQL)
        # 获取url
        customForm_action_sql = self.get_sql_common(type, Bl_value.get_customForm_action())
        customForm_action_url = self.get_bl_value(customForm_action_sql)
        flag, secc,code = apicommon.get_customForm_action(type, customForm_action_url, loginSess, customFormId,seminarId_instanceId, Bl_value.get_customForm_action())
        if flag == 0 and code==200:
            print secc
    # 获取参会人员信息,contactId
    def get_contactId(self, type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取seminar_instanceId值
        seminarId_instanceId_SQL = self.get_value_from_bl(type, Bl_value.get_seminarId_instanceId())
        seminarId_instanceId = self.get_bl_value(seminarId_instanceId_SQL)
        # 获取seminarId
        seminarId = self.get_value_from_bl(type, Bl_value.get_seminarId())
        seminarId = self.get_bl_value(seminarId)
        # 获取url
        contactId_url = self.get_sql_common(type, Bl_value.get_contactId())
        contactId_url = self.get_bl_value(contactId_url)
        flag, contactId = apicommon.get_contactId(type, contactId_url, bakSess, tenantId, seminarId_instanceId,seminarId, Bl_value.get_contactId())
        if flag == 0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_contactId(), str(contactId),Bl_value.get_contactId())
    # 将参会人设置为普通参会人员，之后才可以创建签到大屏，第一步
    # 将参会人设置未普通参会人员，之后创建签到大屏
    def contact_isSignUp(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取seminar_instanceId值
        seminarId_instanceId_SQL = self.get_value_from_bl(type, Bl_value.get_seminarId_instanceId())
        seminarId_instanceId = self.get_bl_value(seminarId_instanceId_SQL)
        # 获取seminarId
        seminarId = self.get_value_from_bl(type, Bl_value.get_seminarId())
        seminarId = self.get_bl_value(seminarId)
        # 获取url
        contactId_url = self.get_sql_common(type, Bl_value.get_ptcontact_one())
        contactId_url = self.get_bl_value(contactId_url)
        # 获取参会人id值
        contactId_SQL = self.get_value_from_bl(type, Bl_value.get_contactId())
        contactId = self.get_bl_value(contactId_SQL)
        flag, contactId = apicommon.contact_isSignUp(type, contactId_url, bakSess, tenantId, seminarId_instanceId,
                                                  seminarId, Bl_value.get_contactId(), contactId)
        if flag == 0:
            print contactId
    def set_contract_items(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取seminar_instanceId值
        seminarId_instanceId_SQL = self.get_value_from_bl(type, Bl_value.get_seminarId_instanceId())
        seminarId_instanceId = self.get_bl_value(seminarId_instanceId_SQL)
        # 获取seminarId
        seminarId = self.get_value_from_bl(type, Bl_value.get_seminarId())
        seminarId = self.get_bl_value(seminarId)
        # 获取参会人id
        contactId_SQL=self.get_value_from_bl(type,Bl_value.get_contactId())
        contactId = self.get_bl_value(contactId_SQL)
        # 获取url
        contactId_url = self.get_sql_common(type, Bl_value.get_contactId_set())
        contactId_url = self.get_bl_value(contactId_url)
        flag, contactId = apicommon.set_contactId(type, contactId_url, bakSess, tenantId, seminarId_instanceId,
                                                  seminarId, Bl_value.get_contactId(),contactId)
        if flag == 0:
            print contactId
    # 设置问卷选项,questionarywj_setItems
    def get_questionarywj_setItems(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取questionid—sjsj值
        questionid_sjsj_SQL = self.get_value_from_bl(type, Bl_value.get_questionid_sjsj())
        questionid_sjsj = self.get_bl_value(questionid_sjsj_SQL)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        questionarywj_setItems_sql = self.get_sql_common(type, Bl_value.get_questionarywj_setItems())
        questionarywj_setItems_url = self.get_bl_value(questionarywj_setItems_sql)
        flag, secc,code = apicommon.get_questionarywj_setItems(type, questionarywj_setItems_url, bakSess, questionid_sjsj,tenantId, Bl_value.get_questionarywj_setItems())
        if flag == 0 and code==200:
            print secc
    # 获取问卷选项item值,questionarywj_get
    def get_questionarywj_get(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取questionid—sjsj值
        questionid_sjsj_SQL = self.get_value_from_bl(type, Bl_value.get_questionid_sjsj())
        questionid_sjsj = self.get_bl_value(questionid_sjsj_SQL)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        questionarywj_get_url = self.get_sql_common(type, Bl_value.get_questionarywj_get())
        questionarywj_get_url = self.get_bl_value(questionarywj_get_url)
        flag, questionid_item = apicommon.get_questionid_item(type, questionarywj_get_url, bakSess, questionid_sjsj, tenantId,Bl_value.get_questionid_item())
        if flag == "0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_questionid_item(), str(questionid_item),Bl_value.get_questionid_item())
    # 获取questionid—sj试卷
    def get_questionid_sj(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        questionid_sj_url = self.get_sql_common(type, Bl_value.get_questionid_sj())
        questionid_sj_url = self.get_bl_value(questionid_sj_url)
        flag, questionid_item = apicommon.get_questionid_sj(type, questionid_sj_url, tenantId,bakSess,  Bl_value.get_questionid_sj())
        if flag=="0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_questionid_sj(), str(questionid_item),Bl_value.get_questionid_sj())
    # 获取字典值id和字典名称
    def get_dicId_and_dicname(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        dic_sql=self.get_sql_common(type,Bl_value.get_dicId_and_dicname())
        dic_url=self.get_bl_value(dic_sql)
        flag,dicId,name=apicommon.get_dicId_dicname(type,dic_url,tenantId,bakSess,Bl_value.get_dicId_and_dicname())
        if flag=="0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_dicId_and_dicname(), str(dicId),Bl_value.get_dicId_and_dicname())
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_dicname(), name,Bl_value.get_dicname())
    # 获取评论区id
    # 获取门禁多次签到接口的通道值passagesId
    def get_passagesId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取seminarId值
        seminarId_SQL = self.get_value_from_bl(type, Bl_value.get_seminarId())
        seminarId = self.get_bl_value(seminarId_SQL)
        # 获取seminar_instanceId
        seminarId_instanceId_sql = self.get_value_from_bl(type, Bl_value.get_seminarId_instanceId())
        seminarId_instanceId = self.get_bl_value(seminarId_instanceId_sql)
        # 获取url
        passagesId_sql = self.get_sql_common(type, Bl_value.get_passagesId())
        passagesId_url = self.get_bl_value(passagesId_sql)
        flag, passagesId,code = apicommon.get_passagesId(type, passagesId_url, bakSess,tenantId,seminarId,seminarId_instanceId,Bl_value.get_passagesId())
        if flag == 0 and code==200:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_passagesId(),str(passagesId),Bl_value.get_passagesId())
    # 文件夹内上传图片
    def get_file_upload(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取url
        file_upload_sql = self.get_sql_common(type, Bl_value.get_file_upload())
        file_upload_url = self.get_bl_value(file_upload_sql)
        flag, file_upload = apicommon.get_file_upload(type,file_upload_url,bakSess,Bl_value.get_file_upload())
        print file_upload
        if flag == "0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_file_mappingId(),str(file_upload),Bl_value.get_file_mappingId())

    # 微讨论下面的帖子id-postId的接口
    def get_forum_post_postId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取nodeId值
        sql_nodeId = self.get_sql_nodeId(type)
        nodeId = self.get_nodeId_value(sql_nodeId)
        # 获取global_topicId值
        sql_global_topicId = self.get_value_from_bl(type, Bl_value.get_global_topicId())
        global_topicId = self.get_bl_value(sql_global_topicId)
        # 获取url
        forum_post_postId_sql=self.get_sql_common(type,Bl_value.get_forum_post_postId())
        forum_post_postId_url=self.get_bl_value(forum_post_postId_sql)
        flag,postId=apicommon.get_forum_post_postId(type,forum_post_postId_url,bakSess,tenantId,nodeId,global_topicId,Bl_value.get_forum_post_postId())
        if flag == "0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_postId(), str(postId),Bl_value.get_postId())
    # 获取评论区id
    def get_PLQId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取nodeId值
        sql_nodeId = self.get_sql_nodeId(type)
        nodeId = self.get_nodeId_value(sql_nodeId)
        # 获取评论区id的url
        PLQID_sql=self.get_sql_common(type,Bl_value.get_PLQID())
        PLQID_url=self.get_bl_value(PLQID_sql)
        print "PLQID_url:",PLQID_url
        flag,PLQID=apicommon.get_PLQID(type,PLQID_url,tenantId,bakSess,nodeId,Bl_value.get_PLQID())
        if flag == "0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_PLQID(), str(PLQID),Bl_value.get_PLQID())

    # 试卷 - 跳转到结果页保存按钮
    def sj_save(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取试卷id
        questionid_sj_sql=self.get_value_from_bl(type,Bl_value.get_questionid_sj())
        questionid_sj=self.get_bl_value(questionid_sj_sql)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        questionary_update_sql=self.get_sql_common(type,Bl_value.get_questionary_update())
        questionary_update_url=self.get_bl_value(questionary_update_sql)
        flag,succ=apicommon.get_questionary_update(type,questionary_update_url,tenantId,bakSess,questionid_sj,Bl_value.get_questionary_update())
        if flag=="0":
            print succ
    # 获取线下会分会场id
    def get_subSeminarId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取seminarId值
        seminarId_SQL = self.get_value_from_bl(type, Bl_value.get_seminarId())
        seminarId = self.get_bl_value(seminarId_SQL)
        # 获取urll
        subSeminarId_sql=self.get_sql_common(type,Bl_value.get_subSeminarId())
        subSeminarId_url=self.get_bl_value(subSeminarId_sql)
        flag,subSeminarId,code=apicommon.get_subSeminarId(type,subSeminarId_url,tenantId,bakSess,seminarId,Bl_value.get_subSeminarId())
        if flag==0 and code==200:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_subSeminarId(), str(subSeminarId), Bl_value.get_subSeminarId())
    # 试卷添加题目
    def questionarysj_setItems(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取试卷id
        questionid_sj_sql = self.get_value_from_bl(type, Bl_value.get_questionid_sj())
        questionid_sj = self.get_bl_value(questionid_sj_sql)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        questionarysj_setItems_sql=self.get_sql_common(type,Bl_value.get_questionarysj_setItems())
        questionarysj_setItems_url=self.get_bl_value(questionarysj_setItems_sql)
        flag,succ=apicommon.get_questionarysj_setItems(type,questionarysj_setItems_url,tenantId,bakSess,questionid_sj,Bl_value.get_questionarysj_setItems())
        if flag=="0":
            print succ
    # 获取文章id
    def get_articleId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        articleId_sql=self.get_sql_common(type,Bl_value.get_articleCategoryId())
        articleId_url=self.get_bl_value(articleId_sql)
        flag,articleCategoryId=apicommon.get_articleCategoryId(type,articleId_url,tenantId,bakSess,tenantId,Bl_value.get_articleCategoryId())
        if flag=="0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_articleCategoryId(), str(articleCategoryId), Bl_value.get_articleCategoryId())
    # 文件夹内获取上传图片的文件id  156
    def get_file_create(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取seminar_instanceId
        seminarId_instanceId_sql = self.get_value_from_bl(type, Bl_value.get_seminarId_instanceId())
        seminarId_instanceId = self.get_bl_value(seminarId_instanceId_sql)
        # 获取FolderId
        FolderId_sql = self.get_value_from_bl(type, Bl_value.get_FolderId())
        FolderId = self.get_bl_value(FolderId_sql)
        # 获取url
        file_create_sql = self.get_sql_common(type, Bl_value.get_file_create())
        file_create_url = self.get_bl_value(file_create_sql)
        flag, file_create = apicommon.get_file_create(type, file_create_url, bakSess, tenantId,seminarId_instanceId,FolderId,Bl_value.get_file_create())
        if flag == "0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_fileId(), str(file_create),Bl_value.get_fileId())
    # 获取留言板的主贴id
    def get_LYBZTId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取nodeId值
        sql_nodeId = self.get_sql_nodeId(type)
        nodeId = self.get_nodeId_value(sql_nodeId)
        # 获取topicId
        topicId_sql = self.get_value_from_bl(type, Bl_value.get_topicId())
        topicId = self.get_bl_value(topicId_sql)
        # 获取url
        LYBZTId_sql = self.get_sql_common(type, Bl_value.get_LYBZTId())
        LYBZTId_url = self.get_bl_value(LYBZTId_sql)
        flag, LYBZTId = apicommon.get_LYBZTId(type,LYBZTId_url,bakSess,tenantId,nodeId,topicId,Bl_value.get_LYBZTId())
        if flag == "0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_LYBZTId(), str(LYBZTId), Bl_value.get_LYBZTId())
    # 获取只有姓名和手机的表单id
    def get_customFormid_nameand_phone(self, type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        customFormid_nameand_phone_sql = self.get_sql_common(type, Bl_value.get_customForm_nameand_phone())
        customFormid_nameand_phone_url = self.get_bl_value(customFormid_nameand_phone_sql)
        flag, customFormid_nameand_phone = apicommon.get_customFormid_nameand_phone(type, customFormid_nameand_phone_url,bakSess, tenantId,Bl_value.get_customFormid_nameand_phone())
        if flag == "0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_customFormid_nameand_phone(),str(customFormid_nameand_phone),Bl_value.get_customFormid_nameand_phone())
    # 获取自定义注册表单id
    def get_zdyresterFormId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        zdyresterFormId_sql = self.get_sql_common(type, Bl_value.get_zdyresterFormId())
        zdyresterFormId_url = self.get_bl_value(zdyresterFormId_sql)
        # 获取schemaId
        schemaId_sql=self.get_value_from_common_config(type,Bl_value.get_dentifi_file_schemaId())
        schemaId=self.get_bl_value(schemaId_sql)
        print "zdyresterFormId_url:",zdyresterFormId_url
        flag, zdyresterFormId = apicommon.get_zdyresterFormId(type,zdyresterFormId_url,bakSess,tenantId,schemaId,Bl_value.get_zdyresterFormId())
        if flag == "0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_zdyresterFormId(),str(zdyresterFormId),Bl_value.get_zdyresterFormId())
    # 获取标签属性值
    def get_tag_field_getList(self, type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        tag_field_getList_sql = self.get_sql_common(type, Bl_value.get_tag_field_getList())
        tag_field_getList_url = self.get_bl_value(tag_field_getList_sql)
        flag, tagSchemaId, tagFieldId, fieldName, displayName, tagId = apicommon.get_tag_field_getList(type,tag_field_getList_url,bakSess,tenantId,Bl_value.get_tag_field_getList())
        if flag == "0":
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_tagSchemaId(), str(tagSchemaId),Bl_value.get_tagSchemaId())
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_tagFieldId(), str(tagFieldId),Bl_value.get_tagFieldId())
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_fieldName(), str(fieldName),Bl_value.get_fieldName())
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_displayName(), str(displayName),Bl_value.get_displayName())
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_tagId(), str(tagId), Bl_value.get_tagId())
    # 往线上会点播创建视频
    def test_webinarb_create_video(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        tag_field_getList_sql = self.get_sql_common(type, Bl_value.get_create_video())
        tag_field_getList_url = self.get_bl_value(tag_field_getList_sql)
        # 获取点播id
        video_sql = self.get_value_from_bl(type, Bl_value.webinarId_DianBo())
        video = self.get_bl_value(video_sql)
        flag,desc,code= apicommon.get_create_video(type,tag_field_getList_url,bakSess,video,tenantId,Bl_value.get_create_video())
        if flag == 0 and code==200:
            print desc
    # 往线上会点播获取视频id值
    def test_webinarb_videoId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取url
        tag_field_getList_sql = self.get_sql_common(type, Bl_value.get_input_video())
        tag_field_getList_url = self.get_bl_value(tag_field_getList_sql)
        # 获取点播id
        video_sql = self.get_value_from_bl(type, Bl_value.webinarId_DianBo())
        video = self.get_bl_value(video_sql)
        # 获取点播instanceId
        video_instanceId_sql = self.get_value_from_bl(type, Bl_value.webinar_instanceId_DianBo())
        video_instanceId = self.get_bl_value(video_instanceId_sql)
        flag, desc = apicommon.get_videoId(type, tag_field_getList_url, bakSess, video, tenantId,Bl_value.get_input_video(),video_instanceId)
        if flag == 0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_videoId(), str(desc),Bl_value.get_videoId())
    # 获取文章id
    def test_get_articleId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取nodeId值
        sql_nodeId = self.get_sql_nodeId(type)
        nodeId = self.get_nodeId_value(sql_nodeId)
        # 获取articleCategoryId值
        articleCategoryId_sql = self.get_value_from_bl(type, Bl_value.get_articleCategoryId())
        articleCategoryId = self.get_bl_value(articleCategoryId_sql)
        # 获取url
        articleId_sql = self.get_sql_common(type, Bl_value.get_articleId())
        articleId_url = self.get_bl_value(articleId_sql)
        flag, articleId= apicommon.get_articleId(type, articleId_url, bakSess,articleCategoryId, tenantId,nodeId)
        if flag == 0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_articleId(), str(articleId),Bl_value.get_articleId())
    # 获取线上会报名表单id
    def get_webinar_BMFormId(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取articleCategoryId值
        webinarId_instanceId_sql = self.get_value_from_bl(type, Bl_value.get_webinarId_instanceId())
        webinarId_instanceId = self.get_bl_value(webinarId_instanceId_sql)
        # 获取url
        articleId_sql = self.get_sql_common(type, Bl_value.get_webinar_BMFormId())
        articleId_url = self.get_bl_value(articleId_sql)
        # 获取schemaId
        schemaId_sql = self.get_value_from_common_config(type, Bl_value.get_dentifi_file_schemaId())
        schemaId = self.get_bl_value(schemaId_sql)
        # 获取memberFormId值
        memberFormId_url = self.get_value_from_common_config(type, Bl_value.get_memberFormId())
        memberFormId = self.get_bl_value(memberFormId_url)
        flag, articleId = apicommon.get_webinar_BMFormId(type, articleId_url, bakSess, webinarId_instanceId, tenantId,schemaId,memberFormId)
        if flag == 0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_webinar_BMFormId(), str(articleId),Bl_value.get_webinar_BMFormId())
    # 获取线上会的互动设置的问卷id
    def get_webinar_question_wj(self,type):
        # 获取bakSess值
        sql_bakSess = self.get_bakSess_url(type)
        bakSess = self.get_bakSess(sql_bakSess)
        # 获取tenantId值
        sql_tenantId = self.get_sql_tenantId_value(type)
        tenantId = self.get_tenantId_value(sql_tenantId)
        # 获取webinarId_instanceId值
        webinarId_instanceId_sql = self.get_value_from_bl(type, Bl_value.get_webinarId_instanceId())
        webinarId_instanceId = self.get_bl_value(webinarId_instanceId_sql)
        # 获取url
        articleId_sql = self.get_sql_common(type, Bl_value.get_webinar_question_wj())
        articleId_url = self.get_bl_value(articleId_sql)
        # 获取schemaId
        schemaId_sql = self.get_value_from_common_config(type, Bl_value.get_schemaId())
        schemaId = self.get_bl_value(schemaId_sql)
        print "schemaID:",schemaId
        # 获取注册表单id
        registerFormId_sql = self.get_value_from_bl(type, Bl_value.get_registerFormId())
        registerFormId = self.get_bl_value(registerFormId_sql)
        flag, articleId,code = apicommon.get_webinar_question_wj(type, articleId_url, bakSess, webinarId_instanceId, tenantId,schemaId,registerFormId)
        if flag == 0 and code==200:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_webinar_question_wj(), str(articleId),Bl_value.get_webinar_question_wj())
if __name__ == '__main__':
    # Api_Common_All().get_login_account_url(u"HW")
    # Api_Common_All().get_menber_login_url(u"HW")
    # Api_Common_All().get_global_topicId(u"HW")
    # Api_Common_All().get_sectionId(u"HW")
    # Api_Common_All().get_topicId(u"HW")
    # Api_Common_All().get_seminarid_And_instanceid(u"HW")
    # Api_Common_All().get_passageId(u"HW")
    Api_Common_All().get_luckyDrawId(u"HW_UAT")
    Api_Common_All().set_luckyDraw_Items(u'HW_UAT')
    # Api_Common_All().get_signingPointId(u"HW")
    # Api_Common_All().get_bigScreen_templateId(u"HW")
    # Api_Common_All().get_bigScreen_configId(u"HW")
    # Api_Common_All().get_signingPointIds(u"HW")
    # Api_Common_All().get_bigScreenId(u"HW")
    # Api_Common_All().get_bigScreenId(u"HW")   重复
    # Api_Common_All().get_productLine(u"HW")
    # Api_Common_All().get_webinarId_and_instanceid(u"HW")
    # Api_Common_All().get_customFormId(u"HW")
    # Api_Common_All().get_open_offline_meetingthe_form(u"HW")
    # Api_Common_All().get_questionid(u"HW")
    # Api_Common_All().get_guestId(u"HW")
    # Api_Common_All().get_productLineId(u"HW")
    # Api_Common_All().get_webinarId_DianBo_and_webinar_instanceId_DianBo(u"HW")
    # Api_Common_All().get_agendaId(u"HW")
    # Api_Common_All().get_categoryId(u"S2")
    # Api_Common_All().get_rootFileId(u"S2")
    # Api_Common_All().get_FolderId(u"S2")
    # Api_Common_All().get_pollId(u"S2")
    # Api_Common_All().get_taskId(u"S2")
    # Api_Common_All().get_task_content(u"S2")
    # Api_Common_All().get_registerFormId(u"S2")
    # Api_Common_All().get_question_sjsj(u"HW_UAT")
    # Api_Common_All().get_seminar_customForm_start(u"HW")  #有问题
    # Api_Common_All().get_customForm_action(u"HW")
    # Api_Common_All().get_contactId(u"HW")
    # Api_Common_All().get_questionarywj_setItems(u"HW_UAT")
    # Api_Common_All().get_questionarywj_get(u"S2")
    # Api_Common_All().get_questionid_sj(u"S2")
    # Api_Common_All().get_dicId_and_dicname(u"S2")
    # Api_Common_All().get_passagesId(u"HW")
    # Api_Common_All().get_file_upload(u"S2")
    # Api_Common_All().get_forum_post_postId(u"S2")
    # Api_Common_All().get_PLQId(u"S2")
    # Api_Common_All().sj_save(u"S2")
    # Api_Common_All().get_subSeminarId(u"HW")
    # Api_Common_All().semain_setModule(u'HW')
    # Api_Common_All().questionarysj_setItems(u"S2")
    # Api_Common_All().get_articleId(u"S2")
    # Api_Common_All().get_file_create(u"S2")
    # Api_Common_All().get_LYBZTId(u"S2")
    # Api_Common_All().get_customFormid_nameand_phone(u"S2")
    # Api_Common_All().get_zdyresterFormId(u"S2")
    # Api_Common_All().get_tag_field_getList(u"S2")
    # Api_Common_All().test_webinarb_create_video(u"HW_UAT")
    # Api_Common_All().test_webinarb_videoId(u"HW_UAT")
    # Api_Common_All().test_get_articleId(u'HW_UAT')
    # Api_Common_All().get_webinar_BMFormId(u'HW_UAT')
    # Api_Common_All().get_webinar_question_wj(u'HW_UAT')
    # Api_Common_All().contact_isSignUp(u'HW_UAT')
    # Api_Common_All().set_contract_items(u'HW_UAT')