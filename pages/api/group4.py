# -*- coding: utf-8 -*-
# import requests,os
from pages.api import apicommon
import time
import datetime
import sys
reload(sys)  #在解释器里修改的编码只能保证当次有效，在重启解释器后，会发现，编码又被重置为默认的ascii了
sys.setdefaultencoding('utf8')
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

"""
马会东开发组
"""
class ApiRequestsfoureFour():


    # 获取自定义表单
    def webinar_open_getCustomFormInfo(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/getCustomFormInfo"

        payload = "{\r\n    \"tenantId\": 1116,\r\n    \"instanceId\": 38369,\r\n    \"customFormId\":13283\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "0d5204e2-e033-4ab0-a754-827c846fb5e8"
        }

        return apicommon.post_req(url, payload, headers)

    # 获取直播会议列表
    def webinar_open_getWebinarList(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/getWebinarList"

        payload = "{\r\n    \"tenantId\": \"1116\",\r\n    \"startTime\": \"\",\r\n    \"status\": 3,\r\n    \"keyword\": \"\",\r\n    \"orderBy\": \"createTime\",\r\n    \"videoType\": \"1\",\r\n    \"start\": 0,\r\n    \"num\": 12,\r\n    \"includeGuest\": \"true\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "6c19b05f-1848-4dca-8ed7-483cdac0ddf4"
        }

        return apicommon.post_req(url, payload, headers)

    #获取会议信息
    def webinar_open_getApplicantInfo(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/getApplicantInfo"

        payload = "{\r\n    \"instanceId\": 38609,\r\n    \"sess\": \"" + apicommon.bakSess + "\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "6d30fa55-8cf7-441c-86ac-221e5948ac4f"
        }

        return apicommon.post_req(url, payload, headers)

    #得到一个点播会议的详情信息
    def webinar_open_getDemandInfo(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/getDemandInfo"

        payload = "{\r\n    \"tenantId\": 1116,\r\n    \"instanceId\": 40145,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "e299aa94-b30e-4b3a-a0a3-dd81b03db9aa"
        }

        return apicommon.post_req(url, payload, headers)

    #根据会议id和唯一字段获取参会人信息
    def seminar_contact_front_getContactInfo(self):
        url = "http://s2-api.smarket.net.cn/seminar/contact/front/getContactInfo"

        payload = "{\r\n  \"seminarId\": 4793,\r\n  \"unique\": \"1528255383000@qq.com\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "5bb535c3-f53a-4332-9f95-f8134efe869d"
        }

        return apicommon.post_req(url, payload, headers)

    #获取抽奖信息
    def luckyDraw_get(self):
        url = "http://s2-api.smarket.net.cn/luckyDraw/get"

        payload = "{\r\n    \"luckyDrawId\": 2657,\r\n    \"hasVirtualAward\": false,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "68c5336f-ff75-494a-bdd1-ce91090a5233"
        }

        return apicommon.post_req(url, payload, headers)

    #获取租户下的某一分类的多产品线下的产品列表
    def product_crossLine_getList(self):
        url = "http://s2-api.smarket.net.cn/product/crossLine/getList"

        payload = "{\r\n  \"tenantId\": \"1116\",\r\n  \"keyword\": \"\",\r\n  \"start\": 0,\r\n  \"num\": 10,\r\n  \"isNew\": \"0\",\r\n  \"categoryId\": \"0\",\r\n  \"withSoldOut\": \"0\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "69d8bf0d-0dbd-45e7-be17-1759492c1d57"
        }

        return apicommon.post_req(url, payload, headers)

    #获取产品线下产品列表
    def product_getList(self):
        url = "http://s2-api.smarket.net.cn/product/getList"

        payload = "{\r\n    \"tenantId\": \"1116\",\r\n    \"productLineId\": \"479\",\r\n    \"keyword\": \"\",\r\n    \"start\": \"0\",\r\n    \"num\": \"10\",\r\n    \"isNew\": \"0\",\r\n    \"categoryId\": \"\",\r\n    \"withSoldOut\": \"1\",\r\n    \"forProject\": \"1\",\r\n    \"isTop\": \"1\",\r\n    \"customFields\": {\r\n      \"checkbox_1\": [\r\n        1,\r\n        2\r\n      ],\r\n      \"radio_1\": 1\r\n    },\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "47bda299-1744-43ec-b11e-1dfb24c58de1"
        }

        return apicommon.post_req(url, payload, headers)

    #获取租户下产品线列表
    def productLine_getList(self):
        url = "http://s2-api.smarket.net.cn/productLine/getList"

        payload = "{\r\n    \"tenantId\": 1116,\r\n    \"withDeleted\": 1,\r\n    \"num\": 10,\r\n    \"start\": 0,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "8764bd44-60b1-48ca-a063-9d670ceb42af"
        }

        return apicommon.post_req(url, payload, headers)

    #获取留言板的发帖的回帖
    def post_getMainAndReplyList(self):
        url = "http://s2-api.smarket.net.cn/post/getMainAndReplyList"

        payload = "{\r\n    \"topicId\": 1431,\r\n    \"start\": 0,\r\n    \"num\": 10,\r\n    \"status\": 0,\r\n    \"isPreview\": 1,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "35d9280c-999c-41b7-8644-697516b5aa5a"
        }

        return apicommon.post_req(url, payload, headers)
    #luckyDraw_result_getState

    #获取大屏抽奖的轮次状态，如果未开始的轮次，标记未开始，已开始的，返回中奖名单
    def luckyDraw_result_getState(self):
        url = "http://s2-api.smarket.net.cn/luckyDraw/result/getState"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"luckyDrawId\": 2657,\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "096b64ce-26b4-4c2e-b4d5-1065718161a6"
        }

        return apicommon.post_req(url, payload, headers)

    #获取某人的未被删除的发送帖子记录
    def post_getListByUser(self):
        # url = "http://s3-api.smarket.net.cn/post/getListByUser"
        #
        # payload = "{\r\n  \"topicId\": 1431,\r\n  \"start\": 0,\r\n  \"num\": 10,\r\n  \"openId\": \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",\r\n  \"cookieId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        # headers = {
        #     'Content-Type': "application/json",
        #     'Cache-Control': "no-cache",
        #     'Postman-Token': "93b89d44-ab22-4397-8dfc-b8c6d0a24c9e"
        # }

        url = "http://s2-api.smarket.net.cn/post/getListByUser"

        payload = "{\r\n  \"topicId\": 1431,\r\n  \"start\": 0,\r\n  \"num\": 10,\r\n  \"openId\": \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",\r\n  \"cookieId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "0abf4997-3160-4d79-85ef-abe981858788"
        }

        return apicommon.post_req(url, payload, headers)

    #获取发帖信息
    def topic_get(self):

        url = "http://s2-api.smarket.net.cn/topic/get"

        payload = "{\r\n  \"topicIds\": [\r\n    617\r\n  ],\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "e6cb73c3-3ecf-472e-a190-a100691edd7e"
        }

        return apicommon.post_req(url, payload, headers)

    #获取已报名的会议列表
    def webinar_open_getAttendList(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/getAttendList"

        payload = "{\r\n    \"tenantId\": 1116,\r\n    \"start\": 0,\r\n    \"num\": 12,\r\n    \"videoType\": \"1\",\r\n    \"includeExtends\": \"1\",\r\n    \"includeGuest\": \"0\",\r\n    \"orderBy\": \"createTime\",\r\n    \"sort\": \"desc\",\r\n    \"sess\": \"" + apicommon.bakSess + "\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "b1158108-8986-4af9-b294-f35f5b30de32"
        }

        return apicommon.post_req(url, payload, headers)

    #获取视频信息
    def webinar_open_getVideoTimeLine(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/getVideoTimeLine"

        payload = "{\r\n    \"videoId\": 1,\r\n    \"tenantId\": 1,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "d250f858-f86c-4ba0-98d4-7b65513cf41f"
        }

        return apicommon.post_req(url, payload, headers)

    #根据实例编号获取该实例的渠道追踪代码
    def webinar_open_trackingCode_getList(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/trackingCode/getList"

        payload = "{\r\n    \"tenantId\": 1116,\r\n    \"instanceId\": 39920,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "ac2e6043-4a53-4167-94b9-5715893b6683"
        }

        return apicommon.post_req(url, payload, headers)

    #获取贴子信息
    def post_get(self):
        url = "http://s2-api.smarket.net.cn/post/get"

        payload = "{\r\n    \"tenantId\": 1116,\r\n    \"nodeId\": 1116,\r\n    \"moduleId\": \"\",\r\n    \"instanceId\": \"\",\r\n    \"postId\": 61321,\r\n    \"memberId\": 10,\r\n    \"openId\": \"\",\r\n    \"cookieId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n    \"sess\": \"" + apicommon.bakSess + "\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "2ed9652a-c011-4645-85b8-9d1d1d45d0c1"
        }

        return apicommon.post_req(url, payload, headers)

    #获取某主贴的所有回贴
    def post_getReplyPost(self):
        url = "http://s2-api.smarket.net.cn/post/getReplyPost"

        payload = "{\r\n    \"tenantId\": 1116,\r\n    \"nodeId\": 1116,\r\n    \"moduleId\": \"\",\r\n     \"instanceId\": \"\",\r\n    \"postId\": 61321,\r\n    \"start\": 0,\r\n    \"num\": 10,\r\n    \"memberId\": 10,\r\n    \"openId\": \"\",\r\n    \"cookieId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n    \"sess\": \"" + apicommon.bakSess + "\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "710a2a82-7e64-46c9-8ccf-389776801894"
        }

        return apicommon.post_req(url, payload, headers)

    #获取某个产品线的字段列表
    def productLine_field_get(self):
        url = "http://s2-api.smarket.net.cn/productLine/field/get"

        payload = "{\r\n    \"productLineId\": 846,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "7984686f-6e22-4837-a633-183007bccd22"
        }

        return apicommon.post_req(url, payload, headers)

    #获取某产品线下具体某个字典值的配置信息
    def productLine_category_getConfigInfo(self):
        url = "http://s2-api.smarket.net.cn/productLine/category/getConfigInfo"

        payload = "{\r\n    \"productLineId\": 846,\r\n    \"dicValueId\": 1,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "f8fc9724-2c75-487e-b94c-3134eee78f0a"
        }

        return apicommon.post_req(url, payload, headers)

    #获取奖品列表信息
    def luckyDraw_getAwardDetailList(self):
        url = "http://s2-api.smarket.net.cn/luckyDraw/getAwardDetailList"

        payload = " {\r\n    \"luckyDrawId\": 2613,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "ca260aca-05be-404a-89e6-a2489c9cc303"
        }

        return apicommon.post_req(url, payload, headers)

    #抽奖
    def luckyDraw_client_action(self):
        url = "http://s2-api.smarket.net.cn/luckyDraw/client/action"

        #20180704
        #payload = "{\r\n    \"luckyDrawId\": 2682,\r\n    \"cookieId\": \"cookieId\",\r\n    \"openId\": \"wechatOpenId\",\r\n    \"memberId\": 1,\r\n    \"nickName\": \"null\",\r\n    \"headImgUrl\": \"www.126.com\",\r\n    \"memberName\": \"this is my name\",\r\n    \"sex\": \"nan\",\r\n    \"city\": \"石家庄\",\r\n    \"province\": \"河北\",\r\n    \"country\": \"中国\",\r\n    \"url\": \"\",\r\n    \"referenceUrl\": \"\",\r\n    \"sess\": \"ee35b80933173a6ec16fe3236fea6b82\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        payload={
            "luckyDrawId": 2682,
            "cookieId": "cookieId",
            "openId": "wechatOpenId",
            "memberId": 1,
            "nickName": "null",
            "headImgUrl": "www.126.com",
            "memberName": "this is my name",
            "sex": "nan",
            "city": "石家庄",
            "province": "河北",
            "country": "中国",
            "url": "",
            "referenceUrl": "",
            "sess": apicommon.bakSess,
            "_cache_with_cached": "1",
            "_cache_refresh": "1",
            "_cache_timeout": "60"
          }
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "a27651da-da1e-43a9-8e90-a7da1d1b48de"
        }

        return apicommon.post_req(url, payload, headers)

    #大屏抽奖的抽奖操作
    def luckyDraw_client_actionByBigScreen(self):
        url = "http://s2-api.smarket.net.cn/luckyDraw/client/actionByBigScreen"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"luckyDrawId\": 2613,\r\n  \"instanceId\": 1,\r\n  \"awardDetailId\": 1,\r\n  \"num\": 1,\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "a846e6cc-6de1-48ba-a677-c2c2c5467fb6"
        }

        return apicommon.post_req(url, payload, headers)

    #获取评论列表
    def comment_getList(self):

        url = "http://s2-api.smarket.net.cn/comment/getList"

        payload = "{\r\n    \"tenantId\": \"1116\",\r\n    \"subVersionId\": \"102161\",\r\n    \"commentId\": \"0\",\r\n    \"start\": \"0\",\r\n    \"num\": \"10\",\r\n    \"topicId\": \"1431\",\r\n    \"sess\": \"" + apicommon.bakSess + "\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "a9bae6c3-a085-4bfe-af8e-feb0a41058e4"
        }

        return apicommon.post_req(url, payload, headers)

    #该接口为后台接口，后期即将移除，请不要继续使用，获取体系下的注册表单列表
    def member_form_getList(self):

        url = "http://s2-api.smarket.net.cn/member/form/getList"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"memberSchemaId\": 244,\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "0f075e53-25ef-4f18-90e3-d0da6d114b80"
        }

        return apicommon.post_req(url, payload, headers)

    #获取个人的普通抽奖记录
    def luckyDraw_result_getUserResultList(self):
        url = "http://s2-api.smarket.net.cn/luckyDraw/result/getUserResultList"

        payload = "\r\n{\r\n  \"luckyDrawId\": 2613,\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"openId\": \"\",\r\n  \"cookieId\": \"\",\r\n  \"start\": 0,\r\n  \"num\": 20,\r\n  \"startTime\": \"2018-05-31\",\r\n  \"endTime\": \"2018-05-31\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "9adb0c6e-6aee-4602-852a-ecb86df6b18e"
        }

        return apicommon.post_req(url, payload, headers)

    #获取产品详细信息
    def product_get(self):
        url = "http://s2-api.smarket.net.cn/product/get"

        payload = "{\r\n    \"productId\": \"846\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "858aa878-f81f-410e-a2bf-b0e8b9a04d48"
        }

        return apicommon.post_req(url, payload, headers)

    #线上会报名接口
    def webinar_open_registration(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/registration"
        base_dir = os.path.join(os.path.dirname(__file__), 'token.md')
        with open(base_dir, 'r') as f:
            Sesson = f.read()
        print "sesson:", Sesson
        payload = "{\r\n    \"instanceId\": 38369,\r\n    \"channel\": \"渠道一\",\r\n    \"items\": [\r\n      {\r\n        \"key\": \"name\",\r\n        \"text\": \"上帝\"\r\n      },\r\n      {\r\n        \"key\": \"city\",\r\n        \"text\": \"天堂\"\r\n      },\r\n      {\r\n        \"key\": \"mobile\",\r\n        \"text\": \"14444444444\"\r\n      },\r\n      {\r\n        \"key\": \"email\",\r\n        \"text\": \"shangdi@tiantang.com\"\r\n      },\r\n      {\r\n        \"key\": \"enterprise\",\r\n        \"text\": \"天宫股份有限公司\"\r\n      },\r\n      {\r\n        \"key\": \"department\",\r\n        \"text\": \"人力资源部\"\r\n      },\r\n      {\r\n        \"key\": \"position\",\r\n        \"text\": \"总监\"\r\n      }\r\n    ],\r\n    \"memberId\": \"\",\r\n    \"sys_source\": \"pc\",\r\n    \"sess\": \""+Sesson+"\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "9bef3366-fa25-4404-8856-02f656eb25ac"
        }

        return apicommon.post_req(url, payload, headers)

    #该接口为后台接口，后期即将移除，请不要继续使用，留言板发帖
    def post_create(self):
        url = "http://s2-api.smarket.net.cn/post/create"

        payload = "{\r\n  \"tenantId\": \"\",\r\n  \"nodeId\": \"\",\r\n  \"moduleId\": \"\",\r\n  \"instanceId\": \"\",\r\n  \"enableReply\": 0,\r\n  \"isAnonymous\": 1,\r\n  \"topicId\": 1431,\r\n  \"content\": \"h\",\r\n  \"postId\": 61327,\r\n  \"memberId\": 0,\r\n  \"openId\": \"\",\r\n  \"cookeId\": \"\",\r\n  \"nickname\": \"\",\r\n  \"createrPic\": \"\",\r\n  \"sess\": \"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "4a84db28-284e-4b31-9b83-cd6408061786"
        }

        return apicommon.post_req(url, payload, headers)

    #检查什么情况下可以继续投票、答问卷，会场开放过程中可以答
    def webinar_event_interaction_check(self):
        url = "http://s2-api.smarket.net.cn/webinar/event/interaction/check"

        payload = "{\r\n  \"instanceId\": 38369,\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "a0aa4389-48a5-44a2-b493-443ddd56c4aa"
        }

        return apicommon.post_req(url, payload, headers)

    #该接口为后台接口，后期即将移除，请不要继续使用，检查某个用户是否已经参与过大屏抽奖
    def luckyDraw_client_hasParticipate(self):
        url = "http://s2-api.smarket.net.cn/luckyDraw/client/hasParticipate"

        payload = "{\r\n  \"tenantId\": \"1116\",\r\n  \"luckyDrawId\": \"2677\",\r\n  \"openId\": \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",\r\n  \"memberId\": \"803868\",\r\n  \"globalUserId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n  \"sess\": \"" + apicommon.bakSess + "\"\r\n}\r\n"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "295b1939-2f14-4ffb-8b9b-8de11ab38faa"
        }

        return apicommon.post_req(url, payload, headers)

    #注册用户接口
    def webinar_open_newRegistration(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/newRegistration"

        #payload = "{\r\n  \"tenantId\": \"1116\",\r\n  \"schemaId\": \"2808\",\r\n  \"instanceId\": \"38369\",\r\n  \"memberFormId\": \"6329\",\r\n  \"url\": \"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/signup.html?memberFormId=6329&configId=246874&memberSchemaId=2808&backUrl=https://f.smarket.net.cn/s/template/39dc846dd6e88089d3990c165e4fad03/view/customForm.html?instanceId=38369&webinarId=6132&customFormId=13283&trackId=2:74&linkId=26812&configId=246966&returnUrl=http%3A%2F%2Ff.smarket.net.cn%2Fs%2Ftemplate%2Fddaae85fe48ff1372217f0db2def1676%2Fhtml%2Fmeeting.html%3FinstanceId%3D38369%26webinarId%3D6132%26customFormId%3D13283%26trackId%3D2%3A74%26linkId%3D26812%26signUpNotify%3Dtrue\",\r\n  \"referenceUrl\": \"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberId=6329&memberFormId=6329&trackId=0&memberSchemaId=2808&configId=246874&backUrl=https://f.smarket.net.cn/s/template/39dc846dd6e88089d3990c165e4fad03/view/customForm.html?instanceId=38369&webinarId=6132&customFormId=13283&trackId=2:74&linkId=26812&configId=246966&returnUrl=http%3A%2F%2Ff.smarket.net.cn%2Fs%2Ftemplate%2Fddaae85fe48ff1372217f0db2def1676%2Fhtml%2Fmeeting.html%3FinstanceId%3D38369%26webinarId%3D6132%26customFormId%3D13283%26trackId%3D2%3A74%26linkId%3D26812%26signUpNotify%3Dtrue\",\r\n  \"token\": \"\",\r\n  \"verify\": \"\",\r\n  \"formData\": [{\r\n    \"fieldName\": \"name\",\r\n    \"value\": \"名\"\r\n  }, {\r\n    \"fieldName\": \"mobile\",\r\n    \"value\": \"13393213133\"\r\n  }, {\r\n    \"fieldName\": \"email\",\r\n    \"value\": \"221530603396434@qq.com\"\r\n  }, {\r\n    \"fieldName\": \"identityNum\",\r\n    \"value\": \"\"\r\n  }, {\r\n    \"fieldName\": \"username\",\r\n    \"value\": \"\"\r\n  }, {\r\n    \"fieldName\": \"avatar\",\r\n    \"value\": {\r\n      \"fileName\": \"\",\r\n      \"mapId\": \"\"\r\n    }\r\n  }, {\r\n    \"fieldName\": \"province\",\r\n    \"value\": [],\r\n    \"otherValue\": \"\"\r\n  }, {\r\n    \"fieldName\": \"password\",\r\n    \"value\": \"EFE6398127928F1B2E9EF3207FB82663\"\r\n  }, {\r\n    \"fieldName\": \"jobNumber\",\r\n    \"value\": \"\"\r\n  }, {\r\n    \"fieldName\": \"enterprise\",\r\n    \"value\": \"\"\r\n  }, {\r\n    \"fieldName\": \"department\",\r\n    \"value\": [],\r\n    \"otherValue\": \"\"\r\n  }, {\r\n    \"fieldName\": \"position\",\r\n    \"value\": [],\r\n    \"otherValue\": \"\"\r\n  }, {\r\n    \"fieldName\": \"gender\",\r\n    \"value\": [],\r\n    \"otherValue\": \"\"\r\n  }, {\r\n    \"fieldName\": \"industry\",\r\n    \"value\": [],\r\n    \"otherValue\": \"\"\r\n  }],\r\n  \"browseInfo\": {\r\n    \"userAgent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36\",\r\n    \"browser\": \"Chrome\",\r\n    \"version\": \"66.0.3359.139\",\r\n    \"os\": \"Windows\",\r\n    \"equipment\": \"电脑端\",\r\n    \"resolution\": \"1536X864\",\r\n    \"referenceUrl\": \"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberId=6329&memberFormId=6329&trackId=0&memberSchemaId=2808&configId=246874&backUrl=https://f.smarket.net.cn/s/template/39dc846dd6e88089d3990c165e4fad03/view/customForm.html?instanceId=38369&webinarId=6132&customFormId=13283&trackId=2:74&linkId=26812&configId=246966&returnUrl=http%3A%2F%2Ff.smarket.net.cn%2Fs%2Ftemplate%2Fddaae85fe48ff1372217f0db2def1676%2Fhtml%2Fmeeting.html%3FinstanceId%3D38369%26webinarId%3D6132%26customFormId%3D13283%26trackId%3D2%3A74%26linkId%3D26812%26signUpNotify%3Dtrue\",\r\n    \"referenceTitle\": \"\",\r\n    \"sess\": \""+apicommon.forntSession+"\"\r\n  },\r\n  \"globalUserId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\"\r\n}"
        payload = {
            "tenantId": "1116",
            "schemaId": "2808",
            "instanceId": "38369",
            "memberFormId": "6329",
            "url": "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/signup.html?memberFormId=6329&configId=246874&memberSchemaId=2808&backUrl=https://f.smarket.net.cn/s/template/39dc846dd6e88089d3990c165e4fad03/view/customForm.html?instanceId=38369&webinarId=6132&customFormId=13283&trackId=2:74&linkId=26812&configId=246966&returnUrl=http%3A%2F%2Ff.smarket.net.cn%2Fs%2Ftemplate%2Fddaae85fe48ff1372217f0db2def1676%2Fhtml%2Fmeeting.html%3FinstanceId%3D38369%26webinarId%3D6132%26customFormId%3D13283%26trackId%3D2%3A74%26linkId%3D26812%26signUpNotify%3Dtrue",
            "referenceUrl": "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberId=6329&memberFormId=6329&trackId=0&memberSchemaId=2808&configId=246874&backUrl=https://f.smarket.net.cn/s/template/39dc846dd6e88089d3990c165e4fad03/view/customForm.html?instanceId=38369&webinarId=6132&customFormId=13283&trackId=2:74&linkId=26812&configId=246966&returnUrl=http%3A%2F%2Ff.smarket.net.cn%2Fs%2Ftemplate%2Fddaae85fe48ff1372217f0db2def1676%2Fhtml%2Fmeeting.html%3FinstanceId%3D38369%26webinarId%3D6132%26customFormId%3D13283%26trackId%3D2%3A74%26linkId%3D26812%26signUpNotify%3Dtrue",
            "token": "",
            "verify": "",
            "formData": [{
                "fieldName": "name",
                "value": "名"
            }, {
                "fieldName": "mobile",
                "value": "13393213133"
            }, {
                "fieldName": "email",
                "value": apicommon.get_mail()
            }, {
                "fieldName": "identityNum",
                "value": ""
            }, {
                "fieldName": "username",
                "value": ""
            }, {
                "fieldName": "avatar",
                "value": {
                    "fileName": "",
                    "mapId": ""
                }
            }, {
                "fieldName": "province",
                "value": [],
                "otherValue": ""
            }, {
                "fieldName": "password",
                "value": "EFE6398127928F1B2E9EF3207FB82663"
            }, {
                "fieldName": "jobNumber",
                "value": ""
            }, {
                "fieldName": "enterprise",
                "value": ""
            }, {
                "fieldName": "department",
                "value": [],
                "otherValue": ""
            }, {
                "fieldName": "position",
                "value": [],
                "otherValue": ""
            }, {
                "fieldName": "gender",
                "value": [],
                "otherValue": ""
            }, {
                "fieldName": "industry",
                "value": [],
                "otherValue": ""
            }],
            "browseInfo": {
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
                "browser": "Chrome",
                "version": "66.0.3359.139",
                "os": "Windows",
                "equipment": "电脑端",
                "resolution": "1536X864",
                "referenceUrl": "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberId=6329&memberFormId=6329&trackId=0&memberSchemaId=2808&configId=246874&backUrl=https://f.smarket.net.cn/s/template/39dc846dd6e88089d3990c165e4fad03/view/customForm.html?instanceId=38369&webinarId=6132&customFormId=13283&trackId=2:74&linkId=26812&configId=246966&returnUrl=http%3A%2F%2Ff.smarket.net.cn%2Fs%2Ftemplate%2Fddaae85fe48ff1372217f0db2def1676%2Fhtml%2Fmeeting.html%3FinstanceId%3D38369%26webinarId%3D6132%26customFormId%3D13283%26trackId%3D2%3A74%26linkId%3D26812%26signUpNotify%3Dtrue",
                "referenceTitle": "",
                "sess": "{{loginSess}}"
            },
            "globalUserId": "39e5bd2a4a1c363d09b9fdd09323b3d8"
        }
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "7b105d92-1bc5-4adc-96e2-68048df7e98a"
        }

        return apicommon.post_req(url, payload, headers)

    #获取直播会议列表（高级查询功能）
    def webinar_open_getWebinarListAdvanced(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/getWebinarListAdvanced"

        payload = "{\r\n    \"tenantId\": \"1116\",\r\n    \"startDate\": \"\",\r\n    \"status\": 3,\r\n    \"keyword\": \"\",\r\n    \"orderby\": \"createTime\",\r\n    \"start\": 0,\r\n    \"num\": 12,\r\n    \"fieldsDisplay\": [\r\n      \"aa\",\r\n      \"numberTest\"\r\n    ],\r\n    \"fieldsCondition\": [\r\n      {\r\n        \"fieldName\": \"numberTest\",\r\n        \"fieldComparison\": \"=\",\r\n         \"fieldValue\": 23,\r\n         \"includeNull\": true\r\n      }\r\n    ],\r\n    \"videoType\": \"1\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }\r\n"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "fd11d1a3-441e-4a33-ba90-85490d385471"
        }

        return apicommon.post_req(url, payload, headers)

    #下载文件互动记录
    def webinar_open_interaction_fileDownLoad(self):
        url = "http://s2-api.smarket.net.cn/open/interaction/fileDownLoad"

        payload = "{\n    \"sess\": \"" + apicommon.forntSession +"\",\n    \"instanceId\":\"38369\",\n    \"fileId\": \"1058036\",\n    \"title\": \"uuu\",\n    \"options\": \"1\",\n    \"_cache_with_cached\": \"1\",\n    \"_cache_refresh\": \"1\",\n    \"_cache_timeout\": \"60\"\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "6b0c54cd-5c57-429a-8b2f-3bf5c7f50064"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        return apicommon.post_req(url, payload, headers)

    #人员参会接口
    def webinar_open_join(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/join"

        payload = 'tenantId=1116&instanceId=38369&joinType=1&cookieId=39e5bd2a4a1c363d09b9fdd09323b3d8&openId=&url=https%3A%2F%2Ff.smarket.net.cn%2Fs%2Ftemplate%2F078f097e0e29d7e56d5ad4a84a085df4%2Fview%2Flogin.html%3FmemberId%3D6329%26memberFormId%3D6329%26trackId%3D0%26memberSchemaId%3D2808%26configId%3D246874%26backUrl%3Dhttps%253A%252F%252Ff.smarket.net.cn%252Fs%252Ftemplate%252F39dc846dd6e88089d3990c165e4fad03%252Fview%252FcustomForm.html%253FinstanceId%253D38369%2526webinarId%253D6132%2526customFormId%253D13283%2526trackId%253D2%253A74%2526linkId%253D26812%2526configId%253D246966%2526returnUrl%253Dhttp%25253A%25252F%25252Ff.smarket.net.cn%25252Fs%25252Ftemplate%25252Fddaae85fe48ff1372217f0db2def1676%25252Fhtml%25252Fmeeting.html%25253FinstanceId%25253D38369%252526webinarId%25253D6132%252526customFormId%25253D13283%252526trackId%25253D2%25253A74%252526linkId%25253D26812%252526signUpNotify%25253Dtrue&globalUserId=39e5bd2a4a1c363d09b9fdd09323b3d8&_cache_with_cached=1&_cache_refresh=1&_cache_timeout=60&sess="+apicommon.forntSession+"'
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            'Postman-Token': "4b5f8b83-0499-43d0-9276-09acc91afa91"
        }

        return apicommon.post_req(url, payload, headers)

    #微论坛帖子详情
    def forum_post_get(self):
        url = "http://s2-api.smarket.net.cn/forum/post/get"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"nodeId\": 1116,\r\n  \"moduleId\": \"1\",\r\n  \"instanceId\": 0,\r\n  \"postId\": 3075,\r\n  \"memberId\": 0,\r\n  \"openId\": \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",\r\n  \"cookieId\": 0,\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "8bad105f-d8f4-4631-8896-e44fc8a755b9"
        }

        return apicommon.post_req(url, payload, headers)

    #微论坛帖子列表
    def forum_stat_homePage(self):
        url = "http://s2-api.smarket.net.cn/forum/stat/homePage"

        payload = "{\r\n  \"status\": 1,\r\n  \"activity\": -1,\r\n  \"sectionId\": 41,\r\n  \"topicId\": 1441,\r\n  \"keyword\": \"\",\r\n  \"orderBy\": 1,\r\n  \"start\": 0,\r\n  \"num\": 10,\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "71f4e18b-6481-4e4f-83ce-c7efccf559fc"
        }

        return apicommon.post_req(url, payload, headers)

    #获取某个微论坛的子版列表
    def forum_section_getList(self):
        url = "http://s2-api.smarket.net.cn/forum/section/getList"

        payload = "{\r\n  \"topicId\": \"1441\",\r\n  \"keyword\": \"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "f952d287-869f-4ee1-a80c-2be8672e6816"
        }

        return apicommon.post_req(url, payload, headers)

    #获取微论坛的回复列表
    def forum_getReplyList(self):
        url = "http://s2-api.smarket.net.cn/forum/getReplyList"

        payload = "{\r\n  \"topicId\": 1441,\r\n  \"openId\": \"\",\r\n  \"cookieId\": \"\",\r\n  \"start\": 0,\r\n  \"num\": 10,\r\n  \"isAll\": 1,\r\n  \"sess\": \"" + apicommon.forntSession + "\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "49c7a101-d011-4aec-8959-f56f31be58f5"
        }

        return apicommon.post_req(url, payload, headers)

    #获取微讨论的主贴ID
    def forum_post_getReplyPost(self):
        url = "http://s2-api.smarket.net.cn/forum/post/getReplyPost"

        payload = "{\r\n  \"postId\": \"5489\",\r\n  \"start\": \"0\",\r\n  \"num\": 10,\r\n  \"cookieId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n  \"openId\": \"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "495f0c1d-96ec-4577-b5eb-c191b0acd81c"
        }

        return apicommon.post_req(url, payload, headers)

    #获取微讨论的主贴列表.可传前端sess,传了sess会帖子信息里面会有发帖人的用户信息，不传sess显示的是匿名用户
    def forum_post_getMainPost(self):
        url = "http://s2-api.smarket.net.cn/forum/post/getMainPost"

        payload = "{\r\n  \"topicId\": \"1441\",\r\n  \"start\": \"0\",\r\n  \"num\": 10,\r\n  \"sectionId\": \"-1\",\r\n  \"cookieId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n  \"openId\": \"\",\r\n  \"orderBy\": 1,\r\n  \"isHot\": -1,\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "00657597-090b-45f6-ac51-34b3c18228cd"
        }

        return apicommon.post_req(url, payload, headers)

    #修改参会人数,并返回登录人的地址
    def webinar_open_attend(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/attend"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"instanceId\": 38369,\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "cffcbdcb-3893-4785-a2a9-d1e741ebd8df"
        }

        return apicommon.post_req(url, payload, headers)

    #微论坛发贴回复
    def forum_post_create(self):
        #20180704
        #import random
        #guid = random.randrange(1000,9999)
        #print guid


        #now = datetime.datetime.now()

        # struct_time = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
