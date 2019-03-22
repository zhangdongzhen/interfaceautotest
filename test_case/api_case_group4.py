# -*- coding: utf-8 -*-
"""
os模块就是对操作系统进行操作，比如取文件的路径。

sys模块提供了一系列有关Python运行环境的变量和函数,例如：
#生成报告是报错，编码错误。python2.7默认使用ascii，设置成utf-8，python2.7以后不用setdefaultencoding了
   reload(sys)
  sys.setdefaultencoding('utf8')
"""
import sys
reload(sys)  #在解释器里修改的编码只能保证当次有效，在重启解释器后，会发现，编码又被重置为默认的ascii了
sys.setdefaultencoding('utf8')
import os
curPath = os.path.abspath(os.path.dirname(__file__)) #os.path.basename(path):返回所给路径path的最底层路径名或者是文件名；
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import time
import unittest
from common.report import report
from common.mail import email_oper
from pages.api.group4 import ApiRequestsfoureFour
from pages.api import apicommon
"""
刘国静开发组
"""


class Api_Case_Group4(unittest.TestCase):
    """ 接口自动化四组测试用例 """

    def setUp(self):
        if apicommon.all_login() == 1:
            print "successful"
        else:
            print "get login session error"
    def test_001_webinar_open_getWebinarInfo(self):
        """获取会场详细信息"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_getWebinarInfo()
        self.assertEqual(actual_result, 0, desc)

    def test_002_webinar_open_getWebinarList(self):
        """获取直播会议列表"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_getWebinarList()
        self.assertEqual(actual_result, 0, desc)

    def test_003_webinar_open_getCustomFormInfo(self):
        """获取自定义表单"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_getCustomFormInfo()
        self.assertEqual(actual_result, 0, desc)

    def test_004_webinar_open_getApplicantInfo(self):
        """获取会议信息"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_getApplicantInfo()
        self.assertEqual(actual_result, 0, desc)

    def test_005_webinar_open_getDemandInfo(self):
        """得到一个点播会议的详情信息"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_getDemandInfo()
        self.assertEqual(actual_result, 0, desc)

    def test_006_seminar_contact_front_getContactInfo(self):
        """根据会议id和唯一字段获取参会人信息"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.seminar_contact_front_getContactInfo()
        self.assertEqual(actual_result, 0, desc)

    def test_007_luckyDraw_get(self):
        """根据会议id和唯一字段获取参会人信息"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.luckyDraw_get()
        self.assertEqual(actual_result, 0, desc)

    def test_008_product_crossLine_getList(self):
        """获取租户下的某一分类的多产品线下的产品列表"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.product_crossLine_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_008_product_getList(self):
        """获取产品线下产品列表"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.product_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_009_productLine_getList(self):
        """获取租户下产品线列表"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.productLine_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_010_post_getMainAndReplyList(self):
        """获取留言板的发帖的回帖"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.post_getMainAndReplyList()
        self.assertEqual(actual_result, 0, desc)

    def test_011_luckyDraw_result_getState(self):
        """获取大屏抽奖的轮次状态，如果未开始的轮次，标记未开始，已开始的，返回中奖名单"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.luckyDraw_result_getState()
        self.assertEqual(actual_result, 0, desc)

    def test_012_post_getListByUser(self):
        """获取某人的未被删除的发送帖子记录"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.post_getListByUser()
        self.assertEqual(actual_result, 0, desc)

    def test_013_topic_get(self):
        """获取发帖信息"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.topic_get()
        self.assertEqual(actual_result, 0, desc)

    def test_014_webinar_open_getAttendList(self):
        """获取已报名的会议列表"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_getAttendList()
        self.assertEqual(actual_result, 0, desc)

    def test_015_webinar_open_getVideoTimeLine(self):
        """获取视频信息"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_getVideoTimeLine()
        self.assertEqual(actual_result, 0, desc)

    def test_016_webinar_open_trackingCode_getList(self):
        """根据实例编号获取该实例的渠道追踪代码"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_trackingCode_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_017_post_get(self):
        """获取贴子信息"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.post_get()
        self.assertEqual(actual_result, 0, desc)


    def test_018_post_getReplyPost(self):
        """获取某主贴的所有回贴"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.post_getReplyPost()
        self.assertEqual(actual_result, 0, desc)

    def test_019_productLine_field_get(self):
        """获取某个产品线的字段列表"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.productLine_field_get()
        self.assertEqual(actual_result, 0, desc)

    def test_020_productLine_category_getConfigInfo(self):
        """获取某产品线下具体某个字典值的配置信息"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.productLine_category_getConfigInfo()
        self.assertEqual(actual_result, 0, desc)

    def test_021_luckyDraw_getAwardDetailList(self):
        """获取奖品列表信息"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.luckyDraw_getAwardDetailList()
        self.assertEqual(actual_result, 0, desc)

    def test_022_luckyDraw_client_action(self):
        """抽奖"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.luckyDraw_client_action()
        self.assertEqual(actual_result, 0, desc)

    def test_023_luckyDraw_client_actionByBigScreen(self):
        """大屏抽奖的抽奖操作"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.luckyDraw_client_actionByBigScreen()
        self.assertEqual(actual_result, 0, desc)

    def test_024_comment_getList(self):
        """获取评论列表"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.comment_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_025_member_form_getList(self):
        """该接口为后台接口，后期即将移除，请不要继续使用，获取体系下的注册表单列表"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.member_form_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_026_luckyDraw_result_getUserResultList(self):
        """获取个人的普通抽奖记录"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.luckyDraw_result_getUserResultList()
        self.assertEqual(actual_result, 0, desc)

    def test_027_product_get(self):
        """获取产品详细信息"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.product_get()
        self.assertEqual(actual_result, 0, desc)

    def test_028_webinar_open_registration(self):
        """线上会报名接口"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_registration()
        self.assertEqual(actual_result, 0, desc)


    def test_029_post_create(self):
        """线上会报名接口"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.post_create()
        self.assertEqual(actual_result, 0, desc)

    def test_030_webinar_event_interaction_check(self):
        """检查什么情况下可以继续投票、答问卷，会场开放过程中可以答"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_event_interaction_check()
        self.assertEqual(actual_result, 0, desc)

    def test_031_luckyDraw_client_hasParticipate(self):
        """该接口为后台接口，后期即将移除，请不要继续使用，检查某个用户是否已经参与过大屏抽奖"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.luckyDraw_client_hasParticipate()
        self.assertEqual(actual_result, 0, desc)

    def test_032_webinar_open_newRegistration(self):
        """注册用户接口"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_newRegistration()
        self.assertEqual(actual_result, 0, desc)

    def test_033_webinar_open_getWebinarListAdvanced(self):
        """获取直播会议列表（高级查询功能）"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_getWebinarListAdvanced()
        self.assertEqual(actual_result, 0, desc)

    def test_034_webinar_open_interaction_fileDownLoad(self):
        """下载文件互动记录"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_interaction_fileDownLoad()
        self.assertEqual(actual_result, 0, desc)

    def test_035_webinar_open_join(self):
        """人员参会接口"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_join()
        self.assertEqual(actual_result, 0, desc)

    def test_036_forum_post_get(self):
        """微论坛帖子详情"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.forum_post_get()
        self.assertEqual(actual_result, 0, desc)

    def test_037_forum_stat_homePage(self):
        """微论坛帖子列表"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.forum_stat_homePage()
        self.assertEqual(actual_result, 0, desc)

    def test_038_forum_section_getList(self):
        """获取某个微论坛的子版列表"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.forum_section_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_039_forum_getReplyList(self):
        """获取微论坛的回复列表"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.forum_getReplyList()
        self.assertEqual(actual_result, 0, desc)

    def test_040_forum_post_getReplyPost(self):
        """获取微讨论的主贴ID"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.forum_post_getReplyPost()
        self.assertEqual(actual_result, 0, desc)

    def test_041_forum_post_getMainPost(self):
        """获取微讨论的主贴列表.可传前端sess,传了sess会帖子信息里面会有发帖人的用户信息，不传sess显示的是匿名用户"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.forum_post_getMainPost()
        self.assertEqual(actual_result, 0, desc)

    def test_042_webinar_open_attend(self):
        """修改参会人数,并返回登录人的地址"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_attend()
        self.assertEqual(actual_result, 0, desc)

    def test_043_forum_post_create(self):
        """微论坛发贴回复"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.forum_post_create()
        self.assertEqual(actual_result, 0, desc)

    def test_044_forum_post_like(self):
        """微论坛给帖子点赞"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.forum_post_like()
        self.assertEqual(actual_result, 0, desc)

    def test_045_luckyDraw_client_participate(self):
        """大屏抽奖，用户现场主动参与抽奖，如扫码"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.luckyDraw_client_participate()
        self.assertEqual(actual_result, 0, desc)

    def test_046_comment_create(self):
        """发表评论"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.comment_create()
        self.assertEqual(actual_result, 0, desc)

    def test_047_member_schema_field_GetList(self):
        """获取体系字段"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.member_schema_field_GetList()
        self.assertEqual(actual_result, 0, desc)

    def test_048_webinar_open_checkRegistration(self):
        """查询用户是否可以报名接口"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.webinar_open_checkRegistration()
        self.assertEqual(actual_result, 0, desc)

    # def test_049_api_luckydraw_get(self):
    #     """获取抽奖详情"""
    #     object = ApiRequestsfoureFour()
    #     actual_result,desc = object.api_luckydraw_get()
    #     self.assertEqual(actual_result, 0, desc)

    def test_050_api_topic_message_Create(self):
        """发主帖/回帖"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.api_topic_message_Create()
        self.assertEqual(actual_result, 0, desc)

    def test_051_api_webinar_channel_query(self):
        """根据会议ID获取该会议的渠道追踪代码"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.api_webinar_channel_query()
        self.assertEqual(actual_result, 0, desc)

    def test_052_api_webinar_contacts_get(self):
        """获取报名人信息/返回报名人状态"""
        object = ApiRequestsfoureFour()
        actual_result,desc = object.api_webinar_contacts_get()
        self.assertEqual(actual_result, 0, desc)

    # def test_053_api_webinar_contacts_signup(self):  #新api，报错
    #     """获会议报名"""
    #     object = ApiRequestsfoureFour()
    #     actual_result,desc = object.api_webinar_contacts_signup()
    #     self.assertEqual(actual_result, 0, desc)


if __name__ == "__main__":
    #全部用例按照数字顺序测试
    #unittest.main()
    StartTime = time.time()
    suite = unittest.TestSuite()
    # 指定单个单元测试（ 需要配置运行方式才能走main函数，参考https://www.cnblogs.com/youreyebows/p/7867508.html）
    suite.addTest(Api_Case_Group4("test_048_webinar_open_checkRegistration"))



    #执行单元测试，生成报告
    AddSuite = report.AllReport()
    AddSuite.onlyneed_suite(suite)

    #发送邮件
    EndTime = time.time()
    PerformTime = EndTime - StartTime
    content ="test_createoffline"

    # SendEmail = email.SendEmailModel()
    SendEmail = email_oper.SendEmailModel()
    #SendEmail.postreport_only(PerformTime,content)












