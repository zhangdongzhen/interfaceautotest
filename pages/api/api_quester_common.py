#-*-encoding:utf-8 -*-
"""
@version:1
@author:刘雅
@file:api_quester_common.py
@time:2019/1/149:46
"""
import requests
import json
import time
from common.common_function.Read_From_Mysql import Read_From_Mysql
import common.common_function.globalvar as gl
class api_quester_common():
    # 获取session专用
    # def post_request(self,type,url,payload,headers,Identifi_field,platform_name):
    #     try:
    #         self.response=requests.request(type,url, data=payload, headers=headers)
    #         self.response_text=self.response.text
    #         self.code=self.response.status_code
    #         json_text=self.response.json()
    #         session=json_text["body"]["content"]["session"]
    #         print "成功"
    #         return "0",session
    #     except:
    #         print "失败"
    #         createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #         print "self.response_text:",self.response_text
    #         response_text = self.response_text.replace("\"", "\\\"")
    #         print "response_text:",response_text
    #         payload=payload.replace("\"", "\\\"")
    #         print "payload:",payload
    #         print "Identifi_field:",Identifi_field
    #         sql="insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field) " \
    #             "values('"+platform_name+"','"+createTime+"','"+url+"','"+response_text+"','"+str(self.code)+"','"+payload+"','"+Identifi_field+"')"
    #         Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
    #         return "1","异常"
    # 获取平常接口的问题
    def post_request_acture(self,type,url,payload,headers,Identifi_field,platform_name):
        try:
            self.response=requests.request(type,url, data=payload, headers=headers)
            self.response_text=self.response.text
            self.code=self.response.status_code
            json_text=self.response.json()
            session=json_text["body"]["content"]
            print "成功"
            return "0",session
        except:
            print "失败"
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "self.response_text:",self.response_text
            response_text = self.response_text.replace("\"", "\\\"")
            print "response_text:",response_text
            payload=payload.replace("\"", "\\\"")
            print "payload:",payload
            print "Identifi_field:",Identifi_field
            sql="insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field) " \
                "values('"+platform_name+"','"+createTime+"','"+url+"','"+response_text+"','"+str(self.code)+"','"+payload+"','"+Identifi_field+"')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1","异常"
    # 获取线下会的seminarId和instanceId
    def post_request_seminarId(self, type, url, payload, headers, Identifi_field, platform_name,flag1,flag2):
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.response_text = self.response.text
            self.code = self.response.status_code
            json_text = self.response.json()
            seminarId = json_text["body"]["content"][flag1]
            instanceId = json_text["body"]["content"][flag2]
            result=json_text["body"]["result"]
            return result, seminarId,instanceId
        except:
            print "失败"
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "self.response_text:", self.response_text
            response_text = self.response_text.replace("\"", "\\\"")
            print "response_text:", response_text
            payload = payload.replace("\"", "\\\"")
            print "payload:", payload
            print "Identifi_field:", Identifi_field
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + response_text + "','" + str(
                self.code) + "','" + payload + "','" + Identifi_field +  "','" + serialnum + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常",""
            # 获取线下会的seminarId和instanceId
    # 获取passageId值
    def post_request_passageId(self, type, url, payload, headers, Identifi_field, platform_name,canshu):
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.response_text = self.response.text
            self.code = self.response.status_code
            json_text = self.response.json()
            passageId = json_text["body"]["content"][0]["items"][0]["passages"][0][canshu]
            result = json_text["body"]["result"]
            return result, passageId
        except:
            print "失败"
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "self.response_text:", self.response_text
            response_text = self.response_text.replace("\"", "\\\"")
            print "response_text:", response_text
            payload = payload.replace("\"", "\\\"")
            print "payload:", payload
            print "Identifi_field:", Identifi_field
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + response_text + "','" + str(
                self.code) + "','" + payload + "','" + Identifi_field +  "','" + serialnum + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常"
    # 获取passageId值
    # def post_request_luckyDrawId(self, type, url, payload, headers, Identifi_field, platform_name):
    #     try:
    #         self.response = requests.request(type, url, data=payload, headers=headers)
    #         self.response_text = self.response.text
    #         self.code = self.response.status_code
    #         json_text = self.response.json()
    #         luckyDrawId = json_text["body"]["content"]["luckyDrawId"]
    #         print "成功"
    #         return "0", luckyDrawId
    #     except:
    #         print "失败"
    #         createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #         print "self.response_text:", self.response_text
    #         response_text = self.response_text.replace("\"", "\\\"")
    #         print "response_text:", response_text
    #         payload = payload.replace("\"", "\\\"")
    #         print "payload:", payload
    #         print "Identifi_field:", Identifi_field
    #         sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field) " \
    #               "values('" + platform_name + "','" + createTime + "','" + url + "','" + response_text + "','" + str(
    #             self.code) + "','" + payload + "','" + Identifi_field + "')"
    #         Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
    #         return "1", "异常"
    # 获取signingPointId
    # 获取passageId值
    def post_request_signingPointId(self, type, url, payload, headers, Identifi_field, platform_name,canshu):
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.response_text = self.response.text
            self.code = self.response.status_code
            json_text = self.response.json()
            signingPointId = json_text["body"]["content"][0]["items"][0][canshu]
            result=json_text["body"]["result"]
            return result, signingPointId
        except:
            print "失败"
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "self.response_text:", self.response_text
            response_text = self.response_text.replace("\"", "\\\"")
            print "response_text:", response_text
            payload = payload.replace("\"", "\\\"")
            print "payload:", payload
            print "Identifi_field:", Identifi_field
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + response_text + "','" + str(
                self.code) + "','" + payload + "','" + Identifi_field +  "','" + serialnum + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常"
        # 获取bigScreen_templateId

    def post_request_bigScreen_templateId(self, type, url, payload, headers, Identifi_field, platform_name):
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.response_text = self.response.text
            self.code = self.response.status_code
            json_text = self.response.json()
            templates0 = json_text["body"]["content"]["templates"][0]["templateId"]
            result = json_text["body"]["result"]
            return result, templates0
        except:
            print "失败"
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "self.response_text:", self.response_text
            response_text = self.response_text.replace("\"", "\\\"")
            print "response_text:", response_text
            payload = payload.replace("\"", "\\\"")
            print "payload:", payload
            print "Identifi_field:", Identifi_field
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + response_text + "','" + str(
                self.code) + "','" + payload + "','" + Identifi_field +  "','" + serialnum + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常"
    # 获取bigScreen_templateId

    def post_request_bigScree(self, type, url, payload, headers, Identifi_field, platform_name,canshu):
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.response_text = self.response.text
            self.code = self.response.status_code
            json_text = self.response.json()
            templates0 = json_text["body"]["content"][canshu]
            result = json_text["body"]["result"]
            return result, templates0
        except:
            print "失败"
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "self.response_text:", self.response_text
            response_text = self.response_text.replace("\"", "\\\"")
            print "response_text:", response_text
            payload = payload.replace("\"", "\\\"")
            print "payload:", payload
            print "Identifi_field:", Identifi_field
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + response_text + "','" + str(
                self.code) + "','" + payload + "','" + Identifi_field +  "','" + serialnum + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常"
    # 获取customFormId
    def post_request_get_customFormId(self, type, url, payload, headers, Identifi_field, platform_name,canshu):
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.response_text = self.response.text
            self.code = self.response.status_code
            json_text = self.response.json()
            templates0 = json_text["body"]["content"][canshu]
            result = json_text["body"]["result"]
            return result, templates0
        except:
            print "失败"
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "self.response_text:", self.response_text
            response_text = self.response_text.replace("\"", "\\\"")
            print "response_text:", response_text
            payload = payload.replace("\"", "\\\"")
            print "payload:", payload
            print "Identifi_field:", Identifi_field
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + response_text + "','" + str(
                self.code) + "','" + payload + "','" + Identifi_field + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常"

    # 获取customFormId
    def post_request_get_registerFormId(self, type, url, payload, headers, Identifi_field, platform_name, canshu):
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.response_text = self.response.text
            self.code = self.response.status_code
            json_text = self.response.json()
            templates0 = json_text["body"]["content"][0][canshu]
            result = json_text["body"]["result"]
            return result, templates0
        except:
            print "失败"
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "self.response_text:", self.response_text
            response_text = self.response_text.replace("\"", "\\\"")
            print "response_text:", response_text
            payload = payload.replace("\"", "\\\"")
            print "payload:", payload
            print "Identifi_field:", Identifi_field
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + response_text + "','" + str(
                self.code) + "','" + payload + "','" + Identifi_field + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常"
    #开启线下会报名表单
    def post_request_successful(self, type, url, payload, headers, Identifi_field, platform_name, flag1):
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.response_text = self.response.text
            print "response_text:",self.response_text
            self.code = self.response.status_code
            json_text = self.response.json()
            seminarId = json_text["body"][flag1]
            result = json_text["body"]["result"]
            return result, seminarId,self.code
        except:
            print "失败"
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "self.response_text:", self.response_text
            response_text = self.response_text.replace("\"", "\\\"")
            print "response_text:", response_text
            payload = payload.replace("\"", "\\\"")
            print "payload:", payload
            print "Identifi_field:", Identifi_field
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + response_text + "','" + str(
                self.code) + "','" + payload + "','" + Identifi_field +  "','" + serialnum + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常",0
            # 获取passageId值
    # 获取productLineId
    def post_request_productLineId(self, type, url, payload, headers, Identifi_field, platform_name,flag1):
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.response_text = self.response.text
            self.code = self.response.status_code
            json_text = self.response.json()
            productLineId = json_text["body"]["content"]["items"][0][flag1]
            result = json_text["body"]["result"]
            return result, productLineId
        except:
            print "失败"
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "self.response_text:", self.response_text
            response_text = self.response_text.replace("\"", "\\\"")
            print "response_text:", response_text
            payload = payload.replace("\"", "\\\"")
            print "payload:", payload
            print "Identifi_field:", Identifi_field
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + response_text + "','" + str(
                self.code) + "','" + payload + "','" + Identifi_field +  "','" + serialnum + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常"


    # 传参两个，返回值两个
    def post_request_intwo_outtwo(self, type, url, payload, headers, Identifi_field, platform_name,flag1,flag2):
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.response_text = self.response.text
            self.code = self.response.status_code
            json_text = self.response.json()
            seminarId = json_text["body"]["content"]["items"][0][flag1]
            instanceId = json_text["body"]["content"]["items"][0][flag2]
            result = json_text["body"]["result"]
            return result, seminarId,instanceId
        except:
            print "失败"
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "self.response_text:", self.response_text
            response_text = self.response_text.replace("\"", "\\\"")
            print "response_text:", response_text
            payload = payload.replace("\"", "\\\"")
            print "payload:", payload
            print "Identifi_field:", Identifi_field
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + response_text + "','" + str(
                self.code) + "','" + payload + "','" + Identifi_field +  "','" + serialnum + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常"
    #获取门禁多次签到接口的通道值
    def post_request_passagesId(self, type, url, payload, headers, Identifi_field, platform_name,flag):
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.response_text = self.response.text
            self.code = self.response.status_code
            json_text = self.response.json()
            seminarId = json_text["body"]["content"][0]["items"][1]["passages"][flag]
            result = json_text["body"]["result"]
            return result, seminarId
        except:
            print "失败"
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "self.response_text:", self.response_text
            response_text = self.response_text.replace("\"", "\\\"")
            print "response_text:", response_text
            payload = payload.replace("\"", "\\\"")
            print "payload:", payload
            print "Identifi_field:", Identifi_field
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + response_text + "','" + str(
                self.code) + "','" + payload + "','" + Identifi_field +  "','" + serialnum + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常"
    # 获取属性标签下tagSchemaId,tagFieldId,fieldName,displayName,tagId
    def tag_field_getList(self, type, url, payload, headers, Identifi_field, platform_name, flag1, flag2, flag3, flag4,flag5):
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.response_text = self.response.text
            self.code = self.response.status_code
            json_text = self.response.json()
            tagSchemaId = json_text["body"]["content"]["items"][0][flag1]
            tagFieldId = json_text["body"]["content"]["items"][0][flag2]
            fieldName = json_text["body"]["content"]["items"][0][flag3]
            displayName = json_text["body"]["content"]["items"][0][flag4]
            tagId = json_text["body"]["content"]["items"][0]["tags"][0][flag5]
            result = json_text["body"]["result"]
            return result, tagSchemaId, tagFieldId, fieldName, displayName, tagId
        except:
            print "失败"
            createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "self.response_text:", self.response_text
            response_text = self.response_text.replace("\"", "\\\"")
            print "response_text:", response_text
            payload = payload.replace("\"", "\\\"")
            print "payload:", payload
            print "Identifi_field:", Identifi_field
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + response_text + "','" + str(
                self.code) + "','" + payload + "','" + Identifi_field +  "','" + serialnum + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常"
            # 获取属性标签下tagSchemaId,tagFieldId,fieldName,displayName,tagId
    # 获取desc方法
    # def Is_successful(self, type, url, payload, headers, Identifi_field, platform_name):
    #     serialnum = gl.get_value('serialnum')
    #     print serialnum
    #     createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     try:
    #         self.response = requests.request(type, url, data=payload, headers=headers)
    #         self.code = self.response.status_code
    #         json_text = self.response.json()
    #         print "json_text:",json_text
    #         self.desc = json_text["body"]["desc"]
    #         self.result = json_text["body"]["result"]
    #         # 获取响应时间
    #         self.response_time = self.response.elapsed.total_seconds()
    #         print "响应时间；",self.response_time
    #     except:
    #         print 366
    #         self.response_text=""
    #         self.code=0
    #     try:
    #         print 370
    #         self.response_text = self.response.text
    #     except:
    #         print 373
    #         self.response_text=""
    #         try:
    #             print 376
    #             self.code = self.response.status_code
    #         except:
    #             print 379
    #             self.code=0
    #         finally:
    #             print 382
    #             serialnum = gl.get_value('serialnum')
    #             sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
    #                   "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.response_text + "','" + str(
    #                 self.code) + "','" + str(payload) + "','" + Identifi_field +  "','" + serialnum +"')"
    #             print "sql:",sql
    #             Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
    #             return "1", "异常",0
    #
    #     if self.code!=200 or self.result !=0 or self.desc!="successful"or self.response_time>3:
    #         # self.code = self.response.status_code
    #         serialnum = gl.get_value('serialnum')
    #         sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
    #               "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.response_text + "','" + str(
    #             self.code) + "','" + str(payload) + "','" + Identifi_field +  "','" + serialnum + "')"
    #         print "sql:", sql
    #         Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
    #         return -1, "异常", 0
    #     else:
    #         return self.result, self.desc,self.code
    #获取变量的请求方法1
    def Is_successful_getvalue(self, type, url, payload, headers, Identifi_field, platform_name,content):
        serialnum = gl.get_value('serialnum')
        print serialnum
        createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        flag = 0
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            # 获取响应时间
            self.response_time = self.response.elapsed.total_seconds()
            self.code = self.response.status_code
            if self.code == 200:
                # 说明此接口通,接下来应该去获取他的响应体
                flag = 0
                # self.response.text
            else:
                # 说明此接口状态不是200，可能是400,401,403,503
                flag = 1
        except:
            # 说明此接口调不通.
            flag = 2
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','异常','" + str(
                "无响应状态码") + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
            print "sql:", sql
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常", 0,""
        isflag = ""
        if flag == 0:
            # 说明状态码为200，包含3种状态:①含有Result，desc(①含有正确的响应体②含有错误的响应体，401,402,403)②没有响应体 ③只断言200
            # 因单纯断言200的方法另有其他方法实现，故不放在此处进行判断
            if len(self.response.text) != 0:
                # 说明含有响应体
                json_text = self.response.json()
                print "json_text:", json_text
                self.desc = json_text["body"]["desc"]
                self.result = json_text["body"]["result"]
                self.pos = json_text["body"][content]
                print "desc:", self.desc
                print "result:", self.result
                if self.desc == "successful" and self.result == 0:
                    if self.response_time > 3:
                        # 说明接口超时
                        isflag = "接口响应超过3秒"
                        serialnum = gl.get_value('serialnum')
                        sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                              "values('" + platform_name + "','" + createTime + "','" + url + "','" + '接口响应超过3秒' + "','" + str(
                            self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                        print "sql:", sql
                        print "result:", self.result
                        print "desc:", self.desc
                        Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                        return self.result, isflag, self.code, self.pos
                    else:
                        # 说明接口正常，没有问题
                        isflag = "接口正常"
                        return self.result, self.desc, self.code,self.pos
                else:
                    # 说明含有响应体但是响应体不是成功，而是401或者身份认证之类
                    serialnum = gl.get_value('serialnum')
                    sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                          "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.response.text + "','" + str(
                        self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                    print "sql:", sql
                    print "result:", self.result
                    print "desc:", self.desc
                    Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                    return self.result, self.desc, self.code,""

            else:
                # 说明没有响应体，为第二种情况
                serialnum = gl.get_value('serialnum')
                sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                      "values('" + platform_name + "','" + createTime + "','" + url + "','" "','" + str(
                    self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                print "sql:", sql
                Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                return -1, "空", self.code,""
        elif flag == 1:
            if len(self.response.text) != 0:
                # 说明含有响应体
                try:
                    json_text = self.response.json()
                    self.desc = json_text['error_msg']
                    self.result = json_text['error_code']
                    serialnum = gl.get_value('serialnum')
                    sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                          "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.desc + "','" + str(
                        self.result) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                    Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                    print "desc:", self.desc
                    print "result:", self.result
                    return self.result, self.desc, self.code,""
                except:
                    # 说明响应体为html格式
                    serialnum = gl.get_value('serialnum')
                    sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                          "values('" + platform_name + "','" + createTime + "','" + url + "','" + '"响应体为html格式"' + "','" + str(
                        -1) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                    print "sql:", sql
                    Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                    print "desc:响应体为html格式",
                    return -1, "异常，响应体为html格式", self.code,""
            else:
                # 说明响应体为空
                serialnum = gl.get_value('serialnum')
                sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                      "values('" + platform_name + "','" + createTime + "','" + url + "','" + '""' + "','" + str(
                    self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                print "sql:", sql
                Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                return -1, "空", self.code,""
    # 获取变量的请求方法2
    def Is_successful_getvalue_02(self, type, url, payload, headers, Identifi_field, platform_name,canshu):
        serialnum = gl.get_value('serialnum')
        print serialnum
        createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        flag = 0
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            # 获取响应时间
            self.response_time = self.response.elapsed.total_seconds()
            self.code = self.response.status_code
            if self.code == 200:
                # 说明此接口通,接下来应该去获取他的响应体
                flag = 0
                # self.response.text
            else:
                # 说明此接口状态不是200，可能是400,401,403,503
                flag = 1
        except:
            # 说明此接口调不通.
            flag = 2
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','异常','" + str(
                "无响应状态码") + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
            print "sql:", sql
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常", 0
        isflag = ""
        if flag == 0:
            # 说明状态码为200，包含3种状态:①含有Result，desc(①含有正确的响应体②含有错误的响应体，401,402,403)②没有响应体 ③只断言200
            # 因单纯断言200的方法另有其他方法实现，故不放在此处进行判断
            if len(self.response.text) != 0:
                # 说明含有响应体
                json_text = self.response.json()
                print "json_text:", json_text
                self.desc = json_text["body"]["desc"]
                self.result = json_text["body"]["result"]
                self.parameter = json_text["body"]["content"][canshu]
                print "desc:", self.desc
                print "result:", self.result
                if self.desc == "successful" and self.result == 0:
                    if self.response_time > 3:
                        # 说明接口超时
                        isflag = "接口响应超过3秒"
                        serialnum = gl.get_value('serialnum')
                        sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                              "values('" + platform_name + "','" + createTime + "','" + url + "','" + '接口响应超过3秒' + "','" + str(
                            self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                        print "sql:", sql
                        print "result:", self.result
                        print "desc:", self.desc
                        Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                        return self.result, isflag, self.code,self.parameter
                    else:
                        # 说明接口正常，没有问题
                        isflag = "接口正常"
                        return self.result, self.desc, self.code,self.parameter
                else:
                    # 说明含有响应体但是响应体不是成功，而是401或者身份认证之类
                    serialnum = gl.get_value('serialnum')
                    sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                          "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.response.text + "','" + str(
                        self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                    print "sql:", sql
                    print "result:", self.result
                    print "desc:", self.desc
                    Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                    return self.result, self.desc, self.code,""

            else:
                # 说明没有响应体，为第二种情况
                serialnum = gl.get_value('serialnum')
                sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                      "values('" + platform_name + "','" + createTime + "','" + url + "','" "','" + str(
                    self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                print "sql:", sql
                Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                return -1, "空", self.code,""
        elif flag == 1:
            if len(self.response.text) != 0:
                # 说明含有响应体
                try:
                    json_text = self.response.json()
                    self.desc = json_text['error_msg']
                    self.result = json_text['error_code']
                    serialnum = gl.get_value('serialnum')
                    sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                          "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.desc + "','" + str(
                        self.result) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                    Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                    print "desc:", self.desc
                    print "result:", self.result
                    return self.result, self.desc, self.code,""
                except:
                    # 说明响应体为html格式
                    serialnum = gl.get_value('serialnum')
                    sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                          "values('" + platform_name + "','" + createTime + "','" + url + "','" + '"响应体为html格式"' + "','" + str(
                        -1) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                    print "sql:", sql
                    Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                    print "desc:响应体为html格式",
                    return -1, "异常，响应体为html格式", self.code,""
            else:
                # 说明响应体为空
                serialnum = gl.get_value('serialnum')
                sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                      "values('" + platform_name + "','" + createTime + "','" + url + "','" + '""' + "','" + str(
                    self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                print "sql:", sql
                Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                return -1, "空", self.code,""

    # 获取code方法
    def Is_successful_code(self, type, url, payload, headers, Identifi_field, platform_name):
        createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.code = self.response.status_code
            # 获取响应时间
            self.response_time = self.response.elapsed.total_seconds()
            print "响应时间；", self.response_time
        except:
            print 366
            self.response_text = ""
            self.code = 0
        try:
            print 370
            self.response_text = self.response.text
        except:
            print 373
            self.response_text = ""
            try:
                print 376
                self.code = self.response.status_code
            except:
                print 379
                self.code = 0
            finally:
                print 382
                serialnum = gl.get_value('serialnum')
                sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                      "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.response_text + "','" + str(
                    self.code) + "','" + str(payload) + "','" + Identifi_field +  "','" + serialnum + "')"
                print "sql:", sql
                Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                return "1", "异常", 0

        if self.code != 200 or self.response_time > 3:
            # self.code = self.response.status_code
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.response_text + "','" + str(
                self.code) + "','" + str(payload) + "','" + Identifi_field +  "','" + serialnum + "')"
            print "sql:", sql
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return self.code
        else:
            return self.code
    # 断言200的方法
    def Is_successful_status(self, type, url, payload, headers, Identifi_field, platform_name):
        createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.code = self.response.status_code
            # 获取响应时间
            self.response_time = self.response.elapsed.total_seconds()
            print "响应时间；", self.response_time
        except:
            print 366
            self.code = 0
            self.response_text=""
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.response_text + "','" + str(
                self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return  0

        if self.code != 200 or self.response_time > 3:
            self.response_text = ""
            # self.code = self.response.status_code
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.response_text + "','" + str(
                self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
            print "sql:", sql
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return 0
        else:
            return self.code

#GET请求
    def Is_successful_get(self, type, url, querystring, headers, Identifi_field, platform_name):
        createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            self.response = requests.request(type, url, headers=headers, params=querystring)
            self.code = self.response.status_code
            # 获取响应时间
            self.response_time = self.response.elapsed.total_seconds()
            print "响应时间；", self.response_time
        except:
            print 366
            self.code = 0
            self.response_text = ""
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.response_text + "','" + str(
                self.code) + "','" + str(querystring) + "','" + Identifi_field + "','" + serialnum + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return 0

        if self.code != 200 or self.response_time > 3:
            # self.code = self.response.status_code
            serialnum = gl.get_value('serialnum')
            self.response_text = ""
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.response_text + "','" + str(
                self.code) + "','" + str(querystring) + "','" + Identifi_field + "','" + serialnum + "')"
            print "sql:", sql
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return 0
        else:
            return self.code
            # 获取desc方法

    def Is_successful(self, type, url, payload, headers, Identifi_field, platform_name):
        serialnum = gl.get_value('serialnum')
        print serialnum
        createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        flag=0
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            # 获取响应时间
            self.response_time = self.response.elapsed.total_seconds()
            self.code=self.response.status_code
            if self.code==200:
               # 说明此接口通,接下来应该去获取他的响应体
               flag=0
               # self.response.text
            else:
                # 说明此接口状态不是200，可能是400,401,403,503
                flag=1
        except:
            # 说明此接口调不通.
            flag=2
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','异常','" + str("无响应状态码") + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
            print "sql:", sql
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return "1", "异常", 0
        isflag=""
        if flag==0:
            # 说明状态码为200，包含3种状态:①含有Result，desc(①含有正确的响应体②含有错误的响应体，401,402,403)②没有响应体 ③只断言200
            # 因单纯断言200的方法另有其他方法实现，故不放在此处进行判断
            if len(self.response.text) !=0:
                # 说明含有响应体
                json_text = self.response.json()
                print "json_text:", json_text
                self.desc = json_text["body"]["desc"]
                self.result = json_text["body"]["result"]
                print "desc:",self.desc
                print "result:",self.result
                if self.desc=="successful" and self.result==0 :
                    if self.response_time>3:
                        # 说明接口超时
                        isflag="接口响应超过3秒"
                        serialnum = gl.get_value('serialnum')
                        sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                              "values('" + platform_name + "','" + createTime + "','" + url + "','" + '接口响应超过3秒' + "','" + str(
                            self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                        print "sql:", sql
                        print "result:", self.result
                        print "desc:", self.desc
                        Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                        return self.result, isflag, self.code
                    else:
                        # 说明接口正常，没有问题
                        isflag="接口正常"
                        return self.result, self.desc, self.code
                else:
                    # 说明含有响应体但是响应体不是成功，而是401或者身份认证之类
                    serialnum = gl.get_value('serialnum')
                    sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                          "values('" + platform_name + "','" + createTime + "','" + url + "','"+self.response.text+"','" + str(
                        self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                    print "sql:", sql
                    print "result:",self.result
                    print "desc:",self.desc
                    Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                    return self.result, self.desc, self.code

            else:
                # 说明没有响应体，为第二种情况
                serialnum = gl.get_value('serialnum')
                sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                      "values('" + platform_name + "','" + createTime + "','" + url + "','" "','" + str(
                    self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                print "sql:", sql
                Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                return -1, "空", self.code
        elif flag==1:
            if len(self.response.text)!=0:
                # 说明含有响应体
                try:
                    json_text = self.response.json()
                    self.desc = json_text['error_msg']
                    self.result = json_text['error_code']
                    serialnum = gl.get_value('serialnum')
                    sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                          "values('" + platform_name + "','" + createTime + "','" + url + "','"+self.desc+"','" + str(
                        self.result) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                    Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                    print "desc:",self.desc
                    print "result:",self.result
                    return self.result, self.desc,self.code
                except:
                    # 说明响应体为html格式
                    serialnum = gl.get_value('serialnum')
                    sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                          "values('" + platform_name + "','" + createTime + "','" + url + "','" + '"响应体为html格式"' + "','" + str(
                        -1) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                    print "sql:", sql
                    Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                    print "desc:响应体为html格式",
                    return -1, "异常，响应体为html格式", self.code
            else:
                # 说明响应体为空
                serialnum = gl.get_value('serialnum')
                sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                      "values('" + platform_name + "','" + createTime + "','" + url + "','" + '""' + "','" + str(
                    self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                print "sql:", sql
                Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                return -1, "空", self.code





        # try:
        #     self.response = requests.request(type, url, data=payload, headers=headers)
        #     self.code = self.response.status_code
        #     json_text = self.response.json()
        #     print "json_text:", json_text
        #     self.desc = json_text["body"]["desc"]
        #     self.result = json_text["body"]["result"]
        #     # 获取响应时间
        #     self.response_time = self.response.elapsed.total_seconds()
        #     print "响应时间；", self.response_time
        # except:
        #     print 366
        #     self.response_text = ""
        #     self.code = 0
        # try:
        #     print 370
        #     self.response_text = self.response.text
        # except:
        #     print 373
        #     self.response_text = ""
        #     try:
        #         print 376
        #         self.code = self.response.status_code
        #     except:
        #         print 379
        #         self.code = 0
        #     finally:
        #         print 382
        #         serialnum = gl.get_value('serialnum')
        #         sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
        #               "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.response_text + "','" + str(
        #             self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
        #         print "sql:", sql
        #         Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
        #         return "1", "异常", 0
        #
        # if self.code != 200 or self.result != 0 or self.desc != "successful" or self.response_time > 3:
        #     # self.code = self.response.status_code
        #     serialnum = gl.get_value('serialnum')
        #     sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
        #           "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.response_text + "','" + str(
        #         self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
        #     print "sql:", sql
        #     Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
        #     return -1, "异常", 0
        # else:
        #     return self.result, self.desc, self.code
# 断言200的方法
    def Is_successful_hwjiankong(self, type, url, payload, headers, Identifi_field, platform_name,rl):
        createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            self.response = requests.request(type, url, data=payload, headers=headers)
            self.code = self.response.status_code
            # 获取响应时间
            self.response_time = self.response.elapsed.total_seconds()
            print "响应时间；", self.response_time
        except:
            print 366
            self.code = 0
            self.response_text=""
            serialnum = gl.get_value('serialnum')
            sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                  "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.response_text + "','" + str(
                self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
            return  0,"0","异常"
        flag=0
        if self.code != 200 :
            if self.response_time>3:
                try:
                    self.response_text =self.response.text
                    flag=0
                except:
                    self.response_text=""
                    flag=1
                finally:
            # self.code = self.response.status_code
                    serialnum = gl.get_value('serialnum')
                    sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                          "values('" + platform_name + "','" + createTime + "','" + url + "','" + '响应时间超过3秒' + "','" + str(
                        self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                    print "sql:", sql
                    Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                    return self.code,"0","响应时间超过3秒"
            else:
                serialnum = gl.get_value('serialnum')
                sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                      "values('" + platform_name + "','" + createTime + "','" + url + "','" + '状态码不是200' + "','" + str(
                    self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                print "sql:", sql
                Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                return self.code, "0","状态码不是200"
        else:
            if self.response_time>3:
                try:
                    self.response_text =self.response.text
                    flag=0
                except:
                    self.response_text=""
                    flag=1
                finally:
            # self.code = self.response.status_code
                    serialnum = gl.get_value('serialnum')
                    sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                          "values('" + platform_name + "','" + createTime + "','" + url + "','" + '响应时间超过3秒' + "','" + str(
                        self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                    print "sql:", sql
                    Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                    return self.code,"0","响应时间超过3秒"
            else:
                print "text:",self.response.text
                if int(self.response.text)<rl:
                    print "baishi"
                    serialnum = gl.get_value('serialnum')
                    sql = "insert into Error_Log(platform_name,Execution_date,fail_inter_name,response_body,status_code,request_body,Identifi_field,serialnum) " \
                          "values('" + platform_name + "','" + createTime + "','" + url + "','" + self.response.text+'短信发送剩余量小于10000' + "','" + str(
                        self.code) + "','" + str(payload) + "','" + Identifi_field + "','" + serialnum + "')"
                    print "sql:", sql
                    Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
                    return self.code, int(self.response.text),"短信发送量少于10000"
                else:
                    print "chenggong"
                    return self.code, self.response.text,"successful"