#        timestamp = time.mktime(now.timetuple())
        url = "http://s2-api.smarket.net.cn/forum/post/create"

 #       payload = "{\"content\":\"<p>邢英丽发帖1530676235121</p>\",\"postId\":\"\",\"topicId\":\"1441\",\"sess\":\"0fb9b885c79495ed8640d6d823952ba8\",\"sectionId\":\"527\",\"title\":\"邢英丽发帖1530676235121\",\"attachments\":[],\"cookieId\":\"d92774b7-c846-4137-ab1f-2670a104b4bf\",\"browseInfo\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36\",\"browser\":\"Chrome\",\"version\":\"66.0.3359.181\",\"os\":\"Windows\",\"equipment\":\"电脑端\",\"resolution\":\"1366X768\",\"referenceUrl\":\"https://f.smarket.net.cn/s/template/69a1e37d00c97c5cad5fa347e5e3a931/html/index.html?topicId=1441&configId=253066\",\"referenceTitle\":\"\",\"sessionId\":\"ec69f3edd1c9908cb8cfeb1e4528488e\"},\"enableReply\":1,\"isAnonymous\":0,\"signUserId\":\"\",\"globalUserId\":\"7707a485-e50c-419a-9ed4-c91f8e50e8ea\"}"
        payload={"content":apicommon.get_new_phone_no(),"postId":"","topicId":"1441","sess":apicommon.forntSession,"sectionId":"527","title":apicommon.get_new_phone_no(),"attachments":[],"cookieId":apicommon.get_random_str(),"browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","browser":"Chrome","version":"66.0.3359.181","os":"Windows","equipment":"电脑端","resolution":"1366X768","referenceUrl":"https://f.smarket.net.cn/s/template/69a1e37d00c97c5cad5fa347e5e3a931/html/index.html?topicId=1441&configId=253066","referenceTitle":"","sessionId":"ec69f3edd1c9908cb8cfeb1e4528488e"},"enableReply":1,"isAnonymous":0,"signUserId":"","globalUserId":apicommon.get_random_str()}
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "26775e1c-dd27-4212-a38b-c6e5a16b853d"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        return apicommon.post_req(url, payload, headers)

    #微论坛给帖子点赞
    def forum_post_like(self):
        url = "http://s2-api.smarket.net.cn/forum/post/like"
        #20180704
        #payload = "{\"postIds\":[\"5660\"],\"cookieId\":\"a8ebc583-5dd4-4722-9cab-f19fc4ec031b\",\"openId\":\"\",\"sess\":\"0fb9b885c79495ed8640d6d823952ba8\",\"browseInfo\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36\",\"browser\":\"Chrome\",\"version\":\"66.0.3359.181\",\"os\":\"Windows\",\"equipment\":\"电脑端\",\"resolution\":\"1366X768\",\"referenceUrl\":\"https://f.smarket.net.cn/s/template/69a1e37d00c97c5cad5fa347e5e3a931/html/index.html?topicId=1441&configId=253066\",\"referenceTitle\":\"\",\"sessionId\":\"ec69f3edd1c9908cb8cfeb1e4528488e\"},\"globalUserId\":\"1bb11fad-3f8f-4836-b5b6-9e1b18999cf5\"}"
        base_dir = os.path.join(os.path.dirname(__file__), 'tokenfornt.md')
        with open(base_dir, 'r') as f:
            Sesson = f.read()
        print "sesson:", Sesson
        print "get_random_str():",apicommon.get_random_str()
        # payload = {"postIds": apicommon.get_random_str(), "cookieId": "a8ebc583-5dd4-4722-9cab-f19fc4ec031b", "openId": "", "sess": "a29121b5d1c11d8c52a03934507f27b1", "browseInfo": {
        #     "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        #     "browser": "Chrome", "version": "66.0.3359.181", "os": "Windows", "equipment": "电脑端",
        #     "resolution": "1366X768",
        #     "referenceUrl": "https://f.smarket.net.cn/s/template/69a1e37d00c97c5cad5fa347e5e3a931/html/index.html?topicId=1441&configId=253066",
        #     "referenceTitle": "", "sessionId": "ec69f3edd1c9908cb8cfeb1e4528488e"}, "globalUserId": apicommon.get_random_str()}
        # payload = {"postIds": ["1","2"], "cookieId": '375c2553191ce2b52035901300fd4127',
        #            "openId": "", "sess": Sesson, "browseInfo": {
        #         "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        #         "browser": "Chrome", "version": "66.0.3359.181", "os": "Windows", "equipment": "电脑端",
        #         "resolution": "1366X768",
        #         "referenceUrl": "https://f.smarket.net.cn/s/template/69a1e37d00c97c5cad5fa347e5e3a931/html/index.html?topicId=1441&configId=253066",
        #         "referenceTitle": "", "sessionId": "ec69f3edd1c9908cb8cfeb1e4528488e"},
        #            "globalUserId": "0f1e46da5314001cd190fe3301d6cb8f"}  81b70629-465a-41ea-a6da-c8f75fb988bf
        # payload = "{\"postIds\": [\"1\", \"2\"], \"cookieId\": \"85f4c71d-6cef-4cf5-9208-99de76503f3e\",\r\n         \"openId\": \"\", \"sess\": \"375c2553191ce2b52035901300fd4127\",\r\n         \"browseInfo\": {\r\n             \"userAgent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36\",\r\n             \"browser\": \"Chrome\", \"version\": \"66.0.3359.181\", \"os\": \"Windows\", \"equipment\": \"电脑端\",\r\n             \"resolution\": \"1366X768\",\r\n             \"referenceUrl\": \"https://f.smarket.net.cn/s/template/69a1e37d00c97c5cad5fa347e5e3a931/html/index.html?topicId=1441&configId=253066\",\r\n             \"referenceTitle\": \"\", \"sessionId\": \"ec69f3edd1c9908cb8cfeb1e4528488e\"},\r\n         \"globalUserId\": \"81b70629-465a-41ea-a6da-c8f75fb988bf\"}"
        payload = "{\"postIds\": ["+apicommon.get_random_str()+"], \"cookieId\": \""+apicommon.get_random_str()+"\",\r\n         \"openId\": \"\", \"sess\": \""+Sesson+"\",\r\n         \"browseInfo\": {\r\n             \"userAgent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36\",\r\n             \"browser\": \"Chrome\", \"version\": \"66.0.3359.181\", \"os\": \"Windows\", \"equipment\": \"电脑端\",\r\n             \"resolution\": \"1366X768\",\r\n             \"referenceUrl\": \"https://f.smarket.net.cn/s/template/69a1e37d00c97c5cad5fa347e5e3a931/html/index.html?topicId=1441&configId=253066\",\r\n             \"referenceTitle\": \"\", \"sessionId\": \"ec69f3edd1c9908cb8cfeb1e4528488e\"},\r\n         \"globalUserId\": \""+apicommon.get_random_str()+"\"}"
        headers = {
        'Content-Type': "application/json"
        }

        return apicommon.post_req(url, payload, headers)

    #大屏抽奖，用户现场主动参与抽奖，如扫码
    def luckyDraw_client_participate(self):
        url = "http://s2-api.smarket.net.cn/luckyDraw/client/participate"
        #20180704
        #payload = "{\r\n \"tenantId\": 968,\r\n  \"luckyDrawId\": 2700,\r\n  \"openId\": \"oqbfJjlUJYAomlkfZlRGpZAKAVE01530603980671\",\r\n   \"memberId\": 649621,\r\n  \"globalUserId\": \"\",\r\n  \"name\": \"this is a name\",\r\n  \"mobile\": 13303300660,\r\n  \"unique\": \"aa@vv.com\",\r\n  \"sess\": \"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        payload ={
         "tenantId": 968,
          "luckyDrawId": 2700,
          "openId": "oqbfJjlUJYAomlkfZlRGpZAKAVE0"+apicommon.get_date(),
           "memberId": 649621,
          "globalUserId": "",
          "name": "this is a name",
          "mobile": 13303300660,
          "unique": apicommon.get_mail(),
          "sess": "",
          "_cache_with_cached":"1",
          "_cache_refresh":"1",
          "_cache_timeout":"60"
        }
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "1ed2cce5-e95b-4450-b14b-4a9a5521a2e9"
        }

        return apicommon.post_req(url, payload, headers)

    #发表评论
    def comment_create(self):

        url = "http://s2-api.smarket.net.cn/comment/create"

        payload = "{\r\n  \"topicId\": 1442,\r\n  \"tenantId\": 1116,\r\n  \"nodeId\": 1116,\r\n  \"moduleId\": \"0\",\r\n  \"instanceId\": \"\",\r\n  \"isAnonymous\": 0,\r\n  \"content\": \"dd\",\r\n  \"commentId\": 0,\r\n  \"openId\": \"\",\r\n  \"cookieId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n  \"nickname\": \"\",\r\n  \"createrPic\": \"\",\r\n  \"createrLocation\": \"\",\r\n  \"subVersionId\": \"228325\",\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "b0db289a-8c70-4d03-9ab1-383e33562402"
        }

        return apicommon.post_req(url, payload, headers)

    #获取体系字段
    def member_schema_field_GetList(self):
        url = "http://s2-api.smarket.net.cn/member/schema/field/GetList"

        payload = "{\r\n  \"tenantId\": \"1116\",\r\n  \"schemaId\": \"1\",\r\n  \"forForm\": \"0\",\r\n  \"showPassword\": \"0\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "9728dd6f-254d-4828-9f65-c9fee92e7732"
        }

        return apicommon.post_req(url, payload, headers)

    #查询用户是否可以报名接口
    def  webinar_open_checkRegistration(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/checkRegistration"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"instanceId\": 40800,\r\n  \"includeFormData\": true,\r\n  \"cookieId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n  \"openId\": \"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "4e2905b7-b2c1-45cf-b0ae-ec39096a681c"
        }

        return apicommon.post_req(url, payload, headers)

    #20180704添加
    # 获取会场详细信息
    def webinar_open_getWebinarInfo(self):
        url = "http://s2-api.smarket.net.cn/webinar/open/getWebinarInfo"

        payload = "{\r\n    \"instanceId\": 38369,\r\n    \"tenantId\": 1116,\r\n    \"includeCustomField\": 0,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "5d5bb52c-270e-409a-ad57-4d4944bd4aa8"
        }

        return apicommon.post_req(url, payload, headers)

    #获取抽奖详情
    def api_luckydraw_get(self):
        # url = "https://s2-api.smarket.net.cn/api/luckydraw/get"
        #
        # payload = "{\r\n\r\n  \"luckyDrawId\": 2613,\r\n  \"sess\":\""+ apicommon.forntSession +"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n\r\n}"
        # headers = {
        #     'Content-Type': "application/json",
        #     'Cache-Control': "no-cache",
        #     'Postman-Token': "b357340e-ede5-42d6-aa6c-08589c49805e"
        # }
        url = "https://s2-api.smarket.net.cn/api/luckydraw/get"

        payload = "{\r\n        \"tenantId\": 1116,\r\n        \"luckyDrawId\": 2760,\r\n        \"sess\":\"" + apicommon.bakSess + "\"\r\n    }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "f8bb5fa3-cf86-402d-93e7-895f98f81fe3"
        }

        return apicommon.post_req(url, payload, headers) # post接口用这句返回

    #发主帖/回帖
    def api_topic_message_Create(self):
        url = "http://s2-api.smarket.net.cn/api/topic/message/create"

        payload = "{\r\n    \"sess\":null,\r\n    \"topicId\":1510,\r\n    \"tenantId\":1116,\r\n    \"enableReply\":1,\r\n    \"content\":\"12312\",\r\n    \"postId\": 61438,\r\n    \"openId\":\"\",\r\n    \"globalUserId\":\"\",\r\n    \"createrPic\":\"\",\r\n    \"nickname\":\"\",\r\n    \"url\":\"\",\r\n    \"referenceUrl\":\"\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "ffa3d2ea-c875-4530-b824-9106be8dc1dc"
        }
        return apicommon.post_req(url, payload, headers)  # post接口用这句返回

    #根据会议ID获取该会议的渠道追踪代码
    def api_webinar_channel_query(self):
        url = "http://s2-api.smarket.net.cn/api/webinar/channel/query"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"webinarId\": 6132\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "a59d45bb-7c52-438f-bad7-48dcc8d1c812"
        }
        return apicommon.post_req(url, payload, headers)  # post接口用这句返回

    #获取报名人信息/返回报名人状态
    def api_webinar_contacts_get(self):
        url = "https://s2-api.smarket.net.cn/api/webinar/contacts/get"

        payload = "{\r\n    \"tenantId\":1116,\r\n    \"webinarId\":6132,\r\n    \"sess\":\""+ apicommon.forntSession +"\",\r\n    \"globalUserId\":1,\r\n    \"openId\":1,\r\n    \"includeRegisterData\":false\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "68f15789-c045-403e-a468-1d8a0c963537"
        }
        return apicommon.post_req(url, payload, headers)  # post接口用这句返回

    #会议报名
    def api_webinar_contacts_signup(self):
        url = "http://s2-api.smarket.net.cn/api/webinar/contacts/signup"

        payload = "{\r\n    \"sess\":\""+ apicommon.forntSession +"\",\r\n    \"tenantId\":1116,\r\n    \"webinarId\":6496,\r\n    \"formId\":10844,\r\n    \"channel\":\"\",\r\n    \"formData\":[\r\n      {\"fieldName\": \"name\", \"value\": \"eric\"},\r\n      {\"fieldName\": \"mobile\", \"value\": \"13315110180\"},\r\n      {\"fieldName\": \"email\", \"value\": \"eric@sinobasedm.com\"},\r\n      {\"fieldName\": \"enterprise\", \"value\": \"sino\"},\r\n      {\"fieldName\": \"department\", \"value\": [\"财务部\"]},\r\n      {\"fieldName\": \"position\", \"value\": [\"董事长\"]},\r\n      {\"fieldName\": \"industry\", \"value\": [\"服务业\"]}\r\n    ],\r\n    \"url\":\"http://s2-webinar.smarket.net.cn\",\r\n    \"source\":\"PC\",\r\n    \"referenceUrl\":\"http://www.smarket.net.cn\",\r\n    \"globalUserId\":\"2468afe1f112b1e78df1e749252975d8\",\r\n    \"weChatId\":0,\r\n    \"browseInfo\":{}\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "03b6b201-9c36-4239-94e3-102f14931c5b"
        }
        return apicommon.post_req(url, payload, headers)  # post接口用这句返回

    #获取点播信息
    def api_webinar_demand_get(self):
        url = "https://s2-api.smarket.net.cn/api/webinar/demand/get"

        payload = "{\r\n    \"tenantId\":1116,\r\n    \"webinarId\":6417,\r\n    \"includeFormField\":true\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "09bf6dfd-460c-415b-883f-746a13a679a6"
        }
        return apicommon.post_req(url, payload, headers)  # post接口用这句返回



