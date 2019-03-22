# -*- coding: utf-8 -*-

import os
import sys
# curPath = os.path.abspath(os.path.dirname(__file__)) #os.path.basename(path):返回所给路径path的最底层路径名或者是文件名；
# # #os.path.dirname(__file__):返回脚本的路径
# rootPath = os.path.split(curPath)[0]  #os.path.split(curPath)[0]:path分割成目录
# sys.path.append(rootPath)
import unittest
from common.report import report
# from test_case.offline_meeting_case import Offline_Meeting_Test
import time
from common.mail import email_oper
# from test_case.sms_case import Sms_Test
# from test_case.wechat_case import Wechat_Test
# from test_case.questionnaire_case import Questionnaire
# from test_case.article_case import Article
# from test_case.webinar_create_case  import Webinar_Case
# from test_case.webinar_case import Webinar_Case
# from test_case.member_case import Member_Test
# from test_case.edm_case import Edm_Test
# from test_case.ady_case import ADY
# from test_case.api_case_group1 import Api_Case_Group1
# from test_case.api_case_group2 import Api_Case_Group2
# from test_case.api_case_group3 import Api_Case_Group3
# from test_case.api_case_group4 import Api_Case_Group4
# from pages.common_pages.ConfigUrl import ConfigUrl
# from test_case.choose_page_case import Choose_Page_Case
# from test_case.form_case import Form_Test
# from test_case.vote_case import Vote_Test
# from test_case.microdiscussion_case import Microdiscussion_Test
# from pages.common_pages.commonsuit import Suit
# from test_case.Luck_draw import Luck_draw
from common.mail import email_send
# from test_case.file_case import File_Test
from test_case.api_all_Interface import ParametrizedTestCase
from test_case.five_common import TestOne
from test_case.api_most_interface import api_most_interface
from pages.api.api_most_all import api_most_all
import common.common_function.globalvar as gl
import datetime

class ConrollerShowInter():


    def Def_List(self,class_name):   #def_list 获取单元测试中，测试函数列表， #class的名字，不用双引号，直接用

        list = []
        def_name = dir(class_name)    #dir():返回当前范围内的变量、方法和定义的类型列表
        for tmp in def_name:
            def_four = str(tmp)[:4]   # str(tmp)[:4] :索引和切片，从下标为0的元素选择到下标为3的元素，不包括下标4的元素
            if def_four == "test":    #取方法前四个字母为test的
                list.append(tmp)     #append() 方法向列表的尾部添加一个新的元素。只接受一个参数
        return list

    def SupportTool_Control_inter(self,execUser,platname):  #SupportTool_Control 用来管理我们的用例启动方式，执行所有配置好的单元测试，生成报告并发送
        StartTime = time.time()       #time()：返回当前时间的时间戳（1970纪元后经过的浮点秒数），需要import time
        suite = unittest.TestSuite()     #创建一个测试集合
        # suite = Suit()  # 创建一个测试集合
        #设置全局变量当前执行的平台
        gl._init()
        serialnum = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        print (serialnum)
        gl.set_value('serialnum',serialnum)
        gl.set_value('currExecPlat',platname)
        currExecPlat = gl.get_value('currExecPlat')
        print currExecPlat
        count = 0
        if platname == 'HW':
            api_most_interface_test = self.Def_List(api_most_interface)  # Def_List 获取指定单元测试中，测试函数列表
            for most_interface in api_most_interface_test:
                 count = count+1
                 suite.addTest(api_most_interface(most_interface))
        db = api_most_all()
        id = db.first_save_exec_record(platname,count,platname,execUser)

        #测试
        #创建测试报告
        AddSuite = report.AllReport()   #AddSuite = report.AllReport() :实例化AllReport类
        AddSuite.onlyneed_suite(suite)    #onlyneed_suite(suite) ：指定suit的report
        db.second_update_exec_record(id)

        # 发送邮件
        EndTime = time.time()
        PerformTime = EndTime - StartTime
        content = "autoTest"
        SendEmail = email_send.SendEmailModel()  #实例化SendEmailModel类
        SendEmail.postreport_only(PerformTime,str(content)) #调用SendEmailModel类中postreport_only方法

if __name__ == '__main__':

        # 此时说明为s2
        A = ConrollerShowInter()
        A.SupportTool_Control_inter("zzp","HW")
    # 这是在dev分支上写的代码
# 测试--刘雅的冲突测试
    # for host, browserType in config.getconfig().items():哥哥哥
    #     print(host)
    #     print(browserType)
    #     driver.setRomteDriver(host, browserType)
    #     driver.choose_brower()
    #     A = ConrollerShow()
    #     A.SupportTool_Control()


