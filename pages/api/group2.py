# -*- coding: utf-8 -*-
# 用于奥点云uat测试
from test_case.base_unit import BaseUnit
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.webinar_pages.index_page import Webinar_IndexPage
import time,unittest
from pages.webinar_pages.create_meeting import Webinar_Create
from pages.webinar_pages.interaction_setting_page import InteractionSetting
from pages.questionnaire_page.new_questionnaire_page import NewQuestionnairePage
from pages.webinar_pages.enter_meeting import enter_meeting

base = BasePage(object)
class ADY(BaseUnit):
   def test_001(self):
       pass
if __name__ == '__main__':
    # StartTime = time.time()
    # suite = unittest.TestSuite()
    # # 指定单个单元测试（ 需要配置运行方式才能走main函数，参考https://www.cnblogs.com/youreyebows/p/7867508.html）
    # suite.addTest(ADY("test_004"))
    # # suite.addTest(Offline_Meeting_Test("test_002_interaction"))
    # # suite.addTest(Offline_Meeting_Test("test_003_createoffline"))
    #
    #
    # # 执行单元测试，生成报告
    # AddSuite = report.AllReport()
    # AddSuite.onlyneed_suite(suite)
    #
    # # 发送邮件
    # EndTime = time.time()
    # PerformTime = EndTime - StartTime
    # content = "test_createoffline"
    #
    # # SendEmail = email.SendEmailModel()
    # SendEmail = email_oper.SendEmailModel()
    # SendEmail.postreport_only(PerformTime, content)
    pass