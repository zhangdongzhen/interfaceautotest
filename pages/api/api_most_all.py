#-*-encoding:utf-8 -*-
"""
@version:1
@author:刘雅
@file:api_most_all.py
@time:2019/1/3010:15
"""
from common.common_function import sql_config
from common.common_function import Bl_value
from common.common_function.Read_From_Mysql import Read_From_Mysql
from pages.api import apicommon
from pages.api import all_bl_out
import time
import common.common_function.globalvar as gl
class api_most_all():
    # 判断变量表中是否存在该变量值，存在则更新，不存在则新增
    def Insert_Or_Update_Common_savebl(self, type, bl_name, bl_value, Variable_name):
        print "27"
        sql_Is = sql_config.get_True_From_Common_savebl(type, bl_name)
        data1 = Read_From_Mysql().Select_Datas_From_User(sql_Is)
        createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print "data1:", data1
        if len(data1) == 0:
            print 38
            SQL2 = "INSERT INTO Common_savebl(Variable_name,Variable_value,platform_name,createTime,updateTime) values ('" + Variable_name + "','" + bl_value + "','" + type + "','" + createTime + "','" + createTime + "')"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(SQL2)
        else:
            print 42
            # SQL2 = "INSERT INTO Common_savebl(Variable_name,Variable_value,platform_name,createTime,updateTime) values ('"+Variable_name+"','" + bl_value + "','" + type + "','" + createTime + "','" + createTime + "')"
            sql3 = "update Common_savebl set Variable_value='" + bl_value + "',updateTime='" + createTime + "' where platform_name='" + type + "' and Variable_name = '" + Variable_name + "'"
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql3)
    # 将结果写入到execution_result表中
    def write_to_execution_result(self,type):
        try:
            successful,fail=self.get_count_total()
            sql=sql_config.write_to_execution_result(type,successful,fail,type)
            print "36:sql:",sql
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
        except:
            successful,fail = self.get_count_total()
            sql = sql_config.write_to_execution_result(type, successful, fail, type)
            Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql)
    # 初始化count_total表
    def set_zero_count_total(self):
        Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql_config.set_count_total())
    # 修改count_total表中的successful字段
    def update_count_total_successful(self):
        successful=Read_From_Mysql().Select_Data_From_User(sql_config.set_count_total_successful())
        Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql_config.set_count_total_successful_and_one(successful))
    # 修改count_total表中的fail字段
    def update_count_total_fail(self):
        fail=Read_From_Mysql().Select_Data_From_User(sql_config.set_count_total_fail())
        Read_From_Mysql().InsertOrUpdate_Data_To_bl(sql_config.set_count_total_fail_and_one(fail))
    # 获取count_total表中的数值
    def get_count_total(self):
        sql=sql_config.get_count_from_count_total()
        print "sql:",sql
        s=Read_From_Mysql().Select_Datas_From_User(sql)
        successful=s[0][0]
        fail=s[0][1]
        return successful,fail
        # print "f:",f
    def run_all_Interface(self,type):
        self.set_zero_count_total()
        # self.account_login(type)
        # self.member_login(type)
        if type=="S2":
            pass
        elif type=="UAT":
            pass
        elif type=="HW":
            pass
        elif type=="HW_UAT":
            pass
        else:
            pass

    # 后台登录的接口
    def account_login(self,type,domain,email,password):
        flag,baksess=apicommon.get_most_account_login(type,domain,email,password,Bl_value.get_Bak_name())
        if flag==0:
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_Bak_name(),baksess,Bl_value.get_Bak_name())
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return flag,baksess
    def member_login(self,type,domain,tenantId,schemaId,memberFormId,memberSchemaId,unique,password):
        flag,loginSess=apicommon.get_most_member_login(type,domain,tenantId,schemaId,memberFormId,memberSchemaId,unique,password,Bl_value.get_member_login())
        print "flag:",flag
        print "loginSess:",loginSess
        if flag==0:
            print "69"
            self.Insert_Or_Update_Common_savebl(type, Bl_value.get_login_name(),loginSess,Bl_value.get_login_name())
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return flag,loginSess
    # seminar_contact_setContactToWechat/绑定微信和参会人员
    def seminar_contact_setContactToWechat(self,type,domain,seminarId,contactId,wechatId,bakSess):
        result, desc,code = apicommon.get_most_seminar_contact_setContactToWechat(type,domain,seminarId,contactId,wechatId,bakSess,type)
        if result ==0 and desc=="successful" and code==200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_member_password_update 修改前台登录用户的密码-jch
    def api_member_password_update(self,type,domain,tenantId,member_password,loginSess):
        result,desc,code = apicommon.get_most_api_member_password_update(type,domain,tenantId,member_password,loginSess)
        if result ==0:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return  result,desc
    #api_member_contacts_simple_signin 注册用户简单登录(通过OpenId或账号密码登录)
    def api_member_contacts_simple_signin(self,type,domain,tenantId,unique,password):
        result, desc,code = apicommon.get_api_member_contacts_simple_signin(type,domain,tenantId,unique,password)
        if result == 0 and desc=="successful" and code ==200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result,desc
    # member_identification_UpdateAvatar 修改注册用户头像
    def member_identification_UpdateAvatar(self,type,domain,tenantId,schemaId,loginSess):
        result, desc, code = apicommon.get_member_identification_UpdateAvatar(type,domain,tenantId,schemaId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_update更新用户信息
    def member_update(self,type,domain,memberFormId,loginSess):
        result, desc, code = apicommon.get_member_update(type,domain,memberFormId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #articleCategory_get获取文章列表
    def articleCategory_get(self,type,domain,loginSess,tenantId,nodeId):
        result, desc, code = apicommon.get_articleCategory_get(type,domain,loginSess,tenantId,nodeId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # comment_getList评论列表
    def comment_getList(self,type,domain,tenantId,topicId,loginSess):
        result, desc, code = apicommon.get_comment_getList(type,domain,tenantId,topicId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # 获取微讨论的详情
    def forum_getForumInfo(self,type,domain,global_topicId,tenantId):
        result, desc, code = apicommon.get_forum_getForumInfo(type,domain,global_topicId,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # forum_getReplyList/获取微论坛的回复列表
    def forum_getReplyList(self,type,domain,global_topicId,loginSess):
        result, desc, code = apicommon.get_forum_getReplyList(type,domain,global_topicId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # forum_post_create/微论坛发贴回复
    def forum_post_create(self,type,domain,topicId,sectionId):
        result, desc, code,pos = apicommon.get_forum_post_create(type,domain,topicId,sectionId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc,pos
        # forum_post_get/微论坛帖子详情
    def forum_post_get(self,type,domain,tenantId,nodeId,postId):
        result, desc, code = apicommon.get_forum_post(type,domain,tenantId,nodeId,postId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # article_browse  文章浏览
    def article_browse(self, type, domain, articleId):
        result, desc,code = apicommon.get_most_article_browse(type, domain, articleId)
        if result == 0:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # forum_post_getMainPost 获取微讨论的主贴列表
    def forum_post_getMainPost(self, type, domain, global_topicId):
        result, desc ,code= apicommon.get_most_forum_post_getMainPost(type, domain, global_topicId)
        if result == 0:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # forum_post_getMainPostNumber/微论坛主贴和回帖统计
    def forum_post_getMainPostNumber(self, type, domain, global_topicId):
        result, desc,code = apicommon.get_most_forum_post_getMainPostNumber(type, domain, global_topicId)
        if result == 0:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # forum_post_getPersonalPostList/微论坛查看个人或者他人帖子信息
    def forum_post_getPersonalPostList(self, type, domain, loginSess):
        result, desc ,code= apicommon.get_most_forum_post_getPersonalPostList(type, domain, loginSess)
        if result == 0:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # forum_post_getReplyPost/获取微讨论的主贴ID
    def forum_post_getReplyPost(self, type, domain, pos):
        result, desc,code = apicommon.get_most_forum_post_getReplyPost(type, domain, pos)
        if result == 0:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # forum_post_like / 微论坛给帖子点赞
    def forum_post_like(self,type,domain,postId,loginSess):
        result, desc,code = apicommon.get_most_forum_post_like(type,domain,postId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # forum_post_update/更新帖子内容
    def forum_post_update(self,type,domain,tenantId,nodeId,section_create):
        result,desc,code=apicommon.get_most_forum_post_update(type,domain,tenantId,nodeId,section_create)
        if result == 0:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # forum_section_getList/获取某个微论坛的子版列表
    def forum_section_getList(self,type,domain,global_topicId):
        result, desc,code = apicommon.get_most_forum_section_getList(type, domain, global_topicId)
        if result == 0:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # article_browseRecord / 文章浏览
    def article_browseRecord(self,type,domain,articleId,bakSess):
        result, desc,code = apicommon.get_most_article_browseRecord(type, domain, articleId,bakSess)
        if result == 0:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # forum_stat_homePage/微论坛帖子列表
    def forum_stat_homePage(self,type,domain,section_create,global_topicId):
        result, desc,code = apicommon.get_most_forum_stat_homePage(type, domain,section_create,global_topicId)
        if result == 0:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # article_Collection/文章收藏
    def article_Collection(self, type, domain, articleId, bakSess):
        result, desc, code = apicommon.get_article_Collection(type, domain, articleId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # forum_post_deletePost/删除自己发的帖子
    def forum_post_deletePost(self, type, domain, topicId, pos):
        result, desc, code = apicommon.get_forum_post_deletePost(type, domain, topicId, pos)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # file_create/该接口为后台接口，后期即将移除，请不要继续使用，上传文件
    def file_create(self, type, domain, tenantId, FolderId, bakSess):
        result, desc, code, fileId = apicommon.get_file_create_upload(type, domain, tenantId, FolderId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc, fileId

    # article_getDetail/获取文章详情
    def article_getDetail(self, type, domain, articleId):
        result, desc, code, topicId = apicommon.get_article_getDetail(type, domain, articleId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc, topicId

    # article_getLikeStatus/获取此用户是否允许继续点赞
    def article_getLikeStatus(self, type, domain, articleId, bakSess):
        result, desc, code = apicommon.get_article_getLikeStatus(type, domain, articleId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # article_getList/该接口即将过期不在维护，使用article_getListByProject替代
    def article_getList(self, type, domain, tenantId, loginSess,categoryId):
        result, desc, code = apicommon.get_article_getList(type, domain, tenantId, loginSess,categoryId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # article_getListByIds/根据文章id数组获取文章列表信息
    def article_getListByIds(self, type, domain, articleId):
        result, desc, code = apicommon.get_article_getListByIds(type, domain, articleId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # article_getListByProject/获取文章列表
    def article_getListByProject(self, type, domain, tenantId, categoryId):
        result, desc, code = apicommon.get_article_getListByProject(type, domain, tenantId, categoryId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # file_update/该接口为后台接口，后期即将移除，请不要继续使用，修改文件
    def file_update(self, type,domain,tenantId,fileIds,mappingId,FolderId,bakSess):
        result, desc, code = apicommon.get_file_update(type,domain,tenantId,fileIds,mappingId,FolderId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # questionary_get/获取问卷信息
    def questionary_get(self, type, domain, questionid_wj):
        result, desc, code = apicommon.get_questionary(type, domain, questionid_wj)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # articleCategory_getSubList/获取文章分组列表
    def articleCategory_getSubList(self,type,domain,categoryId):
        result,desc,code = apicommon.get_most_articleCategory_getSubList(type,domain,categoryId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # questionary_getList/获取问卷列表
    def questionary_getList(self,type,domain,tenantId):
        result,desc,code = apicommon.get_most_questionary_getList(type, domain, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # questionary_reAction/提交试卷
    def questionary_reAction(self,type,domain,questionid_wj,questionid_item):
        code = apicommon.get_most_questionary_reAction(type,domain,questionid_wj,questionid_item)
        if  code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return code
    # article_getTrees/查询文章列表
    def article_getTrees(self,type,domain,bakSess,tenantId,categoryId):
        result, desc,code = apicommon.get_most_article_getTrees(type,domain,bakSess,tenantId,categoryId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # collect_add/收藏信息
    def collect_add(self,type,domain,loginSess):
        result, desc,code,pos = apicommon.get_most_collect_add(type,domain,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc,pos
    # collect_cancel/取消收藏信息
    def collect_cancel(self, type, domain, collectionid,loginSess):
        result, desc, code = apicommon.get_most_collect_cancel(type,
domain,collectionid,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # collect_search/查询收藏的信息列表
    def collect_search(self, type, domain,loginSess):
        result, desc, code = apicommon.get_most_collect_search(type, domain,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # articleCategory_getList/获取栏目列表
    def articleCategory_getList(self, type, domain,tenantId,categoryId):
        result, desc, code = apicommon.get_most_articleCategory_getList(type,domain,tenantId,categoryId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # article_share/文章分享
    def article_share(self,type,domain,articleId,wechatId):
        result, desc, code = apicommon.get_most_article_share(type, domain,articleId,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # file_folder_getInsOfFileList/获取实例下的文件列表
    def file_folder_getInsOfFileList(self,type,domain,tenantId):
        result, desc, code = apicommon.get_most_file_folder_getInsOfFileList(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # questionary_exam_action/用户答题
    def questionary_exam_action(self,type,domain,questionid_sj):
        result, desc, code = apicommon.get_most_questionary_exam_action(type, domain,questionid_sj)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_guest_getList/获取会议嘉宾列表
    def seminar_guest_getList(self,type,domain,tenantId,seminarId):
        result, desc, code = apicommon.get_most_seminar_guest_getList(type, domain,tenantId,seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_guest_getGroupList/获取嘉宾列表
    def seminar_guest_getGroupList(self,type,domain,tenantId,seminarId):
        result, desc, code = apicommon.get_most_seminar_guest_getGroupList(type, domain,tenantId,seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_guest_field_Get/获取嘉宾字段列表
    def api_seminar_guest_field_Get(self,type,domain,tenantId):
        result, desc, code = apicommon.get_most_api_seminar_guest_field_Get(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # guest_get/获取全局嘉宾信息
    def guest_get(self,type,domain,tenantId,guestId):
        result, desc, code = apicommon.get_most_guest_get(type,domain,tenantId,guestId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # guest_getList/取租户嘉宾列表
    def guest_getList(self,type,domain,tenantId):
        result, desc, code = apicommon.get_most_guest_getList(type, domain, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # questionary_view/浏览问卷
    def questionary_view(self, type, domain, questionid_wj):
        result, desc, code = apicommon.get_most_questionary_view(type, domain, questionid_wj)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # questionary_action/提交问卷
    def questionary_action(self, type, domain, questionid_sj):
        result, desc, code = apicommon.get_most_questionary_action(type, domain, questionid_sj)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # article/like-文章点赞
    def article_like(self, type, domain, articleId, wechatId, loginSess):
        result, desc, code = apicommon.get_most_article_like(type, domain, articleId, wechatId, loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # comment_create/新增文章评论
    def comment_create(self, type, domain, tenantId, nodeId,article_topicId):
        result, desc, code, pos = apicommon.get_most_comment_create(type, domain, tenantId, nodeId,article_topicId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc, pos

    # comment_front_delete/删除评论 内容
    def comment_front_delete(self, type, domain, topicid, content):
        result, desc, code = apicommon.get_most_comment_front_delete(type, domain, topicid, content)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # comment_like/点赞评论内容
    def comment_like(self, type, domain, content, loginSess):
        result, desc, code = apicommon.get_most_comment_like(type, domain, content, loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # article_getListByTag/获取租户下文章列表，可通过标签筛选
    def article_getListByTag(self, type, domain, tenantId):
        result, desc, code = apicommon.get_most_article_getListByTag(type, domain, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # article_getListForProject/获取文章列表
    def article_getListForProject(self, type, domain, tenantId, categoryId, seminarId_instanceId):
        result, desc, code = apicommon.get_most_article_getListForProject(type, domain, tenantId, categoryId,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # article_getRecommendedList/获取栏目的子栏目中推荐的文章列表
    def article_getRecommendedList(self, type, domain, categoryId):
        result, desc, code = apicommon.get_most_article_getRecommendedList(type, domain, categoryId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # article_getSharedList/获取分享文章列表
    def article_getSharedList(self, type, domain, tenantId, nodeId, bakSess):
        result, desc, code = apicommon.get_most_article_getSharedList(type, domain, tenantId, nodeId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # file_getListForWeChat/获取微信下的文件
    def file_getListForWeChat(self, type, domain, fileIds):
        result, desc, code = apicommon.get_most_file_getListForWeChat(type, domain, fileIds)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # poll_get/获取投票
    def poll_get(self, type, domain, pollId):
        result, desc, code = apicommon.get_most_poll_get(type, domain, pollId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_agenda_get/获取会议日程信息
    def seminar_agenda_get(self, type, domain, seminarId, agendaId):
        result, desc, code = apicommon.get_most_seminar_agenda_get(type, domain, seminarId, agendaId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_agenda_getGroupList/获取会议日程按天分组
    def seminar_agenda_getGroupList(self, type, domain, seminarId):
        result, desc, code = apicommon.get_most_seminar_agenda_getGroupList(type, domain, seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # poll_action/提交投票
    def poll_action(self, type, domain, pollId):
        result, desc, code = apicommon.get_most_poll_action(type, domain, pollId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # poll_getList/获取投票列表
    def poll_getList(self, type, domain, tenantId, seminarId_instanceId):
        result, desc, code = apicommon.get_most_poll_getList(type, domain, tenantId, seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # poll_HasParticipation/浏览投票
    def poll_HasParticipation(self, type, domain, pollId):
        result, desc, code = apicommon.get_most_poll_HasParticipation(type, domain, pollId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # poll_sendCheckCode/投票发送验证码
    def poll_sendCheckCode(self, type, domain, pollId):
        result, desc, code = apicommon.get_most_poll_sendCheckCode(type, domain, pollId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # poll_start/该接口为后台接口，后期即将移除，请不要继续使用，开始投票
    def poll_start(self, type, domain, tenantId, seminarId_instanceId, pollId, bakSess):
        result, desc, code = apicommon.get_most_poll_start(type, domain, tenantId, seminarId_instanceId, pollId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # poll_stat_getResult / 获取每个投票选项的结果数量
    def poll_stat_getResult(self, type, domain, pollId):
        result, desc, code = apicommon.get_poll_stat_getResult(type, domain, pollId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # poll_stat_getTotal/返回总投票数
    def poll_stat_getTotal(self, type, domain, pollId):
        result, desc, code = apicommon.get_poll_stat_getTotal(type, domain, pollId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # poll_tool_checkRegistration / 报名前验证
    def poll_tool_checkRegistration(self, type, domain, pollId, seminarId_instanceId, loginSess):
        result, desc, code = apicommon.get_poll_tool_checkRegistration(type, domain, pollId, seminarId_instanceId,
                                                                       loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # poll_view/浏览投票
    def poll_view(self, type, domain, pollId):
        result, desc, code = apicommon.get_poll_view(type, domain, pollId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # product_crossLine_getList/获取租户下的某一分类的多产品线下的产品列表
    def product_crossLine_getList(self, type, domain, tenantId):
        result, desc, code = apicommon.get_product_crossLine_getList(type, domain, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # product_get/获取产品详细信息
    def product_get(self, type, domain, productLine):
        result, desc, code = apicommon.get_product_get(type, domain, productLine)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # product_getList/获取产品线下产品列表
    def product_getList(self, type, domain, bakSess, productLineId, tenantId):
        result, desc, code = apicommon.get_product_getList(type, domain, bakSess, productLineId, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # productLine_category_getCategoryTreeList/获取产品线分类树
    def productLine_category_getCategoryTreeList(self, type, domain, productLineId):
        result, desc, code = apicommon.get_productLine_category_getCategoryTreeList(type, domain, productLineId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # productLine_category_getConfigInfo/获取某产品线下具体某个字典值的配置信息
    def productLine_category_getConfigInfo(self, type, domain, productLineId):
        result, desc, code = apicommon.get_productLine_category_getConfigInfo(type, domain, productLineId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # productLine_category_getDetailList/获取产品线分类详细列表
    def productLine_category_getDetailList(self, type, domain, productLineId):
        result, desc, code = apicommon.get_productLine_category_getDetailList(type, domain, productLineId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
     # productLine_category_getList/获取产品线下产品分类的子分类信息
    def productLine_category_getList(self, type, domain, productLineId,dicId):
        result, desc, code = apicommon.get_most_productLine_category_getList(type, domain, productLineId,dicId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # productLine_field_get/获取某个产品线的字段列表
    def productLine_field_get(self, type, domain, productLineId):
        result, desc, code = apicommon.get_most_productLine_field_get(type, domain, productLineId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # productLine_get/获取产品线的信息
    def productLine_get(self, type, domain, productLineId):
        result, desc, code = apicommon.get_most_productLine_get(type, domain, productLineId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # productLine_getList/获取租户下产品线列表
    def productLine_getList(self, type, domain, tenantId):
        result, desc, code = apicommon.get_most_productLine_getList(type, domain, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # weChat_get/该接口为后台接口，后期即将移除，请不要继续使用，获取微信信息
    def weChat_get(self, type, domain, wechatId,bakSess):
        result, desc, code = apicommon.get_most_weChat_get(type, domain,wechatId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # weChat_getAppId/获取微信信息
    def weChat_getAppId(self, type, domain, wechatId):
        result, desc, code = apicommon.get_most_weChat_getAppId(type, domain,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # weChat_getConfig/做微信签名用，获取jssdk配置
    def weChat_getConfig(self, type, domain, wechatId):
        result, desc, code = apicommon.get_most_weChat_getConfig(type, domain, wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # weChat_getDef/获取各平台默认微信号的配置信息
    def weChat_getDef(self, type, domain):
        result, desc, code = apicommon.get_most_weChat_getDef(type, domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # weChat_getDefWx/获取各平台默认微信号的配置信息
    def weChat_getDefWx(self, type, domain):
        result, desc, code = apicommon.get_most_weChat_getDefWx(type, domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_product_get/获取产品详情
    def api_product_get(self, type, domain,tenantId,productLine):
        result, desc, code = apicommon.get_most_api_product_get(type, domain,tenantId,productLine)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # api_productLine_category_config_get/获取某产品线下具体某个字典值的配置信息
    def api_productLine_category_config_get(self, type, domain, tenantId, productLineId):
        result, desc, code = apicommon.get_most_api_productLine_category_config_get(type, domain, tenantId,
                                                                                    productLineId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # api_productLine_category_query/获取产品线分类树
    def api_productLine_category_query(self, type, domain, tenantId, productLineId, dicId):
        result, desc, code = apicommon.get_most_api_productLine_category_query(type, domain, tenantId,
                                                                               productLineId, dicId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # api_productLine_field_get/获取某个产品线的字段列表
    def api_productLine_field_get(self, type, domain, tenantId, productLineId):
        result, desc, code = apicommon.get_most_api_productLine_field_get(type, domain, tenantId, productLineId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # webinar_event_interaction_check/检查什么情况下可以继续投票、答问卷，会场开放过程中可以答
    def webinar_event_interaction_check(self, type, domain, webinarId_instanceId):
        result, desc, code = apicommon.get_most_webinar_event_interaction_check(type, domain, webinarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # webinar_event_interaction_pollResult/答完问卷后置接口，记录互动结果
    def webinar_event_interaction_pollResult(self, type, domain, loginSess, pollId):
        result, desc, code = apicommon.get_most_webinar_event_interaction_pollResult(type, domain, loginSess,
                                                                                     pollId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # webinar_open_attend/修改参会人数,并返回登录人的地址
    def webinar_open_attend(self, type, domain, tenantId, webinarId_instanceId):
        result, desc, code = apicommon.get_most_webinar_open_attend(type, domain, tenantId, webinarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #  webinar_open_checkRegistration/查询用户是否可以报名接口
    def webinar_open_checkRegistration(self, type, domain, tenantId, webinarId_instanceId):
        result, desc, code = apicommon.get_most_webinar_open_checkRegistration(type, domain, tenantId,
                                                                               webinarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # webinar_open_getApplicantInfo/获取会议信息
    def webinar_open_getApplicantInfo(self, type, domain, webinarId_instanceId, bakSess):
        result, desc, code = apicommon.get_most_webinar_open_getApplicantInfo(type, domain, webinarId_instanceId,
                                                                              bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # webinar_open_getAttendList/获取已报名的会议列表
    def webinar_open_getAttendList(self, type, domain, tenantId, bakSess):
        result, desc, code = apicommon.get_most_webinar_open_getAttendList(type, domain, tenantId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # webinar_open_getCustomFormInfo/获取自定义表单
    def webinar_open_getCustomFormInfo(self, type, domain, tenantId, webinarId_instanceId, customFormId):
        result, desc, code = apicommon.get_most_webinar_open_getCustomFormInfo(type, domain, tenantId,
                                                                               webinarId_instanceId, customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_bigScreen_forBigScreenWall_checkIn/有问题，微信签到
    def seminar_bigScreen_forBigScreenWall_checkIn(self,type,domain,contactId,loginSess,bigScreenId):
        result, desc, code = apicommon.get_most_seminar_bigScreen_forBigScreenWall_checkIn(type, domain,contactId,loginSess,bigScreenId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # webinar_open_getDemandInfo/得到一个点播会议的详情信息
    def webinar_open_getDemandInfo(self,type,domain,tenantId,webinarId_instanceId):
        result, desc, code = apicommon.get_most_webinar_open_getDemandInfo(type, domain,tenantId,webinarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # webinar_open_getServerTime/获取服务器时间
    def webinar_open_getServerTime(self,type,domain,tenantId):
        result, desc, code = apicommon.get_most_webinar_open_getServerTime(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # webinar_open_getVideoTimeLine/获取视频信息
    def webinar_open_getVideoTimeLine(self,type,domain,tenantId):
        result, desc, code = apicommon.get_most_webinar_open_getVideoTimeLine(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
     # webinar_open_getWebinarInfo/获取会场详细信息
    def webinar_open_getWebinarInfo(self,type,domain,tenantId,webinarId_instanceId):
        result, desc, code = apicommon.get_most_webinar_open_getWebinarInfo(type, domain, tenantId,webinarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # webinar_open_getWebinarList/获取直播会议列表
    def webinar_open_getWebinarList(self,type,domain,tenantId):
        result, desc, code = apicommon.get_most_webinar_open_getWebinarList(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # customForm_action/线上会报名
    def customForm_action(self,type,domain,loginSess,customFormId,webinarId_instanceId):
        result, desc, code = apicommon.get_most_customForm_action(type, domain, loginSess,customFormId,webinarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # webinar_open_join/人员参会接口
    def webinar_open_join(self,type,domain,loginSess,webinar_instanceId,tenantId):
        result, desc, code = apicommon.get_most_webinar_open_join(type, domain,loginSess,webinar_instanceId,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # webinar_project_shenWan_GetWebinar/获取会议信息
    def webinar_project_shenWan_GetWebinar(self,type,domain,webinarId_instanceId):
        result, desc, code = apicommon.get_most_webinar_project_shenWan_GetWebinar(type, domain,webinarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # webinar_project_shenWan_GetListByIds/跟进会议id数组 获取会议列表
    def webinar_project_shenWan_GetListByIds(self,type,domain,seminarId):
        result, desc, code = apicommon.get_most_webinar_project_shenWan_GetListByIds(type, domain,seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
#webinar_project_shenWan_GetDemandList/获取已发布的点播列表
    def webinar_project_shenWan_GetDemandList(self,type, domain,tenantId):
        result, desc, code = apicommon.get_webinar_project_shenWan_GetDemandList(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #webinar_open_trackingCode_getList/根据实例编号获取该实例的渠道追踪代码
    def webinar_open_trackingCode_getList(self,type, domain,tenantId,webinarId_instanceId):
        result, desc, code = apicommon.get_webinar_open_trackingCode_getList(type, domain,tenantId,webinarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #webinar_open_recordVideoViewCount/记录并获取点播视频的播放次数
    def webinar_open_recordVideoViewCount(self,type, domain,tenantId,webinarId,videoId):
        result, desc, code = apicommon.get_webinar_open_recordVideoViewCount(type, domain,tenantId,webinarId,videoId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #questionary_exam_repeatAction/用户重复回答试题保留最后一次结果
    def questionary_exam_repeatAction(self,type, domain,loginSess,questionid_sj):
        result, desc, code = apicommon.get_questionary_exam_repeatAction(type, domain,loginSess,questionid_sj)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #试卷添加题目
    def toolb_add_title(self,type,domain,bakSess,questionid_sj,tenantId):
        result, desc, code = apicommon.get_toolb_add_title(type,domain,bakSess,questionid_sj,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #questionary_exam_user_GenerateExam/生成试卷
    def questionary_exam_user_GenerateExam(self,type, domain, questionid_sj):
        result, desc, code = apicommon.get_questionary_exam_user_GenerateExam(type, domain, questionid_sj)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #webinar_open_getWebinarListAdvanced/获取直播会议列表（高级查询功能）,有问题
    def webinar_open_getWebinarListAdvanced(self,type, domain, tenantId):
        code = apicommon.get_webinar_open_getWebinarListAdvanced(type, domain, tenantId)
        if code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return code

    #questionary_exam_user_getAnswers/获取某人试卷的试题记录
    def questionary_exam_user_getAnswers(self,type, domain, questionid_wj):
        result, desc, code = apicommon.get_questionary_exam_user_getAnswers(type, domain, questionid_wj)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #questionary_exam_user_getSingleResult/获取某人的答题记录
    def questionary_exam_user_getSingleResult(self,type,domain,questionid_sj,tenantId):
        result, desc, code = apicommon.get_questionary_exam_user_getSingleResult(type,domain,questionid_sj,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #问卷设置短信发送验证码
    def setting_Verification_code(self,type,domain,bakSess,questionid_wj,tenantId):
        result, desc, code = apicommon.get_setting_Verification_code(type,domain,bakSess,questionid_wj,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # questionary_sendCheckCode/问卷发送验证码
    def questionary_sendCheckCode(self, type, domain, questionid_wj, tenantId):
        result, desc, code = apicommon.get_most_questionary_sendCheckCode(type,domain, questionid_wj, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # shortUrl_getList/获取短地址
    def shortUrl_getList(self, type, domain):
        result, desc, code = apicommon.get_most_shortUrl_getList(type, domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # api_webinar_contacts_get/获取报名人信息/返回报名人状态
    def api_webinar_contacts_get(self, type, domain, tenantId, webinarId_instanceId, loginSess):
        result, desc, code = apicommon.get_most_api_webinar_contacts_get(type,domain, tenantId, webinarId_instanceId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # shortUrl_urlStats/获取短网址的统计信息
    def shortUrl_urlStats(self, type, domain):
        result, desc, code = apicommon.get_most_shortUrl_urlStats(type, domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # api_webinar_demand_get/获取点播信息
    def api_webinar_demand_get(self, type, domain, tenantId, webinarId):
        result, desc, code = apicommon.get_most_api_webinar_demand_get(type,domain, tenantId, webinarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # api_webinar_query/获取会议列表
    def api_webinar_query(self, type, domain, tenantId):
        result, desc, code = apicommon.get_most_api_webinar_query(type, domain, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # questionary_tool_checkRegistration/报名前验证
    def questionary_tool_checkRegistration(self, type,domain, questionid_wj, webinarId_instanceId, loginSess):
        result, desc, code = apicommon.get_most_questionary_tool_checkRegistration(type, domain, questionid_wj,webinarId_instanceId, loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # questionary_stat_getResultByAnswerRecord/获取[常规问卷、leads问卷、非随机试卷]答题记录列表(此接口项目使用)
    def questionary_stat_getResultByAnswerRecord(self, type, domain, bakSess, questionid_wj):
        result, desc, code = apicommon.get_most_questionary_stat_getResultByAnswerRecord(type, domain, bakSess, questionid_wj)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_bigScreen_get/获取大屏详细信息
    def seminar_bigScreen_get(self, type, domain, createCheckIn):
        result, desc, code = apicommon.get_most_seminar_bigScreen_get(type,domain, createCheckIn)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_bigScreen_getListByGroup/获取大屏列表
    def seminar_bigScreen_getListByGroup(self, type, domain, seminarId):
        result, desc, code = apicommon.get_most_seminar_bigScreen_getListByGroup(type,domain, seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
# seminar_bigScreen_getPollPreset/获取投票大屏预设信息
    def seminar_bigScreen_getPollPreset(self,type,domain,tenantId,seminarId,createCheckIn,pollId):
        result, desc, code = apicommon.get_most_seminar_bigScreen_getPollPreset(type, domain,tenantId,seminarId,createCheckIn,pollId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_bigScreen_updateCheckIn/更新签到大屏信息
    def seminar_bigScreen_updateCheckIn(self,type,domain,seminarId,createCheckIn,signingPointId):
        result, desc, code = apicommon.get_most_seminar_bigScreen_updateCheckIn(type,domain,seminarId,createCheckIn,signingPointId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_bigScreen_updateLottery/该接口为后台接口，后期即将移除，请不要继续使用，更新留言大屏信息
    def seminar_bigScreen_updateLottery(self,type,domain,seminarId,createCheckIn,topicId,bakSess):
        result, desc, code = apicommon.get_most_seminar_bigScreen_updateLottery(type,domain,seminarId,createCheckIn,topicId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_bigScreen_updateMessage/该接口为后台接口，后期即将移除，请不要继续使用，更新大屏消息
    def seminar_bigScreen_updateMessage(self,type,domain,seminarId,createCheckIn,topicId,bakSess):
        result, desc, code = apicommon.get_most_seminar_bigScreen_updateMessage(type, domain, seminarId, createCheckIn,topicId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_bigScreen_updatePoll/更新投票大屏
    def seminar_bigScreen_updatePoll(self,type,domain,seminarId,createCheckIn,pollId):
        result, desc, code = apicommon.get_most_seminar_bigScreen_updatePoll(type, domain, seminarId, createCheckIn,pollId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_canInteraction/投票线下会前调接口，如果会议已结束，返回结果会有错误信息
    def seminar_canInteraction(self,type,domain,seminarId_instanceId):
        result, desc, code = apicommon.get_most_seminar_canInteraction(type, domain,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_contact_checkIdCard/检查身份证号是否存在
    def seminar_contact_checkIdCard(self,type,domain):
        result, desc, code = apicommon.get_moost_seminar_contact_checkIdCard(type, domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_contact_front_checkIn / 参会人签到
    def seminar_contact_front_checkIn(self,type,domain,tenantId,seminarId,signingPointIds,passageId,loginSess):
        result, desc, code = apicommon.get_most_seminar_contact_front_checkIn(type, domain,tenantId,seminarId,signingPointIds,passageId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_contact_front_editRegContact/通过前台sess更新注册信息,如果有会议id则同时更新报名信息
    def seminar_contact_front_editRegContact(self,type,domain,seminarId,seminarId_instanceId,loginSess):
        result, desc, code = apicommon.get_most_seminar_contact_front_editRegContact(type, domain,seminarId,seminarId_instanceId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_contact_front_getCommonContactInfo / 获取参会人员信息
    def seminar_contact_front_getCommonContactInfo(self,type,domain,seminarId,unique):
        result, desc, code = apicommon.get_most_seminar_contact_front_getCommonContactInfo(type, domain, seminarId,unique)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_contact_front_getContactInfo/根据会议id和唯一字段获取参会人信息
    def seminar_contact_front_getContactInfo(self,type,domain,seminarId,email):
        result, desc, code = apicommon.get_most_seminar_contact_front_getContactInfo(type, domain,seminarId,email)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_contact_front_getRegContact/此接口即将过期不在维护，可使用 member_geneGet 代替
    def seminar_contact_front_getRegContact(self,type,domain,tenantId,loginSess):
        result, desc, code = apicommon.get_most_seminar_contact_front_getRegContact(type, domain, tenantId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_contact_front_regSeminar/标准报名
    def seminar_contact_front_regSeminar(self,type,domain,loginSess,seminarId_instanceId,seminarId,customFormId,wechatId):
        result, desc, code = apicommon.get_most_seminar_contact_front_regSeminar(type,domain,loginSess,seminarId_instanceId,seminarId,customFormId,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_contact_front_unRegister/参会人取消报名
    def seminar_contact_front_unRegister(self,type,domain,seminarId,loginSess):
        result, desc, code = apicommon.get_most_seminar_contact_front_unRegister(type,domain,seminarId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
     # seminar_contact_front_updateSelf/更新参会人员信息 如果传递openId和weChatId会做绑定
    def seminar_contact_front_updateSelf(self,type,domain,tenantId,seminarId,contactId,loginSess):
        result, desc, code = apicommon.get_most_seminar_contact_front_updateSelf(type,domain,tenantId,seminarId,contactId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
     # seminar_contact_getContactToWechat/根据openID获取会中联系人信息
    def seminar_contact_getContactToWechat(self,type,domain,seminarId,wechatId):
        result, desc, code = apicommon.get_most_seminar_contact_getContactToWechat(type,domain,seminarId,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
     # seminar_contact_registerNew/会议报名接口(isProject=1时支持表单短信验证
    def seminar_contact_registerNew(self,type,domain,customFormId,memberFormId):
        result, desc, code = apicommon.get_most_seminar_contact_registerNew(type,domain,customFormId,memberFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_contact_update/此接口即将过期不在维护，可使用seminar_contact_front_editRegContact标准格式实现,有问题
    def seminar_contact_update(self,type,domain,tenantId,seminarId,contactId,bakSess):
        result, desc, code = apicommon.get_most_seminar_contact_update(type,domain,tenantId,seminarId,contactId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # post_create/该接口为后台接口，后期即将移除，请不要继续使用，留言板发帖
    def post_create(self,type,domain,global_topicId,postId):
        result, desc, code,postI = apicommon.get_most_post_create(type,domain,global_topicId,postId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc,postI
    # webinar_open_registration/线上会报名接口
    def webinar_open_registration(self,type,domain,webinarId_instanceId,bakSess):
        result, desc, code = apicommon.get_most_webinar_open_registration(type,domain,webinarId_instanceId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #questionary_HasParticipation/浏览问卷
    def questionary_HasParticipation(self,type,domain,questionid_wj,bakSess):
        result, desc, code = apicommon.get_questionary_HasParticipation(type,domain,questionid_wj,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #post_get/获取贴子信息
    def post_get(self,type,domain,tenantId,nodeId,postId,bakSess):
        result, desc, code = apicommon.get_post_get(type,domain,tenantId,nodeId,postId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #post_getListByUser/获取某人的未被删除的发送帖子记录
    def post_getListByUser(self,type, domain, topicId,bakSess):
        result, desc, code = apicommon.get_post_getListByUser(type, domain, topicId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #post_getMainAndReplyList/获取留言板的发帖的回帖
    def post_getMainAndReplyList(self,type, domain, topicId):
        result, desc, code = apicommon.get_post_getMainAndReplyList(type, domain, topicId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #post_getMainPost/ 获取主贴列表
    def post_getMainPost(self,type, domain, topicId):
        result, desc, code = apicommon.get_post_getMainPost(type, domain, topicId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #post_getMyPost/获取我发的帖子
    def post_getMyPost(self,type, domain, topicId,bakSess):
        result, desc, code = apicommon.get_post_getMyPost(type, domain, topicId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    #post_getReplyPost / 获取某主贴的所有回贴
    def post_getReplyPost(self,type,domain,tenantId,nodeId,postId,bakSess):
        result, desc, code = apicommon.get_post_getReplyPost(type,domain,tenantId,nodeId,postId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #post_like/点赞
    def post_like(self,type,domain):
        result, desc, code = apicommon.get_post_like(type,domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #post_update/主贴编辑 更新帖子内容
    def post_update(self,type,domain,postId,tenantId,nodeId,seminarId_instanceId):
        result, desc, code = apicommon.get_post_update(type,domain,postId,tenantId,nodeId,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #post_deletePost/删除主贴
    def post_deletePost(self,type,domain,tenantId,nodeId,postId,global_topicId):
        result, desc, code = apicommon.get_post_deletePost(type,domain,tenantId,nodeId,postId,global_topicId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
# post_delete/此接口应为后台接口，后期不在开放，请不要调用 删除主贴
    def post_delete(self, type, domain, postId):
        result, desc, code = apicommon.get_most_post_delete(type,domain, postId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_frontGet/获取会议详情
    def seminar_frontGet(self, type, domain, seminarId):
        result, desc, code = apicommon.get_most_seminar_frontGet(type,domain, seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_frontGetList/获取会议列表，无sess调用
    def seminar_frontGetList(self, type, domain, tenantId):
        result, desc, code = apicommon.get_most_seminar_frontGetList(type, domain, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # webinar_registration/线上会报名表单提交
    def webinar_registration(self, type, domain, loginSess,webinar_BMFormId,webinarId_instanceId):
        result, desc, code = apicommon.get_most_webinar_registration(type, domain, loginSess,webinar_BMFormId,webinarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # contact_bindMember/微信账号与会员绑定
    def contact_bindMember(self, type, domain,wechatId,schemaId,loginSess):
        result, desc, code = apicommon.get_most_contact_bindMember(type, domain,wechatId,schemaId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_frontGetListByIds/根据ids获取会议列表
    def seminar_frontGetListByIds(self, type, domain,tenantId):
        result, desc, code = apicommon.get_most_seminar_frontGetListByIds(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_frontGetStatusList/获取会议列表--支持按会议状态搜索
    def seminar_frontGetStatusList(self, type, domain,tenantId):
        result, desc, code = apicommon.get_most_seminar_frontGetStatusList(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_get/ 获取会议详情
    def seminar_get(self, type, domain,seminarId):
        result, desc, code = apicommon.get_most_seminar_get(type, domain,seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_getListWithFormId/会议列表（获取列表，输出：会议logo 会议名称 会议开始时间 会议地点 默认的报名表单Id）注：会议logo如果不存在，则不返回
    def seminar_getListWithFormId(self, type, domain,tenantId):
        result, desc, code = apicommon.get_most_seminar_getListWithFormId(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_register_canRegister/会议是否可以报名 如果有报名返回线下会报名信息，如果没有报名但是有注册返回注册信息，如果没有注册没有报名返回null
    def seminar_register_canRegister(self, type, domain,seminarId_instanceId,bakSess):
        result, desc, code = apicommon.get_most_seminar_register_canRegister(type, domain,seminarId_instanceId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # seminar_register_canRegisterNew/-会议是否可以报名
    def seminar_register_canRegisterNew(self,type,domain,seminarId_instanceId,registerFormId):
        result, desc, code = apicommon.get_most_seminar_register_canRegisterNew(type,domain,seminarId_instanceId,registerFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # contact_getByOpenId/通过openId获取联系人信息
    def contact_getByOpenId(self,type,domain,wechatId):
        result, desc, code = apicommon.get_most_contact_getByOpenId(type,domain,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # contact_getContactStatus/查询openId是否已关注微信号
    def contact_getContactStatus(self,type,domain,wechatId,bakSess):
        result, desc, code = apicommon.get_most_contact_getContactStatus(type,domain,wechatId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # customForm_action/线下会报名接口
    def customForm_seminar_action(self,type,domain,customFormId,seminarId_instanceId):
        result, desc, code = apicommon.get_most_customForm_seminar_action(type,domain,customFormId,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # customForm_checkRegistration/报名前验证
    def customForm_checkRegistration(self,type,domain,registerFormId,seminarId_instanceId):
        result, desc, code = apicommon.get_most_customForm_checkRegistration(type,domain,registerFormId,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
     # seminar_register_getList/获取报名表单列表
    def seminar_register_getList(self,type,domain,seminarId):
        result, desc, code = apicommon.get_most_seminar_register_getList(type,domain,seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_register_getSubList/通过自定义表单id获取报名表单信息
    def seminar_register_getSubList(self,type,domain,customFormId,seminarId_instanceId):
        result, desc, code = apicommon.get_most_seminar_register_getSubList(type,domain,customFormId,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # customForm_checkRepeatable/检查表单的不重复字段是否重复
    def customForm_checkRepeatable(self,type,domain,customFormId):
        result, desc, code = apicommon.get_most_customForm_checkRepeatable(type,domain,customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # customForm_get/获取自定义表单详情
    def customForm_get(self,type,domain,customFormId):
        result, desc, code = apicommon.get_most_customForm_get(type,domain,customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # customForm_getListByIds/该接口为后台接口，后期即将移除，请不要继续使用，获取表单列表
    def customForm_getListByIds(self,type,domain,tenantId,bakSess):
        result, desc, code = apicommon.get_most_customForm_getListByIds(type,domain,tenantId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc

    # customForm_HasParticipation/记录表单的浏览记录
    def customForm_HasParticipation(self,type,domain,customFormId):
        result, desc, code = apicommon.get_most_customForm_HasParticipation(type,domain,customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # customForm_sendCheckCode/自定义表单发送手机修改密码验证码
    def customForm_sendCheckCode(self,type,domain,customFormId):
        result, desc, code = apicommon.get_most_customForm_sendCheckCode(type,domain,customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # customForm_user_getRecordByOpenId/获取粉丝提交表单记录
    def customForm_user_getRecordByOpenId(self,type,domain,customFormId,loginSess):
        result, desc, code = apicommon.get_most_customForm_user_getRecordByOpenId(type,domain,customFormId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
     # customForm_user_getResultByOpenId/获取某个OpenId的答表单的记录
    def customForm_user_getResultByOpenId(self,type,domain,customFormId):
        result, desc, code = apicommon.get_most_customForm_user_getResultByOpenId(type,domain,customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # customForm_view/记录表单的浏览记录
    def customForm_view(self,type,domain,customFormId):
        result, desc, code = apicommon.get_most_customForm_view(type,domain,customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
     # de_contact_front_get/获取de联系人信息
    def de_contact_front_get(self,type, domain, loginSess,tenantId):
        result, desc, code = apicommon.get_most_de_contact_front_get(type,domain,loginSess,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # de_contact_front_getSeminars/ 通过前台sess获取联系人最近参加过的会议
    def de_contact_front_getSeminars(self,type, domain, loginSess,tenantId):
        result, desc, code = apicommon.get_most_de_contact_front_getSeminars(type,domain,loginSess,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # de_contact_getLastSeminarsBySess/获取参与过的会议
    def de_contact_getLastSeminarsBySess(self,type, domain, bakSess,contactId,tenantId):
        result, desc, code = apicommon.get_most_de_contact_getLastSeminarsBySess(type, domain, bakSess,contactId,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # dic_getList/获取字典列表
    def dic_getList(self,type, domain, tenantId):
        result, desc, code = apicommon.get_most_dic_getList(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # dic_params_getList/获取字典值列表
    def dic_params_getList(self,type, domain, tenantId,dicId):
        result, desc, code = apicommon.get_most_dic_params_getList(type, domain,tenantId,dicId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_signingPoint_checkIn_getCheckInCount/获取某会议下签到点的签到数
    def seminar_signingPoint_checkIn_getCheckInCount(self, type, domain, seminarId):
        result, desc, code = apicommon.get_seminar_signingPoint_checkIn_getCheckInCount(type,domain, seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #dic_params_getTree/获取字典树形结构
    def dic_params_getTree(self,type, domain,tenantId,dicId):
        result, desc, code = apicommon.get_dic_params_getTree(type, domain,tenantId,dicId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_signingPoint_front_getMyCheckInLog/查看自己的签到记录，传openid，globaluserid，cookieid，sess
    def seminar_signingPoint_front_getMyCheckInLog(self,type, domain,tenantId,bakSess,seminarId,seminarId_instanceId,signingPointId,passageId):
        result, desc, code = apicommon.get_seminar_signingPoint_front_getMyCheckInLog(type, domain,tenantId,bakSess,seminarId,seminarId_instanceId,signingPointId,passageId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_signingPoint_getCheckInLog/获取签到历史记录
    def seminar_signingPoint_getCheckInLog(self,type, domain,tenantId,seminarId,seminarId_instanceId,signingPointId,passageId,bakSess):
        result, desc, code = apicommon.get_seminar_signingPoint_getCheckInLog(type, domain,tenantId,seminarId,seminarId_instanceId,signingPointId,passageId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_signingPoint_getNumberSignInPassage/获取会议签到点签到统计信息
    def seminar_signingPoint_getNumberSignInPassage(self,type, domain,tenantId,seminarId,seminarId_instanceId,signingPointId,passageId,bakSess):
        result, desc, code = apicommon.get_seminar_signingPoint_getNumberSignInPassage(type, domain,tenantId,seminarId,seminarId_instanceId,signingPointId,passageId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #edm_log_create/创建邮件发送任务
    def edm_log_create(self,type,domain,taskId):
        result, desc, code = apicommon.get_edm_log_create(type,domain,taskId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_subSeminar_frontGet/获取分会场详细信息
    def seminar_subSeminar_frontGet(self,type,domain,subSeminarId):
        result, desc, code = apicommon.get_seminar_subSeminar_frontGet(type,domain,subSeminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_subSeminar_getListByType/获取分会场列表
    def seminar_subSeminar_getListByType(self,type,domain,seminarId):
        result, desc, code = apicommon.get_seminar_subSeminar_getListByType(type,domain,seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_topicTemplate_contact_get/获取联系人信息
    def seminar_topicTemplate_contact_get(self,type,domain,seminarId_instanceId,email):
        result, desc, code = apicommon.get_seminar_topicTemplate_contact_get(type,domain,seminarId_instanceId,email)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_topicTemplate_contact_getByOpenId/通过微信OpenId获取某会议下的联系人
    def seminar_topicTemplate_contact_getByOpenId(self,type,domain,seminarId):
        result, desc, code = apicommon.get_seminar_topicTemplate_contact_getByOpenId(type,domain,seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #edm_send/邮件发送接口，session验证
    def edm_send(self,type,domain,tenantId,bakSess):
        result, desc, code = apicommon.get_edm_send(type,domain,tenantId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_topicTemplate_contact_getState/通过实例ID和唯一字段获取信息
    def seminar_topicTemplate_contact_getState(self,type,domain,seminarId_instanceId,email):
        result, desc, code = apicommon.get_seminar_topicTemplate_contact_getState(type,domain,seminarId_instanceId,email)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #customForm_isFaceImg/检查图片是否包含人脸
    def customForm_isFaceImg(self,type,domain,mappingId):
        result, desc, code = apicommon.get_customForm_isFaceImg(type,domain,mappingId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_topicTemplate_contact_getStateBySess/获取注册状态，有问题
    def seminar_topicTemplate_contact_getStateBySess(self,type,domain,seminarId_instanceId):
        result, desc, code = apicommon.get_seminar_topicTemplate_contact_getStateBySess(type,domain,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_topicTemplate_seminar_getFormInfo/获取表单详细信息
    def seminar_topicTemplate_seminar_getFormInfo(self,type,domain,seminarId_instanceId,registerFormId):
        result, desc, code = apicommon.get_seminar_topicTemplate_seminar_getFormInfo(type,domain,seminarId_instanceId,registerFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_topicTemplate_seminar_getWithAllSub/获取会议信息，包括所有的分会场
    def seminar_topicTemplate_seminar_getWithAllSub(self,type,domain,seminarId_instanceId):
        result, desc, code = apicommon.get_seminar_topicTemplate_seminar_getWithAllSub(type,domain,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_trackingCode_getList/获取渠道追踪代码列表
    def seminar_trackingCode_getList(self,type,domain,seminarId):
        result, desc, code = apicommon.get_seminar_trackingCode_getList(type,domain,seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_bigScreen_forBigScreenWall_getCheckInData/获取大屏签到墙信息
    def seminar_bigScreen_forBigScreenWall_getCheckInData(self,type,domain,createCheckIn,signingPointId):
        result, desc, code = apicommon.get_seminar_bigScreen_forBigScreenWall_getCheckInData(type,domain,createCheckIn,signingPointId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_bigScreen_forBigScreenWall_getWapCheckInfo/获取大屏手机端签到信息
    def seminar_bigScreen_forBigScreenWall_getWapCheckInfo(self,type,domain,createCheckIn,contactId,email):
        result, desc, code = apicommon.get_seminar_bigScreen_forBigScreenWall_getWapCheckInfo(type,domain,createCheckIn,contactId,email)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #field_getList/获取字段列表
    def field_getList(self,type,domain,tenantId):
        result, desc, code = apicommon.get_field_getList(type,domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_bigScreen_getWapMessageInfo/获取wap签到模板联系人信息
    def seminar_bigScreen_getWapMessageInfo(self,type,domain,seminarId,email):
        result, desc, code = apicommon.get_seminar_bigScreen_getWapMessageInfo(type,domain,seminarId,email)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #file_folder_getReleaseFile/获取公布的文件
    def file_folder_getReleaseFile(self,type,domain,fileId):
        result, desc, code = apicommon.get_file_folder_getReleaseFile(type,domain,fileId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #file_getList/获取文件列表
    def file_getList(self,type,domain,tenantId,seminarId_instanceId,FolderId,fileIds):
        result, desc, code,articleCategoryId = apicommon.get_file_getList(type,domain,tenantId,seminarId_instanceId,FolderId,fileIds)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc,articleCategoryId
    #member_changePwd/前台用户修改密码
    def member_changePwd(self,type,domain,schemaId,loginSess):
        result, desc, code = apicommon.get_member_changePwd(type,domain,schemaId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #member_checkUnique/检测用户唯一，检测字段值唯一
    def member_checkUnique(self,type,domain,tenantId):
        result, desc, code = apicommon.get_member_checkUnique(type,domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #luckyDraw_client_action/抽奖
    def luckyDraw_client_action(self,type,domain,luckyDrawId,bakSess):
        result, desc, code = apicommon.get_luckyDraw_client_action(type,domain,luckyDrawId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #member_form_GetForNewForm/新的表单信息 接受formId 和 memberFormId 按新接口的格式返回
    def member_form_GetForNewForm(self,type,domain,registerFormId):
        result, desc, code = apicommon.get_member_form_GetForNewForm(type,domain,registerFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #member_form_GetOAuthUrlByWeChatId/通过wechatId获取授权信息
    def member_form_GetOAuthUrlByWeChatId(self,type,domain,wechatId):
        result, desc, code = apicommon.get_member_form_GetOAuthUrlByWeChatId(type,domain,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #member_form_getTemplate/获取表单模板信息
    def member_form_getTemplate(self,type,domain,memberFormId):
        result, desc, code = apicommon.get_member_form_getTemplate(type,domain,memberFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #member_form_getUnique/找回密码
    def member_form_getUnique(self,type,domain,memberFormId):
        result, desc, code = apicommon.get_member_form_getUnique(type,domain,memberFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_form_search/查询符合条件的表单
    def member_form_search(self, type, domain, tenantId):
        result, desc, code = apicommon.get_most_member_form_search(type, domain, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_form_view/注册表单浏览
    def member_form_view(self, type, domain, memberFormId, loginSess):
        result, desc, code = apicommon.get_most_member_form_view(type, domain,memberFormId, loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_Query/获取会议列表
    def api_seminar_Query(self, type, domain, tenantId):
        result, desc, code = apicommon.get_most_api_seminar_Query(type, domain, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_geneGet/根据已登录的session获取用户信息
    def member_geneGet(self, type, domain, loginSess):
        result, desc, code = apicommon.get_most_member_geneGet(type, domain, loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_site_browse/进入访问专题站行为
    def api_seminar_site_browse(self, type, domain, seminarId, tenantId):
        result, desc, code = apicommon.get_most_api_seminar_site_browse(type, domain, seminarId, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_site_share/分享专题站行为
    def api_seminar_site_share(self, type, domain, seminarId, tenantId):
        result, desc, code = apicommon.get_most_api_seminar_site_share(type, domain,seminarId, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_template_config_get/获取模板信息
    def api_template_config_get(self, type, domain, tenantId):
        result, desc, code = apicommon.get_most_api_template_config_get(type, domain, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_get/根据已登录的session获取用户信息
    def member_get(self, type, domain, tenantId, loginSess):
        result, desc, code = apicommon.get_most_member_get(type, domain, tenantId, loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_topic_board_browse/浏览版面
    def api_topic_board_browse(self, type, domain, topicId, tenantId):
        result, desc, code = apicommon.get_most_api_topic_board_browse(type, domain, topicId, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
# api_topic_browse/浏览主贴
    def api_topic_browse(self,type,domain,postId,tenantId,loginSess3,loginSess):
        result, desc, code = apicommon.get_most_api_topic_browse(type, domain,postId,tenantId,loginSess3,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_topic_comment_query / 微讨论 - 微论坛 - 获取子版的评论列表
    def api_topic_comment_query(self,type,domain,tenantId,topicId,sectionId,loginSess3):
        result, desc, code = apicommon.get_most_api_topic_comment_query(type,domain,tenantId,topicId,sectionId,loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_topic_forum_post_get/获取帖子详情
    def api_topic_forum_post_get(self,type,domain,pos,tenantId):
        result, desc, code = apicommon.get_most_api_topic_forum_post_get(type, domain, pos,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_LookUp/由下向上获取回填信息.实例联系人-模块联系人-注册用户信息.可传前端sess或不传.
    def member_LookUp(self,type,domain,tenantId,seminarId_instanceId):
        result, desc, code = apicommon.get_most_member_LookUp(type, domain,tenantId,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_schema_field_GetList/获取体系字段
    def member_schema_field_GetList(self,type,domain,tenantId,schemaId):
        result, desc, code = apicommon.get_most_member_schema_field_GetList(type, domain, tenantId, schemaId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_schema_orderUnique/获取体系的标识字段及顺序
    def member_schema_orderUnique(self,type,domain,memberSchemaId):
        result, desc, code = apicommon.get_most_member_schema_orderUnique(type,domain,memberSchemaId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_schema_field_sorting_GetList/获取身份标识字段列表
    def member_schema_field_sorting_GetList(self,type,domain,tenantId,schemaId):
        result, desc, code = apicommon.get_most_member_schema_field_sorting_GetList(type, domain,tenantId,schemaId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_sendCheckCode/身份认证体系发送手机修改密码验证码(member_sendCheckCode)新加的接口增加前端的控制（有效期和重发时间）
    def member_sendCheckCode(self,type,domain,unique,memberSchemaId):
        result, desc, code = apicommon.get_most_member_sendCheckCode(type, domain,unique,memberSchemaId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_sendVerificationCode/向手机号码发送验证码
    def member_sendVerificationCode(self,type,domain,memberFormId,loginSess3):
        result, desc, code = apicommon.get_most_member_sendVerificationCode(type, domain, memberFormId, loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_sendVerificationCodeToMail/向用户邮箱发送验证码
    def member_sendVerificationCodeToMail(self,type,domain,memberFormId):
        result, desc, code = apicommon.get_most_member_sendVerificationCodeToMail(type, domain, memberFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_topic_forum_post_query/微讨论-微论坛-获取微论坛的主帖列表
    def api_topic_forum_post_query(self,type,domain,tenantId,topicId,section_create,loginSess3):
        result, desc, code = apicommon.get_most_api_topic_forum_post_query(type, domain, tenantId,topicId,section_create,loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_updateByField/会员修改，只修改给定的字段.需要登录
    def member_updateByField(self,type,domain,loginSess):
        result, desc, code = apicommon.get_most_member_updateByField(type, domain,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_topic_forum_post_reply_query/微讨论-微论坛-获取微论坛主贴的回帖列表
    def api_topic_forum_post_reply_query(self,type,domain,tenantId,postId,loginSess3):
        result, desc, code = apicommon.get_most_api_topic_forum_post_reply_query(type, domain,tenantId,postId, loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_topic_get/微讨论-获取版面详情
    def api_topic_get(self,type,domain,tenantId,topicId):
        result, desc, code = apicommon.get_most_api_topic_get(type, domain, tenantId,topicId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_topic_message_Create/发主帖/回帖
    def api_topic_message_Create(self,type,domain,tenantId,topicId,loginSess3):
        result, desc, code = apicommon.get_most_api_topic_message_Create(type, domain, tenantId, topicId,loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_topic_message_get/微讨论-留言板-获取留言板帖子的详细信息
    def api_topic_message_get(self,type,domain,tenantId,postId,bakSess):
        result, desc, code = apicommon.get_most_api_topic_message_get(type, domain, tenantId,postId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_topic_message_Query/获取主题帖列表以及对应帖子的回复列表
    def api_topic_message_Query(self,type,domain,topicId,tenantId):
        result, desc, code = apicommon.get_most_api_topic_message_Query(type, domain,topicId,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_topic_message_reply_Query/某主帖的回复列表
    def api_topic_message_reply_Query(self,type,domain,postId,loginSess3,tenantId):
        result, desc, code = apicommon.get_most_api_topic_message_reply_Query(type, domain,postId,loginSess3,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_topic_share/分享主贴
    def api_topic_share(self,type,domain,topicId,loginSess3,tenantId,loginSess):
        result, desc, code = apicommon.get_most_api_topic_share(type, domain,topicId,loginSess3,tenantId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_loginByOpenId/使用openId登录，如果未登录会返回绑定使用的authCode
    def member_loginByOpenId(self,type,domain,schemaId,wechatId):
        result, desc, code = apicommon.get_most_member_loginByOpenId(type, domain,schemaId,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # luckyDraw_client_actionByBigScreen/大屏抽奖的抽奖操作
    def luckyDraw_client_actionByBigScreen(self,type, domain, tenantId,luckyDrawId):
        result, desc, code = apicommon.get_most_luckyDraw_client_actionByBigScreen(type, domain,tenantId,luckyDrawId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_identification_sorting_Get/按当前租户的身份标识优先级来获取注册用户的个人信息
    def member_identification_sorting_Get(self,type, domain, tenantId,loginSess3):
        result, desc, code = apicommon.get_most_member_identification_sorting_Get(type, domain,tenantId,loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # luckyDraw_client_GetMyRedPacketLog/微信红包抽奖业务专用，通过OpenId获取当前用户的在该场活动的所有抽奖记录
    def luckyDraw_client_GetMyRedPacketLog(self,type, domain, tenantId,luckyDrawId):
        result, desc, code = apicommon.get_most_luckyDraw_client_GetMyRedPacketLog(type, domain,tenantId,luckyDrawId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
     # api_customform_browse/记录表单的浏览记录
    def api_customform_browse(self,type, domain, tenantId,customFormId):
        result, desc, code = apicommon.get_most_api_customform_browse(type, domain,tenantId,customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_customform_field_check/检查表单的不重复字段是否重复/不重复
    def api_customform_field_check(self,type, domain, tenantId,customFormId):
        result, desc, code = apicommon.get_most_api_customform_field_check(type, domain,tenantId,customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_customform_submit/自定义表单提交
    def api_customform_submit(self,type, domain, tenantId,customFormId):
        result, desc, code = apicommon.get_most_api_customform_submit(type, domain,tenantId,customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_forgetPwd/找回密码
    def member_forgetPwd(self,type, domain,memberSchemaId,memberFormId):
        code = apicommon.get_most_member_forgetPwd(type, domain,memberSchemaId,memberFormId)
        if  code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return code
    # member_UpdateIdentityInfo/修改身份信息
    def member_UpdateIdentityInfo(self,type, domain,tenantId,schemaId,memberFormIda,loginSess3):
        result, desc, code = apicommon.get_most_member_UpdateIdentityInfo(type, domain,tenantId,schemaId,memberFormIda,loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_interaction_record/记录一个互动
    def member_interaction_record(self,type, domain,tenantId,pollId):
        result, desc, code = apicommon.get_most_member_interaction_record(type, domain,tenantId,pollId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #  webinar_event_interaction_questionnaireResult/提交问卷
    def webinar_event_interaction_questionnaireResult(self,type, domain,webinarId_instanceId,questionid_wj):
        result, desc, code = apicommon.get_most_webinar_event_interaction_questionnaireResult(type, domain,webinarId_instanceId,questionid_wj)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_member_associate_Logout/让关联微信粉丝或匿名用户的注册用户退出登录
    def member_member_associate_Logout(self,type, domain,loginSess):
        result, desc, code = apicommon.get_most_member_member_associate_Logout(type, domain,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_login/前台session
    def member_member_login(self,type, domain,tenantId ,schemaId):
        result, desc, code = apicommon.get_most_member_member_login(type, domain,tenantId ,schemaId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_form_get/获取表单信息
    def member_form_get(self,type, domain,memberFormId ,bakSess):
        result, desc, code = apicommon.get_most_member_form_get(type, domain,memberFormId ,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_member_contacts_register/用户注册
    def api_member_contacts_register(self,type, domain,tenantId ,memberFormId):
        result, desc, code = apicommon.get_most_api_member_contacts_register(type, domain,tenantId ,memberFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_questionnaire_browse/记录问卷浏览记录
    def api_questionnaire_browse(self,type, domain,tenantId ,questionid_wj):
        result, desc, code = apicommon.get_most_api_questionnaire_browse(type, domain,tenantId ,questionid_wj)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_questionnaire_get/获取问卷信息
    def api_questionnaire_get(self,type, domain,tenantId ,questionid_wj):
        result, desc, code = apicommon.get_most_api_questionnaire_get(type, domain,tenantId ,questionid_wj)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_questionnaire_query/查询问卷列表/全部
    def api_questionnaire_query(self,type, domain,tenantId ):
        result, desc, code = apicommon.get_most_api_questionnaire_query(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_questionnaire_submit/提交问卷
    def api_questionnaire_submit(self,type, domain,tenantId ,questionid_wj):
        result, desc, code = apicommon.get_most_api_questionnaire_submit(type, domain,tenantId,questionid_wj)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_app_getconfiginfo/获取App相关的配置信息
    def api_seminar_app_getconfiginfo(self,type, domain,bakSess ,tenantId):
        result, desc, code = apicommon.get_most_api_seminar_app_getconfiginfo(type, domain,bakSess ,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_app_monitor_getappinfo/获取设备信息
    def api_seminar_app_monitor_getappinfo(self,type, domain,seminarId):
        result, desc, code = apicommon.get_most_api_seminar_app_monitor_getappinfo(type, domain,seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_app_monitor_getclientalias/获取设备自定义编号GetNumberapp\seminar\monitor
    def api_seminar_app_monitor_getclientalias(self, type, domain, tenantId, seminarId):
        result, desc, code = apicommon.get_most_api_seminar_app_monitor_getclientalias(type,domain, tenantId, seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_app_monitor_updateclientinfo/更新设备信息UpdateInfo
    def api_seminar_app_monitor_updateclientinfo(self, type, domain, seminarId):
        result, desc, code = apicommon.get_most_api_seminar_app_monitor_updateclientinfo(type, domain, seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_bigscreen_contacts_Get/获取大屏手机端签到信息/服务号租户
    def api_seminar_bigscreen_contacts_Get(self, type, domain, tenantId, createCheckIn,contactId):
        result, desc, code = apicommon.get_most_api_seminar_bigscreen_contacts_Get(type, domain, tenantId, createCheckIn, contactId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_bigscreen_Get/获取大屏详细信息
    def api_seminar_bigscreen_Get(self, type, domain, tenantId, createCheckIn):
        result, desc, code = apicommon.get_most_api_seminar_bigscreen_Get(type, domain,tenantId, createCheckIn)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # api_seminar_bigscreen_group_query/获取大屏组列表/服务号租户
    def api_seminar_bigscreen_group_query(self, type, domain, tenantId, seminarId):
        result, desc, code = apicommon.get_most_api_seminar_bigscreen_group_query(type, domain, tenantId, seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_contacts_field_Get/获取联系人字段列表
    def api_seminar_contacts_field_Get(self, type, domain, tenantId, seminarId):
        result, desc, code = apicommon.get_most_api_seminar_contacts_field_Get(type, domain,tenantId, seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # api_seminar_contacts_Get/线下会根据sess、openid、globalUserId查询报名信息
    def api_seminar_contacts_Get(self, type, domain, tenantId, seminarId, bakSess):
        result, desc, code = apicommon.get_most_api_seminar_contacts_Get(type, domain,tenantId, seminarId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # api_seminar_contacts_SignUp/线下会报名(报名时可以新增或更新注册信息)
    def api_seminar_contacts_SignUp(self, type, domain, tenantId, seminarId, customFormId):
        result, desc, code = apicommon.get_most_api_seminar_contacts_SignUp(type, domain,tenantId, seminarId, customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # api_seminar_contacts_Update/线下会根据sess更新报名信息（可选是否更新注册信息）/更新注册信息
    def api_seminar_contacts_Update(self, type, domain, tenantId, loginSess3):
        result, desc, code = apicommon.get_most_api_seminar_contacts_Update(type, domain,tenantId, loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
     # api_seminar_customform_subseminar_get/获取报名表单关联的分会场信息
    def api_seminar_customform_subseminar_get(self, type, domain,tenantId, seminarId, customFormId):
        result, desc, code = apicommon.get_most_api_seminar_customform_subseminar_get(type, domain, tenantId, seminarId, customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #file_downloadWithEmail/文章资料下载
    def file_downloadWithEmail(self,type,domain,articleId,fileIds,email,tenantId,loginSess):
        result, desc, code = apicommon.get_file_downloadWithEmail(type,domain,articleId,fileIds,email,tenantId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #member_identification_information_Get/用户详情页调的接口，区别与getInfo
    def member_identification_information_Get(self,type,domain,tenantId,schemaId,memberId):
        result, desc, code = apicommon.get_member_identification_information_Get(type,domain,tenantId,schemaId,memberId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #file_delete/该接口为后台接口，后期即将移除，请不要继续使用，删除文件
    def file_delete(self,type,domain,tenantId,fileId,bakSess):
        result, desc, code = apicommon.get_file_delete(type,domain,tenantId,fileId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # webinar_open_getLuckyDrawRoster/获取会议的中奖名单
    def webinar_open_getLuckyDrawRoster(self,type,domain,webinarId,tenantId,webinarId_instanceId):
        result, desc, code = apicommon.get_webinar_open_getLuckyDrawRoster(type,domain,webinarId,tenantId,webinarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #luckyDraw_client_hasParticipate/有问题，该接口为后台接口，后期即将移除，请不要继续使用，检查某个用户是否已经参与过大屏抽奖，--创建线下会，报名会议后参与的抽奖
    def luckyDraw_client_hasParticipate(self,type,domain,tenantId,luckyDrawId,bakSess):
        result, desc, code = apicommon.get_luckyDraw_client_hasParticipate(type,domain,tenantId,luckyDrawId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #luckyDraw_client_participate/有问题，大屏抽奖，用户现场主动参与抽奖，如扫码-马叔，手机端有问题
    def luckyDraw_client_participate(self,type,domain,tenantId,luckyDrawId,bakSess):
        code = apicommon.get_luckyDraw_client_participate(type,domain,tenantId,luckyDrawId,bakSess)
        if  code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return code
    #luckyDraw_client_saveUserInfo/收集中奖用户信息
    def luckyDraw_client_saveUserInfo(self,type,domain,luckyDrawId):
        result, desc, code = apicommon.get_luckyDraw_client_saveUserInfo(type,domain,luckyDrawId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #luckyDraw/client/saveUserInfo统计
    def luckyDraw_client_saveUserInfo_count(self,type,domain,luckyDrawId):
        result, desc, code = apicommon.get_luckyDraw_client_saveUserInfo_count(type,domain,luckyDrawId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #luckyDraw_client_share/分享后参与情况，使用该接口获取分享资格
    def luckyDraw_client_share(self,type,domain,luckyDrawId):
        result, desc, code = apicommon.get_luckyDraw_client_share(type,domain,luckyDrawId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #luckyDraw_get/获取抽奖信息
    def luckyDraw_get(self,type,domain,luckyDrawId):
        result, desc, code = apicommon.get_luckyDraw_get(type,domain,luckyDrawId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #luckyDraw_getAwardDetailList/获取奖品列表信息
    def luckyDraw_getAwardDetailList(self,type,domain,luckyDrawId):
        result, desc, code = apicommon.get_luckyDraw_getAwardDetailList(type,domain,luckyDrawId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #luckyDraw_redPacket_getLotteryRecord/大屏红包抽奖获取中奖名单
    def luckyDraw_redPacket_getLotteryRecord(self,type,domain,tenantId,luckyDrawId):
        result, desc, code = apicommon.get_luckyDraw_redPacket_getLotteryRecord(type,domain,tenantId,luckyDrawId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #luckyDraw_redPacket_pushMessage/前端推送消息到node服务器
    def luckyDraw_redPacket_pushMessage(self,type,domain,luckyDrawId,tenantId,bakSess):
        result, desc, code = apicommon.get_luckyDraw_redPacket_pushMessage(type,domain,luckyDrawId,tenantId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #luckyDraw_result_getState/获取大屏抽奖的轮次状态，如果未开始的轮次，标记未开始，已开始的，返回中奖名单
    def luckyDraw_result_getState(self,type,domain,tenantId,luckyDrawId):
        result, desc, code = apicommon.get_luckyDraw_result_getState(type,domain,tenantId,luckyDrawId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # luckyDraw_result_getUserResultList/获取个人的普通抽奖记录
    def luckyDraw_result_getUserResultList(self,type,domain,luckyDrawId,bakSess):
        result, desc, code = apicommon.get_luckyDraw_result_getUserResultList(type,domain,luckyDrawId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #luckyDraw_view/检测是否参与过抽奖
    def luckyDraw_view(self,type,domain,luckyDrawId):
        result, desc, code = apicommon.get_luckyDraw_view(type,domain,luckyDrawId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #topic_get/获取发帖信息
    def topic_get(self,type,domain,topicId):
        result, desc, code = apicommon.get_topic_get(type,domain,topicId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_productLine_query/获取租户下产品线列表
    def api_productLine_query(self,type,domain,tenantId):
        result, desc, code = apicommon.get_api_productLine_query(type,domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_poll_share/分享投票行为
    def api_poll_share(self,type,domain,pollId,tenantId):
        result, desc, code = apicommon.get_api_poll_share(type,domain,pollId,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_poll_browse/浏览投票行为
    def api_poll_browse(self,type,domain,pollId,tenantId):
        result, desc, code = apicommon.get_api_poll_browse(type,domain,pollId,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_webinar_channel_query/根据会议ID获取该会议的渠道追踪代码
    def api_webinar_channel_query(self, type, domain, tenantId, webinarId):
        result, desc, code = apicommon.get_most_api_webinar_channel_query(type, domain, tenantId, webinarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_webinar_contacts_signup/会议报名
    def api_webinar_contacts_signup(self, type, domain,loginSess3,tenantId,webinarId,customFormId):
        result, desc, code = apicommon.get_api_webinar_contacts_signup(type, domain,loginSess3,tenantId,webinarId,customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_webinar_get/获取直播会议信息
    def api_webinar_get(self, type, domain,tenantId,webinarId):
        result, desc, code = apicommon.get_api_webinar_get(type, domain,tenantId,webinarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_webinar_interaction_filedownload_create/下载文件互动记录，有问题
    def api_webinar_interaction_filedownload_create(self, type, domain,tenantId,loginSess3,webinarId,fileId):
        result, desc, code = apicommon.get_api_webinar_interaction_filedownload_create(type, domain,tenantId,loginSess3,webinarId,fileId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_wechat_contacts_check/根据openIds批量查询用户对某个微信号的关注状态/-1 ：返回所有包含关注和未关注的
    def api_wechat_contacts_check(self, type, domain,tenantId,wechatId):
        result, desc, code = apicommon.get_api_wechat_contacts_check(type, domain,tenantId,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_wechat_contacts_get/获取微信粉丝信息/简体
    def api_wechat_contacts_get(self, type, domain,tenantId,wechatId):
        result, desc, code = apicommon.get_api_wechat_contacts_get(type, domain,tenantId,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_wechat_get/获取微信信息
    def api_wechat_get(self, type, domain,tenantId,wechatId):
        result, desc, code = apicommon.get_api_wechat_get(type, domain,tenantId,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_wechat_jssdk_config_get/获取微信jssdk配置
    def api_wechat_jssdk_config_get(self, type, domain,tenantId,wechatId):
        result, desc, code = apicommon.get_api_wechat_jssdk_config_get(type, domain,tenantId,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_article_category_get/获取栏目的详细信息/带模板
    def api_article_category_get(self, type, domain,tenantId,articleId):
        result, desc, code = apicommon.get_api_article_category_get(type, domain,tenantId,articleId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_common_shorturl_create/公共服务-短链接-生成短链接
    def api_common_shorturl_create(self, type, domain):
        result, desc, code = apicommon.get_api_common_shorturl_create(type, domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_content_collect_query/查询我收藏的信息
    def api_content_collect_query(self, type, domain,tenantId,bakSess):
        result, desc, code = apicommon.get_api_content_collect_query(type, domain,tenantId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_customform_record_query/获取某个OpenId的表单的记录
    def api_customform_record_query(self, type, domain,tenantId,customFormId):
        result, desc, code = apicommon.get_api_customform_record_query(type, domain,tenantId,customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_customform_share/分享表单行为
    def api_customform_share(self, type, domain,tenantId,customFormId):
        result, desc, code = apicommon.get_api_customform_share(type, domain,tenantId,customFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_dic_get/20180810-根据字典表id获取字典列表及字典值所级联的下级字典表名称
    def api_dic_get(self, type, domain,tenantId,dicId):
        result, desc, code = apicommon.get_api_dic_get(type, domain,tenantId,dicId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_dic_gettree/根据字典表id获取字典树形(当前字典值及下级字典值)结构 最多返回两级
    def api_dic_gettree(self, type, domain,dicId,tenantId):
        result, desc, code = apicommon.get_api_dic_gettree(type, domain,dicId,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_dic_params_set/新增或修改字典表的值
    def api_dic_params_set(self, type, domain,tenantId,dicId,bakSess):
        result, desc, code = apicommon.get_api_dic_params_set(type, domain,tenantId,dicId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_seminar_field_Get/获取线下会会议属性字段列表
    def api_seminar_field_Get(self, type, domain,tenantId):
        result, desc, code = apicommon.get_api_seminar_field_Get(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #interaction_getCountByType/获取实例的行为记录数量
    def interaction_getCountByType(self, type, domain,tenantId,seminarId_instanceId):
        result, desc, code = apicommon.get_interaction_getCountByType(type, domain,tenantId,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #interaction_getDetailList/ 获取租户下一个用户的某类型的互动记录
    def interaction_getDetailList(self, type, domain,tenantId,seminarId_instanceId,memberId):
        result, desc, code = apicommon.get_interaction_getDetailList(type, domain,tenantId,seminarId_instanceId,memberId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #interaction_getFileDownloads/获取租户下载文件记录，如果传递memberWords则获取这个人的下载记录，如果传递fileWords，则获取这个文件的下载记录
    def interaction_getFileDownloads(self, type, domain,tenantId):
        result, desc, code = apicommon.get_interaction_getFileDownloads(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # interaction_getListByMember/获取前台sess对应的互动行为记录
    def interaction_getListByMember(self, type, domain, tenantId, loginSess3):
        result, desc, code = apicommon.get_most_interaction_getListByMember(type, domain, tenantId, loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # interaction_getStatCountList/该接口为后台接口，后期即将移除，请不要继续使用，获取用户在实例中的（浏览/分享/资料）计数,有问题
    def interaction_getStatCountList(self, type, domain, tenantId, seminarId_instanceId, bakSess):
        result, desc, code = apicommon.get_most_interaction_getStatCountList(type, domain, tenantId,seminarId_instanceId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_form_Get/获取报名表单详细信息
    def api_seminar_form_Get(self, type, domain, tenantId, seminarId):
        result, desc, code = apicommon.get_most_api_seminar_form_Get(type, domain, tenantId, seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_Get/获取线下会议相关信息
    def api_seminar_Get(self, type, domain, tenantId, seminarId):
        result, desc, code = apicommon.get_most_api_seminar_Get(type, domain, tenantId, seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_signingpoint_interaction_get/线下会获取互动设置的领奖点列表，从来都没有启用过的互动不在返回列表
    def api_seminar_signingpoint_interaction_get(self, type, domain, tenantId, seminarId):
        result, desc, code = apicommon.get_most_api_seminar_signingpoint_interaction_get(type, domain, tenantId,seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_signingpoint_Statistics/签到点按通道统计签到人次
    def api_seminar_signingpoint_Statistics(self, type, domain, tenantId, seminarId, passageId):
        result, desc, code = apicommon.get_most_api_seminar_signingpoint_Statistics(type, domain, tenantId, seminarId,passageId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_seminar_subseminar_Query/获取分会场列表
    def api_seminar_subseminar_Query(self, type, domain, tenantId, seminarId):
        result, desc, code = apicommon.get_most_api_seminar_subseminar_Query(type, domain, tenantId, seminarId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_webinar_demand_record/奥点云点播观看次数，写成死值
    def api_webinar_demand_record(self, type, domain, tenantId, webinarId,videoId):
        result, desc, code = apicommon.get_most_api_webinar_demand_record(type, domain, tenantId, webinarId,videoId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # article_getCollectionList/微信模块获取收藏列表,有问题
    def article_getCollectionList(self, type, domain, loginSess3):
        code = apicommon.get_most_article_getCollectionList(type, domain, loginSess3)
        if code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return code
    # app_seminar_contact_nfc_bind/该接口为APP专用接口，项目不要使用，nfc批量绑定
    def app_seminar_contact_nfc_bind(self, type, domain, seminarId, bakSess):
        result, desc, code = apicommon.get_most_app_seminar_contact_nfc_bind(type, domain, seminarId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # app_seminar_contact_nfc_getBindRecord/获取绑卡记录，有问题
    def app_seminar_contact_nfc_getBindRecord(self, type, domain, seminarId, contactId, bakSess):
        result, desc, code = apicommon.get_most_app_seminar_contact_nfc_getBindRecord(type, domain, seminarId,contactId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # app_seminar_contact_nfc_getList/该接口为APP专用接口，项目不要使用，获取nfc绑定关系列表
    def app_seminar_contact_nfc_getList(self, type, domain, seminarId, bakSess):
        result, desc, code = apicommon.get_most_app_seminar_contact_nfc_getList(type, domain, seminarId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # app_seminar_contact_prints_getList/APP获取打印大屏签到信息
    def app_seminar_contact_prints_getList(self, type, domain, seminarId, signingPointId, loginSess3):
        result, desc, code = apicommon.get_most_app_seminar_contact_prints_getList(type, domain, seminarId,signingPointId, loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # tag_api_thirdTrigger_add/有问题，产品第三方行为触发-马震(华为不用，不监控 )
    def tag_api_thirdTrigger_add(self, type, domain, tenantId):
        code = apicommon.get_most_tag_api_thirdTrigger_add(type, domain, tenantId)
        if code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return code
    # app_seminar_contact_prints_getSigningPointInfo/获取会议下签到点缩略信息
    def app_seminar_contact_prints_getSigningPointInfo(self, type, domain, seminarId, bakSess):
        result, desc, code = apicommon.get_most_app_seminar_contact_prints_getSigningPointInfo(type, domain, seminarId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
     # app_seminar_contact_prints_updatePrintLog/更新APP打印大屏签到日志
    def app_seminar_contact_prints_updatePrintLog(self, type, domain, seminarId, tenantId, seminarId_instanceId,contactId, bakSess):
        result, desc, code = apicommon.get_most_app_seminar_contact_prints_updatePrintLog(type, domain, seminarId,tenantId,seminarId_instanceId,contactId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # tag_application_GetByObject/获取某个应用的标签使用情况-马叔
    def tag_application_GetByObject(self, type, domain, tenantId, seminarId_instanceId, bakSess):
        result, desc, code = apicommon.get_most_tag_application_GetByObject(type, domain, tenantId,seminarId_instanceId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # app_seminar_getList/该接口为APP专用接口，项目不要使用，获取会议列表
    def app_seminar_getList(self, type, domain, tenantId):
        result, desc, code = apicommon.get_most_app_seminar_getList(type, domain, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # tag_application_getByOpenId/通过粉丝OpenId来获取用户的标签
    def tag_application_getByOpenId(self, type, domain, tenantId):
        result, desc, code = apicommon.get_most_tag_application_getByOpenId(type, domain, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # app_seminar_signingPoint_checkIn_create/该接口为APP专用接口，项目不要使用，创建签到信
    def app_seminar_signingPoint_checkIn_create(self, type, domain, signingPointId, contactId, seminarId, bakSess):
        result, desc, code = apicommon.get_most_app_seminar_signingPoint_checkIn_create(type, domain, signingPointId,contactId, seminarId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #app_seminar_signingPoint_checkIn_getList/该接口为APP专用接口，项目不要使用，获取签到历史记录
    def app_seminar_signingPoint_checkIn_getList(self, type, domain,seminarId_instanceId,bakSess):
        result, desc, code = apicommon.get_app_seminar_signingPoint_checkIn_getList(type, domain,seminarId_instanceId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #app_seminar_signingPoint_checkIn_getListCompressed/获取签到历史记录,压缩版
    def app_seminar_signingPoint_checkIn_getListCompressed(self, type, domain,seminarId_instanceId,bakSess):
        code = apicommon.get_app_seminar_signingPoint_checkIn_getListCompressed(type, domain,seminarId_instanceId,bakSess)
        if code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return code
    #app_seminar_signingPoint_contact_getList/该接口为APP专用接口，项目不要使用，获取签到点通道下人员
    def app_seminar_signingPoint_contact_getList(self, type, domain,seminarId_instanceId,signingPointId,passageId,bakSess):
        result, desc, code = apicommon.get_app_seminar_signingPoint_contact_getList(type, domain,seminarId_instanceId,signingPointId,passageId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #account_channel_get/获取实例详情信息
    def account_channel_get(self, type, domain,seminarId_instanceId):
        result, desc, code = apicommon.get_account_channel_get(type, domain,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #account_getAuth/获取验证信息
    def account_getAuth(self, type, domain,nodeId,bakSess,seminarId_instanceId):
        result, desc, code = apicommon.get_account_getAuth(type, domain,nodeId,bakSess,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #account_getAuthByInstance/该接口为后台接口，后期即将移除，请不要继续使用，通过实例获取验证信息
    def account_getAuthByInstance(self, type, domain,seminarId_instanceId,bakSess):
        result, desc, code = apicommon.get_account_getAuthByInstance(type, domain,seminarId_instanceId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #admin_member_identification_query/客户管理-注册用户-根据自定义列表字段查询注册用户列表
    def admin_member_identification_query(self, type, domain,tenantId,bakSess):
        result, desc, code = apicommon.get_admin_member_identification_query(type, domain,tenantId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # anonymous_getId/获取一个全局用户Id（cookieId）
    def anonymous_getId(self, type, domain):
        result, desc, code = apicommon.get_anonymous_getId(type, domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #anonymous_setInfo/设置匿名用户信息
    def anonymous_setInfo(self, type, domain):
        result, desc, code = apicommon.get_anonymous_setInfo(type, domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #tag_application_GetListByType/查询租户下某种对象类型的应用的标签列表
    def tag_application_GetListByType(self, type, domain,tenantId,seminarId_instanceId):
        result, desc, code = apicommon.get_tag_application_GetListByType(type, domain,tenantId,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #tag_field_GetList/？？？？？？
    def tag_field_GetList(self, type, domain,tenantId,bakSess):
        result, desc, code = apicommon.get_tag_field_GetList(type, domain,tenantId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_article_category_interaction_browse/记录栏目浏览互动行为
    def api_article_category_interaction_browse(self, type, domain,tenantId,categoryId,wechatId):
        result, desc, code = apicommon.get_api_article_category_interaction_browse(type, domain,tenantId,categoryId,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_article_category_interaction_share/记录栏目分享互动行为
    def api_article_category_interaction_share(self, type, domain,tenantId,categoryId,wechatId):
        result, desc, code = apicommon.get_api_article_category_interaction_share(type, domain,tenantId,categoryId,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #tag_use_getListByType/获取租户可用的标签列表
    def tag_use_getListByType(self, type, domain,tenantId,nodeId,seminarId_instanceId):
        result, desc, code = apicommon.get_tag_use_getListByType(type, domain,tenantId,nodeId,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_article_category_query/项目使用，获取栏目列表/栏目id为空
    def api_article_category_query(self, type, domain,tenantId):
        result, desc, code = apicommon.get_api_article_category_query(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_article_get/获取文章详情
    def api_article_get(self, type, domain,tenantId,articleId):
        result, desc, code = apicommon.get_api_article_get(type, domain,tenantId,articleId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #template_template_getConfig/获取模板配置
    def template_template_getConfig(self, type, domain):
        result, desc, code = apicommon.get_template_template_getConfig(type, domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_article_interaction_create/记录文章的互动记录，包含浏览和分享
    def api_article_interaction_create(self, type, domain,tenantId,articleId):
        result, desc, code = apicommon.get_api_article_interaction_create(type, domain,tenantId,articleId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #templateMessage_batchSend/发送模板消息，微信模板,templateId-为开启的模板id
    def templateMessage_batchSend(self, type, domain,wechatId,bakSess):
        result, desc, code = apicommon.get_templateMessage_batchSend(type, domain,wechatId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_article_like_check/检查当前用户是否可以对文章点赞
    def api_article_like_check(self, type, domain,tenantId,articleId):
        result, desc, code = apicommon.get_api_article_like_check(type, domain,tenantId,articleId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
# templateMessage_getContactList/获取粉丝列表，发送模板消息用
    def templateMessage_getContactList(self,type,domain,wechatId):
        result, desc, code = apicommon.get_most_templateMessage_getContactList(type, domain,wechatId )
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_article_query/获取文章列表
    def api_article_query(self,type,domain,tenantId):
        result, desc, code = apicommon.get_most_api_article_query(type, domain, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # topic_post_getAllList/获取留言列表根据指定条件
    def topic_post_getAllList(self,type,domain,seminarId_instanceId,tenantId,bakSess):
        result, desc, code = apicommon.get_most_topic_post_getAllList(type, domain, seminarId_instanceId,tenantId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # topic_stat_homePage/获取讨论版的列表
    def topic_stat_homePage(self,type,domain,tenantId,seminarId_instanceId,bakSess):
        result, desc, code = apicommon.get_most_topic_stat_homePage(type, domain, tenantId,seminarId_instanceId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_member_contacts_get/获取注册用户信息
    def api_member_contacts_get(self,type,domain,tenantId,loginSess2):
        result, desc, code = apicommon.get_most_api_member_contacts_get(type, domain, tenantId,loginSess2)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_register/注册
    def member_register(self,type,domain,tenantId,schemaId,memberFormId):
        result, desc, code, loginId = apicommon.get_most_member_register(type, domain, tenantId,schemaId,memberFormId)
        print "result:",result
        print "desc:",desc
        print "code:",code
        print "loginId:",loginId
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc, loginId
    # article_shareRecord/分享记录，globalUserId、openId和sess至少填一个
    def article_shareRecord(self,type,domain,articleId,loginSess3):
        result, desc, code = apicommon.get_most_article_shareRecord(type, domain,articleId,loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # account_changePassword/该接口为后台接口，后期即将移除，请不要继续使用，修改密码
    def account_changePassword(self,type,domain,bakSess,member_password):
        result, desc, code = apicommon.get_most_account_changePassword(type, domain, bakSess,member_password)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_member_contacts_password_update/当前注册用户登录后修改密码
    def api_member_contacts_password_update(self,type,domain,tenantId,member_password,loginSess3):
        result, desc, code = apicommon.get_most_api_member_contacts_password_update(type, domain,tenantId,member_password,loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # admin_member_identification_updatelog_query/客户管理-注册用户-查询注册用户变更记录日志列表
    def admin_member_identification_updatelog_query(self,type,domain,tenantId,loginId,bakSess):
        result, desc, code = apicommon.get_most_admin_member_identification_updatelog_query(type, domain, tenantId,loginId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_member_contacts_update/当前注册用户更新自己的信息
    def api_member_contacts_update(self,type,domain,tenantId,loginSess3):
        result, desc, code = apicommon.get_most_api_member_contacts_update(type, domain, tenantId,loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # anonymous_checkSess/验证前台sess
    def anonymous_checkSess(self,type,domain,loginSess3):
        result, desc, code = apicommon.get_most_anonymous_checkSess(type, domain,loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_questionnaire_share/分享问卷行为
    def api_questionnaire_share(self,type,domain,questionid_sj,tenantId):
        result, desc, code = apicommon.get_most_api_questionnaire_share(type, domain,questionid_sj,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_file_interaction_share/记录文件分享互动行为
    def api_file_interaction_share(self,type,domain,tenantId,fileIds):
        result, desc, code = apicommon.get_most_api_file_interaction_share(type, domain,tenantId,fileIds)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_file_query/查询文件列表（带分页）
    def api_file_query(self,type,domain,tenantId,fileId,fileIds):
        result, desc, code = apicommon.get_most_api_file_query(type, domain, tenantId,fileId,fileIds)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_luckydraw_browse/浏览抽奖
    def api_luckydraw_browse(self,type,domain,luckyDrawId,tenantId,loginSess3):
        result, desc, code = apicommon.get_most_api_luckydraw_browse(type, domain,luckyDrawId,tenantId,loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_luckydraw_fieldinfo_query/获取前台显示中奖字段
    def api_luckydraw_fieldinfo_query(self,type,domain,luckyDrawId,createCheckIn,tenantId):
        result, desc, code = apicommon.get_most_api_luckydraw_fieldinfo_query(type, domain,luckyDrawId,createCheckIn,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_luckydraw_fieldinfo_update-设置前台显示中奖字段
    def api_luckydraw_fieldinfo_update(self,type,domain,luckyDrawId,createCheckIn,tenantId):
        result, desc, code = apicommon.get_most_api_luckydraw_fieldinfo_update(type, domain, luckyDrawId, createCheckIn,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_luckydraw_get/获取抽奖详情
    def api_luckydraw_get(self,type,domain,tenantId,luckyDrawId):
        result, desc, code = apicommon.get_most_api_luckydraw_get(type, domain,tenantId, luckyDrawId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_luckydraw_share/转发(分享)抽奖
    def api_luckydraw_share(self,type,domain,luckyDrawId,tenantId,loginSess3):
        result, desc, code = apicommon.get_most_api_luckydraw_share(type, domain,luckyDrawId,tenantId,loginSess3)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_luckydraw_user_query/获取大屏抽奖用户(1-100条)
    def api_luckydraw_user_query(self, type, domain,luckyDrawId,createCheckIn):
        result, desc, code = apicommon.get_api_luckydraw_user_query(type, domain,luckyDrawId,createCheckIn)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_member_contacts_check/检查唯一字段值是不是可用
    def api_member_contacts_check(self, type, domain,tenantId,schemaId):
        result, desc, code = apicommon.get_api_member_contacts_check(type, domain,tenantId,schemaId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_member_image_code_get/获取图片验证码
    def api_member_image_code_get(self, type, domain, tenantId):
        code = apicommon.get_api_member_image_code_get(type, domain, tenantId)
        if code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return code
    #api_product_query/获取产品线下产品列表
    def api_product_query(self, type, domain, tenantId,productLineId):
        result, desc, code = apicommon.get_api_product_query(type, domain, tenantId,productLineId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_seminar_app_checkinpoint_userpermit_query/app专用，获取用户签到点权限列表
    def api_seminar_app_checkinpoint_userpermit_query(self, type, domain,seminarId,loginSess1,tenantId):
        result, desc, code = apicommon.get_api_seminar_app_checkinpoint_userpermit_query(type, domain,seminarId,loginSess1,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_seminar_bigscreen_information_push/向NODE服务推送消息
    def api_seminar_bigscreen_information_push(self, type, domain,createCheckIn,tenantId):
        result, desc, code = apicommon.get_api_seminar_bigscreen_information_push(type, domain,createCheckIn,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #article_like/点赞，globalUserId、openId和sess至少填一个
    def article_like_one(self, type, domain,articleId,loginSess1):
        result, desc, code = apicommon.get_article_like(type, domain,articleId,loginSess1)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #seminar_getList/获取会议列表，该接口为APP专用接口，项目不要使用
    def seminar_getList(self, type, domain,tenantId):
        result, desc, code = apicommon.get_seminar_getList(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #articleCategory_get/获取单个栏目
    def articleCategory_get_one(self, type, domain,tenantId,categoryId):
        result, desc, code = apicommon.get_articleCategory_get_one(type, domain,tenantId,categoryId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #interaction_record/记录一个互动
    def interaction_record(self, type, domain,tenantId):
        result, desc, code = apicommon.get_interaction_record(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #product_crossLine_getListByIdList/根据产品id数组获取产品列表
    def product_crossLine_getListByIdList(self, type, domain,productLine):
        result, desc, code = apicommon.get_product_crossLine_getListByIdList(type, domain,productLine)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_seminar_contacts_Query/根据session获取此用户在某租户下参与过的所有会议
    def api_seminar_contacts_Query(self, type, domain,tenantId,bakSess):
        result, desc, code = apicommon.get_api_seminar_contacts_Query(type, domain,tenantId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #project_getInfoByLang/通过openId获取联系人信息,可返回不同地区语言
    def project_getInfoByLang(self, type, domain,wechatId):
        result, desc, code = apicommon.get_project_getInfoByLang(type, domain,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #article_getListByTags/获取租户下文章列表，可通过标签筛选
    def article_getListByTags(self, type, domain,tenantId):
        result, desc, code = apicommon.get_article_getListByTags(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_shorturl_generate/生成短地址,但是url按现在的url设置，因为路径变更了
    def api_shorturl_generate(self, type, domain):
        result, desc, code = apicommon.get_api_shorturl_generate(type, domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_seminar_app_signingpoint_group_Query/获取会议下的所有签到点信息
    def api_seminar_app_signingpoint_group_Query(self, type, domain,seminarId_instanceId):
        result, desc, code = apicommon.get_api_seminar_app_signingpoint_group_Query(type, domain,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #file_folder_getReleaseFileList/文件夹列表
    def file_folder_getReleaseFileList(self, type, domain,FolderId,accKey):
        result, desc, code = apicommon.get_file_folder_getReleaseFileList(type, domain,FolderId,accKey)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #member_identification_information_GetByOpenId/有问题，通过openId获取注册信息
    def member_identification_information_GetByOpenId(self, type, domain,tenantId):
        result, desc, code = apicommon.get_member_identification_information_GetByOpenId(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #app_seminar_contact_getListCompressed/该接口为APP专用接口，项目不要使用，获取压缩过的会议联系人
    def app_seminar_contact_getListCompressed(self, type, domain,seminarId_instanceId,bakSess):
        code = apicommon.get_app_seminar_contact_getListCompressed(type, domain,seminarId_instanceId,bakSess)
        if code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return code
    # app_seminar_signingPoint_getGroupList/该接口为APP专用接口，项目不要使用，获取会议下的所有签到点信息
    def app_seminar_signingPoint_getGroupList(self, type, domain, seminarId_instanceId):
        result, desc, code = apicommon.get_most_app_seminar_signingPoint_getGroupList(type, domain,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # comment_getList/获取评论列表
    def obtain_comment_getList(self, type, domain, tenantId, topicId, bakSess):
        result, desc, code = apicommon.get_most_comment_getList(type, domain, tenantId, topicId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # app_seminar_contact_field_getCustomFields/该接口为APP专用接口，项目不要使用，获取联系人字段
    def app_seminar_contact_field_getCustomFields(self, type, domain, seminarId_instanceId):
        result, desc, code = apicommon.get_most_app_seminar_contact_field_getCustomFields(type, domain,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # webinar_open_newRegistration/注册用户接口
    def webinar_open_newRegistration(self, type, domain, tenantId, schemaId, webinarId_instanceId, memberFormId,loginSess):
        result, desc, code = apicommon.get_most_webinar_open_newRegistration(type, domain, tenantId, schemaId,webinarId_instanceId, memberFormId,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # file_cutImage/裁剪平台图片资源内容
    def file_cutImage(self, type, domain, mappingId):
        result, desc, code = apicommon.get_file_cutImage(type, domain, mappingId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_geneRegister/注册用户
    def member_geneRegister(self, type, domain, tenantId, schemaId, memberFormId, loginSess):
        result, desc, code, memberId = apicommon.get_most_member_geneRegister(type, domain, tenantId, schemaId,memberFormId, loginSess)
        print "result:", result
        print "desc:", desc
        print "memberId:", memberId
        print "code:",code
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc, memberId
    # app_seminar_contact_getList/该接口为APP专用接口，项目不要使用，获取会议联系人
    def app_seminar_contact_getList(self, type, domain, webinarId_instanceId, bakSess):
        result, desc, code = apicommon.get_most_app_seminar_contact_getList(type, domain, webinarId_instanceId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
        # member_getById/获取某个会员信息

    def member_getById(self, type, domain, tenantId, memberId, bakSess):
        result, desc, code = apicommon.get_most_member_getById(type, domain, tenantId, memberId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # article_getListByTags
    def article_getListByTags(self, type, domain, tenantId):
        result, desc, code = apicommon.get_most_article_getListByTags(type, domain, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # app_seminar_contact_getByUniqueField/根据参会二维码获取会议联系人
    def app_seminar_contact_getByUniqueField(self, type, domain, seminarId, bakSess):
        result, desc, code = apicommon.get_most_app_seminar_contact_getByUniqueField(type, domain, seminarId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
     # member_identification_getList/获取注册用列表,有问题
    def member_identification_getList(self, type, domain, tenantId, schemaId, bakSess):
        result, desc, code = apicommon.get_most_member_identification_getList(type, domain, tenantId, schemaId, bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_member_setEnable/启用/停用注册用户,马叔
    def member_member_setEnable(self, type, domain, schemaId, tenantId, bakSess,memberId):
        result, desc, code = apicommon.get_most_member_member_setEnable(type, domain, schemaId, tenantId, bakSess,memberId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_file_interaction_preview/记录文件预览互动行为
    def api_file_interaction_preview(self,type,domain,tenantId,fileIds):
        result, desc, code = apicommon.get_most_api_file_interaction_preview(type, domain,tenantId,fileIds)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_member_form_get/获取表单信息
    def api_member_form_get(self,type,domain,tenantId,memberFormId):
        result, desc, code = apicommon.get_most_api_member_form_get(type, domain, tenantId, memberFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # webinar_open_interaction_fileDownLoad/下载文件互动记录,有问题
    def webinar_open_interaction_fileDownLoad(self,type,domain,loginSess1,webinarId_instanceId,fileId):
        result, desc, code = apicommon.get_most_webinar_open_interaction_fileDownLoad(type, domain,loginSess1,webinarId_instanceId,fileId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_webinar_live_sendmsg-直播发消息(提问)
    def api_webinar_live_sendmsg(self,type,domain,loginSess3,webinarId,tenantId):
        result, desc, code = apicommon.get_most_api_webinar_live_sendmsg(type, domain,loginSess3,webinarId,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # api_webinar_live_site_browse/访问直播会议专题页
    def api_webinar_live_site_browse(self,type,domain,loginSess3,webinarId,tenantId):
        result, desc, code = apicommon.get_most_api_webinar_live_site_browse(type, domain, loginSess3, webinarId, tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_form_getList/该接口为后台接口，后期即将移除，请不要继续使用，获取体系下的注册表单列表
    def member_form_getList(self,type,domain,tenantId,memberSchemaId,bakSess):
        result, desc, code = apicommon.get_most_member_form_getList(type, domain,tenantId,memberSchemaId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # seminar_topicTemplate_seminar_get/获取会议相关信息
    def seminar_topicTemplate_seminar_get(self,type,domain,seminarId_instanceId):
        result, desc, code = apicommon.get_most_seminar_topicTemplate_seminar_get(type, domain,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_webinar_live_share/直播分享
    def api_webinar_live_share(self, type, domain,loginSess3,webinarId,tenantId):
        result, desc, code = apicommon.get_api_webinar_live_share(type, domain, loginSess3,webinarId,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_webinar_demand_share/分享点播
    def api_webinar_demand_share(self, type, domain,loginSess3,webinarId,tenantId):
        result, desc, code = apicommon.get_api_webinar_demand_share(type, domain, loginSess3,webinarId,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #webinar_demand_site_browse/访问点播专题页面
    def webinar_demand_site_browse(self, type, domain,loginSess3,webinarId,tenantId):
        result, desc, code = apicommon.get_webinar_demand_site_browse(type, domain, loginSess3,webinarId,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_webinar_demand_play/播放点播
    def api_webinar_demand_play(self, type, domain,loginSess3,webinarId,tenantId):
        result, desc, code = apicommon.get_api_webinar_demand_play(type, domain, loginSess3,webinarId,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #member_integral_update/积分变更
    def member_integral_update(self, type, domain,tenantId,loginSess1,seminarId_instanceId):
        result, desc, code = apicommon.get_member_integral_update(type, domain,tenantId,loginSess1,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #admin_account_create/账号-用户管理添加账号
    def admin_account_create(self, type, domain,tenantId,nodeId,password,bakSess):
        result, desc, code ,userid= apicommon.get_admin_account_create(type, domain,tenantId,nodeId,password,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc,userid
    #admin_account_update/编辑用户资料
    def admin_account_update(self, type, domain,tenantId,nodeId,userid,bakSess):
        result, desc, code = apicommon.get_admin_account_update(type, domain,tenantId,nodeId,userid,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #admin_account_disableUser/禁用用户
    def admin_account_disableUser(self, type, domain,tenantId,nodeId,userid,bakSess):
        result, desc, code = apicommon.get_admin_account_disableUser(type, domain,tenantId,nodeId,userid,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #admin_account_delete/删除用户
    def admin_account_delete(self, type, domain,tenantId,userid,bakSess):
        result, desc, code = apicommon.get_admin_account_delete(type, domain,tenantId,userid,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #admin_application_get/获取手机key值
    def admin_application_get(self, type, domain,tenantId,bakSess):
        result, desc, code = apicommon.get_admin_application_get(type, domain,tenantId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #sms_addSmsLog/发送短信
    def sms_addSmsLog(self, type, domain,tenantId):
        result, desc, code = apicommon.get_sms_addSmsLog(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_article_collection_check/检查当前注册用户是否可以收藏该文章
    def api_article_collection_check(self, type, domain,tenantId,articleId,loginSess1):
        result, desc, code = apicommon.get_api_article_collection_check(type, domain,tenantId,articleId,loginSess1)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_customform_get/获取自定义表单详情
    def api_customform_get(self, type, domain, tenantId,customFormId,bakSess):
        result, desc, code = apicommon.get_api_customform_get(type, domain, tenantId,customFormId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_file_download_interaction_query/获取注册用户邮件中文章模板关联文件下载的记录
    def api_file_download_interaction_query(self, type, domain, tenantId,loginSess1):
        result, desc, code = apicommon.get_api_file_download_interaction_query(type, domain, tenantId,loginSess1)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api_member_form_share/分享注册表单记录互动行为
    def api_member_form_share(self, type, domain, tenantId,registerFormId,loginSess1):
        result, desc, code = apicommon.get_api_member_form_share(type, domain, tenantId,registerFormId,loginSess1)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #questionary_getResultList/该接口为后台接口，后期即将移除，请不要继续使用，获取从某个实例进来回答问卷的列表
    def questionary_getResultList(self, type, domain, tenantId,bakSess):
        result, desc, code = apicommon.get_questionary_getResultList(type, domain, tenantId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #member_GetTokenByOpenId/通过openId 获取token
    def member_GetTokenByOpenId(self, type, domain):
        result, desc, code,token = apicommon.get_most_member_GetTokenByOpenId(type, domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc,token
    #member_admin_unbindWeChat/用户和微信解绑--数据删除插件使用
    def member_admin_unbindWeChat(self, type, domain, tenantId,memberSchemaId,wechatId):
        result, desc, code = apicommon.get_member_admin_unbindWeChat(type, domain, tenantId,memberSchemaId,wechatId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #account_verifySession/验证session,并获取相应的信息
    def account_verifySession(self, type, domain, loginSess1):
        result, desc, code = apicommon.get_account_verifySession(type, domain, loginSess1)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #admin_member_integral_updateitems/批量积分变更
    def admin_member_integral_updateitems(self, type, domain,seminarId_instanceId,wechatId,bakSess):
        result, desc, code = apicommon.get_admin_member_integral_updateitems(type, domain,seminarId_instanceId,wechatId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api/seminar/signingpoint/query/查询实例下的签到点列表
    def api_seminar_signingpoint_query(self, type, domain,tenantId,seminarId_instanceId):
        result, desc, code = apicommon.get_api_seminar_signingpoint_query(type, domain,tenantId,seminarId_instanceId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #admin/account/userRole/set/编辑后台账号权限
    def admin_account_userRole_set(self, type, domain,tenantId,nodeId,bakSess):
        result, desc, code = apicommon.get_admin_account_userRole_set(type, domain,tenantId,nodeId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #admin/tag/trigger/score/getlist/根据租户id获取行为标签触发分值
    def admin_tag_trigger_score_getlist(self, type, domain,tenantId,bakSess):
        result, desc, code = apicommon.get_admin_tag_trigger_score_getlist(type, domain,tenantId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api/seminar/contacts/ticket/get/获取联系人电子门票图片
    def api_seminar_contacts_ticket(self, type, domain,tenantId):
        result, desc, code = apicommon.get_api_seminar_contacts_ticket(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api/seminar/contacts/qrcode/browse/参会人签到二维码浏览（次数+1）
    def api_seminar_contacts_qrcode_browse(self, type, domain,tenantId):
        result, desc, code = apicommon.get_api_seminar_contacts_qrcode_browse(type, domain,tenantId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #customForm_reAction自定义表单重复提交，更新之前的提交结果(项目需要用)
    def customForm_reAction(self, type, domain,registerFormId):
        result, desc, code = apicommon.get_customForm_reAction(type, domain,registerFormId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api/file/folder/interaction/share/记录文件夹分享互动行为
    def api_file_folder_interaction_share(self, type, domain,tenantId,FolderId):
        result, desc, code = apicommon.get_api_file_folder_interaction_share(type, domain,tenantId,FolderId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #member_integral_get/查询注册用户|微信粉丝积分
    def member_integral_get(self, type, domain,tenantId,loginSess1):
        result, desc, code = apicommon.get_member_integral_get(type, domain,tenantId,loginSess1)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #api/member/integral/integrallog/query/查询变更日志
    def api_member_integral_integrallog_query(self, type, domain,tenantId,seminarId_instanceId,loginSess1):
        result, desc, code = apicommon.get_api_member_integral_integrallog_query(type, domain,tenantId,seminarId_instanceId,loginSess1)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    #admin_account_password_update/客户管理中修改用户密码
    def admin_account_password_update(self, type, domain,tenantId,nodeId,bakSess):
        result, desc, code = apicommon.get_admin_account_password_update(type, domain,tenantId,nodeId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
# 二维码密串登录
    def dimensional_code_string(self,type,domain):
        result, desc, code = apicommon.get_most_dimensional_code_string(type,domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # account/getOAuthTokenByOpen/为account/verifyToken提供token
    def account_getOAuthTokenByOpen(self,type,domain,tenantId,bakSess):
        result, desc, code,pos = apicommon.get_most_account_getOAuthTokenByOpen(type,domain,tenantId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc,pos
    # account/verifyToken/为九芝兰提供验证token的接口，九芝兰使用smarket3给它的token来查询租户信息
    def account_verifyToken(self,type,domain,tokenfor_verifyToken):
        result, desc, code = apicommon.get_most_account_verifyToken(type, domain,tokenfor_verifyToken)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member/GetTokenByOpenId/通过openId 获取token
    def member_GetTokenByOpenId_a(self,type,domain):
        result, desc, code, pos = apicommon.get_most_member_GetTokenByOpenId(type, domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc, pos
    # member/bind/绑定第三方 当前实名用户与第三方登录用户绑定
    def member_bind(self,type,domain,loginSess,tokenfor_memberbind):
        result, desc, code = apicommon.get_most_member_bind(type, domain, loginSess,tokenfor_memberbind)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member/unbind/解绑第三方 当前实名用户与第三方登录用户解绑
    def member_unbind(self,type,domain,loginSess):
        result, desc, code = apicommon.get_most_member_unbind(type, domain, loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # member_geneUpdate/更新注册用户信息
    def member_geneUpdate(self,type,domain,loginSess):
        result, desc, code = apicommon.get_most_member_geneUpdate(type, domain,loginSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
# 给对象打标签
    def tag_application_SetOnObject(self,type,domain,tenantId,tagSchemaId,tagFieldId,fieldName,displayName,tagId,bakSess):
        result, desc, code = apicommon.tag_application_SetOnObject(type,domain,tenantId,tagSchemaId,tagFieldId,fieldName,displayName,tagId,bakSess)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
#     线上会转发接口,只有s2有
    def webinar_open_transfer(self,type,domain):
        code = apicommon.webinar_open_transfer(type,domain)
        if  code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return code
# 查看自己的签到记录
    def seminar_signingPoint_getCheckInLog_contactId(self,type,domain,tenantId,bakSess,seminarId,seminarId_instanceId,signingPointId,passageId,contactId):
        result, desc, code = apicommon.seminar_signingPoint_getCheckInLog_contactId(type,domain,tenantId,bakSess,seminarId,seminarId_instanceId,signingPointId,passageId,contactId)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # 二维码密串登陆,只有s2平台有
    def admin_account_login_tokenLogin(self,type, domain):
        result, desc, code = apicommon.admin_account_login_tokenLogin(type,domain)
        if result == 0 and desc == "successful" and code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return result, desc
    # 获取图片验证码
    def member_getImageCode(self,type, domain):
        code = apicommon.member_getImageCode(type, domain)
        if  code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return code
    # 华为410361账号监控
    def sms_balance(self,type):
        code,num,desc = apicommon.sms_balance(type)
        if code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return code,num,desc
        # 华为400310
    def sms_balance_two(self, type):
        code, num, desc = apicommon.sms_balance_two(type)
        if code == 200:
            self.update_count_total_successful()
        else:
            self.update_count_total_fail()
        return code, num, desc
if __name__ == '__main__':
    # HW,HW_UAT,S2,UAT,DELL
    api_most_all().account_login(u"HW")