if __name__ == "__main__":
    apicommon.all_login()
    o = ApiRequestsfoureFour()
    #o.webinar_open_getWebinarInfo()
    # o.webinar_open_getCustomFormInfo()
    # o.webinar_open_getWebinarList()
    # o.webinar_open_getApplicantInfo()
    # o.webinar_open_getDemandInfo()
    # o.seminar_contact_front_getContactInfo()
    # o.luckyDraw_get()
    # o.product_crossLine_getList()
    # o.product_getList()
    # o.productLine_getList()
    # o.post_getMainAndReplyList()
    # o.luckyDraw_result_getState()
    # o.post_getListByUser()
    # o.topic_get()
    # o.webinar_open_getAttendList()
    # o.webinar_open_getVideoTimeLine()
    # o.webinar_open_trackingCode_getList()
    # o.post_get()
    # o.post_getReplyPost()
    # o.productLine_field_get()
    # o.productLine_category_getConfigInfo()
    # o.luckyDraw_getAwardDetailList()
    #o.luckyDraw_client_action()
    # o.luckyDraw_client_actionByBigScreen()
    # o.comment_getList()
    # o.member_form_getList()
    # o.luckyDraw_result_getUserResultList()
    # o.product_get()
    # o.webinar_open_registration()
    # o.post_create()
    # o.webinar_event_interaction_check()
    # o.luckyDraw_client_hasParticipate()
    #o.webinar_open_newRegistration()
    # o.webinar_open_getWebinarListAdvanced()
    # o.webinar_open_interaction_fileDownLoad()
    # o.webinar_open_join()
    # o.forum_post_get()
    # o.forum_stat_homePage()
    # o.forum_section_getList()
    # o.forum_getReplyList()
    # o.forum_post_getReplyPost()
    # o.forum_post_getMainPost()
    # o.webinar_open_attend()
    o.api_luckydraw_get()
    # o.api_webinar_contacts_signup()#新api，报错
    # o.comment_create()
    # o.luckyDraw_client_participate()
    # o.member_schema_field_GetList()
    # o.webinar_open_checkRegistration()










