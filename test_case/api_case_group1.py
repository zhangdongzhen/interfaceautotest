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
from pages.common_pages.login_page import LoginPage
from pages.api.group2 import ApiRequestsTwo
from common.mail import email_oper
from pages.api.group1 import ApiRequestsOne
from pages.api.group3 import ApiRequestsThree
from pages.api.group4 import ApiRequestsfoureFour
from pages.api import apicommon
"""
刘国静开发组
"""


class Api_Case_Group1(unittest.TestCase):
    """ 接口自动化一组测试用例 """
    def setUp(self):
        if apicommon.all_login() == 1:
            print "successful"
        else:
            print "get login session error"


    def test_001_seminar_frontGet(self):
        """获取会议详情"""
        object = ApiRequestsOne()
        # object.seminar_frontGet()
        actual_result,desc = object.seminar_frontGet()
        
        self.assertEqual(actual_result, 0, desc)

    def test_002_seminar_getList(self):
        """获取会议列表"""
        object = ApiRequestsOne()
        # object.seminar_getList()
        actual_result,desc = object.seminar_getList()

        self.assertEqual(actual_result, 0, desc)

    def test_003_seminar_topicTemplate_seminar_get(self):
        """获取会议相关信息"""
        object = ApiRequestsOne()
        # object.seminar_topicTemplate_seminar_get()
        actual_result,desc = object.seminar_topicTemplate_seminar_get()

        self.assertEqual(actual_result, 0, desc)

    def test_004_seminar_contact_register(self):

        """会议报名接口"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_contact_register()
        self.assertEqual(actual_result, 0, desc)

    def test_005_seminar_agenda_get(self):
        """获取会议日程信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_agenda_get()
        self.assertEqual(actual_result, 0, desc)

    def test_006_seminar_agenda_getGroupList(self):
        """获取会议日程按天分组"""
        object = ApiRequestsOne()
        # object.seminar_agenda_getGroupList()
        actual_result,desc = object.seminar_agenda_getGroupList()

        self.assertEqual(actual_result, 0, desc)

    def test_007_seminar_guest_getGroupList(self):
        """获取嘉宾列表"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_guest_getGroupList()
        self.assertEqual(actual_result, 0, desc)

    def test_008_app_seminar_contact_field_getCustomFields(self):
        """该接口为APP专用接口，项目不要使用，获取联系人字段"""
        object = ApiRequestsOne()
        actual_result,desc = object.app_seminar_contact_field_getCustomFields()
        self.assertEqual(actual_result, 0, desc)

    def test_009_seminar_subSeminar_frontGet(self):
        """获取分会场详细信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_subSeminar_frontGet()
        self.assertEqual(actual_result, 0, desc)

    def test_010_de_contact_getLastSeminarsBySess(self):
        """获取参与过的会议"""
        object = ApiRequestsOne()
        actual_result,desc = object.de_contact_getLastSeminarsBySess()
        # print actual_result
        self.assertEqual(actual_result, 0, u"接口测试不通过")

    def test_011_field_getList(self):
        """获取参与过的会议"""
        object = ApiRequestsOne()
        actual_result,desc = object.field_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_012_shortUrl_getList(self):
        """获取短地址"""
        object = ApiRequestsOne()
        actual_result,desc = object.shortUrl_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_013_app_seminar_contact_getByUniqueField(self):
        """根据参会二维码获取会议联系人"""
        object = ApiRequestsOne()
        actual_result,desc = object.app_seminar_contact_getByUniqueField()
        self.assertEqual(actual_result, 0, desc)

    def test_014_app_seminar_contact_getList(self):
        """该接口为APP专用接口，项目不要使用，获取会议联系人"""
        object = ApiRequestsOne()
        actual_result,desc = object.app_seminar_contact_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_015_app_seminar_contact_getListCompressed(self):
        """该接口为APP专用接口，项目不要使用，获取压缩过的会议联系人"""
        object = ApiRequestsOne()
        actual_result = object.app_seminar_contact_getListCompressed()
        self.assertEqual(actual_result,200)

    def test_016_app_seminar_contact_prints_getSigningPointInfo(self):
        """获取会议下签到点缩略信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.app_seminar_contact_prints_getSigningPointInfo()
        self.assertEqual(actual_result, 0, desc)

    def test_017_app_seminar_getList(self):
        """该接口为APP专用接口，项目不要使用，获取会议列表"""
        object = ApiRequestsOne()
        actual_result,desc = object.app_seminar_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_018_app_seminar_signingPoint_checkIn_getListCompressed(self):
        """该获取签到历史记录,压缩版"""
        object = ApiRequestsOne()
        actual_result = object.app_seminar_signingPoint_checkIn_getListCompressed()
        self.assertEqual(actual_result,200)

    def test_019_app_seminar_signingPoint_contact_getList(self):
        """该接口为APP专用接口，项目不要使用，获取签到点通道下人员"""
        object = ApiRequestsOne()
        actual_result,desc = object.app_seminar_signingPoint_contact_getList()
        self.assertEqual(actual_result, 0, desc)


    def test_020_app_seminar_signingPoint_getGroupList(self):
        """该接口为APP专用接口，项目不要使用，获取会议下的所有签到点信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.app_seminar_signingPoint_getGroupList()
        self.assertEqual(actual_result, 0, desc)

    def test_021_seminar_bigScreen_forBigScreenWall_getCheckInData(self):
        """获取大屏签到墙信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_bigScreen_forBigScreenWall_getCheckInData()
        self.assertEqual(actual_result, 0, desc)

    def test_022_seminar_bigScreen_forBigScreenWall_getWapCheckInfo(self):
        """获取大屏手机端签到信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_bigScreen_forBigScreenWall_getWapCheckInfo()
        self.assertEqual(actual_result, 0, desc)

    def test_023_seminar_bigScreen_get(self):
        """获取大屏详细信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_bigScreen_get()
        self.assertEqual(actual_result, 0, desc)

    def test_024_seminar_bigScreen_getListByGroup(self):
        """获取大屏列表"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_bigScreen_getListByGroup()
        self.assertEqual(actual_result, 0, desc)

    def test_025_seminar_bigScreen_getPollPreset(self):
        """获取投票大屏预设信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_bigScreen_getPollPreset()
        self.assertEqual(actual_result, 0, desc)

    def test_026_seminar_contact_front_checkIn(self):
        """参会人签到"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_contact_front_checkIn()
        self.assertEqual(actual_result, 0, desc)

    def test_027_seminar_guest_getList(self):
        """获取会议嘉宾列表"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_guest_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_028_seminar_register_getList(self):
        """获取报名表单列表"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_register_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_029_seminar_subSeminar_getListByType(self):
        """获取分会场列表"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_subSeminar_getListByType()
        self.assertEqual(actual_result, 0, desc)

    def test_030_seminar_topicTemplate_seminar_getFormInfo(self):
        """获取表单详细信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_topicTemplate_seminar_getFormInfo()
        self.assertEqual(actual_result, 0, desc)

    def test_031_seminar_topicTemplate_seminar_getWithAllSub(self):
        """获取会议信息，包括所有的分会场"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_topicTemplate_seminar_getWithAllSub()
        self.assertEqual(actual_result, 0, desc)

    def test_032_questionary_action(self):
        """提交问卷"""
        object = ApiRequestsOne()
        actual_result,desc = object.questionary_action()
        self.assertEqual(actual_result, 0, desc)

    def test_033_questionary_exam_action(self):
        """用户答题"""
        object = ApiRequestsOne()
        actual_result,desc = object.questionary_exam_action()
        self.assertEqual(actual_result, 0, desc)

    def test_034_questionary_get(self):
        """获取问卷信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.questionary_get()
        self.assertEqual(actual_result, 0, desc)

    def test_035_questionary_getList(self):
        """获取问卷信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.questionary_getList()
        self.assertEqual(actual_result, 0, desc)


    def test_036_questionary_HasParticipation(self):
        """浏览问卷"""
        object = ApiRequestsOne()
        actual_result,desc = object.questionary_HasParticipation()
        self.assertEqual(actual_result, 0, desc)

    def test_037_customForm_get(self):
        """获取自定义表单详情"""
        object = ApiRequestsOne()
        actual_result,desc = object.customForm_get()
        self.assertEqual(actual_result, 0, desc)

    def test_038_seminar_frontGetList(self):
        """获取会议列表，无sess调用"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_frontGetList()
        self.assertEqual(actual_result, 0, desc)

    def test_039_questionary_view(self):
        """获取会议列表，无sess调用"""
        object = ApiRequestsOne()
        actual_result,desc = object.questionary_view()
        self.assertEqual(actual_result, 0, desc)

    def test_040_seminar_contact_getContactToWechat(self):
        """根据openID获取会中联系人信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_contact_getContactToWechat()
        self.assertEqual(actual_result, 0, desc)

    def test_041_seminar_contact_front_getCommonContactInfo(self):
        """获取参会人员信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_contact_front_getCommonContactInfo()
        self.assertEqual(actual_result, 0, desc)

    def test_042_seminar_bigScreen_updateMessage(self):
        """该接口为后台接口，后期即将移除，请不要继续使用，更新大屏消息"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_bigScreen_updateMessage()
        self.assertEqual(actual_result, 0, desc)

    def test_043_seminar_topicTemplate_contact_get(self):
        """获取联系人信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_topicTemplate_contact_get()
        self.assertEqual(actual_result, 0, desc)

    def test_044_seminar_register_canRegistert(self):
        """会议是否可以报名 如果有报名返回线下会报名信息，如果没有报名但是有注册返回注册信息，如果没有注册没有报名返回null"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_register_canRegister()
        self.assertEqual(actual_result, 0, desc)

    def test_045_de_contact_front_get(self):
        """获取de联系人信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.de_contact_front_get()
        self.assertEqual(actual_result, 0, desc)

    def test_046_customForm_view(self):
        """记录表单的浏览记录"""
        object = ApiRequestsOne()
        actual_result,desc = object.customForm_view()
        self.assertEqual(actual_result, 0, desc)

    def test_047_questionary_exam_user_getSingleResult(self):
        """获取某人的答题记录"""
        object = ApiRequestsOne()
        actual_result,desc = object.questionary_exam_user_getSingleResult()
        self.assertEqual(actual_result, 0, desc)

    def test_048_questionary_exam_user_GenerateExam(self):
        """生成试卷"""
        object = ApiRequestsOne()
        actual_result,desc = object.questionary_exam_user_GenerateExam()
        self.assertEqual(actual_result, 0, desc)

    def test_049_seminar_signingPoint_checkIn_getCheckInCount(self):
        """获取某会议下签到点的签到数"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_signingPoint_checkIn_getCheckInCount()
        self.assertEqual(actual_result, 0, desc)

    def test_050_seminar_topicTemplate_contact_getByOpenId(self):
        """通过微信OpenId获取某会议下的联系人"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_topicTemplate_contact_getByOpenId()
        self.assertEqual(actual_result, 0, desc)

    def test_051_seminar_register_getSubList(self):
        """通过自定义表单id获取报名表单信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_register_getSubList()
        self.assertEqual(actual_result, 0, desc)

    def test_052_seminar_contact_setContactToWechat(self):
        """绑定微信和参会人员"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_contact_setContactToWechat()
        self.assertEqual(actual_result, 0, desc)

    def test_053_seminar_bigScreen_updateLottery(self):
        """该接口为后台接口，后期即将移除，请不要继续使用，更新留言大屏信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_bigScreen_updateLottery()
        self.assertEqual(actual_result, 0, desc)

    def test_054_customForm_checkRepeatable(self):
        """检查表单的不重复字段是否重复"""
        object = ApiRequestsOne()
        actual_result,desc = object.customForm_checkRepeatable()
        self.assertEqual(actual_result, 0, desc)

    def test_055_seminar_contact_front_getRegContact(self):
        """此接口即将过期不在维护，可使用 member_geneGet 代替"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_contact_front_getRegContact()
        self.assertEqual(actual_result, 0, desc)


    def test_056_seminar_contact_front_regSeminar(self):
        """此接口即将过期不在维护，可使用 member_geneGet 代替"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_contact_front_regSeminar()
        self.assertEqual(actual_result, 0, desc)

    def test_057_customForm_user_getResultByOpenId(self):
        """获取某个OpenId的答表单的记录"""
        object = ApiRequestsOne()
        actual_result,desc = object.customForm_user_getResultByOpenId()
        self.assertEqual(actual_result, 0, desc)

    def test_058_customForm_action(self):
        """自定义表单提交"""
        object = ApiRequestsOne()
        actual_result,desc = object.customForm_action()
        self.assertEqual(actual_result, 0, desc)

    def test_059_customForm_getListByIds(self):
        """该接口为后台接口，后期即将移除，请不要继续使用，获取表单列表"""
        object = ApiRequestsOne()
        actual_result,desc = object.customForm_getListByIds()
        self.assertEqual(actual_result, 0, desc)

    def test_060_seminar_trackingCode_getList(self):
        """获取渠道追踪代码列表"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_trackingCode_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_061_poll_stat_getResult(self):
        """获取每个投票选项的结果数量"""
        object = ApiRequestsOne()
        actual_result,desc = object.poll_stat_getResult()
        self.assertEqual(actual_result, 0, desc)

    def test_062_seminar_get(self):
        """获取会议详情"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_get()
        self.assertEqual(actual_result, 0, desc)

    def test_063_app_seminar_contact_nfc_getList(self):
        """该接口为APP专用接口，项目不要使用，获取nfc绑定关系列表"""
        object = ApiRequestsOne()
        actual_result,desc = object.app_seminar_contact_nfc_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_064_customForm_checkRegistration(self):
        """报名前验证"""
        object = ApiRequestsOne()
        actual_result,desc = object.customForm_checkRegistration()
        self.assertEqual(actual_result, 0, desc)

    def test_065_seminar_register_canRegisterNew(self):
        """会议是否可以报名"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_register_canRegisterNew()
        self.assertEqual(actual_result, 0, desc)

    def test_066_app_seminar_signingPoint_checkIn_create(self):
        """该接口为APP专用接口，项目不要使用，创建签到信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.app_seminar_signingPoint_checkIn_create()
        self.assertEqual(actual_result, 0, desc)


    def test_067_questionary_tool_checkRegistration(self):
        """报名前验证"""
        object = ApiRequestsOne()
        actual_result,desc = object.questionary_tool_checkRegistration()
        self.assertEqual(actual_result, 0, desc)


    def test_068_customForm_sendCheckCode(self):
        """自定义表单发送手机修改密码验证码"""
        object = ApiRequestsOne()
        actual_result,desc = object.customForm_sendCheckCode()
        self.assertEqual(actual_result, 0, desc)

    def test_069_seminar_contact_registerNew(self):
        """会议报名接口"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_contact_registerNew()
        self.assertEqual(actual_result, 0, desc)

    def test_070_seminar_bigScreen_forBigScreenWall_checkIn(self):
        """微信签到"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_bigScreen_forBigScreenWall_checkIn()
        self.assertEqual(actual_result, 0, desc)

    def test_071_seminar_bigScreen_updateCheckIn(self):
        """更新签到大屏信息"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_bigScreen_updateCheckIn()
        self.assertEqual(actual_result, 0, desc)

    def test_072_seminar_contact_update(self):
        """此接口即将过期不在维护，可使用seminar_contact_front_editRegContact标准格式实现"""
        object = ApiRequestsOne()
        actual_result,desc = object.seminar_contact_update()
        self.assertEqual(actual_result, 0, desc)

    def test_073_poll_view(self):
        """浏览投票"""
        object = ApiRequestsOne()
        actual_result,desc = object.poll_view()
        self.assertEqual(actual_result, 0, desc)

    def test_074_poll_action(self):
        """提交投票"""
        object = ApiRequestsOne()
        actual_result,desc = object.poll_action()
        self.assertEqual(actual_result, 0, desc)

    def test_075_questionary_reAction(self):
        """提交问卷"""
        object = ApiRequestsOne()
        actual_result,desc = object.questionary_reAction()
        self.assertEqual(actual_result, 0, desc)

    def test_076_questionary_exam_user_getAnswers(self):
        """获取某人试卷的试题记录"""
        object = ApiRequestsOne()
        actual_result,desc = object.questionary_exam_user_getAnswers()
        self.assertEqual(actual_result, 0, desc)

    def test_077_questionary_exam_repeatAction(self):
        """用户重复回答试题保留最后一次结果"""
        object = ApiRequestsOne()
        actual_result,desc = object.questionary_exam_repeatAction()
        self.assertEqual(actual_result, 0, desc)

    def test_078_app_seminar_contact_nfc_bind(self):
        """该接口为APP专用接口，项目不要使用，nfc批量绑定"""
        object = ApiRequestsOne()
        actual_result,desc = object.app_seminar_contact_nfc_bind()
        self.assertEqual(actual_result, 0, desc)

    def test_079_seminar_signingPoint_getNumberSignInPassage(self):
        """获取会议签到点签到统计信息"""
        object = ApiRequestsOne()
        actual_result, desc = object.seminar_signingPoint_getNumberSignInPassage()
        self.assertEqual(actual_result, 0, desc)

    def test_080_poll_get(self):
        """获取投票"""
        object = ApiRequestsOne()
        actual_result, desc = object.poll_get()
        self.assertEqual(actual_result, 0, desc)

    def test_081_api_seminar_app_checkinpoint_userpermit_query(self):
        """app专用，获取用户签到点权限列表"""
        object = ApiRequestsOne()
        actual_result, desc = object.api_seminar_app_checkinpoint_userpermit_query()
        self.assertEqual(actual_result, 0, desc)

    def test_082_api_template_config_get(self):
        """获取模板信息"""
        object = ApiRequestsOne()
        actual_result, desc = object.api_template_config_get()
        self.assertEqual(actual_result, 0, desc)










if __name__ == "__main__":
    #全部用例按照数字顺序测试
    #unittest.main()
    StartTime = time.time()
    suite = unittest.TestSuite()
    # 指定单个单元测试（ 需要配置运行方式才能走main函数，参考https://www.cnblogs.com/youreyebows/p/7867508.html）
    suite.addTest(Api_Case_Group1("test_010_de_contact_getLastSeminarsBySess"))



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