#-*-encoding:utf-8 -*-
"""
@version:1
@author:刘雅
@file:api_most_interface.py
@time:2019/1/3010:12
"""
import unittest
from pages.api import all_bl_out
from pages.api.api_most_all import api_most_all
import common.common_function.globalvar as gl
import datetime
# import common.dingding.dingding as dingding
class HW_UAT_interface(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global list
        list=all_bl_out.get_all_bl('HW_UAT')
        api_most_all().set_zero_count_total()
        #设置全局变量为当前时间戳
        gl._init()
        serialnum = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        print (serialnum)
        gl.set_value('serialnum',serialnum)
    @classmethod
    def tearDownClass(cls):
        # 将总的结果保存到结果表中
        api_most_all().write_to_execution_result('HW_UAT')
        #发钉钉
        # platform_name = 'HW_UAT'
        # serialnum = gl.get_value('serialnum')
        # loginfo, casecount = dingding.getLoginfo(platform_name, serialnum)
        # platname = u'华为产品'  # 接口测试平台名称
        # if casecount > 0 :
        #     dingding.dd(loginfo, casecount, platname)
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_001_account_login(self):
        flag,bakSess=api_most_all().hw_uat_account_login("HW_UAT",list['HW_UAT_domain'],list['email'],list['password'])
        self.assertEqual(flag,0,"获取后台登录session失败")
        list['bakSess']=bakSess
    def test_002_member_login(self):
        flag, loginSess =api_most_all().member_login('HW_UAT',list['HW_UAT_domain'],list['tenantId'],list['schemaId'],list['memberFormId'],list['memberSchemaId'],list['unique'],list['member_password'])
        self.assertEqual(flag, 0, "获取前台登录session失败")
        list['loginSess'] = loginSess
    def test_003_seminar_contact_setContactToWechat(self):
        result, desc = api_most_all().seminar_contact_setContactToWechat("HW_UAT",list['HW_UAT_domain'],list['seminarId'],list['contactId'],list['wechatId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # 修改前台登录用户的密码-jch
    def test_005_api_member_password_update(self):
        result,desc = api_most_all().api_member_password_update("HW_UAT",list['HW_UAT_domain'],list['tenantId'],list['member_password'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # 注册用户简单登录(通过OpenId或账号密码登录)
    def test_006_api_member_contacts_simple_signin(self):
        result, desc = api_most_all().api_member_contacts_simple_signin("HW_UAT", list["HW_UAT_domain"], list['tenantId'],list["unique"],list["member_password"],list['memberFormId'])
        self.assertEqual(result, 0, desc)
    # member_identification_UpdateAvatar 修改注册用户头像
    def test_007_member_identification_UpdateAvatar(self):
        result, desc = api_most_all().member_identification_UpdateAvatar("HW_UAT", list["HW_UAT_domain"], list['tenantId'],list["schemaId"], list["loginSess"])
        self.assertEqual(result, 0, desc)
    # member_update更新用户信息
    def test_008_member_update(self):
        result, desc = api_most_all().member_update("HW_UAT", list["HW_UAT_domain"], list['nophoneform'],list["loginSess"])
        self.assertEqual(result, 0, desc)
    #articleCategory_get获取文章列表
    def test_009_articleCategory_get(self):
        result, desc = api_most_all().articleCategory_get("HW_UAT", list["HW_UAT_domain"], list['loginSess'], list["tenantId"], list["nodeId"])
        self.assertEqual(result, 0, desc)
    # comment_getList评论列表
    def test_010_comment_getList(self):
        result, desc = api_most_all().comment_getList("HW_UAT", list["HW_UAT_domain"], list['tenantId'], list["topicId"],list["loginSess"])
        self.assertEqual(result, 0, desc)
    # 获取微讨论的详情
    def test_011_forum_getForumInfo(self):
        result, desc = api_most_all().forum_getForumInfo("HW_UAT", list["HW_UAT_domain"], list['global_topicId'], list["tenantId"])
        self.assertEqual(result, 0, desc)
    # forum_getReplyList/获取微论坛的回复列表
    def test_012_forum_getReplyList(self):
        result, desc = api_most_all().forum_getReplyList("HW_UAT", list["HW_UAT_domain"], list['global_topicId'],list["loginSess"])
        self.assertEqual(result, 0, desc)
    #forum_post_create/微论坛发贴回复
    def test_013_forum_post_create(self):
        result, desc ,pos= api_most_all().forum_post_create("HW_UAT", list["HW_UAT_domain"], list['topicId'],list["section_create"])
        self.assertEqual(result, 0, desc)
        list["pos"]=pos
    # forum_post_get/微论坛帖子详情
    def test_014_forum_post_get(self):
        result, desc = api_most_all().forum_post_get("HW_UAT", list["HW_UAT_domain"], list['tenantId'], list['nodeId'], list["postId"])
        self.assertEqual(result, 0, desc)
    # article_browse 文章浏览
    def test_015_article_browse(self):
        result, desc = api_most_all().article_browse("HW_UAT", list['HW_UAT_domain'], list['articleId'])
        self.assertEqual(result, 0, desc)
    # forum_post_getMainPost 获取微讨论的主贴列表
    def test_016_forum_post_getMainPost(self):
        result, desc = api_most_all().forum_post_getMainPost("HW_UAT", list['HW_UAT_domain'], list['global_topicId'])
        self.assertEqual(result, 0, desc)
    # forum_post_getMainPostNumber/微论坛主贴和回帖统计
    def test_017_forum_post_getMainPostNumber(self):
        result, desc = api_most_all().forum_post_getMainPostNumber("HW_UAT", list['HW_UAT_domain'], list['global_topicId'])
        self.assertEqual(result, 0, desc)
    # forum_post_getPersonalPostList/微论坛查看个人或者他人帖子信息
    def test_018_forum_post_getPersonalPostList(self):
        result, desc = api_most_all().forum_post_getPersonalPostList("HW_UAT", list['HW_UAT_domain'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # forum_post_getReplyPost/获取微讨论的主贴ID
    def test_019_forum_post_getReplyPost(self):
        result, desc = api_most_all().forum_post_getReplyPost("HW_UAT", list['HW_UAT_domain'], list['pos'])
        self.assertEqual(result, 0, desc)
    # forum_post_like / 微论坛给帖子点赞
    def test_020_forum_post_like(self):
        result, desc = api_most_all().forum_post_like("HW_UAT", list['HW_UAT_domain'], list['postId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # forum_post_update/更新帖子内容
    def test_021_forum_post_update(self):
        result,desc=api_most_all().forum_post_update("HW_UAT",list['HW_UAT_domain'],list['tenantId'],list['nodeId'],list['section_create'])
        self.assertEqual(result, 0, desc)
    # forum_section_getList/获取某个微论坛的子版列表
    def test_022_forum_section_getList(self):
        result, desc = api_most_all().forum_section_getList("HW_UAT", list['HW_UAT_domain'], list['global_topicId'])
        self.assertEqual(result, 0, desc)
    # article_browseRecord / 文章浏览
    def test_023_article_browseRecord(self):
        result, desc = api_most_all().article_browseRecord("HW_UAT", list['HW_UAT_domain'], list['articleId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # forum_stat_homePage/微论坛帖子列表
    def test_024_forum_stat_homePage(self):
        result, desc = api_most_all().forum_stat_homePage("HW_UAT", list['HW_UAT_domain'], list['section_create'], list['global_topicId'])
        self.assertEqual(result, 0, desc)
    # article_Collection/文章收藏
    def test_025_article_Collection(self):
        result, desc = api_most_all().article_Collection("HW_UAT", list['HW_UAT_domain'], list['articleId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # forum_post_deletePost/删除自己发的帖子
    def test_026_forum_post_deletePost(self):
        result, desc= api_most_all().forum_post_deletePost("HW_UAT", list["HW_UAT_domain"], list['topicId'],list["pos"])
        self.assertEqual(result, 0, desc)
    # file_create/该接口为后台接口，后期即将移除，请不要继续使用，上传文件
    def test_027_file_create(self):
        result, desc,fileId= api_most_all().file_create("HW_UAT", list["HW_UAT_domain"], list['tenantId'], list['FolderId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
        list["fileIds"]=fileId
    # article_getDetail/获取文章详情
    def test_028_article_getDetail(self):
        result, desc, topicId = api_most_all().article_getDetail("HW_UAT", list["HW_UAT_domain"], list['articleId'])
        self.assertEqual(result, 0, desc)
    #article_getLikeStatus/获取此用户是否允许继续点赞
    def test_029_article_getLikeStatus(self):
        result, desc, = api_most_all().article_getLikeStatus("HW_UAT", list["HW_UAT_domain"], list['articleId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #article_getList/该接口即将过期不在维护，使用article_getListByProject替代
    def test_030_article_getList(self):
        result, desc, = api_most_all().article_getList("HW_UAT", list["HW_UAT_domain"], list['tenantId'], list['loginSess'],list['categoryId'])
        self.assertEqual(result, 0, desc)
    # article_getListByIds/根据文章id数组获取文章列表信息
    def test_031_article_getListByIds(self):
        result, desc, = api_most_all().article_getListByIds("HW_UAT", list["HW_UAT_domain"], list['articleId'])
        self.assertEqual(result, 0, desc)
    # article_getListByProject/获取文章列表
    def test_032_article_getListByProject(self):
        result, desc, = api_most_all().article_getListByProject("HW_UAT", list["HW_UAT_domain"], list['tenantId'],list['categoryId'])
        self.assertEqual(result, 0, desc)
    # file_update/该接口为后台接口，后期即将移除，请不要继续使用，修改文件
    def test_033_file_update(self):
        result, desc= api_most_all().file_update("HW_UAT", list["HW_UAT_domain"], list['tenantId'],list['fileIds'],list['mappingId'],list['FolderId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # questionary_get/获取问卷信息
    def test_034_questionary_get(self):
        result, desc = api_most_all().questionary_get("HW_UAT", list["HW_UAT_domain"], list["questionid_wj"])
        self.assertEqual(result, 0, desc)
    # questionary_view/浏览问卷
    def test_035_questionary_view(self):
        result, desc = api_most_all().questionary_view("HW_UAT", list['HW_UAT_domain'], list['questionid_wj'])
        self.assertEqual(result, 0, desc)
    # questionary_action/提交问卷
    def test_036_questionary_action(self):
        result, desc = api_most_all().questionary_action("HW_UAT", list['HW_UAT_domain'], list['questionid_sj'])
        self.assertEqual(result, 0, desc)
    # article/like-文章点赞
    def test_037_article_like(self):
        result, desc = api_most_all().article_like("HW_UAT", list['HW_UAT_domain'], list['articleId'], list['wechatId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # comment_create/新增文章评论           （article_topicId）不知道用哪个，暂时未执行
    def test_038_comment_create(self):
        result, desc, pos = api_most_all().comment_create("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['nodeId'],list['article_topicId'])
        self.assertEqual(result, 0, desc)
        list['content'] = pos
    # comment_front_delete/删除评论 内容           与038有关联，未执行
    def test_039_comment_front_delete(self):
        result, desc = api_most_all().comment_front_delete("HW_UAT", list['HW_UAT_domain'], list['topicId'],list['content'])
        self.assertEqual(result, 0, desc)
    # comment_like评论内容                       与038有关联，未执行
    def test_040_comment_like(self):
        result, desc = api_most_all().comment_like("HW_UAT", list['HW_UAT_domain'], list['content'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # article_getListByTag/获取租户下文章列表，可通过标签筛选
    def test_041_article_getListByTag(self):
        result, desc = api_most_all().article_getListByTag("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # article_getListForProject/获取文章列表
    def test_042_article_getListForProject(self):
        result, desc = api_most_all().article_getListForProject("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['categoryId'], list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # article_getRecommendedList/获取栏目的子栏目中推荐的文章列表
    def test_043_article_getRecommendedList(self):
        result, desc = api_most_all().article_getRecommendedList("HW_UAT", list['HW_UAT_domain'], list['categoryId'])
        self.assertEqual(result, 0, desc)
    # article_getSharedList/获取分享文章列表
    def test_044_article_getSharedList(self):
        result, desc = api_most_all().article_getSharedList("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['nodeId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # article_getTrees/查询文章列表
    def test_045_article_getTrees(self):
        result, desc = api_most_all().article_getTrees("HW_UAT", list['HW_UAT_domain'], list
        ['bakSess'], list['tenantId'], list['categoryId'])
        self.assertEqual(result, 0, desc)
    # collect_add/收藏信息
    def test_046_collect_add(self):
        result, desc, pos = api_most_all().collect_add("HW_UAT", list['HW_UAT_domain'], list
        ['loginSess'])
        self.assertEqual(result, 0, desc)
        list["collectionid"] = pos
    # collect_cancel/取消收藏信息
    def test_047_collect_cancel(self):
        result, desc = api_most_all().collect_cancel("HW_UAT", list['HW_UAT_domain'], list
        ['collectionid'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # collect_search/查询收藏的信息列表
    def test_048_collect_search(self):
        result, desc = api_most_all().collect_search("HW_UAT", list['HW_UAT_domain'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # articleCategory_getList/获取栏目列表
    def test_049_articleCategory_getList(self):
        result, desc = api_most_all().articleCategory_getList("HW_UAT", list['HW_UAT_domain'], list
        ['tenantId'], list['categoryId'])
        self.assertEqual(result, 0, desc)
    # articleCategory_getSubList/获取文章分组列表
    def test_050_articleCategory_getSubList(self):
        result,desc = api_most_all().articleCategory_getSubList("HW_UAT",list['HW_UAT_domain'],list['categoryId'])
        self.assertEqual(result, 0, desc)
    # questionary_getList/获取问卷列表
    def test_051_questionary_getList(self):
        result,desc = api_most_all().articleCategory_getSubList("HW_UAT",list['HW_UAT_domain'],list['tenantId'])
        self.assertEqual(result, 0, desc)
    # questionary_reAction/提交试卷
    def test_052_questionary_reAction(self):
        code= api_most_all().questionary_reAction("HW_UAT",list['HW_UAT_domain'],list['questionid_wj'],list['questionid_item'])
        self.assertEqual(code, 200, "断言200失败")
    # article_share/文章分享
    def test_053_article_share(self):
        result,desc = api_most_all().article_share("HW_UAT",list['HW_UAT_domain'],list['articleId'],list['wechatId'])
        self.assertEqual(result, 0, desc)
    # file_folder_getInsOfFileList/获取实例下的文件列表
    def test_054_file_folder_getInsOfFileList(self):
        result, desc = api_most_all().file_folder_getInsOfFileList("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # questionary_exam_action/用户答题
    def test_055_questionary_exam_action(self):
        result, desc = api_most_all().questionary_exam_action("HW_UAT", list['HW_UAT_domain'], list['questionid_sj'])
        self.assertEqual(result, 0, desc)
    # seminar_guest_getList/获取会议嘉宾列表
    def test_056_seminar_guest_getList(self):
        result, desc = api_most_all().seminar_guest_getList("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId'])
        self.assertEqual(result, 0, desc)
    # seminar_guest_getGroupList/获取嘉宾列表
    def test_057_seminar_guest_getGroupList(self):
        result, desc = api_most_all().seminar_guest_getGroupList("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_guest_field_Get/获取嘉宾字段列表
    def test_058_api_seminar_guest_field_Get(self):
        result, desc = api_most_all().api_seminar_guest_field_Get("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # guest_get/获取全局嘉宾信息
    def test_059_guest_get(self):
        result, desc = api_most_all().guest_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['guestId'])
        self.assertEqual(result, 0, desc)
    # guest_getList/取租户嘉宾列表
    def test_060_guest_getList(self):
        result, desc = api_most_all().guest_getList("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # file_getListForWeChat/获取微信下的文件 [注]：此用例要与test_file_create_027同时执行
    def test_061_file_getListForWeChat(self):
        result, desc = api_most_all().file_getListForWeChat("HW_UAT", list['HW_UAT_domain'], list['fileIds'])
        self.assertEqual(result, 0, desc)
    # poll_get/获取投票
    def test_062_poll_get(self):
        result, desc = api_most_all().poll_get("HW_UAT", list['HW_UAT_domain'], list['pollId'])
        self.assertEqual(result, 0, desc)
    # seminar_agenda_get/获取会议日程信息
    def test_063_seminar_agenda_get(self):
        result, desc = api_most_all().seminar_agenda_get("HW_UAT", list['HW_UAT_domain'], list['seminarId'], list['agendaId'])
        self.assertEqual(result, 0, desc)
    # seminar_agenda_getGroupList/获取会议日程按天分组
    def test_064_seminar_agenda_getGroupList(self):
        result, desc = api_most_all().seminar_agenda_getGroupList("HW_UAT", list['HW_UAT_domain'], list['seminarId'])
        self.assertEqual(result, 0, desc)
    # poll_action/提交投票
    def test_065_poll_action(self):
        result, desc = api_most_all().poll_action("HW_UAT", list['HW_UAT_domain'], list['pollId'])
        self.assertEqual(result, 0, desc)
    # poll_getList/获取投票列表
    def test_066_poll_getList(self):
        result, desc = api_most_all().poll_getList("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # poll_HasParticipation/浏览投票
    def test_067_poll_HasParticipation(self):
        result, desc = api_most_all().poll_HasParticipation("HW_UAT", list['HW_UAT_domain'], list['pollId'])
        self.assertEqual(result, 0, desc)
    # poll_sendCheckCode/投票发送验证码
    def test_068_poll_sendCheckCode(self):
        result, desc = api_most_all().poll_sendCheckCode("HW_UAT", list['HW_UAT_domain'], list['pollId'])
        self.assertEqual(result, 0, desc)
    # poll_start/该接口为后台接口，后期即将移除，请不要继续使用，开始投票
    def test_069_poll_start(self):
        result, desc = api_most_all().poll_start("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['seminarId_instanceId'], list['pollId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # poll_stat_getResult / 获取每个投票选项的结果数量
    def test_070_poll_stat_getResult(self):
        result, desc = api_most_all().poll_stat_getResult("HW_UAT", list['HW_UAT_domain'], list['pollId'])
        self.assertEqual(result, 0, desc)
    # poll_stat_getTotal/返回总投票数
    def test_071_poll_stat_getTotal(self):
        result, desc = api_most_all().poll_stat_getTotal("HW_UAT", list['HW_UAT_domain'], list['pollId'])
        self.assertEqual(result, 0, desc)
    # poll_tool_checkRegistration/报名前验证
    def test_072_poll_tool_checkRegistration(self):
        result, desc = api_most_all().poll_tool_checkRegistration("HW_UAT", list['HW_UAT_domain'], list['pollId'],list['seminarId_instanceId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # poll_view/浏览投票
    def test_073_poll_view(self):
        result, desc = api_most_all().poll_view("HW_UAT", list['HW_UAT_domain'], list['pollId'])
        self.assertEqual(result, 0, desc)
    # product_crossLine_getList/获取租户下的某一分类的多产品线下的产品列表
    def test_074_product_crossLine_getList(self):
        result, desc = api_most_all().product_crossLine_getList("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # product_get/获取产品详细信息
    def test_075_product_get(self):
        result, desc = api_most_all().product_get("HW_UAT", list['HW_UAT_domain'], list['productLine'])
        self.assertEqual(result, 0, desc)
    # product_getList/获取产品线下产品列表
    def test_076_product_getList(self):
        result, desc = api_most_all().product_getList("HW_UAT", list['HW_UAT_domain'], list['bakSess'], list['productLineId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # productLine_category_getCategoryTreeList/获取产品线分类树
    def test_077_productLine_category_getCategoryTreeList(self):
        result, desc = api_most_all().productLine_category_getCategoryTreeList("HW_UAT", list['HW_UAT_domain'],list['productLineId'])
        self.assertEqual(result, 0, desc)
    # productLine_category_getConfigInfo/获取某产品线下具体某个字典值的配置信息
    def test_078_productLine_category_getConfigInfo(self):
        result, desc = api_most_all().productLine_category_getConfigInfo("HW_UAT", list['HW_UAT_domain'],list['productLineId'])
        self.assertEqual(result, 0, desc)
    # productLine_category_getDetailList/获取产品线分类详细列表
    def test_079_productLine_category_getDetailList(self):
        result, desc = api_most_all().productLine_category_getDetailList("HW_UAT", list['HW_UAT_domain'],list['productLineId'])
        self.assertEqual(result, 0, desc)
    # productLine_category_getList/获取产品线下产品分类的子分类信息
    def test_080_productLine_category_getList(self):
        result, desc = api_most_all().productLine_category_getList("HW_UAT", list['HW_UAT_domain'], list['productLineId'], list['dicId'])
        self.assertEqual(result, 0, desc)
    # productLine_field_get/获取某个产品线的字段列表
    def test_081_productLine_field_get(self):
        result, desc = api_most_all().productLine_field_get("HW_UAT", list['HW_UAT_domain'], list['productLineId'])
        self.assertEqual(result, 0, desc)
    # productLine_get/获取产品线的信息
    def test_082_productLine_get(self):
        result, desc = api_most_all().productLine_get("HW_UAT", list['HW_UAT_domain'], list['productLineId'])
        self.assertEqual(result, 0, desc)
    # productLine_getList/获取租户下产品线列表
    def test_083_productLine_getList(self):
        result, desc = api_most_all().productLine_getList("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # weChat_get/该接口为后台接口，后期即将移除，请不要继续使用，获取微信信息
    def test_084_weChat_get(self):
        result, desc = api_most_all().weChat_get("HW_UAT", list['HW_UAT_domain'], list['wechatId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # weChat_getAppId/获取微信信息
    def test_085_weChat_getAppId(self):
        result, desc = api_most_all().weChat_getAppId("HW_UAT", list['HW_UAT_domain'], list['wechatId'])
        self.assertEqual(result, 0, desc)
    # weChat_getConfig/做微信签名用，获取jssdk配置
    def test_086_weChat_getConfig(self):
        result, desc = api_most_all().weChat_getConfig("HW_UAT", list['HW_UAT_domain'], list['wechatId'])
        print "list['wechatId']:",list['wechatId']
        self.assertEqual(result, 0, desc)
    # weChat_getDef/获取各平台默认微信号的配置信息
    def test_087_weChat_getDef(self):
        result, desc = api_most_all().weChat_getDef("HW_UAT", list['HW_UAT_domain'])
        self.assertEqual(result, 0, desc)
    # weChat_getDefWx/获取各平台默认微信号的配置信息
    def test_088_weChat_getDefWx(self):
        result, desc = api_most_all().weChat_getDefWx("HW_UAT", list['HW_UAT_domain'])
        self.assertEqual(result, 0, desc)
    # api_product_get/获取产品详情
    def test_089_api_product_get(self):
        result, desc = api_most_all().api_product_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['productLine'])
        self.assertEqual(result, 0, desc)
    # api_productLine_category_config_get/获取某产品线下具体某个字典值的配置信息
    def test_090_api_productLine_category_config_get(self):
        result, desc = api_most_all().api_productLine_category_config_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['productLineId'])
        self.assertEqual(result, 0, desc)
    # api_productLine_category_query/获取产品线分类树
    def test_091_api_productLine_category_query(self):
        result, desc = api_most_all().api_productLine_category_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['productLineId'], list['dicId'])
        self.assertEqual(result, 0, desc)
    # api_productLine_field_get/获取某个产品线的字段列表
    def test_092_api_productLine_field_get(self):
        result, desc = api_most_all().api_productLine_field_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['productLineId'])
        self.assertEqual(result, 0, desc)
    # webinar_event_interaction_check/检查什么情况下可以继续投票、答问卷，会场开放过程中可以答
    def test_093_webinar_event_interaction_check(self):
        result, desc = api_most_all().webinar_event_interaction_check("HW_UAT", list['HW_UAT_domain'],list['webinarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # webinar_event_interaction_pollResult/答完问卷后置接口，记录互动结果
    def test_094_webinar_event_interaction_pollResult(self):
        result, desc = api_most_all().webinar_event_interaction_pollResult("HW_UAT", list['HW_UAT_domain'],list['loginSess'], list['pollId'])
        self.assertEqual(result, 0, desc)
    # webinar_open_attend/修改参会人数,并返回登录人的地址
    def test_095_webinar_open_attend(self):
        result, desc = api_most_all().webinar_open_attend("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['webinarId_instanceId'])
        self.assertEqual(result, 0, desc)
    #  webinar_open_checkRegistration/查询用户是否可以报名接口
    def test_096_webinar_open_checkRegistration(self):
        result, desc = api_most_all().webinar_open_checkRegistration("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['webinarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # webinar_open_getApplicantInfo/获取会议信息
    def test_097_webinar_open_getApplicantInfo(self):
        result, desc = api_most_all().webinar_open_getApplicantInfo("HW_UAT", list['HW_UAT_domain'],list['webinarId_instanceId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # webinar_open_getAttendList/获取已报名的会议列表
    def test_098_webinar_open_getAttendList(self):
        result, desc = api_most_all().webinar_open_getAttendList("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # webinar_open_getCustomFormInfo/获取自定义表单
    def test_099_webinar_open_getCustomFormInfo(self):
        result, desc = api_most_all().webinar_open_getCustomFormInfo("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['webinarId_instanceId'],list['customFormId'])
        self.assertEqual(result, 0, desc)
    # seminar_bigScreen_forBigScreenWall_checkIn/有问题，微信签到
    def test_100_seminar_bigScreen_forBigScreenWall_checkIn(self):
        result, desc = api_most_all().seminar_bigScreen_forBigScreenWall_checkIn("HW_UAT", list['HW_UAT_domain'],list['contactId'],list['loginSess'],list['bigScreenId'])
        self.assertEqual(result, 0, desc)
    # webinar_open_getDemandInfo/得到一个点播会议的详情信息
    def test_101_webinar_open_getDemandInfo(self):
        result, desc = api_most_all().webinar_open_getDemandInfo("HW_UAT", list['HW_UAT_domain'],list['tenantId'],list['webinarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # webinar_open_getServerTime/获取服务器时间
    def test_102_webinar_open_getServerTime(self):
        result, desc = api_most_all().webinar_open_getServerTime("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # webinar_open_getVideoTimeLine/获取视频信息
    def test_103_webinar_open_getVideoTimeLine(self):
        result, desc = api_most_all().webinar_open_getVideoTimeLine("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # webinar_open_getWebinarInfo/获取会场详细信息
    def test_104_webinar_open_getWebinarInfo(self):
        result, desc = api_most_all().webinar_open_getWebinarInfo("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['webinarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # webinar_open_getWebinarList/获取直播会议列表
    def test_105_webinar_open_getWebinarList(self):
        result, desc = api_most_all().webinar_open_getWebinarList("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # customForm_action/线上会报名[注]：此用例要与用例test_member_login_002同时执行
    def test_106_customForm_action(self):
        result, desc = api_most_all().customForm_action("HW_UAT", list['HW_UAT_domain'], list['loginSess'], list['customFormId'], list['webinarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # webinar_open_join/人员参会接口
    def test_107_webinar_open_join(self):
        result, desc = api_most_all().webinar_open_join("HW_UAT", list['HW_UAT_domain'],list['loginSess'],list['webinarId_instanceId'],list['tenantId'])
        self.assertEqual(result, 0, desc)
    # webinar_project_shenWan_GetWebinar/获取会议信息
    def test_108_webinar_project_shenWan_GetWebinar(self):
        result, desc = api_most_all().webinar_project_shenWan_GetWebinar("HW_UAT", list['HW_UAT_domain'],list['webinarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # webinar_project_shenWan_GetListByIds/跟进会议id数组 获取会议列表
    def test_109_webinar_project_shenWan_GetListByIds(self):
        result, desc = api_most_all().webinar_project_shenWan_GetListByIds("HW_UAT", list['HW_UAT_domain'],list['seminarId'])
        self.assertEqual(result, 0, desc)
    # webinar_project_shenWan_GetDemandList/获取已发布的点播列表
    def test_110_webinar_project_shenWan_GetDemandList(self):
        result, desc = api_most_all().webinar_project_shenWan_GetDemandList("HW_UAT", list['HW_UAT_domain'],list['tenantId'])
        self.assertEqual(result, 0, desc)
    # webinar_open_trackingCode_getList/根据实例编号获取该实例的渠道追踪代码
    def test_111_webinar_open_trackingCode_getList(self):
        result, desc = api_most_all().webinar_open_trackingCode_getList("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['webinarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # webinar_open_recordVideoViewCount/记录并获取点播视频的播放次数
    def test_112_webinar_open_recordVideoViewCount(self):
        result, desc = api_most_all().webinar_open_recordVideoViewCount("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['webinarId_DianBo'],list['videoId'])
        self.assertEqual(result, 0, desc)
    # questionary_exam_repeatAction/用户重复回答试题保留最后一次结果
    def test_113_questionary_exam_repeatAction(self):
        result, desc = api_most_all().questionary_exam_repeatAction("HW_UAT", list['HW_UAT_domain'], list['loginSess'],list['questionid_sj'])
        self.assertEqual(result, 0, desc)
    # 试卷添加题目
    def test_114_toolb_add_title(self):
        result, desc = api_most_all().toolb_add_title("HW_UAT", list['HW_UAT_domain_com'], list['bakSess'],list['questionid_sj'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # questionary_exam_user_GenerateExam/生成试卷
    def test_115_questionary_exam_user_GenerateExam(self):
        result, desc = api_most_all().questionary_exam_user_GenerateExam("HW_UAT", list['HW_UAT_domain'],list['questionid_sjsj'])
        self.assertEqual(result, 0, desc)
    # webinar_open_getWebinarListAdvanced/获取直播会议列表（高级查询功能）,有问题
    def test_116_webinar_open_getWebinarListAdvanced(self):
        code= api_most_all().webinar_open_getWebinarListAdvanced("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(code,200, "状态码不是200")
    # questionary_exam_user_getAnswers/获取某人试卷的试题记录
    def test_117_questionary_exam_user_getAnswers(self):
        result, desc = api_most_all().questionary_exam_user_getAnswers("HW_UAT", list['HW_UAT_domain'],list['questionid_wj'])
        self.assertEqual(result, 0, desc)
    # questionary_exam_user_getSingleResult/获取某人的答题记录
    def test_118_questionary_exam_user_getSingleResult(self):
        result, desc = api_most_all().questionary_exam_user_getSingleResult("HW_UAT", list['HW_UAT_domain'],list['questionid_sj'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # 问卷设置短信发送验证码
    def test_119_setting_Verification_code(self):
        result, desc = api_most_all().setting_Verification_code("HW_UAT", list['HW_UAT_domain_com'], list['bakSess'],list['questionid_wj'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # questionary_sendCheckCode/问卷发送验证码
    def test_120_questionary_sendCheckCode(self):
        result, desc = api_most_all().questionary_sendCheckCode("HW_UAT", list['HW_UAT_domain'], list['questionid_wj'], list['tenantId'])
        print "list['questionid_wj']:", list['questionid_wj']
        print "list['tenantId']:", list['tenantId']
        self.assertEqual(result, 0, desc)
    # shortUrl_getList/获取短地址
    def test_121_shortUrl_getList(self):
        result, desc = api_most_all().shortUrl_getList("HW_UAT", list['HW_UAT_domain'])
        self.assertEqual(result, 0, desc)
    # api_webinar_contacts_get/获取报名人信息/返回报名人状态
    def test_122_api_webinar_contacts_get(self):
        result, desc = api_most_all().api_webinar_contacts_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['webinarId_instanceId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # shortUrl_urlStats/获取短网址的统计信息
    def test_123_shortUrl_urlStats(self):
        result, desc = api_most_all().shortUrl_urlStats("HW_UAT", list['HW_UAT_domain'])
        self.assertEqual(result, 0, desc)
    # api_webinar_demand_get/获取点播信息
    def test_124_api_webinar_demand_get(self):
        result, desc = api_most_all().api_webinar_demand_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['webinarId'])
        self.assertEqual(result, 0, desc)
    # api_webinar_query/获取会议列表
    def test_125_api_webinar_query(self):
        result, desc = api_most_all().api_webinar_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # questionary_tool_checkRegistration / 报名前验证
    def test_126_questionary_tool_checkRegistration(self):
        result, desc = api_most_all().questionary_tool_checkRegistration("HW_UAT", list['HW_UAT_domain'], list['webinar_question_wj'], list['webinarId_instanceId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # questionary_stat_getResultByAnswerRecord/获取[常规问卷、leads问卷、非随机试卷]答题记录列表(此接口项目使用)
    def test_127_questionary_stat_getResultByAnswerRecord(self):
        result, desc = api_most_all().questionary_stat_getResultByAnswerRecord("HW_UAT", list['HW_UAT_domain'], list['bakSess'],list['questionid_wj'],)
        self.assertEqual(result, 0, desc)
    # seminar_bigScreen_get/获取大屏详细信息
    def test_128_seminar_bigScreen_get(self):
        result, desc = api_most_all().seminar_bigScreen_get("HW_UAT", list['HW_UAT_domain'], list['bigScreenId'] )
        self.assertEqual(result, 0, desc)
    # seminar_bigScreen_getListByGroup/获取大屏列表
    def test_129_seminar_bigScreen_getListByGroup(self):
        result, desc = api_most_all().seminar_bigScreen_getListByGroup("HW_UAT", list['HW_UAT_domain'], list['bigScreenId'])
        self.assertEqual(result, 0, desc)
    # seminar_bigScreen_getPollPreset/获取投票大屏预设信息
    def test_130_seminar_bigScreen_getPollPreset(self):
        result, desc = api_most_all().seminar_bigScreen_getPollPreset("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId'], list['bigScreenId'],list['pollId'])
        self.assertEqual(result, 0, desc)
    # seminar_bigScreen_updateCheckIn/更新签到大屏信息
    def test_131_seminar_bigScreen_updateCheckIn(self):
        result, desc = api_most_all().seminar_bigScreen_updateCheckIn("HW_UAT", list['HW_UAT_domain'], list['seminarId'],list['bigScreenId'], list['signingPointId'])
        self.assertEqual(result, 0, desc)
    # seminar_bigScreen_updateLottery/该接口为后台接口，后期即将移除，请不要继续使用，更新留言大屏信息
    def test_132_seminar_bigScreen_updateLottery(self):
        result, desc = api_most_all().seminar_bigScreen_updateLottery("HW_UAT", list['HW_UAT_domain'], list['seminarId'],list['bigScreenId'], list['topicId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # seminar_bigScreen_updateMessage/该接口为后台接口，后期即将移除，请不要继续使用，更新大屏消息
    def test_133_seminar_bigScreen_updateMessage(self):
        result, desc = api_most_all().seminar_bigScreen_updateMessage("HW_UAT", list['HW_UAT_domain'], list['seminarId'],list['bigScreenId'], list['topicId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # seminar_bigScreen_updatePoll/更新投票大屏
    def test_134_seminar_bigScreen_updatePoll(self):
        result, desc = api_most_all().seminar_bigScreen_updatePoll("HW_UAT", list['HW_UAT_domain'], list['seminarId'],list['bigScreenId'], list['pollId'])
        self.assertEqual(result, 0, desc)
    # seminar_canInteraction/投票线下会前调接口，如果会议已结束，返回结果会有错误信息
    def test_135_seminar_canInteraction(self):
        result, desc = api_most_all().seminar_canInteraction("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # seminar_contact_checkIdCard/检查身份证号是否存在
    def test_136_seminar_contact_checkIdCard(self):
        result, desc = api_most_all().seminar_contact_checkIdCard("HW_UAT", list['HW_UAT_domain'])
        self.assertEqual(result, 0, desc)
    # seminar_contact_front_checkIn / 参会人签到
    def test_137_seminar_contact_front_checkIn(self):
        result, desc = api_most_all().seminar_contact_front_checkIn("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId'], list['signingPointIds'],list['passageId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # seminar_contact_front_editRegContact/通过前台sess更新注册信息,如果有会议id则同时更新报名信息
    def test_138_seminar_contact_front_editRegContact(self):
        result, desc = api_most_all().seminar_contact_front_editRegContact("HW_UAT", list['HW_UAT_domain'],list['seminarId'],list['seminarId_instanceId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # seminar_contact_front_getCommonContactInfo / 获取参会人员信息
    def test_139_seminar_contact_front_getCommonContactInfo(self):
        result, desc = api_most_all().seminar_contact_front_getCommonContactInfo("HW_UAT", list['HW_UAT_domain'],list['seminarId'], list['unique'])
        self.assertEqual(result, 0, desc)
    # seminar_contact_front_getContactInfo/根据会议id和唯一字段获取参会人信息
    def test_140_seminar_contact_front_getContactInfo(self):
        result, desc = api_most_all().seminar_contact_front_getContactInfo("HW_UAT", list['HW_UAT_domain'],list['seminarId'],list['email'])
        self.assertEqual(result, 0, desc)
    # seminar_contact_front_getRegContact/此接口即将过期不在维护，可使用 member_geneGet 代替
    def test_141_seminar_contact_front_getRegContact(self):
        result, desc = api_most_all().seminar_contact_front_getRegContact("HW_UAT", list['HW_UAT_domain'],list['tenantId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # seminar_contact_front_regSeminar/标准报名
    def test_142_seminar_contact_front_regSeminar(self):
        result, desc = api_most_all().seminar_contact_front_regSeminar("HW_UAT", list['HW_UAT_domain'],list['loginSess'],list['seminarId_instanceId'],list['seminarId'],list['customFormId'],list['wechatId'])
        self.assertEqual(result, 0, desc)
    # seminar_contact_front_unRegister/参会人取消报名
    def test_143_seminar_contact_front_unRegister(self):
        result, desc = api_most_all().seminar_contact_front_unRegister("HW_UAT", list['HW_UAT_domain'],list['seminarId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # seminar_contact_front_updateSelf/更新参会人员信息 如果传递openId和weChatId会做绑定
    def test_144_seminar_contact_front_updateSelf(self):
        result, desc = api_most_all().seminar_contact_front_updateSelf("HW_UAT", list['HW_UAT_domain'],list['tenantId'],list['seminarId'],list['contactId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # seminar_contact_getContactToWechat/根据openID获取会中联系人信息
    def test_145_seminar_contact_getContactToWechat(self):
        result, desc = api_most_all().seminar_contact_getContactToWechat("HW_UAT", list['HW_UAT_domain'],list['seminarId'],list['wechatId'])
        self.assertEqual(result, 0, desc)
    # seminar_contact_registerNew/会议报名接口(isProject=1时支持表单短信验证
    def test_146_seminar_contact_registerNew(self):
        result, desc = api_most_all().seminar_contact_registerNew("HW_UAT", list['HW_UAT_domain'],list['customFormId'],list['memberFormId'])
        self.assertEqual(result, 0, desc)
    # seminar_contact_update/此接口即将过期不在维护，可使用seminar_contact_front_editRegContact标准格式实现,有问题
    def test_147_seminar_contact_update(self):
        result, desc = api_most_all().seminar_contact_update("HW_UAT", list['HW_UAT_domain'],list['tenantId'],list['seminarId'],list['contactId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # post_create/该接口为后台接口，后期即将移除，请不要继续使用，留言板发帖
    def test_148_post_create(self):
        result, desc,postI = api_most_all().post_create("HW_UAT", list['HW_UAT_domain'],list['global_topicId'],list['postId'])
        self.assertEqual(result, 0, desc)
        list['postI']=postI
    # webinar_open_registration/线上会报名接口
    def test_149_webinar_open_registration(self):
        result, desc = api_most_all().webinar_open_registration("HW_UAT", list['HW_UAT_domain'],list['webinarId_instanceId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    #questionary_HasParticipation/浏览问卷
    def test_150_questionary_HasParticipation(self):
        result, desc = api_most_all().questionary_HasParticipation("HW_UAT", list['HW_UAT_domain'],list['questionid_wj'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #post_get/获取贴子信息
    def test_151_post_get(self):
        result, desc = api_most_all().post_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['nodeId'], list['postId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #post_getListByUser/获取某人的未被删除的发送帖子记录
    def test_152_post_getListByUser(self):
        result, desc = api_most_all().post_getListByUser("HW_UAT", list['HW_UAT_domain'], list['topicId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    #post_getMainAndReplyList/获取留言板的发帖的回帖
    def test_153_post_getMainAndReplyList(self):
        result, desc = api_most_all().post_getMainAndReplyList("HW_UAT", list['HW_UAT_domain'], list['topicId'])
        self.assertEqual(result, 0, desc)
    #post_getMainPost/ 获取主贴列表
    def test_154_post_getMainPost(self):
        result, desc = api_most_all().post_getMainPost("HW_UAT", list['HW_UAT_domain'], list['topicId'])
        self.assertEqual(result, 0, desc)
    #post_getMyPost/获取我发的帖子
    def test_155_post_getMyPost(self):
        result, desc = api_most_all().post_getMyPost("HW_UAT", list['HW_UAT_domain'], list['topicId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #post_getReplyPost/获取某主贴的所有回贴
    def test_156_post_getReplyPost(self):
        result,desc=api_most_all().post_getReplyPost("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['nodeId'], list['postId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #post_like/点赞
    def test_157_post_like(self):
        result,desc=api_most_all().post_like("HW_UAT", list['HW_UAT_domain'])
        self.assertEqual(result, 0, desc)
    #post_update/主贴编辑 更新帖子内容
    def test_158_post_update(self):
        result,desc=api_most_all().post_update("HW_UAT", list['HW_UAT_domain'], list['postId'], list['tenantId'], list['nodeId'], list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    #post_deletePost/删除主贴
    def test_159_global_topicId(self):
        result,desc=api_most_all().post_deletePost("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['nodeId'], list['postI'], list['global_topicId'])
        self.assertEqual(result, 0, desc)
    # post_delete/此接口应为后台接口，后期不在开放，请不要调用 删除主贴
    def test_160_post_delete(self):
        result, desc = api_most_all().post_delete("HW_UAT", list['HW_UAT_domain'], list['postId'])
        self.assertEqual(result, 0, desc)
    # seminar_frontGet/获取会议详情
    def test_161_seminar_frontGet(self):
        result, desc = api_most_all().seminar_frontGet("HW_UAT", list['HW_UAT_domain'], list
        ['seminarId'])
        self.assertEqual(result, 0, desc)
    # seminar_frontGetList/获取会议列表，无sess调用
    def test_162_seminar_frontGetList(self):
        result, desc = api_most_all().seminar_frontGetList("HW_UAT", list['HW_UAT_domain'], list
        ['tenantId'])
        self.assertEqual(result, 0, desc)
    # webinar_registration/线上会报名表单提交
    def test_163_webinar_registration(self):
        result, desc = api_most_all().webinar_registration("HW_UAT", list['HW_UAT_domain'], list
        ['loginSess'], list['memberFormId'], list['webinarId_instanceId'])
        print "list['registerFormId']:", list['registerFormId']
        self.assertEqual(result, 0, desc)
    # contact_bindMember/微信账号与会员绑定
    def test_164_contact_bindMember(self):
        result, desc = api_most_all().contact_bindMember("HW_UAT", list['HW_UAT_domain'], list
        ['wechatId'], list['schemaId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # seminar_frontGetListByIds/根据ids获取会议列表
    def test_165_seminar_frontGetListByIds(self):
        result, desc = api_most_all().seminar_frontGetListByIds("HW_UAT", list['HW_UAT_domain'],list['tenantId'], )
        self.assertEqual(result, 0, desc)
    # seminar_frontGetStatusList/获取会议列表--支持按会议状态搜索
    def test_166_seminar_frontGetStatusList(self):
        result, desc = api_most_all().seminar_frontGetStatusList("HW_UAT", list['HW_UAT_domain'],list['tenantId'], )
        self.assertEqual(result, 0, desc)
    # seminar_get/ 获取会议详情
    def test_167_seminar_get(self):
        result, desc = api_most_all().seminar_get("HW_UAT", list['HW_UAT_domain'], list['seminarId'], )
        self.assertEqual(result, 0, desc)
        # seminar_getListWithFormId/会议列表（获取列表，输出：会议logo 会议名称 会议开始时间 会议地点默认的报名表单Id）注：会议logo如果不存在，则不返回
    def test_168_seminar_getListWithFormId(self):
        result, desc = api_most_all().seminar_getListWithFormId("HW_UAT", list['HW_UAT_domain'], list['tenantId'], )
        self.assertEqual(result, 0, desc)
        # seminar_register_canRegister/会议是否可以报名 如果有报名返回线下会报名信息，如果没有报名但是有注册返回注册信息，如果没有注册没有报名返回null
    def test_169_seminar_register_canRegister(self):
        result, desc = api_most_all().seminar_register_canRegister("HW_UAT", list['HW_UAT_domain'],list['seminarId_instanceId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # seminar_register_canRegisterNew/-会议是否可以报名
    def test_170_seminar_register_canRegisterNew(self):
        result, desc = api_most_all().seminar_register_canRegisterNew("HW_UAT", list['HW_UAT_domain'],list['seminarId_instanceId'],list['registerFormId'])
        self.assertEqual(result, 0, desc)
    # contact_getByOpenId/通过openId获取联系人信息
    def test_171_contact_getByOpenId(self):
        result, desc = api_most_all().contact_getByOpenId("HW_UAT", list['HW_UAT_domain'],list['wechatId'])
        self.assertEqual(result, 0, desc)
    # contact_getContactStatus/查询openId是否已关注微信号
    def test_172_contact_getContactStatus(self):
        result, desc = api_most_all().contact_getContactStatus("HW_UAT", list['HW_UAT_domain'],list['wechatId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # customForm_action/线下会报名接口
    def test_173_customForm_seminar_action(self):
        result, desc = api_most_all().customForm_seminar_action("HW_UAT", list['HW_UAT_domain'],list['customFormId'],list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # customForm_checkRegistration/报名前验证
    def test_174_customForm_checkRegistration(self):
        result, desc = api_most_all().customForm_checkRegistration("HW_UAT", list['HW_UAT_domain'],list['registerFormId'],list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # seminar_register_getList/获取报名表单列表
    def test_175_seminar_register_getList(self):
        result, desc = api_most_all().seminar_register_getList("HW_UAT", list['HW_UAT_domain'],list['seminarId'])
        self.assertEqual(result, 0, desc)
    # seminar_register_getSubList/通过自定义表单id获取报名表单信息
    def test_176_seminar_register_getSubList(self):
        result, desc = api_most_all().seminar_register_getSubList("HW_UAT", list['HW_UAT_domain'],list['customFormId'],list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # customForm_checkRepeatable/检查表单的不重复字段是否重复
    def test_177_customForm_checkRepeatable(self):
        result, desc = api_most_all().customForm_checkRepeatable("HW_UAT", list['HW_UAT_domain'],list['customFormId'])
        self.assertEqual(result, 0, desc)
    # customForm_get/获取自定义表单详情
    def test_178_customForm_get(self):
        result, desc = api_most_all().customForm_get("HW_UAT", list['HW_UAT_domain'], list['customFormId'])
        self.assertEqual(result, 0, desc)
    # customForm_getListByIds/该接口为后台接口，后期即将移除，请不要继续使用，获取表单列表
    def test_179_customForm_getListByIds(self):
        result, desc = api_most_all().customForm_getListByIds("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # customForm_HasParticipation/记录表单的浏览记录
    def test_180_customForm_HasParticipation(self):
        result, desc = api_most_all().customForm_HasParticipation("HW_UAT", list['HW_UAT_domain'],list['customFormId'])
        self.assertEqual(result, 0, desc)
    # customForm_sendCheckCode/自定义表单发送手机修改密码验证码
    def test_181_customForm_sendCheckCode(self):
        result, desc = api_most_all().customForm_sendCheckCode("HW_UAT", list['HW_UAT_domain'],list['customFormId'])
        self.assertEqual(result, 0, desc)
    # customForm_user_getRecordByOpenId/获取粉丝提交表单记录
    def test_182_customForm_user_getRecordByOpenId(self):
        result, desc = api_most_all().customForm_user_getRecordByOpenId("HW_UAT", list['HW_UAT_domain'],list['customFormId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # customForm_user_getResultByOpenId/获取某个OpenId的答表单的记录
    def test_183_customForm_user_getResultByOpenId(self):
        result, desc = api_most_all().customForm_user_getResultByOpenId("HW_UAT", list['HW_UAT_domain'],list['customFormId'])
        self.assertEqual(result, 0, desc)
    # customForm_view/记录表单的浏览记录
    def test_184_customForm_view(self):
        result, desc = api_most_all().customForm_view("HW_UAT", list['HW_UAT_domain'], list['customFormId'])
        self.assertEqual(result, 0, desc)
     # de_contact_front_get/获取de联系人信息
    def test_185_de_contact_front_get(self):
        result, desc = api_most_all().de_contact_front_get("HW_UAT", list['HW_UAT_domain'], list['loginSess'],list['tenantId'])
        self.assertEqual(result, 0, desc)
    # de_contact_front_getSeminars/ 通过前台sess获取联系人最近参加过的会议
    def test_186_de_contact_front_getSeminars(self):
        result, desc = api_most_all().de_contact_front_getSeminars("HW_UAT", list['HW_UAT_domain'], list['loginSess'],list['tenantId'])
        self.assertEqual(result, 0, desc)
    # de_contact_getLastSeminarsBySess/获取参与过的会议
    def test_187_de_contact_getLastSeminarsBySess(self):
        result, desc = api_most_all().de_contact_getLastSeminarsBySess("HW_UAT", list['HW_UAT_domain'], list['bakSess'],list['contactId'],list['tenantId'])
        self.assertEqual(result, 0, desc)
    # dic_getList/获取字典列表
    def test_188_dic_getList(self):
        result, desc = api_most_all().dic_getList("HW_UAT", list['HW_UAT_domain'],list['tenantId'])
        self.assertEqual(result, 0, desc)
    # dic_params_getList/获取字典值列表
    def test_189_dic_params_getList(self):
        result, desc = api_most_all().dic_params_getList("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['dicId'])
        self.assertEqual(result, 0, desc)
#seminar_signingPoint_checkIn_getCheckInCount/获取某会议下签到点的签到数
    def test_190_seminar_signingPoint_checkIn_getCheckInCount(self):
        result, desc = api_most_all().seminar_signingPoint_checkIn_getCheckInCount("HW_UAT", list['HW_UAT_domain'], list['bigScreenId'])
        self.assertEqual(result, 0, desc)
    #dic_params_getTree/获取字典树形结构
    def test_191_dic_params_getTree(self):
        result, desc = api_most_all().dic_params_getTree("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['dicId'])
        self.assertEqual(result, 0, desc)
    #seminar_signingPoint_front_getMyCheckInLog/查看自己的签到记录，传openid，globaluserid，cookieid，sess
    def test_192_seminar_signingPoint_front_getMyCheckInLog(self):
        result, desc = api_most_all().seminar_signingPoint_front_getMyCheckInLog("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['bakSess'], list['seminarId'], list['seminarId_instanceId'], list['signingPointId'],list['passageId'])
        self.assertEqual(result, 0, desc)
    #seminar_signingPoint_getCheckInLog/获取签到历史记录
    def test_193_seminar_signingPoint_getCheckInLog(self):
        result, desc = api_most_all().seminar_signingPoint_getCheckInLog("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['seminarId'], list['seminarId_instanceId'], list['signingPointId'],list['passageId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #seminar_signingPoint_getNumberSignInPassage/获取会议签到点签到统计信息
    def test_194_seminar_signingPoint_getNumberSignInPassage(self):
        result, desc = api_most_all().seminar_signingPoint_getNumberSignInPassage("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId'],list['seminarId_instanceId'],list['signingPointId'], list['passageId'],
                                                                         list['bakSess'])
        self.assertEqual(result, 0, desc)
    #edm_log_create/创建邮件发送任务
    def test_195_edm_log_create(self):
        result, desc = api_most_all().edm_log_create("HW_UAT", list['HW_UAT_domain'], list['taskId'])
        self.assertEqual(result, 0, desc)
    #seminar_subSeminar_frontGet/获取分会场详细信息
    def test_196_seminar_subSeminar_frontGet(self):
        result, desc = api_most_all().seminar_subSeminar_frontGet("HW_UAT", list['HW_UAT_domain'], list['subSeminarId'])
        self.assertEqual(result, 0, desc)
    #seminar_subSeminar_getListByType/获取分会场列表
    def test_197_seminar_subSeminar_getListByType(self):
        result, desc = api_most_all().seminar_subSeminar_getListByType("HW_UAT", list['HW_UAT_domain'], list['seminarId'])
        self.assertEqual(result, 0, desc)
    #seminar_topicTemplate_contact_get/获取联系人信息
    def test_198_seminar_topicTemplate_contact_get(self):
        result, desc = api_most_all().seminar_topicTemplate_contact_get("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'], list['email'])
        self.assertEqual(result, 0, desc)
    #seminar_topicTemplate_contact_getByOpenId/通过微信OpenId获取某会议下的联系人
    def test_199_seminar_topicTemplate_contact_getByOpenId(self):
        result, desc = api_most_all().seminar_topicTemplate_contact_getByOpenId("HW_UAT", list['HW_UAT_domain'], list['seminarId'])
        self.assertEqual(result, 0, desc)
#edm_send/邮件发送接口，session验证
    def test_200_edm_send(self):
        result, desc = api_most_all().edm_send("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #seminar_topicTemplate_contact_getState/通过实例ID和唯一字段获取信息
    def test_201_seminar_topicTemplate_contact_getState(self):
        result, desc = api_most_all().seminar_topicTemplate_contact_getState("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'], list['email'])
        self.assertEqual(result, 0, desc)
    #customForm_isFaceImg/检查图片是否包含人脸
    def test_202_customForm_isFaceImg(self):
        result, desc = api_most_all().customForm_isFaceImg("HW_UAT", list['HW_UAT_domain'], list['mappingId'])
        self.assertEqual(result, 0, desc)
    #seminar_topicTemplate_contact_getStateBySess/获取注册状态，有问题
    def test_203_seminar_topicTemplate_contact_getStateBySess(self):
        result, desc = api_most_all().seminar_topicTemplate_contact_getStateBySess("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    #seminar_topicTemplate_seminar_getFormInfo/获取表单详细信息
    def test_204_seminar_topicTemplate_seminar_getFormInfo(self):
        result, desc = api_most_all().seminar_topicTemplate_seminar_getFormInfo("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'], list['registerFormId'])
        self.assertEqual(result, 0, desc)
    #seminar_topicTemplate_seminar_getWithAllSub/获取会议信息，包括所有的分会场
    def test_205_seminar_topicTemplate_seminar_getWithAllSub(self):
        result, desc = api_most_all().seminar_topicTemplate_seminar_getWithAllSub("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    #seminar_trackingCode_getList/获取渠道追踪代码列表
    def test_206_seminar_trackingCode_getList(self):
        result, desc = api_most_all().seminar_trackingCode_getList("HW_UAT", list['HW_UAT_domain'], list['seminarId'])
        self.assertEqual(result, 0, desc)
    #seminar_bigScreen_forBigScreenWall_getCheckInData/获取大屏签到墙信息
    def test_207_seminar_bigScreen_forBigScreenWall_getCheckInData(self):
        result, desc = api_most_all().seminar_bigScreen_forBigScreenWall_getCheckInData("HW_UAT", list['HW_UAT_domain'], list['bigScreenId'], list['signingPointId'])
        self.assertEqual(result, 0, desc)
    #seminar_bigScreen_forBigScreenWall_getWapCheckInfo/获取大屏手机端签到信息
    def test_208_seminar_bigScreen_forBigScreenWall_getWapCheckInfo(self):
        result, desc = api_most_all().seminar_bigScreen_forBigScreenWall_getWapCheckInfo("HW_UAT", list['HW_UAT_domain'], list['bigScreenId'], list['contactId'], list['email'])
        self.assertEqual(result, 0, desc)
    #field_getList/获取字段列表
    def test_209_field_getList(self):
        result, desc = api_most_all().field_getList("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #seminar_bigScreen_getWapMessageInfo/获取wap签到模板联系人信息
    def test_210_seminar_bigScreen_getWapMessageInfo(self):
        result, desc = api_most_all().seminar_bigScreen_getWapMessageInfo("HW_UAT", list['HW_UAT_domain'], list['seminarId'], list['email'])
        self.assertEqual(result, 0, desc)
    #file_folder_getReleaseFile/获取公布的文件
    def test_211_file_folder_getReleaseFile(self):
        result, desc = api_most_all().file_folder_getReleaseFile("HW_UAT", list['HW_UAT_domain'], list['fileIds'])
        self.assertEqual(result, 0, desc)
    #file_getList/获取文件列表
    def test_212_file_getList(self):
        result, desc, articleCategoryId = api_most_all().file_getList("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId_instanceId'], list['FolderId'],list['fileIds'])
        self.assertEqual(result, 0, desc)
        list['articleCategoryId'] = articleCategoryId
    #member_changePwd/前台用户修改密码
    def test_213_member_changePwd(self):
        result, desc= api_most_all().member_changePwd("HW_UAT", list['HW_UAT_domain'], list['schemaId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    #member_checkUnique/检测用户唯一，检测字段值唯一
    def test_214_member_checkUnique(self):
        result, desc= api_most_all().member_checkUnique("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #luckyDraw_client_action/抽奖
    def test_215_luckyDraw_client_action(self):
        result, desc= api_most_all().luckyDraw_client_action("HW_UAT", list['HW_UAT_domain'], list['luckyDrawId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #member_form_GetForNewForm/新的表单信息 接受formId 和 memberFormId 按新接口的格式返回
    def test_216_member_form_GetForNewForm(self):
        result, desc= api_most_all().member_form_GetForNewForm("HW_UAT", list['HW_UAT_domain'], list['registerFormId'])
        self.assertEqual(result, 0, desc)
    #member_form_GetOAuthUrlByWeChatId/通过wechatId获取授权信息
    def test_217_member_form_GetOAuthUrlByWeChatId(self):
        result, desc= api_most_all().member_form_GetOAuthUrlByWeChatId("HW_UAT", list['HW_UAT_domain'], list['wechatId'])
        self.assertEqual(result, 0, desc)
    #member_form_getTemplate/获取表单模板信息
    def test_218_member_form_getTemplate(self):
        result, desc= api_most_all().member_form_getTemplate("HW_UAT", list['HW_UAT_domain'], list['memberFormId'])
        self.assertEqual(result, 0, desc)
    #member_form_getUnique/找回密码
    def test_219_member_form_getUnique(self):
        result, desc= api_most_all().member_form_getUnique("HW_UAT", list['HW_UAT_domain'], list['memberFormId'])
        self.assertEqual(result, 0, desc)
    # member_form_search/查询符合条件的表单
    def test_220_member_form_search(self):
        result, desc = api_most_all().member_form_search("HW_UAT", list['HW_UAT_domain'], list ['tenantId'])
        self.assertEqual(result, 0, desc)
    # member_form_view/注册表单浏览
    def test_221_member_form_view(self):
        result, desc = api_most_all().member_form_view("HW_UAT", list['HW_UAT_domain'], list ['memberFormId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # api_seminar_Query/获取会议列表
    def test_222_api_seminar_Query(self):
        result, desc = api_most_all().api_seminar_Query("HW_UAT", list['HW_UAT_domain'], list ['tenantId'])
        self.assertEqual(result, 0, desc)
    # member_geneGet/根据已登录的session获取用户信息
    def test_223_member_geneGet(self):
        result, desc = api_most_all().member_geneGet("HW_UAT", list['HW_UAT_domain'], list ['loginSess'])
        self.assertEqual(result, 0, desc)
    # api_seminar_site_browse/进入访问专题站行为
    def test_224_api_seminar_site_browse(self):
        result, desc = api_most_all().api_seminar_site_browse("HW_UAT", list['HW_UAT_domain'], list ['seminarId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_site_share/分享专题站行为
    def test_225_api_seminar_site_share(self):
        result, desc = api_most_all().api_seminar_site_share("HW_UAT", list['HW_UAT_domain'], list ['seminarId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # api_template_config_get/获取模板信息
    def test_226_api_template_config_get(self):
        result, desc = api_most_all().api_template_config_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # member_get/根据已登录的session获取用户信息
    def test_227_member_get(self):
        result, desc = api_most_all().member_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # api_topic_board_browse/浏览版面
    def test_228_api_topic_board_browse(self):
        result, desc = api_most_all().api_topic_board_browse("HW_UAT", list['HW_UAT_domain'], list['topicId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
        # member_login/前台登陆loginSess3
    # def test_229_member_login(self):
    #     flag, loginSess = api_most_all().member_login('HW_UAT', list['HW_UAT_domain'], list['tenantId'], list['schemaId'],list['memberFormId'], list['memberSchemaId'], list['unique'],list['password'])
    #     self.assertEqual(flag, 0, "获取前台登录session失败")
    #     list['loginSess3'] = loginSess
    #     print"list['loginSess3']:", list['loginSess3']
    # api_topic_browse/浏览主贴
    def test_230_api_topic_browse(self):
        result, desc = api_most_all().api_topic_browse("HW_UAT", list['HW_UAT_domain'], list['postId'], list['tenantId'],list['loginSess'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # api_topic_comment_query / 微讨论 - 微论坛 - 获取子版的评论列表
    def test_231_api_topic_comment_query(self):
        result, desc = api_most_all().api_topic_comment_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['topicId'], list['section_create'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # api_topic_forum_post_get/获取帖子详情
    def test_232_api_topic_forum_post_get(self):
        result, desc = api_most_all().api_topic_forum_post_get("HW_UAT", list['HW_UAT_domain'], list['pos'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # member_LookUp/由下向上获取回填信息.实例联系人-模块联系人-注册用户信息.可传前端sess或不传.
    def test_233_member_LookUp(self):
        result, desc = api_most_all().member_LookUp("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # member_schema_field_GetList/获取体系字段
    def test_234_member_schema_field_GetList(self):
        result, desc = api_most_all().member_schema_field_GetList("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['schemaId'])
        self.assertEqual(result, 0, desc)
    # member_schema_orderUnique/获取体系的标识字段及顺序
    def test_235_member_schema_orderUnique(self):
        result, desc = api_most_all().member_schema_orderUnique("HW_UAT", list['HW_UAT_domain'], list['memberSchemaId'])
        self.assertEqual(result, 0, desc)
    # member_schema_field_sorting_GetList/获取身份标识字段列表
    def test_236_member_schema_field_sorting_GetList(self):
        result, desc = api_most_all().member_schema_field_sorting_GetList("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['schemaId'])
        self.assertEqual(result, 0, desc)
    # member_sendCheckCode/身份认证体系发送手机修改密码验证码(member_sendCheckCode)新加的接口增加前端的控制（有效期和重发时间）
    def test_237_member_sendCheckCode(self):
        result, desc = api_most_all().member_sendCheckCode("HW_UAT", list['HW_UAT_domain'], list['unique'],list['memberSchemaId'])
        self.assertEqual(result, 0, desc)
    # member_sendVerificationCode/向手机号码发送验证码
    def test_238_member_sendVerificationCode(self):
        result, desc = api_most_all().member_sendVerificationCode("HW_UAT", list['HW_UAT_domain'], list['memberFormId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # member_sendVerificationCodeToMail/向用户邮箱发送验证码
    def test_239_member_sendVerificationCodeToMail(self):
        result, desc = api_most_all().member_sendVerificationCodeToMail("HW_UAT", list['HW_UAT_domain'], list['memberFormId'])
        self.assertEqual(result, 0, desc)
    # api_topic_forum_post_query/微讨论-微论坛-获取微论坛的主帖列表
    def test_240_api_topic_forum_post_query(self):
        result, desc = api_most_all().api_topic_forum_post_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['topicId'], list['section_create'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # member_updateByField/会员修改，只修改给定的字段.需要登录
    def test_241_member_updateByField(self):
        result, desc = api_most_all().member_updateByField("HW_UAT", list['HW_UAT_domain'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # api_topic_forum_post_reply_query/微讨论-微论坛-获取微论坛主贴的回帖列表
    def test_242_api_topic_forum_post_reply_query(self):
        result, desc = api_most_all().api_topic_forum_post_reply_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['postId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # api_topic_get/微讨论-获取版面详情
    def test_243_api_topic_get(self):
        result, desc = api_most_all().api_topic_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['topicId'])
        self.assertEqual(result, 0, desc)
    # api_topic_message_Create/发主帖/回帖
    def test_244_api_topic_message_Create(self):
        result, desc = api_most_all().api_topic_message_Create("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['topicId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # api_topic_message_get/微讨论-留言板-获取留言板帖子的详细信息
    def test_245_api_topic_message_get(self):
        result, desc = api_most_all().api_topic_message_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['postId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # api_topic_message_Query/获取主题帖列表以及对应帖子的回复列表
    def test_246_api_topic_message_Query(self):
        result, desc = api_most_all().api_topic_message_Query("HW_UAT", list['HW_UAT_domain'], list['topicId'],list['tenantId'])
        self.assertEqual(result, 0, desc)
    # api_topic_message_reply_Query/某主帖的回复列表
    def test_247_api_topic_message_reply_Query(self):
        result, desc = api_most_all().api_topic_message_reply_Query("HW_UAT", list['HW_UAT_domain'], list['postId'],list['loginSess'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # api_topic_share/分享主贴
    def test_248_api_topic_share(self):
        result, desc = api_most_all().api_topic_share("HW_UAT", list['HW_UAT_domain'], list['topicId'], list['loginSess'],list['tenantId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # member_loginByOpenId/使用openId登录，如果未登录会返回绑定使用的authCode
    def test_249_member_loginByOpenId(self):
        result, desc = api_most_all().member_loginByOpenId("HW_UAT", list['HW_UAT_domain'], list['schemaId'], list['wechatId'])
        self.assertEqual(result, 0, desc)
    # luckyDraw_client_actionByBigScreen/大屏抽奖的抽奖操作
    def test_250_luckyDraw_client_actionByBigScreen(self):
        result, desc = api_most_all().luckyDraw_client_actionByBigScreen("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['luckyDrawId'])
        self.assertEqual(result, 0, desc)
    # member_identification_sorting_Get/按当前租户的身份标识优先级来获取注册用户的个人信息
    def test_251_member_identification_sorting_Get(self):
        result, desc = api_most_all().member_identification_sorting_Get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # luckyDraw_client_GetMyRedPacketLog/微信红包抽奖业务专用，通过OpenId获取当前用户的在该场活动的所有抽奖记录
    def test_252_luckyDraw_client_GetMyRedPacketLog(self):
        result, desc = api_most_all().luckyDraw_client_GetMyRedPacketLog("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['luckyDrawId'])
        self.assertEqual(result, 0, desc)
    # api_customform_browse/记录表单的浏览记录
    def test_253_api_customform_browse(self):
        result, desc = api_most_all().api_customform_browse("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['customFormId'])
        self.assertEqual(result, 0, desc)
    # api_customform_field_check/检查表单的不重复字段是否重复/不重复
    def test_254_api_customform_field_check(self):
        result, desc = api_most_all().api_customform_field_check("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['customFormId'])
        self.assertEqual(result, 0, desc)
    # api_customform_submit/自定义表单提交
    def test_255_api_customform_submit(self):
        result, desc = api_most_all().api_customform_submit("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['customFormId'])
        self.assertEqual(result, 0, desc)
    # member_forgetPwd/找回密码
    def test_256_member_forgetPwd(self):
        code= api_most_all().member_forgetPwd("HW_UAT", list['HW_UAT_domain'], list['memberSchemaId'],list['memberFormId'])
        self.assertEqual(code, 200, "状态码不是200")
    # member_UpdateIdentityInfo/修改身份信息
    def test_257_member_UpdateIdentityInfo(self):
        result, desc = api_most_all().member_UpdateIdentityInfo("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['schemaId'], list['memberFormId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # member_interaction_record/记录一个互动
    def test_258_member_interaction_record(self):
        result, desc = api_most_all().member_interaction_record("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['pollId'], )
        self.assertEqual(result, 0, desc)
    #  webinar_event_interaction_questionnaireResult/提交问卷
    def test_259_webinar_event_interaction_questionnaireResult(self):
        result, desc = api_most_all().webinar_event_interaction_questionnaireResult("HW_UAT", list['HW_UAT_domain'], list['webinarId_instanceId'],list['questionid_wj'])
        self.assertEqual(result, 0, desc)
    # member_member_associate_Logout/让关联微信粉丝或匿名用户的注册用户退出登录
    def test_260_member_member_associate_Logout(self):
        result, desc = api_most_all().member_member_associate_Logout("HW_UAT", list['HW_UAT_domain'], list['loginSess'] )
        self.assertEqual(result, 0, desc)
    # member_login/前台session
    # def test_261_member_member_login(self):
    #     flag, loginSess = api_most_all().member_login('HW_UAT', list['HW_UAT_domain'], list['tenantId'], list['schemaId'],list['memberFormId'], list['memberSchemaId'], list['unique'],list['password'])
    #     self.assertEqual(flag, 0, "获取前台登录session失败")
    #     list['loginSess2'] = loginSess
    #     print"list['loginSess2']:", list['loginSess2']
    # member_form_get/获取表单信息
    def test_262_member_form_get(self):
        result, desc = api_most_all().member_form_get("HW_UAT", list['HW_UAT_domain'], list['memberFormId'],list['bakSess'] )
        self.assertEqual(result, 0, desc)
    # api_member_contacts_register/用户注册
    def test_263_api_member_contacts_register(self):
        result, desc = api_most_all().api_member_contacts_register("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['nophoneform'] )
        self.assertEqual(result, 0, desc)
    # api_questionnaire_browse/记录问卷浏览记录
    def test_264_api_questionnaire_browse(self):
        result, desc = api_most_all().api_questionnaire_browse("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['questionid_wj'])
        self.assertEqual(result, 0, desc)
    # api_questionnaire_get/获取问卷信息
    def test_265_api_questionnaire_get(self):
        result, desc = api_most_all().api_questionnaire_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['questionid_wj'])
        self.assertEqual(result, 0, desc)
    # api_questionnaire_query/查询问卷列表/全部
    def test_266_api_questionnaire_query(self):
        result, desc = api_most_all().api_questionnaire_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # api_questionnaire_submit/提交问卷
    def test_267_api_questionnaire_submit(self):
        result, desc = api_most_all().api_questionnaire_submit("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['questionid_wj'])
        self.assertEqual(result, 0, desc)
    # api_seminar_app_getconfiginfo/获取App相关的配置信息
    def test_268_api_seminar_app_getconfiginfo(self):
        result, desc = api_most_all().api_seminar_app_getconfiginfo("HW_UAT", list['HW_UAT_domain'], list['bakSess'],list['tenantId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_app_monitor_getappinfo/获取设备信息
    def test_269_api_seminar_app_monitor_getappinfo(self):
        result, desc = api_most_all().api_seminar_app_monitor_getappinfo("HW_UAT", list['HW_UAT_domain'], list['seminarId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_app_monitor_getclientalias/获取设备自定义编号GetNumberapp\seminar\monitor
    def test_270_api_seminar_app_monitor_getclientalias(self):
        result, desc = api_most_all().api_seminar_app_monitor_getclientalias("HW_UAT", list ['HW_UAT_domain'], list['tenantId'], list['seminarId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_app_monitor_updateclientinfo/更新设备信息UpdateInfo
    def test_271_api_seminar_app_monitor_updateclientinfo(self):
        result, desc = api_most_all().api_seminar_app_monitor_updateclientinfo("HW_UAT", list['HW_UAT_domain'], list['seminarId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_bigscreen_contacts_Get/获取大屏手机端签到信息/服务号租户
    def test_272_api_seminar_bigscreen_contacts_Get(self):
        result, desc = api_most_all().api_seminar_bigscreen_contacts_Get("HW_UAT", list ['HW_UAT_domain'], list['tenantId'], list['bigScreenId'], list['contactId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_bigscreen_Get/获取大屏详细信息
    def test_273_api_seminar_bigscreen_Get(self):
        result, desc = api_most_all().api_seminar_bigscreen_Get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['bigScreenId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_bigscreen_group_query/获取大屏组列表/服务号租户
    def test_274_api_seminar_bigscreen_group_query(self):
        result, desc = api_most_all().api_seminar_bigscreen_group_query("HW_UAT", list
        ['HW_UAT_domain'], list['tenantId'], list['seminarId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_contacts_field_Get/获取联系人字段列表
    def test_275_api_seminar_contacts_field_Get(self):
        result, desc = api_most_all().api_seminar_bigscreen_group_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['seminarId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_contacts_Get/线下会根据sess、openid、globalUserId查询报名信息
    def test_276_api_api_seminar_contacts_Get(self):
        result, desc = api_most_all().api_seminar_contacts_Get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
        # api_seminar_contacts_SignUp/线下会报名(报名时可以新增或更新注册信息)
    def test_277_api_seminar_contacts_SignUp(self):
        result, desc = api_most_all().api_seminar_contacts_SignUp("HW_UAT", list['HW_UAT_domain'],list['tenantId'],list['seminarId'], list['customFormId'])
        self.assertEqual(result, 0, desc)
        # api_seminar_contacts_Update/线下会根据sess更新报名信息（可选是否更新注册信息）/更新注册信息
    def test_278_api_seminar_contacts_Update(self):
        result, desc = api_most_all().api_seminar_contacts_Update("HW_UAT", list['HW_UAT_domain'],list['tenantId'],list['loginSess'],list['seminarId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_customform_subseminar_get/获取报名表单关联的分会场信息
    def test_279_api_seminar_customform_subseminar_get(self):
        result, desc = api_most_all().api_seminar_customform_subseminar_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId'], list ['customFormId'])
        self.assertEqual(result, 0, desc)
    #file_downloadWithEmail/文章资料下载
    def test_280_file_downloadWithEmail(self):
        result, desc= api_most_all().file_downloadWithEmail("HW_UAT", list['HW_UAT_domain'], list['articleId'],list['fileIds'], list['email'], list['tenantId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    #member_identification_information_Get/用户详情页调的接口，区别与getInfo
    def test_281_member_identification_information_Get(self):
        result, desc= api_most_all().member_identification_information_Get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['schemaId'], list['memberId'])
        self.assertEqual(result, 0, desc)
    #file_delete/该接口为后台接口，后期即将移除，请不要继续使用，删除文件
    def test_282_file_delete(self):
        result, desc= api_most_all().file_delete("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['fileId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #webinar_open_getLuckyDrawRoster/获取会议的中奖名单
    def test_283_webinar_open_getLuckyDrawRoster(self):
        result, desc= api_most_all().webinar_open_getLuckyDrawRoster("HW_UAT", list['HW_UAT_domain'], list['webinarId'], list['tenantId'], list['webinarId_instanceId'])
        self.assertEqual(result, 0, desc)
    #luckyDraw_client_hasParticipate/有问题，该接口为后台接口，后期即将移除，请不要继续使用，检查某个用户是否已经参与过大屏抽奖，--创建线下会，报名会议后参与的抽奖
    def test_284_luckyDraw_client_hasParticipate(self):
        result, desc= api_most_all().luckyDraw_client_hasParticipate("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['luckyDrawId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #luckyDraw_client_participate/有问题，大屏抽奖，用户现场主动参与抽奖，如扫码-马叔，手机端有问题
    def test_285_luckyDraw_client_participate(self):
        code= api_most_all().luckyDraw_client_participate("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['luckyDrawId'], list['bakSess'])
        self.assertEqual(code, 200, "断言200错误")
    #luckyDraw_client_saveUserInfo/收集中奖用户信息
    def test_286_luckyDraw_client_saveUserInfo(self):
        result, desc= api_most_all().luckyDraw_client_saveUserInfo("HW_UAT", list['HW_UAT_domain'], list['luckyDrawId'])
        self.assertEqual(result, 0, desc)
    #luckyDraw/client/saveUserInfo统计
    def test_287_luckyDraw_client_saveUserInfo_count(self):
        result, desc= api_most_all().luckyDraw_client_saveUserInfo_count("HW_UAT", list['HW_UAT_domain'], list['luckyDrawId'])
        self.assertEqual(result, 0, desc)
    #luckyDraw_client_share/分享后参与情况，使用该接口获取分享资格
    def test_288_luckyDraw_client_share(self):
        result, desc= api_most_all().luckyDraw_client_share("HW_UAT", list['HW_UAT_domain'], list['luckyDrawId'])
        self.assertEqual(result, 0, desc)
    #luckyDraw_get/获取抽奖信息
    def test_289_luckyDraw_get(self):
        result, desc= api_most_all().luckyDraw_get("HW_UAT", list['HW_UAT_domain'], list['luckyDrawId'])
        self.assertEqual(result, 0, desc)
    #luckyDraw_getAwardDetailList/获取奖品列表信息
    def test_290_luckyDraw_getAwardDetailList(self):
        result, desc= api_most_all().luckyDraw_getAwardDetailList("HW_UAT", list['HW_UAT_domain'], list['luckyDrawId'])
        self.assertEqual(result, 0, desc)
    #luckyDraw_redPacket_getLotteryRecord/大屏红包抽奖获取中奖名单
    def test_291_luckyDraw_redPacket_getLotteryRecord(self):
        result, desc= api_most_all().luckyDraw_redPacket_getLotteryRecord("HW_UAT", list['HW_UAT_domain'],list['tenantId'], list['luckyDrawId'])
        self.assertEqual(result, 0, desc)
    #luckyDraw_redPacket_pushMessage/前端推送消息到node服务器
    def test_292_luckyDraw_redPacket_pushMessage(self):
        result, desc= api_most_all().luckyDraw_redPacket_pushMessage("HW_UAT", list['HW_UAT_domain'], list['luckyDrawId'],list['tenantId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #luckyDraw_result_getState/获取大屏抽奖的轮次状态，如果未开始的轮次，标记未开始，已开始的，返回中奖名单
    def test_293_luckyDraw_result_getState(self):
        result, desc= api_most_all().luckyDraw_result_getState("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['luckyDrawId'])
        self.assertEqual(result, 0, desc)
    #luckyDraw_result_getUserResultList/获取个人的普通抽奖记录
    def test_294_luckyDraw_result_getUserResultList(self):
        result, desc= api_most_all().luckyDraw_result_getUserResultList("HW_UAT", list['HW_UAT_domain'], list['luckyDrawId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #luckyDraw_view/检测是否参与过抽奖
    def test_295_luckyDraw_view(self):
        result, desc= api_most_all().luckyDraw_view("HW_UAT", list['HW_UAT_domain'], list['luckyDrawId'])
        self.assertEqual(result, 0, desc)
    #topic_get/获取发帖信息
    def test_296_topic_get(self):
        result, desc= api_most_all().topic_get("HW_UAT", list['HW_UAT_domain'], list['topicId'])
        self.assertEqual(result, 0, desc)
    #api_productLine_query/获取租户下产品线列表
    def test_297_api_productLine_query(self):
        result, desc= api_most_all().api_productLine_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #api_poll_share/分享投票行为
    def test_298_api_poll_share(self):
        result, desc= api_most_all().api_poll_share("HW_UAT", list['HW_UAT_domain'], list['pollId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #api_poll_browse/浏览投票行为
    def test_299_api_poll_browse(self):
        result, desc= api_most_all().api_poll_browse("HW_UAT", list['HW_UAT_domain'], list['pollId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # api_webinar_channel_query/根据会议ID获取该会议的渠道追踪代码
    def test_300_api_webinar_channel_query(self):
        result, desc = api_most_all().api_webinar_channel_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['webinarId'])
        self.assertEqual(result, 0, desc)
    #api_webinar_contacts_signup/会议报名
    def test_301_api_webinar_contacts_signup(self):
        result, desc = api_most_all().api_webinar_contacts_signup("HW_UAT", list['HW_UAT_domain'], list['loginSess'], list['tenantId'],list['webinarId'],list['customFormId'])
        self.assertEqual(result, 0, desc)
    #api_webinar_get/获取直播会议信息
    def test_302_api_webinar_get(self):
        result, desc = api_most_all().api_webinar_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['webinarId'])
        self.assertEqual(result, 0, desc)
    #api_webinar_interaction_filedownload_create/下载文件互动记录，有问题
    def test_303_api_webinar_interaction_filedownload_create(self):
        result, desc = api_most_all().api_webinar_interaction_filedownload_create("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['loginSess'],list['webinarId'],list['fileId'])
        self.assertEqual(result, 0, desc)
    #api_wechat_contacts_check/根据openIds批量查询用户对某个微信号的关注状态/-1 ：返回所有包含关注和未关注的
    def test_304_api_wechat_contacts_check(self):
        result, desc = api_most_all().api_wechat_contacts_check("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['wechatId'])
        self.assertEqual(result, 0, desc)
    #api_wechat_contacts_get/获取微信粉丝信息/简体
    def test_305_api_wechat_contacts_get(self):
        result, desc = api_most_all().api_wechat_contacts_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['wechatId'],list['openId'])
        self.assertEqual(result, 0, desc)
    #api_wechat_get/获取微信信息
    def test_306_api_wechat_get(self):
        result, desc = api_most_all().api_wechat_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['wechatId'])
        self.assertEqual(result, 0, desc)
    #api_wechat_jssdk_config_get/获取微信jssdk配置
    def test_307_api_wechat_jssdk_config_get(self):
        result, desc = api_most_all().api_wechat_jssdk_config_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['wechatId'])
        self.assertEqual(result, 0, desc)
    #api_article_category_get/获取栏目的详细信息/带模板
    def test_308_api_article_category_get(self):
        result, desc = api_most_all().api_article_category_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['articleId'])
        self.assertEqual(result, 0, desc)
    #api_common_shorturl_create/公共服务-短链接-生成短链接
    def test_309_api_common_shorturl_create(self):
        result, desc = api_most_all().api_common_shorturl_create("HW_UAT", list['HW_UAT_domain'])
        self.assertEqual(result, 0, desc)
    #api_content_collect_query/查询我收藏的信息
    def test_310_api_content_collect_query(self):
        result, desc = api_most_all().api_content_collect_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #api_customform_record_query/获取某个OpenId的表单的记录
    def test_311_api_customform_record_query(self):
        result, desc = api_most_all().api_customform_record_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['customFormId'])
        self.assertEqual(result, 0, desc)
    #api_customform_share/分享表单行为
    def test_312_api_customform_share(self):
        result, desc = api_most_all().api_customform_share("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['customFormId'])
        self.assertEqual(result, 0, desc)
    #api_dic_get/20180810-根据字典表id获取字典列表及字典值所级联的下级字典表名称
    def test_313_api_dic_get(self):
        result, desc = api_most_all().api_dic_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['dicId'])
        self.assertEqual(result, 0, desc)
    #api_dic_gettree/根据字典表id获取字典树形(当前字典值及下级字典值)结构 最多返回两级
    def test_314_api_dic_gettree(self):
        result, desc = api_most_all().api_dic_gettree("HW_UAT", list['HW_UAT_domain'], list['dicId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #api_dic_params_set/新增或修改字典表的值
    def test_315_api_dic_params_set(self):
        result, desc = api_most_all().api_dic_params_set("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['dicId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #api_seminar_field_Get/获取线下会会议属性字段列表
    def test_316_api_seminar_field_Get(self):
        result, desc = api_most_all().api_seminar_field_Get("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #interaction_getCountByType/获取实例的行为记录数量
    def test_317_interaction_getCountByType(self):
        result, desc = api_most_all().interaction_getCountByType("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    #interaction_getDetailList/ 获取租户下一个用户的某类型的互动记录
    def test_318_interaction_getDetailList(self):
        result, desc = api_most_all().interaction_getDetailList("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['seminarId_instanceId'],list['memberId'])
        self.assertEqual(result, 0, desc)
    #interaction_getFileDownloads/获取租户下载文件记录，如果传递memberWords则获取这个人的下载记录，如果传递fileWords，则获取这个文件的下载记录
    def test_319_interaction_getFileDownloads(self):
        result, desc = api_most_all().interaction_getFileDownloads("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
# interaction_getListByMember/获取前台sess对应的互动行为记录
    def test_320_interaction_getListByMember(self):
        result, desc = api_most_all().interaction_getListByMember("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # interaction_getStatCountList/该接口为后台接口，后期即将移除，请不要继续使用，获取用户在实例中的（浏览/分享/资料）计数,有问题
    def test_321_interaction_getStatCountList(self):
        result, desc = api_most_all().interaction_getStatCountList("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId_instanceId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # api_seminar_form_Get/获取报名表单详细信息
    def test_322_api_seminar_form_Get(self):
        result, desc = api_most_all().api_seminar_form_Get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_Get/获取线下会议相关信息
    def test_323_api_seminar_Get(self):
        result, desc = api_most_all().api_seminar_Get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['seminarId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_signingpoint_interaction_get/线下会获取互动设置的领奖点列表，从来都没有启用过的互动不在返回列表
    def test_324_api_seminar_signingpoint_interaction_get(self):
        result, desc = api_most_all().api_seminar_signingpoint_interaction_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['seminarId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_signingpoint_Statistics/签到点按通道统计签到人次
    def test_325_api_seminar_signingpoint_Statistics(self):
        result, desc = api_most_all().api_seminar_signingpoint_Statistics("HW_UAT", list['HW_UAT_domain'],list['tenantId'], list['seminarId'],list['passageId'])
        self.assertEqual(result, 0, desc)
    # api_seminar_subseminar_Query/获取分会场列表
    def test_326_api_seminar_subseminar_Query(self):
        result, desc = api_most_all().api_seminar_subseminar_Query("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId'])
        self.assertEqual(result, 0, desc)
    # api_webinar_demand_record/奥点云点播观看次数，写成死值
    def test_327_api_webinar_demand_record(self):
        result, desc = api_most_all().api_webinar_demand_record("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['webinarId_DianBo'],list['videoId'])
        self.assertEqual(result, 0, desc)
    # article_getCollectionList/微信模块获取收藏列表,有问题
    def test_328_article_getCollectionList(self):
        code = api_most_all().article_getCollectionList("HW_UAT", list['HW_UAT_domain'], list['loginSess'])
        self.assertEqual(code, 200, "断言200失败")
    # app_seminar_contact_nfc_bind/该接口为APP专用接口，项目不要使用，nfc批量绑定
    def test_329_app_seminar_contact_nfc_bind(self):
        result, desc = api_most_all().app_seminar_contact_nfc_bind("HW_UAT", list['HW_UAT_domain'], list['seminarId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # app_seminar_contact_nfc_getBindRecord/获取绑卡记录，有问题
    def test_330_app_seminar_contact_nfc_getBindRecord(self):
        result, desc = api_most_all().app_seminar_contact_nfc_getBindRecord("HW_UAT", list['HW_UAT_domain'], list['seminarId'],list['contactId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # app_seminar_contact_nfc_getList/该接口为APP专用接口，项目不要使用，获取nfc绑定关系列表
    def test_331_app_seminar_contact_nfc_getList(self):
        result, desc = api_most_all().app_seminar_contact_nfc_getList("HW_UAT", list['HW_UAT_domain'], list['seminarId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # app_seminar_contact_prints_getList/APP获取打印大屏签到信息
    def test_332_app_seminar_contact_prints_getList(self):
        result, desc = api_most_all().app_seminar_contact_prints_getList("HW_UAT", list['HW_UAT_domain'], list['seminarId'],list['signingPointId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # tag_api_thirdTrigger_add/有问题，产品第三方行为触发-马震(华为不用，不监控 )
    def test_333_tag_api_thirdTrigger_add(self):
        code = api_most_all().tag_api_thirdTrigger_add("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(code, 200, "断言200失败")
    # app_seminar_contact_prints_getSigningPointInfo/获取会议下签到点缩略信息
    def test_334_app_seminar_contact_prints_getSigningPointInfo(self):
        result, desc = api_most_all().app_seminar_contact_prints_getSigningPointInfo("HW_UAT", list['HW_UAT_domain'], list['seminarId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # app_seminar_contact_prints_updatePrintLog/更新APP打印大屏签到日志
    def test_335_app_seminar_contact_prints_updatePrintLog(self):
        result, desc = api_most_all().app_seminar_contact_prints_updatePrintLog("HW_UAT", list['HW_UAT_domain'],list['seminarId'], list['tenantId'],list['seminarId_instanceId'], list['contactId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # tag_application_GetByObject/获取某个应用的标签使用情况-马叔
    def test_336_tag_application_GetByObject(self):
        result, desc = api_most_all().tag_application_GetByObject("HW_UAT", list['HW_UAT_domain'],list['tenantId'], list['seminarId_instanceId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # app_seminar_getList/该接口为APP专用接口，项目不要使用，获取会议列表
    def test_337_app_seminar_getList(self):
        result, desc = api_most_all().app_seminar_getList("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # tag_application_getByOpenId/通过粉丝OpenId来获取用户的标签
    def test_338_tag_application_getByOpenId(self):
        result, desc = api_most_all().tag_application_getByOpenId("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # app_seminar_signingPoint_checkIn_create/该接口为APP专用接口，项目不要使用，创建签到信息
    def test_339_app_seminar_signingPoint_checkIn_create(self):
        result, desc = api_most_all().app_seminar_signingPoint_checkIn_create("HW_UAT", list['HW_UAT_domain'], list['signingPointId'], list['contactId'], list['seminarId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #app_seminar_signingPoint_checkIn_getList/该接口为APP专用接口，项目不要使用，获取签到历史记录
    def test_340_app_seminar_signingPoint_checkIn_getList(self):
        result, desc = api_most_all().app_seminar_signingPoint_checkIn_getList("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #app_seminar_signingPoint_checkIn_getListCompressed/获取签到历史记录,压缩版
    def test_341_app_seminar_signingPoint_checkIn_getListCompressed(self):
        code = api_most_all().app_seminar_signingPoint_checkIn_getListCompressed("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'], list['bakSess'])
        self.assertEqual(code,200)
    #app_seminar_signingPoint_contact_getList/该接口为APP专用接口，项目不要使用，获取签到点通道下人员
    def test_342_app_seminar_signingPoint_contact_getList(self):
        result, desc = api_most_all().app_seminar_signingPoint_contact_getList("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'], list['signingPointId'], list['passageId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #account_channel_get/获取实例详情信息
    def test_343_account_channel_get(self):
        result, desc = api_most_all().account_channel_get("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    #account_getAuth/获取验证信息
    def test_344_account_getAuth(self):
        result, desc = api_most_all().account_getAuth("HW_UAT", list['HW_UAT_domain'], list['nodeId'], list['bakSess'], list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    #account_getAuthByInstance/该接口为后台接口，后期即将移除，请不要继续使用，通过实例获取验证信息
    def test_345_account_getAuthByInstance(self):
        result, desc = api_most_all().account_getAuthByInstance("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #admin_member_identification_query/客户管理-注册用户-根据自定义列表字段查询注册用户列表
    def test_346_admin_member_identification_query(self):
        result, desc = api_most_all().admin_member_identification_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #anonymous_getId/获取一个全局用户Id（cookieId）
    def test_347_anonymous_getId(self):
        result, desc = api_most_all().anonymous_getId("HW_UAT", list['HW_UAT_domain'])
        self.assertEqual(result, 0, desc)
    #anonymous_setInfo/设置匿名用户信息
    def test_348_anonymous_setInfo(self):
        result, desc = api_most_all().anonymous_setInfo("HW_UAT", list['HW_UAT_domain'])
        self.assertEqual(result, 0, desc)
    #tag_application_GetListByType/查询租户下某种对象类型的应用的标签列表
    def test_349_tag_application_GetListByType(self):
        result, desc = api_most_all().tag_application_GetListByType("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    #tag_field_GetList/？？？？？？
    def test_350_tag_field_GetList(self):
        result, desc = api_most_all().tag_field_GetList("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #api_article_category_interaction_browse/记录栏目浏览互动行为
    def test_351_api_article_category_interaction_browse(self):
        result, desc = api_most_all().api_article_category_interaction_browse("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['categoryId'], list['wechatId'])
        self.assertEqual(result, 0, desc)
    #api_article_category_interaction_share/记录栏目分享互动行为
    def test_352_api_article_category_interaction_share(self):
        result, desc = api_most_all().api_article_category_interaction_share("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['categoryId'], list['wechatId'])
        self.assertEqual(result, 0, desc)
    #tag_use_getListByType/获取租户可用的标签列表
    def test_353_tag_use_getListByType(self):
        result, desc = api_most_all().tag_use_getListByType("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['nodeId'], list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    #api_article_category_query/项目使用，获取栏目列表/栏目id为空
    def test_354_api_article_category_query(self):
        result, desc = api_most_all().api_article_category_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #api_article_get/获取文章详情
    def test_355_api_article_get(self):
        result, desc = api_most_all().api_article_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['articleId'])
        self.assertEqual(result, 0, desc)
    #template_template_getConfig/获取模板配置
    def test_356_template_template_getConfig(self):
        result, desc = api_most_all().template_template_getConfig("HW_UAT", list['HW_UAT_domain'])
        self.assertEqual(result, 0, desc)
    #api_article_interaction_create/记录文章的互动记录，包含浏览和分享
    def test_357_api_article_interaction_create(self):
        result, desc = api_most_all().api_article_interaction_create("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['articleId'])
        self.assertEqual(result, 0, desc)
    #templateMessage_batchSend/发送模板消息，微信模板,templateId-为开启的模板id
    def test_358_templateMessage_batchSend(self):
        result, desc = api_most_all().HW_UAT_templateMessage_batchSend("HW_UAT", list['HW_UAT_domain'], list['wechatId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #api_article_like_check/检查当前用户是否可以对文章点赞
    def test_359_api_article_like_check(self):
        result, desc = api_most_all().api_article_like_check("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['articleId'])
        self.assertEqual(result, 0, desc)
# templateMessage_getContactList/获取粉丝列表，发送模板消息用
    def test_360_templateMessage_getContactList(self):
        result, desc = api_most_all().templateMessage_getContactList("HW_UAT", list['HW_UAT_domain'],list['wechatId'])
        self.assertEqual(result, 0, desc)
    # api_article_query/获取文章列表
    def test_361_api_article_query(self):
        result, desc = api_most_all().api_article_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # topic_post_getAllList/获取留言列表根据指定条件
    def test_362_topic_post_getAllList(self):
        result, desc = api_most_all().topic_post_getAllList("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'],list['tenantId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # topic_stat_homePage/获取讨论版的列表
    def test_363_topic_stat_homePage(self):
        result, desc = api_most_all().topic_stat_homePage("HW_UAT", list['HW_UAT_domain'], list['tenantId'],  list['seminarId_instanceId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # api_member_contacts_get/获取注册用户信息
    def test_364_api_member_contacts_get(self):
        result, desc = api_most_all().api_member_contacts_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # member_register/注册
    def test_365_member_register(self):
        result, desc, loginId = api_most_all().member_register("HW_UAT", list["HW_UAT_domain"], list['tenantId'],list["schemaId"],list["nophoneform"])
        self.assertEqual(result, 0, desc)
        list["loginId"] = loginId
    # article_shareRecord/分享记录，globalUserId、openId和sess至少填一个
    def test_366_article_shareRecord(self):
        result, desc = api_most_all().article_shareRecord("HW_UAT", list['HW_UAT_domain'], list['articleId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # account_changePassword/该接口为后台接口，后期即将移除，请不要继续使用，修改密码
    def test_367_account_changePassword(self):
        result, desc = api_most_all().account_changePassword("HW_UAT", list['HW_UAT_domain'], list['bakSess'], list['password'])
        self.assertEqual(result, 0, desc)
    # api_member_contacts_password_update/当前注册用户登录后修改密码
    def test_368_api_member_contacts_password_update(self):
        result, desc = api_most_all().api_member_contacts_password_update("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['member_password'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # admin_member_identification_updatelog_query/客户管理-注册用户-查询注册用户变更记录日志列表
    def test_369_admin_member_identification_updatelog_query(self):
        result, desc = api_most_all().admin_member_identification_updatelog_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['loginId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # api_member_contacts_update/当前注册用户更新自己的信息
    def test_370_api_member_contacts_update(self):
        result, desc = api_most_all().api_member_contacts_update("HW_UAT", list['HW_UAT_domain'],list['tenantId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # anonymous_checkSess/验证前台sess
    def test_371_anonymous_checkSess(self):
        result, desc = api_most_all().anonymous_checkSess("HW_UAT", list['HW_UAT_domain'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # api_questionnaire_share/分享问卷行为
    def test_372_api_questionnaire_share(self):
        result, desc = api_most_all().api_questionnaire_share("HW_UAT", list['HW_UAT_domain'], list['questionid_sj'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # api_file_interaction_share/记录文件分享互动行为
    def test_373_api_file_interaction_share(self):
        result, desc = api_most_all().api_file_interaction_share("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['fileIds'])
        self.assertEqual(result, 0, desc)
    # api_file_query/查询文件列表（带分页）
    def test_374_api_file_query(self):
        result, desc = api_most_all().api_file_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['fileId'], list['fileIds'])
        self.assertEqual(result, 0, desc)
    # api_luckydraw_browse/浏览抽奖
    def test_375_api_luckydraw_browse(self):
        result, desc = api_most_all().api_luckydraw_browse("HW_UAT", list['HW_UAT_domain'], list['luckyDrawId'], list['tenantId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # api_luckydraw_fieldinfo_query/获取前台显示中奖字段
    def test_376_api_luckydraw_fieldinfo_query(self):
        result, desc = api_most_all().api_luckydraw_fieldinfo_query("HW_UAT", list['HW_UAT_domain'], list['luckyDrawId'], list['bigScreenId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # api_luckydraw_fieldinfo_update-设置前台显示中奖字段
    def test_377_api_luckydraw_fieldinfo_update(self):
        result, desc = api_most_all().api_luckydraw_fieldinfo_update("HW_UAT", list['HW_UAT_domain'], list['luckyDrawId'],list['bigScreenId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # api_luckydraw_get/获取抽奖详情
    def test_378_api_luckydraw_get(self):
        result, desc = api_most_all().api_luckydraw_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['luckyDrawId'])
        self.assertEqual(result, 0, desc)
    # api_luckydraw_share/转发(分享)抽奖
    def test_379_api_luckydraw_share(self):
        result, desc = api_most_all().api_luckydraw_share("HW_UAT", list['HW_UAT_domain'], list['luckyDrawId'],list['tenantId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    #api_luckydraw_user_query/获取大屏抽奖用户(1-100条)
    def test_380_api_luckydraw_user_query(self):
        result, desc = api_most_all().api_luckydraw_user_query("HW_UAT", list['HW_UAT_domain'], list['luckyDrawId'], list['bigScreenId'])
        self.assertEqual(result, 0, desc)
    #api_member_contacts_check/检查唯一字段值是不是可用
    def test_381_api_member_contacts_check(self):
        result, desc = api_most_all().api_member_contacts_check("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['schemaId'])
        self.assertEqual(result, 0, desc)
    #api_member_image_code_get/获取图片验证码
    def test_382_api_member_image_code_get(self):
        code = api_most_all().api_member_image_code_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(code,200)
    #api_product_query/获取产品线下产品列表
    def test_383_api_product_query(self):
        result, desc = api_most_all().api_product_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['productLineId'])
        self.assertEqual(result, 0, desc)
    #获取前台sesssion-1
    # def test_384_member_login1(self):
    #     flag, loginSess = api_most_all().member_login('HW_UAT', list['HW_UAT_domain'], list['tenantId'], list['schemaId'],list['memberFormId'], list['memberSchemaId'], list['unique'],list['password'])
    #     self.assertEqual(flag, 0, "获取前台登录session失败")
    #     list['loginSess1'] = loginSess
    #     print"list['loginSess1']:", list['loginSess1']
    #api_seminar_app_checkinpoint_userpermit_query/app专用，获取用户签到点权限列表
    def test_385_api_seminar_app_checkinpoint_userpermit_query(self):
        result, desc = api_most_all().api_seminar_app_checkinpoint_userpermit_query("HW_UAT", list['HW_UAT_domain'], list['seminarId'], list['loginSess'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #api_seminar_bigscreen_information_push/向NODE服务推送消息
    def test_386_api_seminar_bigscreen_information_push(self):
        result, desc = api_most_all().api_seminar_bigscreen_information_push("HW_UAT", list['HW_UAT_domain'], list['bigScreenId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #article_like/点赞，globalUserId、openId和sess至少填一个
    def test_387_article_like(self):
        result, desc = api_most_all().article_like_one("HW_UAT", list['HW_UAT_domain'], list['articleId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    #seminar_getList/获取会议列表，该接口为APP专用接口，项目不要使用
    def test_388_seminar_getList(self):
        result, desc = api_most_all().seminar_getList("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #articleCategory_get/获取单个栏目
    def test_389_articleCategory_get(self):
        result, desc = api_most_all().articleCategory_get_one("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['categoryId'])
        self.assertEqual(result, 0, desc)
    #interaction_record/记录一个互动
    def test_390_interaction_record(self):
        result, desc = api_most_all().interaction_record("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #product_crossLine_getListByIdList/根据产品id数组获取产品列表
    def test_391_product_crossLine_getListByIdList(self):
        result, desc = api_most_all().product_crossLine_getListByIdList("HW_UAT", list['HW_UAT_domain'], list['productLine'])
        self.assertEqual(result, 0, desc)
    #api_seminar_contacts_Query/根据session获取此用户在某租户下参与过的所有会议
    def test_392_api_seminar_contacts_Query(self):
        result, desc = api_most_all().api_seminar_contacts_Query("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #project_getInfoByLang/通过openId获取联系人信息,可返回不同地区语言
    def test_393_project_getInfoByLang(self):
        result, desc = api_most_all().project_getInfoByLang("HW_UAT", list['HW_UAT_domain'], list['wechatId'])
        self.assertEqual(result, 0, desc)
    #article_getListByTags/获取租户下文章列表，可通过标签筛选
    def test_394_article_getListByTags(self):
        result, desc = api_most_all().article_getListByTags("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #api_shorturl_generate/生成短地址,但是url按现在的url设置，因为路径变更了
    def test_395_api_shorturl_generate(self):
        result, desc = api_most_all().api_shorturl_generate("HW_UAT", list['HW_UAT_domain'])
        self.assertEqual(result, 0, desc)
    #api_seminar_app_signingpoint_group_Query/获取会议下的所有签到点信息
    def test_396_api_seminar_app_signingpoint_group_Query(self):
        result, desc = api_most_all().api_seminar_app_signingpoint_group_Query("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    #file_folder_getReleaseFileList/文件夹列表
    def test_397_file_folder_getReleaseFileList(self):
        result, desc = api_most_all().file_folder_getReleaseFileList("HW_UAT", list['HW_UAT_domain'], list['FolderId'],list['accKey'])
        self.assertEqual(result, 0, desc)
    #member_identification_information_GetByOpenId/有问题，通过openId获取注册信息
    def test_398_member_identification_information_GetByOpenId(self):
        result, desc = api_most_all().member_identification_information_GetByOpenId("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['openId'],list['unionId'])
        self.assertEqual(result, 0, desc)
    #app_seminar_contact_getListCompressed/该接口为APP专用接口，项目不要使用，获取压缩过的会议联系人
    def test_399_app_seminar_contact_getListCompressed(self):
        code = api_most_all().app_seminar_contact_getListCompressed("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'], list['bakSess'])
        self.assertEqual(code,200)
# app_seminar_signingPoint_getGroupList/该接口为APP专用接口，项目不要使用，获取会议下的所有签到点信息
    def test_400_app_seminar_signingPoint_getGroupList(self):
        result, desc = api_most_all().app_seminar_signingPoint_getGroupList("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # comment_getList/获取评论列表
    def test_401_comment_getList(self):
        result, desc = api_most_all().obtain_comment_getList("HW_UAT", list['HW_UAT_domain'],list['tenantId'],list['topicId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # app_seminar_contact_field_getCustomFields/该接口为APP专用接口，项目不要使用，获取联系人字段
    def test_402_app_seminar_contact_field_getCustomFields(self):
        result, desc = api_most_all().app_seminar_contact_field_getCustomFields("HW_UAT", list['HW_UAT_domain'],list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # webinar_open_newRegistration/注册用户接口
    def test_403_webinar_open_newRegistration(self):
        result, desc = api_most_all().webinar_open_newRegistration("HW_UAT", list['HW_UAT_domain'],list['tenantId'],list['schemaId'],list['webinarId_instanceId'],list['memberFormId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # file_cutImage/裁剪平台图片资源内容
    def test_404_file_cutImage(self):
        result, desc = api_most_all().file_cutImage("HW_UAT", list['HW_UAT_domain'], list['mappingId'])
        self.assertEqual(result, 0, desc)
    # member_geneRegister/注册用户
    def test_405_member_geneRegister(self):
        result, desc,memberId = api_most_all().member_geneRegister("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['schemaId'], list['nophoneform'], list['loginSess'])
        self.assertEqual(result, 0, desc)
        # list['memberId']=memberId
    # app_seminar_contact_getList/该接口为APP专用接口，项目不要使用，获取会议联系人
    def test_406_app_seminar_contact_getList(self):
        result, desc = api_most_all().app_seminar_contact_getList("HW_UAT", list['HW_UAT_domain'], list['webinarId_instanceId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # member_getById/获取某个会员信息
    def test_407_member_getById(self):
        result, desc = api_most_all().member_getById("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['memberId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # article_getListByTags
    def test_408_article_getListByTags(self):
        result, desc = api_most_all().article_getListByTags("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # app_seminar_contact_getByUniqueField/根据参会二维码获取会议联系人
    def test_409_app_seminar_contact_getByUniqueField(self):
        result, desc = api_most_all().app_seminar_contact_getByUniqueField("HW_UAT", list['HW_UAT_domain'], list['seminarId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # member_identification_getList/获取注册用列表,有问题
    def test_410_member_identification_getList(self):
        result, desc = api_most_all().member_identification_getList("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['schemaId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # member_member_setEnable/启用/停用注册用户,马叔
    def test_411_member_member_setEnable(self):
        result, desc = api_most_all().member_member_setEnable("HW_UAT", list['HW_UAT_domain'], list['schemaId'], list['tenantId'], list['bakSess'],list['memberId'])
        self.assertEqual(result, 0, desc)
    # api_file_interaction_preview/记录文件预览互动行为
    def test_412_api_file_interaction_preview(self):
        result, desc = api_most_all().api_file_interaction_preview("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['fileIds'])
        self.assertEqual(result, 0, desc)
    # api_member_form_get/获取表单信息
    def test_413_api_member_form_get(self):
        result, desc = api_most_all().api_member_form_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['memberFormId'])
        self.assertEqual(result, 0, desc)
    # webinar_open_interaction_fileDownLoad/下载文件互动记录,有问题
    def test_414_webinar_open_interaction_fileDownLoad(self):
        result, desc = api_most_all().webinar_open_interaction_fileDownLoad("HW_UAT", list['HW_UAT_domain'], list['loginSess'],list['webinarId_instanceId'],list['fileId'])
        self.assertEqual(result, 0, desc)
    # open_interaction_fileDownLoad/下载文件互动记录
    # def test_open_interaction_fileDownLoad_415(self):
    #     result, desc = api_most_all().webinar_open_interaction_fileDownLoad("HW_UAT", list['HW_UAT_domain'], list['loginSess1'],list['webinarId_instanceId'],list['fileId'])
    #     self.assertEqual(result, 0, desc)
    # api_webinar_live_sendmsg-直播发消息(提问)
    def test_416_api_webinar_live_sendmsg(self):
        result, desc = api_most_all().api_webinar_live_sendmsg("HW_UAT", list['HW_UAT_domain'], list['loginSess'],list['webinarId'],list['tenantId'])
        self.assertEqual(result, 0, desc)
    # api_webinar_live_site_browse/访问直播会议专题页
    def test_417_api_webinar_live_site_browse(self):
        result, desc = api_most_all().api_webinar_live_site_browse("HW_UAT", list['HW_UAT_domain'], list['loginSess'],list['webinarId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # member_form_getList/该接口为后台接口，后期即将移除，请不要继续使用，获取体系下的注册表单列表
    def test_418_member_form_getList(self):
        result, desc = api_most_all().member_form_getList("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['memberSchemaId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # seminar_topicTemplate_seminar_get/获取会议相关信息
    def test_419_seminar_topicTemplate_seminar_get(self):
        result, desc = api_most_all().seminar_topicTemplate_seminar_get("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    #api_webinar_live_share/直播分享
    def test_420_api_webinar_live_share(self):
        result, desc = api_most_all().api_webinar_live_share("HW_UAT", list['HW_UAT_domain'], list['loginSess'], list['webinarId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #api_webinar_demand_share/分享点播
    def test_421_api_webinar_demand_share(self):
        result, desc = api_most_all().api_webinar_demand_share("HW_UAT", list['HW_UAT_domain'], list['loginSess'], list['webinarId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #webinar_demand_site_browse/访问点播专题页面
    def test_422_webinar_demand_site_browse(self):
        result, desc = api_most_all().webinar_demand_site_browse("HW_UAT", list['HW_UAT_domain'], list['loginSess'], list['webinarId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #api_webinar_demand_play/播放点播
    def test_423_api_webinar_demand_play(self):
        result, desc = api_most_all().api_webinar_demand_play("HW_UAT", list['HW_UAT_domain'], list['loginSess'], list['webinarId'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #member_integral_update/积分变更
    def test_424_member_integral_update(self):
        result, desc = api_most_all().member_integral_update("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['loginSess'], list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    #admin_account_create/账号-用户管理添加账号
    def test_425_admin_account_create(self):
        result, desc,userid = api_most_all().admin_account_create("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['nodeId'], list['password'], list['bakSess'])
        self.assertEqual(result, 0, desc)
        list['userid']=userid
    #admin_account_update/编辑用户资料
    def test_426_admin_account_update(self):
        result, desc = api_most_all().admin_account_update("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['nodeId'], list['userid'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #admin_account_disableUser/禁用用户
    def test_427_admin_account_disableUser(self):
        result, desc = api_most_all().admin_account_disableUser("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['nodeId'], list['userid'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #admin_account_delete/删除用户
    def test_428_admin_account_delete(self):
        result, desc = api_most_all().admin_account_delete("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['userid'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #admin_application_get/获取手机key值
    def test_429_admin_application_get(self):
        result, desc = api_most_all().admin_application_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #sms_addSmsLog/发送短信
    def test_430_sms_addSmsLog(self):
        result, desc = api_most_all().sms_addSmsLog("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    #api_article_collection_check/检查当前注册用户是否可以收藏该文章
    def test_431_api_article_collection_check(self):
        result, desc = api_most_all().api_article_collection_check("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['articleId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    #api_customform_get/获取自定义表单详情
    def test_432_api_customform_get(self):
        result, desc = api_most_all().api_customform_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['customFormId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # api_file_download_interaction_query/获取注册用户邮件中文章模板关联文件下载的记录
    def test_433_api_file_download_interaction_query(self):
        result, desc = api_most_all().api_file_download_interaction_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    #api_member_form_share/分享注册表单记录互动行为
    def test_434_api_member_form_share(self):
        result, desc = api_most_all().api_member_form_share("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['memberFormId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    #questionary_getResultList/该接口为后台接口，后期即将移除，请不要继续使用，获取从某个实例进来回答问卷的列表
    def test_435_questionary_getResultList(self):
        result, desc = api_most_all().questionary_getResultList("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    #member_GetTokenByOpenId/通过openId 获取token
    def test_436_member_GetTokenByOpenId(self):
        result, desc,token = api_most_all().member_GetTokenByOpenId("HW_UAT", list['HW_UAT_domain'])
        self.assertEqual(result, 0, desc)
        list['tokenfor_memberbind']=token
    #member_admin_unbindWeChat/用户和微信解绑--数据删除插件使用
    def test_437_member_admin_unbindWeChat(self):
        result, desc = api_most_all().member_admin_unbindWeChat("HW_UAT", list['HW_UAT_domain'], list['wechatId'], list['memberSchemaId'], list['wechatId'])
        self.assertEqual(result, 0, desc)
    #account_verifySession/验证session,并获取相应的信息
    def test_438_account_verifySession(self):
        result, desc = api_most_all().account_verifySession("HW_UAT", list['HW_UAT_domain'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    #admin_member_integral_updateitems/批量积分变更
    def test_439_admin_member_integral_updateitems(self):
        result, desc = api_most_all().admin_member_integral_updateitems("HW_UAT", list['HW_UAT_domain'], list['seminarId_instanceId'], list['wechatId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # api/seminar/signingpoint/query/查询实例下的签到点列表
    def test_440_api_seminar_signingpoint_query(self):
        result, desc = api_most_all().api_seminar_signingpoint_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId_instanceId'])
        self.assertEqual(result, 0, desc)
    # admin/account/userRole/set/编辑后台账号权限
    def test_441_admin_account_userRole_set(self):
        result, desc = api_most_all().admin_account_userRole_set("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['nodeId'], list['bakSess'],list['userId'],list['roleId'])
        self.assertEqual(result, 0, desc)
    # admin/tag/trigger/score/getlist/根据租户id获取行为标签触发分值
    def test_442_admin_tag_trigger_score_getlist(self):
        result, desc = api_most_all().admin_tag_trigger_score_getlist("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # api/seminar/contacts/ticket/get/获取联系人电子门票图片
    def test_443_api_seminar_contacts_ticket(self):
        result, desc = api_most_all().api_seminar_contacts_ticket("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['contactId'],list['qrCode'])
        self.assertEqual(result, 0, desc)
    # api/seminar/contacts/qrcode/browse/参会人签到二维码浏览（次数+1）
    def test_444_api_seminar_contacts_qrcode_browse(self):
        result, desc = api_most_all().api_seminar_contacts_qrcode_browse("HW_UAT", list['HW_UAT_domain'], list['tenantId'])
        self.assertEqual(result, 0, desc)
    # customForm_reAction自定义表单重复提交，更新之前的提交结果(项目需要用)
    def test_445_customForm_reAction(self):
        result, desc = api_most_all().customForm_reAction("HW_UAT", list['HW_UAT_domain'], list['registerFormId'])
        self.assertEqual(result, 0, desc)
    # api/file/folder/interaction/share/记录文件夹分享互动行为
    def test_446_api_file_folder_interaction_share(self):
        result, desc = api_most_all().api_file_folder_interaction_share("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['FolderId'])
        self.assertEqual(result, 0, desc)
    # member_integral_get/查询注册用户|微信粉丝积分
    def test_447_member_integral_get(self):
        result, desc = api_most_all().member_integral_get("HW_UAT", list['HW_UAT_domain'], list['tenantId'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # api/member/integral/integrallog/query/查询变更日志
    def test_448_api_member_integral_integrallog_query(self):
        result, desc = api_most_all().api_member_integral_integrallog_query("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['seminarId_instanceId'],list['loginSess'])
        self.assertEqual(result, 0, desc)
    # admin_account_password_update/客户管理中修改用户密码
    def test_449_admin_account_password_update(self):
        result, desc = api_most_all().admin_account_password_update("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['nodeId'], list['bakSess'])
        self.assertEqual(result, 0, desc)
    # 二维码密串登录
    def test_450_dimensional_code_string(self):
        result, desc = api_most_all().dimensional_code_string("HW_UAT", list['HW_UAT_domain_com'],list['loginToken'])
        self.assertEqual(result, 0, desc)
    # account/getOAuthTokenByOpen/为account/verifyToken提供token
    def test_451_account_getOAuthTokenByOpen(self):
        result, desc,pos = api_most_all().account_getOAuthTokenByOpen("HW_UAT", list['HW_UAT_domain_com'],list['tenantId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
        list['tokenfor_verifyToken']=pos
    # account/verifyToken/为九芝兰提供验证token的接口，九芝兰使用smarket3给它的token来查询租户信息
    def test_452_account_verifyToken(self):
        result, desc = api_most_all().account_verifyToken("HW_UAT", list['HW_UAT_domain'],list['tokenfor_verifyToken'])
        self.assertEqual(result, 0, desc)
    # member/GetTokenByOpenId/通过openId 获取token
    def test_453_member_GetTokenByOpenId(self):
        result, desc, pos = api_most_all().member_GetTokenByOpenId_a("HW_UAT", list['HW_UAT_domain'])
        self.assertEqual(result, 0, desc)
        list['tokenfor_memberbind'] = pos
    # member/bind/绑定第三方 当前实名用户与第三方登录用户绑定
    def test_454_member_bind(self):
        result, desc = api_most_all().member_bind("HW_UAT", list['HW_UAT_domain'], list['loginSess'],list['tokenfor_memberbind'])
        self.assertEqual(result, 0, desc)
    # member/unbind/解绑第三方 当前实名用户与第三方登录用户解绑
    def test_455_member_unbind(self):
        result, desc = api_most_all().member_unbind("HW_UAT", list['HW_UAT_domain'], list['loginSess'])
        self.assertEqual(result, 0, desc)

    # member_geneUpdate/更新注册用户信息
    def test_457_member_geneUpdate(self):
        result, desc = api_most_all().member_geneUpdate("HW_UAT", list['HW_UAT_domain'], list['loginSess'])
        self.assertEqual(result, 0, desc)
    # 给对象打标签
    def test_004_tag_application_SetOnObject(self):
        result, desc = api_most_all().tag_application_SetOnObject("HW_UAT", list['HW_UAT_domain'], list['tenantId'],list['tagSchemaId'],list['tagFieldId'],list['fieldName'],list['displayName'],list['tagId'],list['bakSess'])
        self.assertEqual(result, 0, desc)
    # 查看自己的签到记录
    def test_458_seminar_signingPoint_getCheckInLog(self):
        result, desc = api_most_all().seminar_signingPoint_getCheckInLog_contactId("HW_UAT",list['HW_UAT_domain'],list['tenantId'],list['bakSess'],list['seminarId'],list['seminarId_instanceId'],list['signingPointId'],list['passageId'],list['contactId'])
        self.assertEqual(result, 0, desc)
    # 获取一个图片验证码
    def test_459_member_getImageCode(self):
        code = api_most_all().member_getImageCode("HW_UAT", list['HW_UAT_domain'])
        self.assertEqual(code, 200, "断言200错误")
if __name__ == '__main__':
    suite = unittest.TestSuite()
    # 指定单个单元测试（ 需要配置运行方式才能走main函数，参考https://www.cnblogs.com/youreyebows/p/7867508.html）
    suite = unittest.TestSuite()
    # 指定单个单元测试（ 需要配置运行方式才能走main函数，参考https://www.cnblogs.com/youreyebows/p/7867508.html）
    suite.addTest(HW_UAT_interface("test_001_account_login"))
    # suite.addTest(HW_UAT_interface("test_002_member_login"))
    # suite.addTest(HW_UAT_interface("test_004_tag_application_SetOnObject"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_member_password_update_005"))
    # suite.addTest(HW_UAT_interface("test_006_api_member_contacts_simple_signin"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_identification_UpdateAvatar_007"))
    # suite.addTest(HW_UAT_interface("test_008_member_update"))
    # suite.addTest(api_most_interface("test_009_articleCategory_get"))
    # suite.addTest(api_most_interface_HW_UAT("test_comment_getList_010"))
    # suite.addTest(api_most_interface_HW_UAT("test_forum_getForumInfo_011"))
    # suite.addTest(api_most_interface_HW_UAT("test_forum_getReplyList_012"))
    # suite.addTest(api_most_interface_HW_UAT("forum_post_create_013"))  # 生成pos
    # suite.addTest(api_most_interface_HW_UAT("forum_post_get_014"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_browse_015"))
    # suite.addTest(api_most_interface_HW_UAT("test_forum_post_getMainPost_016"))
    # suite.addTest(api_most_interface_HW_UAT("test_forum_post_getMainPostNumber_017"))
    # suite.addTest(api_most_interface_HW_UAT("test_forum_post_getPersonalPostList_018"))
    # suite.addTest(api_most_interface_HW_UAT("test_forum_post_getReplyPost_019")) # 与13一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_forum_post_like_020"))
    # suite.addTest(api_most_interface_HW_UAT("test_forum_post_update_021"))
    # suite.addTest(api_most_interface_HW_UAT("test_forum_section_getList_022"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_browseRecord_023"))
    # suite.addTest(api_most_interface_HW_UAT("test_forum_stat_homePage_024"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_Collection_025"))
    # suite.addTest(api_most_interface_HW_UAT("test_forum_post_deletePost_026"))#(需要跟用例“013”一起执行)
    # suite.addTest(api_most_interface_HW_UAT("test_file_create_027"))  # 生成fileIds
    # suite.addTest(api_most_interface_HW_UAT("test_article_getDetail_028"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_getLikeStatus_029"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_getList_030"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_getListByIds_031"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_getListByProject_032"))
    # suite.addTest(api_most_interface_HW_UAT("test_file_update_033"))#(需要跟用例“027”一起执行)
    # suite.addTest(api_most_interface_HW_UAT("test_questionary_get_034"))
    # suite.addTest(api_most_interface_HW_UAT("test_questionary_view_035"))
    # suite.addTest(api_most_interface_HW_UAT("test_questionary_action_036"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_like_037"))
    # suite.addTest(HW_UAT_interface("test_038_comment_create"))  #生成content
    # suite.addTest(api_most_interface_HW_UAT("test_comment_front_delete_039"))#需要与038一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_comment_like_040"))#需要与038一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_article_getListByTag_041"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_getListForProject_042"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_getRecommendedList_043"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_getSharedList_044"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_getTrees_045"))
    # suite.addTest(api_most_interface_HW_UAT("test_collect_add_046"))
    # suite.addTest(api_most_interface_HW_UAT("test_collect_cancel_047"))
    # suite.addTest(api_most_interface_HW_UAT("test_collect_search_048"))
    # suite.addTest(api_most_interface_HW_UAT("test_articleCategory_getList_049"))
    # suite.addTest(api_most_interface_HW_UAT("test_articleCategory_getSubList_050"))
    # suite.addTest(api_most_interface_HW_UAT("test_questionary_getList_051"))
    # suite.addTest(api_most_interface("test_052_questionary_reAction"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_share_053"))
    # suite.addTest(api_most_interface_HW_UAT("test_file_folder_getInsOfFileList_054"))
    # suite.addTest(api_most_interface_HW_UAT("test_questionary_exam_action_055"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_guest_getList_056"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_guest_getGroupList_057"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_guest_field_Get_058"))
    # suite.addTest(api_most_interface_HW_UAT("test_guest_get_059"))
    # suite.addTest(api_most_interface_HW_UAT("test_guest_getList_060"))
    # suite.addTest(api_most_interface_HW_UAT("test_file_getListForWeChat_061")) # 此用例要与test_file_create_027同时执行
    # suite.addTest(api_most_interface_HW_UAT("test_poll_get_062"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_agenda_get_063"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_agenda_getGroupList_064"))
    # suite.addTest(api_most_interface_HW_UAT("test_poll_action_065"))
    # suite.addTest(api_most_interface_HW_UAT("test_poll_getList_066"))
    # suite.addTest(api_most_interface_HW_UAT("test_poll_HasParticipation_067"))
    # suite.addTest(api_most_interface_HW_UAT("test_poll_sendCheckCode_068"))
    # suite.addTest(api_most_interface_HW_UAT("test_poll_start_069"))
    # suite.addTest(api_most_interface_HW_UAT("test_poll_stat_getResult_070"))
    # suite.addTest(api_most_interface_HW_UAT("test_poll_stat_getTotal_071"))
    # suite.addTest(api_most_interface_HW_UAT("test_poll_tool_checkRegistration_072"))
    # suite.addTest(api_most_interface_HW_UAT("test_poll_view_073"))
    # suite.addTest(api_most_interface_HW_UAT("test_product_crossLine_getList_074"))
    # suite.addTest(api_most_interface_HW_UAT("test_product_get_075"))
    # suite.addTest(api_most_interface_HW_UAT("test_product_getList_076"))
    # suite.addTest(api_most_interface_HW_UAT("test_productLine_category_getCategoryTreeList_077"))
    # suite.addTest(api_most_interface_HW_UAT("test_productLine_category_getConfigInfo_078"))
    # suite.addTest(api_most_interface_HW_UAT("test_productLine_category_getDetailList_079"))
    # suite.addTest(api_most_interface_HW_UAT("test_productLine_category_getList_080"))
    # suite.addTest(api_most_interface_HW_UAT("test_productLine_field_get_081"))
    # suite.addTest(api_most_interface_HW_UAT("test_productLine_get_082"))
    # suite.addTest(api_most_interface_HW_UAT("test_productLine_getList_083"))
    # suite.addTest(api_most_interface_HW_UAT("test_weChat_get_084"))
    # suite.addTest(api_most_interface_HW_UAT("test_weChat_getAppId_085"))
    # suite.addTest(api_most_interface_HW_UAT("test_weChat_getConfig_086"))
    # suite.addTest(api_most_interface_HW_UAT("test_weChat_getDef_087"))
    # suite.addTest(api_most_interface_HW_UAT("test_weChat_getDefWx_088"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_product_get_089"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_productLine_category_config_get_090"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_productLine_category_query_091"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_productLine_field_get_092"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_event_interaction_check_093"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_event_interaction_pollResult_094"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_attend_095"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_checkRegistration_096"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_getApplicantInfo_097"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_getAttendList_098"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_getCustomFormInfo_099"))
    suite.addTest(HW_UAT_interface("test_100_seminar_bigScreen_forBigScreenWall_checkIn"))#  报错，未在当前通道
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_getDemandInfo_101"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_getServerTime_102"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_getVideoTimeLine_103"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_getWebinarInfo_104"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_getWebinarList_105"))
    # suite.addTest(api_most_interface_HW_UAT("test_customForm_action_106")) #此用例要与用例test_member_login_002同时执行
    # suite.addTest(HW_UAT_interface("test_107_webinar_open_join")) #报错，参数无效
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_project_shenWan_GetWebinar_108"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_project_shenWan_GetListByIds_109")) #报错，参数无效
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_project_shenWan_GetDemandList_110"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_trackingCode_getList_111"))
    # suite.addTest(HW_UAT_interface("test_112_webinar_open_recordVideoViewCount"))#postman接口不通：点播视频不存在
    # suite.addTest(api_most_interface_HW_UAT("test_questionary_exam_repeatAction_113"))
    # suite.addTest(HW_UAT_interface("test_114_toolb_add_title"))#有问题 待完善（s2接口文档没有该接口）
    # suite.addTest(HW_UAT_interface("test_115_questionary_exam_user_GenerateExam"))#postman接口不通：题库试题为空,不能生成试卷
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_getWebinarListAdvanced_116"))#postman接口不通:检索条件在自定义字段中不存在或检索条件错误
    # suite.addTest(api_most_interface_HW_UAT("test_questionary_exam_user_getAnswers_117"))
    # suite.addTest(api_most_interface_HW_UAT("test_questionary_exam_user_getSingleResult_118"))
    # suite.addTest(HW_UAT_interface("test_119_setting_Verification_code"))#有问题 待完善（s2接口文档没有该接口口文档没有该接口）
    # suite.addTest(HW_UAT_interface("test_120_questionary_sendCheckCode")) #有时能通，有时参数无效
    # suite.addTest(api_most_interface_HW_UAT("test_shortUrl_getList_121"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_webinar_contacts_get_122"))
    # suite.addTest(api_most_interface_HW_UAT("test_shortUrl_urlStats_123"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_webinar_demand_get_124"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_webinar_query_125")) #sort取值超出范围，但将sort注释掉就没问题
    # suite.addTest(HW_UAT_interface("test_126_questionary_tool_checkRegistration"))
    # suite.addTest(api_most_interface_HW_UAT("test_questionary_stat_getResultByAnswerRecord_127")) #将id1id2注释掉就没问题
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_bigScreen_get_128"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_bigScreen_getListByGroup_129"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_bigScreen_getPollPreset_130"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_bigScreen_updateCheckIn_131"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_bigScreen_updateLottery_132"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_bigScreen_updateMessage_133"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_bigScreen_updatePoll_134"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_canInteraction_135"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_contact_checkIdCard_136"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_contact_front_checkIn_137"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_contact_front_editRegContact_138"))
    # suite.addTest(HW_UAT_interface("test_139_seminar_contact_front_getCommonContactInfo"))  # 报错参会者未找到
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_contact_front_getContactInfo_140"))# 报错，类型和参数不匹配
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_contact_front_getRegContact_141"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_contact_front_regSeminar_142"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_contact_front_unRegister_143"))#此用例要与用例test_member_login_002同时执行
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_contact_front_updateSelf_144"))# 未完成（有问题）
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_contact_getContactToWechat_145"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_contact_registerNew_146"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_contact_update_147"))
    # suite.addTest(api_most_interface_HW_UAT("test_post_create_148"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_registration_149")) # 未完成（有问题）
    # suite.addTest(api_most_interface_HW_UAT("test_questionary_HasParticipation_150"))
    # suite.addTest(api_most_interface_HW_UAT("test_post_get_151"))
    # suite.addTest(api_most_interface_HW_UAT("test_post_getListByUser_152"))
    # suite.addTest(api_most_interface_HW_UAT("test_post_getMainAndReplyList_153"))
    # suite.addTest(api_most_interface_HW_UAT("test_post_getMainPost_154"))
    # suite.addTest(api_most_interface_HW_UAT("test_post_getMyPost_155"))
    # suite.addTest(api_most_interface_HW_UAT("test_post_getReplyPost_156"))
    # suite.addTest(api_most_interface_HW_UAT("test_post_like_157"))
    # suite.addTest(api_most_interface_HW_UAT("test_post_update_158"))
    # suite.addTest(api_most_interface_HW_UAT("test_global_topicId_159"))#postman接口不通:帖子不存在或非自己发的帖子
    # suite.addTest(api_most_interface_HW_UAT("test_post_delete_160"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_frontGet_161"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_frontGetList_162"))
    # suite.addTest(HW_UAT_interface("test_163_webinar_registration")) #未找到表单所属类型
    # suite.addTest(api_most_interface_HW_UAT("test_contact_bindMember_164"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_frontGetListByIds_165"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_frontGetStatusList_166"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_get_167"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_getListWithFormId_168"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_register_canRegister_169"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_register_canRegisterNew_170"))
    # suite.addTest(api_most_interface_HW_UAT("test_contact_getByOpenId_171"))
    # suite.addTest(api_most_interface_HW_UAT("test_contact_getContactStatus_172"))
    # suite.addTest(api_most_interface_HW_UAT("test_customForm_seminar_action_173"))
    # suite.addTest(api_most_interface_HW_UAT("test_customForm_checkRegistration_174"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_register_getList_175"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_register_getSubList_176"))
    # suite.addTest(api_most_interface_HW_UAT("test_customForm_checkRepeatable_177"))
    # suite.addTest(api_most_interface_HW_UAT("test_customForm_get_178"))
    # suite.addTest(api_most_interface_HW_UAT("test_customForm_getListByIds_179"))
    # suite.addTest(api_most_interface_HW_UAT("test_customForm_HasParticipation_180"))
    # suite.addTest(api_most_interface_HW_UAT("test_customForm_sendCheckCode_181"))
    # suite.addTest(api_most_interface_HW_UAT("test_customForm_user_getRecordByOpenId_182"))
    # suite.addTest(api_most_interface_HW_UAT("test_customForm_user_getResultByOpenId_183"))
    # suite.addTest(api_most_interface_HW_UAT("test_customForm_view_184"))
    # suite.addTest(api_most_interface_HW_UAT("test_de_contact_front_get_185")) #此用例要与用例test_member_login_002同时执行
    # suite.addTest(api_most_interface_HW_UAT("test_de_contact_front_getSeminars_186"))
    # suite.addTest(api_most_interface_HW_UAT("test_de_contact_getLastSeminarsBySess_187"))
    # suite.addTest(api_most_interface_HW_UAT("test_dic_getList_188"))
    # suite.addTest(api_most_interface_HW_UAT("test_dic_params_getList_189"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_signingPoint_checkIn_getCheckInCount_190"))
    # suite.addTest(api_most_interface_HW_UAT("test_dic_params_getTree_191"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_signingPoint_front_getMyCheckInLog_192"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_signingPoint_getCheckInLog_193"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_signingPoint_getNumberSignInPassage_194"))
    # suite.addTest(api_most_interface_HW_UAT("test_edm_log_create_195"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_subSeminar_frontGet_196"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_subSeminar_getListByType_197"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_topicTemplate_contact_get_198"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_topicTemplate_contact_getByOpenId_199"))
    # suite.addTest(api_most_interface_HW_UAT("test_edm_send_200"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_topicTemplate_contact_getState_201"))
    # suite.addTest(api_most_interface_HW_UAT("test_customForm_isFaceImg_202"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_topicTemplate_contact_getStateBySess_203"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_topicTemplate_seminar_getFormInfo_204"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_topicTemplate_seminar_getWithAllSub_205"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_trackingCode_getList_206"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_bigScreen_forBigScreenWall_getCheckInData_207"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_bigScreen_forBigScreenWall_getWapCheckInfo_208"))
    # suite.addTest(api_most_interface_HW_UAT("test_field_getList_209"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_bigScreen_getWapMessageInfo_210"))
    # suite.addTest(api_most_interface_HW_UAT("test_file_folder_getReleaseFile_211"))#需要和027一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_file_getList_212"))#（需要与用例027同时执行，获取fileIds）
    # suite.addTest(api_most_interface_HW_UAT("test_member_changePwd_213"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_checkUnique_214"))
    # suite.addTest(HW_UAT_interface("test_215_luckyDraw_client_action"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_form_GetForNewForm_216"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_form_GetOAuthUrlByWeChatId_217"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_form_getTemplate_218"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_form_getUnique_219"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_form_search_220"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_form_view_221"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_Query_222")) #AssertionError: successful
    # suite.addTest(api_most_interface_HW_UAT("test_member_geneGet_223"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_site_browse_224"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_site_share_225"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_template_config_get_226"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_get_227"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_topic_board_browse_228"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_login_229"))  # 229生成loginSess3
    # suite.addTest(api_most_interface_HW_UAT("test_api_topic_browse_230"))   # 需要与229,229生成loginSess3一起执行
    # suite.addTest(api_most_interface("test_231_api_topic_comment_query"))   # 需要与229一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_api_topic_forum_post_get_232"))   # 需要与013,013生成pos一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_member_LookUp_233"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_schema_field_GetList_234"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_schema_orderUnique_235"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_schema_field_sorting_GetList_236"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_sendCheckCode_237"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_sendVerificationCode_238")) #(postman此接口不通)  需要与229一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_member_sendVerificationCodeToMail_239"))
    # suite.addTest(api_most_interface("test_240_api_topic_forum_post_query"))  #(postman此接口SESSION无效)需要与229一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_member_updateByField_241")) #需要与229一起执行，(该接口执行不通过，postman此接口也执行不通过报错原因为不能识别的数据格式：。兼容性注册时用到)
    # suite.addTest(api_most_interface_HW_UAT("test_api_topic_forum_post_reply_query_242"))  #(postman此接口SESSION无效)需要与229一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_api_topic_get_243"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_topic_message_Create_244"))  #(postman此接口SESSION无效)需要与229一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_api_topic_message_get_245"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_topic_message_Query_246"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_topic_message_reply_Query_247"))  #(postman此接口SESSION无效)需要与229一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_api_topic_share_248"))  #(postman此接口SESSION无效)需要与229一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_member_loginByOpenId_249"))
    # suite.addTest(api_most_interface_HW_UAT("test_luckyDraw_client_actionByBigScreen_250"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_identification_sorting_Get_251")) #报错，认证失败 需要与其他用例（229）一起执行）
    # suite.addTest(api_most_interface_HW_UAT("test_luckyDraw_client_GetMyRedPacketLog_252"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_customform_browse_253"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_customform_field_check_254"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_customform_submit_255"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_forgetPwd_256"))  #监控200
    # suite.addTest(api_most_interface_HW_UAT("test_member_UpdateIdentityInfo_257"))   #报错，需要泛型对象
    # suite.addTest(api_most_interface_HW_UAT("test_member_interaction_record_258"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_event_interaction_questionnaireResult_259"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_member_associate_Logout_260"))  # 需要与其他用例（229）一起执行）
    # suite.addTest(api_most_interface_HW_UAT("test_member_member_login_261")) # 生成loginSess2
    # suite.addTest(api_most_interface_HW_UAT("test_member_form_get_262"))
    # suite.addTest(HW_UAT_interface("test_263_api_member_contacts_register"))   #报错，系统错误
    # suite.addTest(api_most_interface_HW_UAT("test_api_questionnaire_browse_264"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_questionnaire_get_265"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_questionnaire_query_266"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_questionnaire_submit_267"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_app_getconfiginfo_268"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_app_monitor_getappinfo_269"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_app_monitor_getclientalias_270"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_app_monitor_updateclientinfo_271"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_bigscreen_contacts_Get_272"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_bigscreen_Get_273"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_bigscreen_group_query_274"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_contacts_field_Get_275"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_api_seminar_contacts_Get_276"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_contacts_SignUp_277"))
    # suite.addTest(HW_UAT_interface("test_278_api_seminar_contacts_Update"))#(需要跟用 例“229”一起执行)
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_customform_subseminar_get_279"))  # AssertionError: successful
    # suite.addTest(api_most_interface_HW_UAT("test_file_downloadWithEmail_280"))# 与027一起执行，报错：文件检索失败
    # suite.addTest(HW_UAT_interface("test_281_member_identification_information_Get"))  # 表里面没有memberId
    # suite.addTest(api_most_interface_HW_UAT("test_file_delete_282"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_getLuckyDrawRoster_283"))
    # suite.addTest(api_most_interface_HW_UAT("test_luckyDraw_client_hasParticipate_284"))#参数取值范围错误
    # suite.addTest(api_most_interface_HW_UAT("test_luckyDraw_client_participate_285"))#postman接口不通：参数取值范围错误（原抽奖找不到数据）
    # suite.addTest(api_most_interface_HW_UAT("test_luckyDraw_client_saveUserInfo_286"))
    # suite.addTest(api_most_interface_HW_UAT("test_luckyDraw_client_saveUserInfo_count_287"))
    # suite.addTest(api_most_interface_HW_UAT("test_luckyDraw_client_share_288"))
    # suite.addTest(api_most_interface_HW_UAT("test_luckyDraw_get_289"))
    # suite.addTest(HW_UAT_interface("test_290_luckyDraw_getAwardDetailList"))#postman接口不通：没有对应的数据
    # suite.addTest(api_most_interface_HW_UAT("test_luckyDraw_redPacket_getLotteryRecord_291"))
    # suite.addTest(api_most_interface_HW_UAT("test_luckyDraw_redPacket_pushMessage_292"))
    # suite.addTest(api_most_interface_HW_UAT("test_luckyDraw_result_getState_293"))
    # suite.addTest(api_most_interface_HW_UAT("test_luckyDraw_result_getUserResultList_294"))
    # suite.addTest(api_most_interface_HW_UAT("test_luckyDraw_view_295"))
    # suite.addTest(api_most_interface_HW_UAT("test_topic_get_296"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_productLine_query_297"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_poll_share_298"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_poll_browse_299"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_webinar_channel_query_300"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_webinar_contacts_signup_301"))#需要与用例229一起执行（loginSess3）
    # suite.addTest(api_most_interface_HW_UAT("test_api_webinar_get_302"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_webinar_interaction_filedownload_create_303"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_wechat_contacts_check_304"))
    # suite.addTest(HW_UAT_interface("test_305_api_wechat_contacts_get"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_wechat_get_306"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_wechat_jssdk_config_get_307"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_article_category_get_308"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_common_shorturl_create_309"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_content_collect_query_310"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_customform_record_query_311"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_customform_share_312"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_dic_get_313"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_dic_gettree_314"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_dic_params_set_315"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_field_Get_316"))
    # suite.addTest(api_most_interface_HW_UAT("test_interaction_getCountByType_317"))
    # suite.addTest(api_most_interface_HW_UAT("test_interaction_getDetailList_318"))#(memberId表里没有)
    # suite.addTest(api_most_interface_HW_UAT("test_interaction_getFileDownloads_319"))
    # suite.addTest(api_most_interface_HW_UAT("test_interaction_getListByMember_320"))
    # suite.addTest(api_most_interface_HW_UAT("test_interaction_getStatCountList_321"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_form_Get_322"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_Get_323"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_signingpoint_interaction_get_324"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_signingpoint_Statistics_325"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_subseminar_Query_326"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_webinar_demand_record_327"))# 接口说明写成死值
    # suite.addTest(api_most_interface("test_328_article_getCollectionList"))#  此接口postman不通，在这里执行也报错报收藏数据暂无
    # suite.addTest(api_most_interface_HW_UAT("test_app_seminar_contact_nfc_bind_329"))
    # suite.addTest(api_most_interface_HW_UAT("test_app_seminar_contact_nfc_getBindRecord_330"))
    # suite.addTest(api_most_interface_HW_UAT("test_app_seminar_contact_nfc_getList_331"))
    # suite.addTest(api_most_interface("test_332_app_seminar_contact_prints_getList"))# 需要与229一起执行，把signPointId变量写成signingPointId
    # suite.addTest(api_most_interface("test333_tag_api_thirdTrigger_add_"))# 此接口不通，postman也报错：系统错误
    # suite.addTest(api_most_interface_HW_UAT("test_app_seminar_contact_prints_getSigningPointInfo_334"))
    # suite.addTest(api_most_interface_HW_UAT("test_app_seminar_contact_prints_updatePrintLog_335"))
    # suite.addTest(api_most_interface_HW_UAT("test_tag_application_GetByObject_336"))
    # suite.addTest(api_most_interface_HW_UAT("test_app_seminar_getList_337"))
    # suite.addTest(api_most_interface_HW_UAT("test_tag_application_getByOpenId_338"))
    # suite.addTest(api_most_interface_HW_UAT("test_app_seminar_signingPoint_checkIn_create_339"))
    # suite.addTest(api_most_interface_HW_UAT("test_app_seminar_signingPoint_checkIn_getList_340"))
    # suite.addTest(HW_UAT_interface("test_341_app_seminar_signingPoint_checkIn_getListCompressed"))#只验证了code（新增了一个获取code方法））
    # suite.addTest(api_most_interface_HW_UAT("test_app_seminar_signingPoint_contact_getList_342"))
    # suite.addTest(api_most_interface_HW_UAT("test_account_channel_get_343"))
    # suite.addTest(api_most_interface_HW_UAT("test_account_getAuth_344"))
    # suite.addTest(api_most_interface_HW_UAT("test_account_getAuthByInstance_345"))
    # suite.addTest(api_most_interface_HW_UAT("test_admin_member_identification_query_346"))
    # suite.addTest(api_most_interface_HW_UAT("test_anonymous_getId_347"))
    # suite.addTest(HW_UAT_interface("test_348_anonymous_setInfo"))
    # suite.addTest(api_most_interface_HW_UAT("test_tag_application_GetListByType_349"))
    # suite.addTest(api_most_interface_HW_UAT("test_tag_field_GetList_350"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_article_category_interaction_browse_351"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_article_category_interaction_share_352"))
    # suite.addTest(api_most_interface_HW_UAT("test_tag_use_getListByType_353"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_article_category_query_354"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_article_get_355"))
    # suite.addTest(api_most_interface_HW_UAT("test_template_template_getConfig_356"))
    # suite.addTest(HW_UAT_interface("test_357_api_article_interaction_create"))#
    # suite.addTest(HW_UAT_interface("test_358_templateMessage_batchSend"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_article_like_check_359"))
    # suite.addTest(api_most_interface_HW_UAT("test_templateMessage_getContactList_360"))
    # suite.addTest(api_most_interface("test_361_api_article_query"))
    # suite.addTest(api_most_interface_HW_UAT("test_topic_post_getAllList_362"))
    # suite.addTest(api_most_interface_HW_UAT("test_topic_stat_homePage_363"))
    # suite.addTest(api_most_interface("test_364_api_member_contacts_get"))   #需要与261一起执行
    # suite.addTest(HW_UAT_interface("test_365_member_register"))    #365生成loginId    (报错'NoneType' object is not iterable)
    # suite.addTest(api_most_interface("test_366_article_shareRecord"))   # 需要与229一起执行
    # suite.addTest(HW_UAT_interface("test_367_account_changePassword"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_member_contacts_password_update_368"))   # 需要与229一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_admin_member_identification_updatelog_query_369")) # 未执行 需要与261，365一起执行
    # suite.addTest(api_most_interface("test_370_api_member_contacts_update"))  # 需要与229一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_anonymous_checkSess_371"))   # 需要与229一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_api_questionnaire_share_372"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_file_interaction_share_373"))#fileId写成变量形式报错，写成死值执行通过
    # suite.addTest(api_most_interface_HW_UAT("test_api_file_query_374")) #与027一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_api_luckydraw_browse_375"))# 需要与229一起执行
    # suite.addTest(api_most_interface("test_api_luckydraw_fieldinfo_query_376"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_luckydraw_fieldinfo_update_377"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_luckydraw_get_378"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_luckydraw_share_379"))  # 需要与229一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_api_luckydraw_user_query_380"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_member_contacts_check_381"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_member_image_code_get_382"))#postman返回的是图片，只验证了code（新增了一个获取code方法）
    # suite.addTest(api_most_interface_HW_UAT("test_api_product_query_383"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_login_1_384"))  # 生成loginSess1
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_app_checkinpoint_userpermit_query_385"))#需要与用例384一起执行 获取loginSess1
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_bigscreen_information_push_386"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_like_387"))#需要与用例384一起执行 获取loginSess1
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_getList_388"))
    # suite.addTest(api_most_interface_HW_UAT("test_articleCategory_get_389"))
    # suite.addTest(api_most_interface_HW_UAT("test_interaction_record_390"))
    # suite.addTest(api_most_interface_HW_UAT("test_product_crossLine_getListByIdList_391"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_contacts_Query_392"))
    # suite.addTest(api_most_interface_HW_UAT("test_project_getInfoByLang_393"))
    # suite.addTest(api_most_interface_HW_UAT("test_article_getListByTags_394"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_shorturl_generate_395"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_app_signingpoint_group_Query_396"))
    # suite.addTest(api_most_interface_HW_UAT("test_file_folder_getReleaseFileList_397"))#有问题，folderId：文件夹不允许访问,验证失败
    # suite.addTest(HW_UAT_interface("test_398_member_identification_information_GetByOpenId"))
    # suite.addTest(api_most_interface_HW_UAT("test_app_seminar_contact_getListCompressed_399"))#postman返回值乱码，只验证了code（新增了一个获取code方法）待验证正确性
    # suite.addTest(api_most_interface_HW_UAT("test_app_seminar_signingPoint_getGroupList_400"))
    # suite.addTest(api_most_interface_HW_UAT("test_comment_getList_401"))
    # suite.addTest(api_most_interface_HW_UAT("test_app_seminar_contact_field_getCustomFields_402"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_newRegistration_403"))
    # suite.addTest(api_most_interface_HW_UAT("test_file_cutImage_404"))
    # suite.addTest(HW_UAT_interface("test_405_member_geneRegister"))# 生成 memberId报错TypeError: 'NoneType' object is not iterable
    # suite.addTest(api_most_interface_HW_UAT("test_app_seminar_contact_getList_406"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_getById_407"))  #未执行通过，应与405一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_article_getListByTags_408"))
    # suite.addTest(api_most_interface_HW_UAT("test_app_seminar_contact_getByUniqueField_409")) #postman此接口和在这里都执行不通，报参会人不存在
    # suite.addTest(api_most_interface_HW_UAT("test_member_identification_getList_410"))
    # suite.addTest(api_most_interface("test_411_member_member_setEnable"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_file_interaction_preview_412")) # 报错，文件不存在
    # suite.addTest(api_most_interface_HW_UAT("test_api_member_form_get_413"))
    # suite.addTest(api_most_interface_HW_UAT("test_webinar_open_interaction_fileDownLoad_414"))  #需要与384一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_api_webinar_live_sendmsg_416"))  #需要与229一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_api_webinar_live_site_browse_417"))  #需要与229一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_member_form_getList_418"))
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_topicTemplate_seminar_get_419"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_webinar_live_share_420"))#需要与用例229一起执行，获取loginSess3
    # suite.addTest(api_most_interface_HW_UAT("test_api_webinar_demand_share_421"))#需要与用例229一起执行，获取loginSess3
    # suite.addTest(api_most_interface("test_422_webinar_demand_site_browse"))#需要与用例229一起执行，获取loginSess3
    # suite.addTest(api_most_interface_HW_UAT("test_api_webinar_demand_play_423"))#需要与用例229一起执行，获取loginSess3
    # suite.addTest(api_most_interface_HW_UAT("test_member_integral_update_424"))#需要与用例384一起执行，获取loginSess1
    # suite.addTest(api_most_interface_HW_UAT("test_admin_account_create_425"))# 生成userid
    # suite.addTest(api_most_interface_HW_UAT("test_admin_account_update_426"))#需要与用例425一起执行，获取userid
    # suite.addTest(api_most_interface_HW_UAT("test_admin_account_disableUser_427"))#需要与用例425一起执行，获取userid
    # suite.addTest(api_most_interface_HW_UAT("test_admin_account_delete_428"))  #需要与用例425一起执行，获取userid
    # suite.addTest(api_most_interface_HW_UAT("test_admin_application_get_429"))
    # suite.addTest(api_most_interface_HW_UAT("test_sms_addSmsLog_430"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_article_collection_check_431"))#与384用例一起执行，获取loginSess1
    # suite.addTest(api_most_interface_HW_UAT("test_api_customform_get_432"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_file_download_interaction_query_433"))#与384用例一起执行，获取loginSess1
    # suite.addTest(api_most_interface("test_434_api_member_form_share"))#有问题，注册表单不存在
    # suite.addTest(api_most_interface_HW_UAT("test_questionary_getResultList_435"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_GetTokenByOpenId_436"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_admin_unbindWeChat_437"))
    # suite.addTest(api_most_interface_HW_UAT("test_account_verifySession_438"))#与384用例一起执行，获取loginSess1
    # suite.addTest(api_most_interface_HW_UAT("test_admin_member_integral_updateitems_439"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_signingpoint_query_440"))
    # suite.addTest(HW_UAT_interface("test_441_admin_account_userRole_set"))#需要与用例425一起执行，获取userid
    # suite.addTest(api_most_interface_HW_UAT("test_admin_tag_trigger_score_getlist_442"))
    # suite.addTest(HW_UAT_interface("test_443_api_seminar_contacts_ticket"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_seminar_contacts_qrcode_browse_444"))
    # suite.addTest(api_most_interface_HW_UAT("test_customForm_reAction_445"))
    # suite.addTest(api_most_interface_HW_UAT("test_api_file_folder_interaction_share_446"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_integral_get_447"))#与384用例一起执行，获取loginSess1
    # suite.addTest(api_most_interface_HW_UAT("test_api_member_integral_integrallog_query_448"))#与384用例一起执行，获取loginSess1
    # suite.addTest(api_most_interface_HW_UAT("test_admin_account_password_update_449"))#需要与用例425一起执行，获取userid
    # suite.addTest(HW_UAT_interface("test_450_dimensional_code_string"))  # 报错
    # suite.addTest(api_most_interface_HW_UAT("test_account_getOAuthTokenByOpen_451"))  # 生成tokenfor_verifyToken，执行报错
    # suite.addTest(api_most_interface_HW_UAT("test_account_verifyToken_452"))  # 未执行，需与451一起执行
    # suite.addTest(api_most_interface_HW_UAT("test_member_GetTokenByOpenId_453"))  # 生成tokenfor_memberbind
    # suite.addTest(api_most_interface_HW_UAT("test_member_bind_454"))  #应与 384,453 一起执行,报错，认证失败
    # suite.addTest(api_most_interface_HW_UAT("test_member_unbind_455"))  # 应与 384 一起执行,报错，认证失败
    #  # 456  #postman中没有body体未写
    # suite.addTest(api_most_interface("test_457_member_geneUpdate"))  # 应与 384 一起执行,报错
    # suite.addTest(api_most_interface_HW_UAT("test_seminar_signingPoint_getCheckInLog_458"))
    # suite.addTest(api_most_interface_HW_UAT("test_member_getImageCode_459"))
    # suite.addTest(api_most_interface("test_460_sms_balance"))
    # suite.addTest(api_most_interface("test_461_sms_balance_two"))
    runner = unittest.TextTestRunner()
    runner.run(suite)