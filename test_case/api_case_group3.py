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
from pages.api.group3 import ApiRequestsThree
from pages.api import apicommon

"""
刘晓旺开发组
"""


class Api_Case_Group3(unittest.TestCase):
    """ 接口自动化三组测试用例 """

    def setUp(self):
        if apicommon.all_login() == 1:
            print "successful"
        else:
            print "get login session error"
    def test_001_article_getDetail(self):
        """获取文章详情信息"""
        object = ApiRequestsThree()
        actual_result,desc = object.article_getDetail()
        self.assertEqual(actual_result, 0, desc)

    def test_002_article_getListByProject(self):
        """获取文章列表"""
        object = ApiRequestsThree()
        actual_result,desc = object.article_getListByProject()
        self.assertEqual(actual_result, 0, desc)

    def test_003_file_getList(self):
        """获取文件列表"""
        object = ApiRequestsThree()
        actual_result,desc = object.file_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_004_weChat_getAppId(self):
        """获取微信信息"""
        object = ApiRequestsThree()
        actual_result,desc = object.weChat_getAppId()
        self.assertEqual(actual_result, 0, desc)

    def test_005_weChat_getConfig(self):
        """做微信签名用，获取jssdk配置"""
        object = ApiRequestsThree()
        actual_result,desc = object.weChat_getConfig()
        self.assertEqual(actual_result, 0, desc)

    def test_006_template_template_getConfig(self):
        """获取一个全局用户Id（cookieId）"""
        object = ApiRequestsThree()
        actual_result,desc = object.template_template_getConfig()
        self.assertEqual(actual_result, 0, desc)

    def test_007_articleCategory_get(self):
        """获取单个栏目"""
        object = ApiRequestsThree()
        actual_result,desc = object.articleCategory_get()
        self.assertEqual(actual_result, 0, desc)

    def test_008_articleCategory_getList(self):
        """获取栏目列表"""
        object = ApiRequestsThree()
        actual_result,desc = object.articleCategory_getList()
        self.assertEqual(actual_result, 0, desc)

    def test_009_articleCategory_getSubList(self):
        """获取文章分组列表"""
        object = ApiRequestsThree()
        actual_result,desc = object.articleCategory_getSubList()
        self.assertEqual(actual_result, 0, desc)

    def test_010_contact_getByOpenId(self):
        """通过openId获取联系人信息"""
        object = ApiRequestsThree()
        actual_result,desc = object.contact_getByOpenId()
        self.assertEqual(actual_result, 0, desc)

    def test_011_productLine_category_getCategoryTreeList(self):
        """获取产品线分类树"""
        object = ApiRequestsThree()
        actual_result,desc = object.productLine_category_getCategoryTreeList()
        self.assertEqual(actual_result, 0, desc)

    def test_012_article_browse(self):
        """文章浏览"""
        object = ApiRequestsThree()
        actual_result,desc = object.article_browse()
        self.assertEqual(actual_result, 0, desc)

    def test_013_file_getListForWeChat(self):
        """获取微信下的文件列表"""
        object = ApiRequestsThree()
        actual_result,desc = object.file_getListForWeChat()
        self.assertEqual(actual_result, 0, desc)

    def test_014_article_getRecommendedList(self):
        """获取栏目的子栏目中推荐的文章列表"""
        object = ApiRequestsThree()
        actual_result,desc = object.article_getRecommendedList()
        self.assertEqual(actual_result, 0, desc)

    def test_015_weChat_get(self):
        """该接口为后台接口，后期即将移除，请不要继续使用，获取微信信息"""
        object = ApiRequestsThree()
        actual_result,desc = object.weChat_get()
        self.assertEqual(actual_result, 0, desc)

    def test_016_weChat_getDef(self):
        """获取各平台默认微信号的配置信息"""
        object = ApiRequestsThree()
        actual_result,desc = object.weChat_getDef()
        self.assertEqual(actual_result, 0, desc)

    def test_017_article_share(self):
        """微信的jssdk"""
        object = ApiRequestsThree()
        actual_result,desc = object.article_share()
        self.assertEqual(actual_result, 0, desc)

    def test_018_contact_getContactStatus(self):
        """查询openId是否已关注微信号"""
        object = ApiRequestsThree()
        actual_result,desc = object.contact_getContactStatus()
        self.assertEqual(actual_result, 0, desc)

    def test_019_article_getLikeStatus(self):
        """获取此用户是否允许继续点赞,articleId和cookieId是必填字段,openId不传就以cookieId查询用户身份,传openId则cookieId和openId满足其一即可返回此用户的点赞状态"""
        object = ApiRequestsThree()
        actual_result,desc = object.article_getLikeStatus()
        self.assertEqual(actual_result, 0, desc)


    def test_020_article_like(self):
        """点赞，globalUserId、openId和sess至少填一个"""
        object = ApiRequestsThree()
        actual_result,desc = object.article_like()
        self.assertEqual(actual_result, 0, desc)

    def test_021_article_shareRecord(self):
        """分享记录，globalUserId、openId和sess至少填一个"""
        object = ApiRequestsThree()
        actual_result,desc = object.article_shareRecord()
        self.assertEqual(actual_result, 0, desc)

    def test_022_file_downloadWithEmail(self):
        """文章资料下载"""
        object = ApiRequestsThree()
        actual_result,desc = object.file_downloadWithEmail()
        self.assertEqual(actual_result, 0, desc)

    def test_023_article_getListByIds(self):
        """根据文章id数组获取文章列表信息"""
        object = ApiRequestsThree()
        actual_result,desc = object.article_getListByIds()
        self.assertEqual(actual_result, 0, desc)

    def test_024_contact_bindMember(self):
        """微信账号与会员绑定"""
        object = ApiRequestsThree()
        actual_result,desc = object.contact_bindMember()
        self.assertEqual(actual_result, 0, desc)

    def test_025_contact_bindMember(self):
        """创建邮件发送任务"""
        object = ApiRequestsThree()
        actual_result,desc = object.contact_bindMember()
        self.assertEqual(actual_result, 0, desc)

    def test_026_article_getTrees(self):
        """查询文章列表"""
        object = ApiRequestsThree()
        actual_result,desc = object.article_getTrees()
        self.assertEqual(actual_result, 0, desc)

    def test_027_edm_sendEmail(self):
        """中转接口发送邮件"""
        object = ApiRequestsThree()
        actual_result,desc = object.edm_sendEmail()
        self.assertEqual(actual_result, 0, desc)

    def test_028_api_article_category_query(self):
        """项目使用，获取栏目列表"""
        object = ApiRequestsThree()
        actual_result,desc = object.api_article_category_query()
        self.assertEqual(actual_result, 0, desc)

    def test_029_api_article_query(self):
        """获取文章列表"""
        object = ApiRequestsThree()
        actual_result,desc = object.api_article_query()
        self.assertEqual(actual_result, 0, desc)

    def test_030_api_content_collect_query(self):
        """查询我收藏的信息"""
        object = ApiRequestsThree()
        actual_result,desc = object.api_content_collect_query()
        self.assertEqual(actual_result, 0, desc)

    def test_031_api_file_query(self):
        """查询文件列表（带分页）"""
        object = ApiRequestsThree()
        actual_result,desc = object.api_file_query()
        self.assertEqual(actual_result, 0, desc)

    def test_032_api_productLine_query(self):
        """获取租户下产品线列表"""
        object = ApiRequestsThree()
        actual_result,desc = object.api_productLine_query()
        self.assertEqual(actual_result, 0, desc)

    def test_033_api_product_query(self):
        """获取产品线下产品列表"""
        object = ApiRequestsThree()
        actual_result,desc = object.api_product_query()
        self.assertEqual(actual_result, 0, desc)



if __name__ == "__main__":
    #全部用例按照数字顺序测试
    #unittest.main()
    StartTime = time.time()
    suite = unittest.TestSuite()
    # 指定单个单元测试（ 需要配置运行方式才能走main函数，参考https://www.cnblogs.com/youreyebows/p/7867508.html）
    suite.addTest(Api_Case_Group3("test_024_contact_bindMember"))



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