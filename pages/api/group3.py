# -*- coding: utf-8 -*-
# import requests,os
from pages.api import apicommon

"""
刘晓旺开发组
"""

class ApiRequestsThree():

    #获取模板配置
    def template_template_getConfig(self):
        url = "http://s2-api.smarket.net.cn/template/template/getConfig"

        payload = " {\r\n    \"configId\": 48617,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "6c40384f-7a9f-4927-9fda-0d1603db814b"
        }

        return apicommon.post_req(url, payload, headers)


    #做微信签名用，获取jssdk配置
    def weChat_getConfig(self):
        url = "http://s2-api.smarket.net.cn/weChat/getConfig"

        payload = "{\r\n    \"weChatId\": 45830,\r\n    \"jsApiList\": [\r\n      \"stopRecord\",\r\n      \"onVoiceRecordEnd\",\r\n      \"uploadVoice\",\r\n      \"startRecord\"\r\n    ],\r\n    \"url\": \"http://uao.so/907bb3d9ec\",\r\n    \"onDebug\": false\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "e0128a2b-ee9e-485c-9634-46a74f594afa"
        }

        return apicommon.post_req(url, payload, headers)



    # 获取微信信息
    def weChat_getAppId(self):
        url = "http://s2-api.smarket.net.cn/weChat/getAppId"

        payload = "{\r\n    \"weChatId\":\" \"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "975eafb3-26cb-42cf-bfdf-4771b5c5090f"
        }

        return apicommon.post_req(url, payload, headers)

    #获取文件列表
    def file_getList_016(self):
        url = "http://s2-api.smarket.net.cn/file/getList"

        payload = "{\r\n    \"tenantId\": 1116,\r\n    \"moduleType\": \"\",\r\n    \"instanceId\": 478,\r\n    \"folderId\": 1057315,\r\n    \"name\": \"\",\r\n    \"labelname\": \"\",\r\n    \"start\": 0,\r\n    \"num\": 20,\r\n    \"type\": 1,\r\n    \"fileIds\": 1057315,\r\n    \"isShowSys\": 0,\r\n    \"fileTypes\": [],\r\n    \"sortType\": 1,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "ef960d9d-9f0b-4434-ba34-8f493bc71f2b"
        }

        return apicommon.post_req(url, payload, headers)

    #获取文章列表
    def article_getListByProject(self):
        url = "http://s2-api.smarket.net.cn/article/getListByProject"

        payload = "{\r\n    \"tenantId\": 1116,\r\n    \"moduleId\": 1,\r\n    \"instanceId\": 12,\r\n    \"articleCategoryId\": 100080,\r\n    \"title\": \"\",\r\n    \"isRecommend\": -1,\r\n    \"isStick\": -1,\r\n    \"start\": 0,\r\n    \"num\": 20,\r\n    \"withStat\": 1,\r\n    \"withTemplate\": 1,\r\n    \"getAll\": 1,\r\n    \"typeId\": \"\",\r\n    \"searchColumns\": [],\r\n    \"tags\": [],\r\n    \"article\": 1,\r\n    \"categoryId\": 22,\r\n    \"startTime\": \"2015-12-02 16:47:41\",\r\n    \"endTime\": \"2015-12-02 16:47:41\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "9b3d92d7-b159-475e-b47f-355357148580"
        }

        return apicommon.post_req(url, payload, headers)

    #获取文章详情信息
    def article_getDetail(self):
        url = "http://s2-api.smarket.net.cn/article/getDetail"

        payload = " {\r\n    \"withStat\": 0,\r\n    \"articleId\": 102161,\r\n    \"withTemplate\": 1,\r\n    \"isScroll\": 0,\r\n    \"withTag\": 0\r\n   \r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "e420c6c3-c6c1-4474-80c9-9f74ada165a1"
        }

        return apicommon.post_req(url, payload, headers)

    #获取单个栏目
    def articleCategory_get(self):
        url = "http://s2-api.smarket.net.cn/articleCategory/get"

        payload = " {\r\n    \"tenantId\": 1116,\r\n    \"id\": 102161,\r\n    \"withTemplate\": 0\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "a4fc1947-62dc-46e5-a9ed-3747a71c1fcb"
        }

        return apicommon.post_req(url, payload, headers)

    #获取栏目列表
    def articleCategory_getList(self):
        url = "http://s2-api.smarket.net.cn/articleCategory/getList"

        payload = "{\r\n    \"tenantId\": 1116,\r\n    \"moduleId\": \"\",\r\n    \"instanceId\": \"\",\r\n    \"isEnabled\": -1,\r\n    \"articleCategoryId\": 0,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "6924e13f-4c94-42b9-b5c5-31a4e8f41787"
        }

        return apicommon.post_req(url, payload, headers)

    #获取文章分组列表
    def articleCategory_getSubList(self):
        url = "http://s2-api.smarket.net.cn/articleCategory/getSubList"

        payload = " {\r\n    \"articleCategoryId\": 102161,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "83b766ce-d240-44f2-8cb9-d51cbe64fb49"
        }

        return apicommon.post_req(url, payload, headers)

    #通过openId获取联系人信息
    def contact_getByOpenId(self):
        url = "http://s2-api.smarket.net.cn/contact/getByOpenId"

        payload = "{\r\n    \"weChatId\": \"38503\",\r\n    \"openId\": \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",\r\n    \"schemaId\": \"4989\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "e12ec7a8-8181-4fae-9145-51ef3c86b492"
        }

        return apicommon.post_req(url, payload, headers)

    #获取产品线分类树
    def productLine_category_getCategoryTreeList(self):
        url = "http://s2-api.smarket.net.cn/productLine/category/getCategoryTreeList"

        payload = "{\r\n    \"productLineId\": 479,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "d45ed040-bde6-443f-bcf9-adaa326584e7"
        }

        return apicommon.post_req(url, payload, headers)

    #文章浏览
    def article_browse(self):
        url = "http://s2-api.smarket.net.cn/article/browse"

        payload = "{\r\n  \"articleId\": 228325,\r\n  \"globalUserId\": \"\",\r\n  \"openId\": \"\",\r\n  \"url\": \"a\",\r\n  \"referenceUrl\": \"b\",\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"pageTitle\": \"my file title\",\r\n  \"equipment\": \"User Agent\",\r\n  \"weChatId\": \"25491\",\r\n  \"resolution\": \"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "ad8910e6-9e2c-456a-ac4a-eeaa4fbbe833"
        }

        return apicommon.post_req(url, payload, headers)

    #获取微信下的文件列表
    def file_getListForWeChat(self):
        url = "http://s2-api.smarket.net.cn/file/getListForWeChat"

        payload = "{\r\n    \"fileIds\": [\r\n      1058115,\r\n      1003340,\r\n      1003339\r\n    ],\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "2a35b280-f8f9-47aa-8d2d-06a565a4ab6a"
        }

        return apicommon.post_req(url, payload, headers)

    #获取栏目的子栏目中推荐的文章列表
    def article_getRecommendedList(self):
        url = "http://s2-api.smarket.net.cn/article/getRecommendedList"

        payload = " {\r\n    \"articleCategoryId\": 229890,\r\n    \"start\": 0,\r\n    \"num\": 5,\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "a132a4bf-fb4a-4f45-acce-74ad65089332"
        }

        return apicommon.post_req(url, payload, headers)

    #该接口为后台接口，后期即将移除，请不要继续使用，获取微信信息
    def weChat_get(self):

        url = "http://s2-api.smarket.net.cn/weChat/get"

        payload = "{\r\n  \"weChatId\": 38503,\r\n  \"sess\": \""+apicommon.bakSess+"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "a9f3bd5a-0919-4e82-8a09-bfb035601927"
        }

        return apicommon.post_req(url, payload, headers)

    #获取各平台默认微信号的配置信息
    def weChat_getDef(self):
        url = "http://s2-api.smarket.net.cn/weChat/getDef"

        payload = "{\r\n  \r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "f30d8160-b999-4a4d-a2f8-f9b1e041e03e"
        }

        return apicommon.post_req(url, payload, headers)

    #微信的jssdk
    def article_share(self):
        url = "http://s2-api.smarket.net.cn/article/share"

        payload = "{\r\n  \"url\": \"https://f.smarket.net.cn/s/template/69a1e37d00c97c5cad5fa347e5e3a931/html/index.html?topicId=1441&configId=253066\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "4d6e35eb-1e2d-4e38-ac6b-99ac3f399ec5"
        }

        return apicommon.post_req(url, payload, headers)

    #查询openId是否已关注微信号
    def contact_getContactStatus(self):

        url = "http://s2-api.smarket.net.cn/contact/getContactStatus"

        payload = "{\r\n    \"weChatId\": \"104\",\r\n    \"openIds\": [\r\n      \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",\r\n      \"sdfsdgertrtggg\"\r\n    ],\r\n    \"status\": -1,\r\n    \"sess\": \""+apicommon.bakSess+"\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "01feb45f-cb83-4090-8730-524d83d5a373"
        }

        return apicommon.post_req(url, payload, headers)

    #获取此用户是否允许继续点赞,articleId和cookieId是必填字段,openId不传就以cookieId查询用户身份,传openId则cookieId和openId满足其一即可返回此用户的点赞状态
    def article_getLikeStatus(self):

        url = "http://s2-api.smarket.net.cn/article/getLikeStatus"

        payload = "{\r\n    \"articleId\": \"228325\",\r\n    \"globalUserId\": \"\",\r\n    \"openId\": \"\",\r\n    \"sess\": \""+apicommon.bakSess+"\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "ad023819-f26e-432e-b354-3b88a5a2869c"
        }

        return apicommon.post_req(url, payload, headers)

    #点赞，globalUserId、openId和sess至少填一个
    def article_like(self):
        url = "http://s2-api.smarket.net.cn/article/like"

        payload = "{\r\n    \"articleId\": \"228325\",\r\n    \"globalUserId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n    \"openId\": \"\",\r\n    \"url\": \"\",\r\n    \"referenceUrl\": \"\",\r\n    \"sess\": \""+apicommon.forntSession+"\",\r\n    \"weChatId\": \"\",\r\n    \"resolution\": \"\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "3bca6e6b-1cfe-4575-8640-c1255fa13037"
        }

        return apicommon.post_req(url, payload, headers)

    #分享记录，globalUserId、openId和sess至少填一个
    def article_shareRecord(self):
        url = "http://s2-api.smarket.net.cn/article/shareRecord"

        payload = "{\r\n  \"articleId\": 228325,\r\n  \"tick\": \"\",\r\n  \"mediaId\": 12044,\r\n  \"referenceUrl\": \"a\",\r\n  \"url\": \"\",\r\n  \"openId\": \"\",\r\n  \"globalUserId\": \"39e5bd2a4a1c363d09b9fdd09323b3d8\",\r\n  \"sess\": \""+apicommon.forntSession+"\",\r\n  \"weChatId\": \"\",\r\n  \"resolution\": \"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "f3c86748-5c06-419b-9668-ee0f9d724d13"
        }

        return apicommon.post_req(url, payload, headers)

    #文章资料下载
    def file_downloadWithEmail(self):
        url = "http://s2-api.smarket.net.cn/file/downloadWithEmail"
        base_dir = os.path.join(os.path.dirname(__file__), 'tokenfornt.md')
        with open(base_dir, 'r') as f:
            Sessionfront=f.read()
            # 0fb9b885c79495ed8640d6d823952ba8
        payload = "{\r\n    \"articleId\":\"228325\",\r\n    \"openId\":\"\",\r\n    \"globalUserId\":\"e7b0306b56427af5f140adb2a40ee915\",\r\n    \"fileList\":[\r\n        \"1057377\"\r\n    ],\r\n    \"email\":\"782123179@qq.com\",\r\n    \"forEmailTemp\":0,\r\n    \"referenceUrl\":\"https://f.smarket.net.cn/s/template/27bfd3aaa163a0b75e40770732dbbaa3/html/info.html?articleId=228325&configId=246947\",\r\n    \"moduleType\":26,\r\n    \"instanceId\":\"0\",\r\n    \"extra\":{\r\n        \"tenantId\":\"1116\",\r\n        \"instanceId\":\"0\",\r\n        \"memberId\":0,\r\n        \"moduleId\":\"0\",\r\n        \"openId\":\"\",\r\n        \"weChatId\":0,\r\n        \"objInstanceId\":0\r\n    },\r\n    \"browseInfo\":{\r\n        \"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36\",\r\n        \"browser\":\"Chrome\",\r\n        \"version\":\"67.0.3396.79\",\r\n        \"os\":\"Windows\",\r\n        \"equipment\":\"电脑端\",\r\n        \"resolution\":\"1280X720\",\r\n        \"referenceUrl\":\"https://f.smarket.net.cn/s/template/f619f723e83dccccc76a0d20c664b69a/html/list.html?articleCategoryId=102161&configId=246876&pageTitle=%E6%96%87%E7%AB%A0%E9%A2%98%E7%9B%AE__%E6%9C%AC%E5%9C%B0%E6%96%87%E7%AB%A0_%E6%96%87%E7%AB%A0%E7%AE%A1%E7%90%86__Smarket%E6%99%BA%E8%90%A5\",\r\n        \"referenceTitle\":\"\",\r\n        \"sess\": \""+Sessionfront+"\"\r\n    }\r\n}\r\n"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "6ae6674c-9e01-4207-b222-c2ebc07d7825"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        return apicommon.post_req(url, payload, headers)

    #根据文章id数组获取文章列表信息
    def article_getListByIds(self):
        url = "http://s2-api.smarket.net.cn/article/getListByIds"

        payload = "{\r\n  \"articleIds\": [\r\n    102161\r\n  ],\r\n  \"withStat\": 1,\r\n  \"withTemplate\": \"1\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "1f1118f9-ea5e-4bc9-bc9f-b6741559baa9"
        }

        return apicommon.post_req(url, payload, headers)

    #微信账号与会员绑定
    def contact_bindMember(self):
        url = "http://s2-api.smarket.net.cn/contact/bindMember"

        payload = "{\r\n  \"weChatId\": \"38503\",\r\n  \"openId\": \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",\r\n  \"schemaId\": 40,\r\n  \"sess\": \"{{loginSess}}\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "6114e895-8622-49ee-ba19-0edc3438208f"
        }

        return apicommon.post_req(url, payload, headers)

    #创建邮件发送任务
    def contact_bindMember(self):

        url = "http://s2-api.smarket.net.cn/contact/bindMember"

        payload = "{\r\n  \"weChatId\": \"38503\",\r\n  \"openId\": \"otqO01CM74B9qQ2ZFwGiglaZFxzg\",\r\n  \"schemaId\": 40,\r\n  \"sess\": \""+apicommon.forntSession+"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "9deae7e4-1daa-459b-b120-07d9cfd817f3"
        }

        return apicommon.post_req(url, payload, headers)

    #查询文章列表
    def article_getTrees(self):
        url = "http://s2-api.smarket.net.cn/article/getTrees"

        payload = "{   \r\n    \"sess\":\""+apicommon.bakSess+"\",\r\n    \"tenantId\": \"1116\",\r\n    \"moduleId\": \"1\",\r\n    \"instanceId\": \"38503\",\r\n    \"articleCategoryId\": \"102195\",\r\n    \"startTime\": \"2018-03-09\",\r\n    \"endTime\": \"2018-06-20\",\r\n    \"start\": 0,\r\n    \"num\": 20,\r\n    \"typeId\": \"2\",\r\n    \"_cache_with_cached\": \"1\",\r\n    \"_cache_refresh\": \"1\",\r\n    \"_cache_timeout\": \"60\"\r\n  }"
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "be08b32e-383c-46d8-912c-5c06ef324575"
        }

        return apicommon.post_req(url, payload, headers)

    def file_getList(self):
        url = "http://s2-api.smarket.net.cn/file/getList"

        payload = {
            "tenantId": 1116,
            "moduleType": "",
            "instanceId": 478,
            "folderId": 1057315,
            "name": "",
            "labelname": "",
            "start": 0,
            "num": 20,
            "type": 1,
            "fileIds": 1057315,
            "isShowSys": 0,
            "fileTypes": [],
            "sortType": 1,
            "_cache_with_cached": "1",
            "_cache_refresh": "1",
            "_cache_timeout": "60"
          }
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "be08b32e-383c-46d8-912c-5c06ef324575"
        }

        return apicommon.post_req(url, payload, headers)

    #中转接口发送邮件
    def edm_sendEmail(self):
        #20180704
        # 1、url = "http://projectsapi.smarket.net.cn/beisensignsmarketapi"错误
        #2、headers定义的类型是"application/x-www-form-urlencoded"，那么提交Json他也不会处理的。所以payload没有用处
        url = "http://projectsapi.smarket.net.cn/beisensignsmarketapi?smkproxyurl=http%3A%2F%2FS2-oldapi.smarket.net.cn%2Fedm%2FsendEmail"
        payload1 = {
            "tenantId": 1116,
            "moduleType": "",
            "instanceId": 478,
            "folderId": 1057315,
            "name": "",
            "labelname": "",
            "start": 0,
            "num": 20,
            "type": 1,
            "fileIds": 1057315,
            "isShowSys": 0,
            "fileTypes": [],
            "sortType": 1,
            "_cache_with_cached": "1",
            "_cache_refresh": "1",
            "_cache_timeout": "60"
        }
        payload= {'content' :'%E6%82%A8%E5%A5%BD%EF%BC%81%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80%E5%A6%82%E4%B8%8B%3Cbr%2F%3Ehttp%3A%2F%2Fuatcontent.wechat.smarket.net.cn%2Findex.php%3FmappingId%3D65412a1678c326edb74e31a88abddaf9%26type%3Ddownload%3Cbr%2F%3E',
        'subject':'会议资料下载',
                       'toEmails':'765233482@qq.com'}
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
        }
        return apicommon.post_req(url, payload, headers)

    #项目使用，获取栏目列表/
    def api_article_category_query(self):
        url = "http://s2-api.smarket.net.cn/api/article/category/query"

        payload = "{\n        \"tenantId\":1116,\n        \"articleCategoryId\": \"\",\n        \"instanceId\": \"\",\n        \"isEnabled\": \"0\",\n        \"start\": 0,\n        \"num\": 20\n    }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "0eedb1b2-612a-47f2-924b-0fedf4f71322"
        }
        return apicommon.post_req(url, payload, headers)# post接口用这句返回

    #获取文章列表
    def api_article_query(self):
        url = "http://s2-api.smarket.net.cn/api/article/query"

        payload = "{\r\n        \"tenantId\":\"1116\",\r\n        \"instanceId\": \"\",\r\n        \"articleIds\":\"\",\r\n        \"typeIds\": \"\",\r\n        \"articleCategoryId\": \"\",\r\n        \"title\": \"\",\r\n        \"summary\": \"\",\r\n        \"isRecommend\": \"\",\r\n        \"hasChildrenCategory\": \"\",\r\n        \"isTop\": \"\",\r\n        \"isWithStat\": \"\",\r\n        \"sort\": [1],\r\n        \"tags\": \"\",\r\n        \"start\": 0,\r\n        \"num\": 50\r\n    }"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "5a4198fa-13bf-45cb-a249-07e65e74a338"
        }
        return apicommon.post_req(url, payload, headers)  # post接口用这句返回

    #查询我收藏的信息
    def api_content_collect_query(self):
        url = "http://s2-api.smarket.net.cn/api/content/collect/query"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"sess\": \"" + apicommon.bakSess + "\",\r\n  \"start\": 1,\r\n  \"num\": 50,\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "f8335875-10f6-4d12-8e35-6149f6a930e1"
        }

        return apicommon.post_req(url, payload, headers)  # post接口用这句返回

    #查询文件列表（带分页）
    def api_file_query(self):
        url = "http://s2-api.smarket.net.cn/api/file/query"

        payload = "{    \r\n        \"tenantId\":1116,\r\n        \"folderId\": 1061327,\r\n        \"instanceId\": \"\",\r\n        \"keyword\": \"Email\",\r\n        \"fileIds\": [1061328,1061329,1061330],\r\n        \"fileType\": [\"xls/xlsx\"],\r\n        \"isFolder\": \"\",\r\n        \"sort\": [1],\r\n        \"start\": \"0\",\r\n        \"num\": \"10\"\r\n    \r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "5b61099a-d584-44eb-9c93-cce84131dd7f"
        }
        return apicommon.post_req(url, payload, headers)  # post接口用这句返回

    #获取租户下产品线列表
    def api_productLine_query(self):
        # url = "http://s2-api.smarket.net.cn/api/productline/query"
        #
        # payload = "{\r\n  \"tenantId\": 1116,\r\n  \"withDeleted\": 1,\r\n  \"num\": 10,\r\n  \"start\": 0,\r\n  \"sess\":\""+ apicommon.forntSession +"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n}"
        # headers = {
        #     'Content-Type': "application/json",
        #     'Cache-Control': "no-cache",
        #     'Postman-Token': "cb86f375-7abe-4dfd-94db-1104b5a1504a"
        # }

        url = "http://s2-api.smarket.net.cn/api/productline/query"

        payload = "{\r\n    \"tenantId\": 1116,\r\n    \"withDeleted\": 0,\r\n    \"num\": 10,\r\n    \"start\": 0\r\n}"
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "b88ed54b-48f2-46ac-af3c-05f06b788889"
        }
        return apicommon.post_req(url, payload, headers)  # post接口用这句返回

    #获取产品线下产品列表
    def api_product_query(self):
        url = "https://s2-api.smarket.net.cn/api/product/query"

        payload = "{\r\n  \"tenantId\": 1116,\r\n  \"productIds\": [867,907],\r\n  \"productLineId\": 491,\r\n  \"keyword\": \"\",\r\n  \"start\": 0,\r\n  \"num\": 10,\r\n  \"isNew\": 0,\r\n  \"categoryId\": 0,\r\n  \"withSoldOut\": 0,\r\n  \"sort\": 1,\r\n  \"isTop\": 0,\r\n  \"conditions\": {\r\n    \"checkbox_1\": [\r\n\r\n      1,\r\n\r\n      2\r\n\r\n    ],\r\n\r\n    \"radio_1\": 1\r\n\r\n  },\r\n \"sess\":\""+apicommon.forntSession +"\",\r\n  \"_cache_with_cached\":\"1\",\r\n  \"_cache_refresh\":\"1\",\r\n  \"_cache_timeout\":\"60\"\r\n\r\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "8e45543d-44d9-4285-aaeb-adc55aa9f825"
        }
        return apicommon.post_req(url, payload, headers)  # post接口用这句返回
if __name__ == "__main__":
    apicommon.all_login()
    o = ApiRequestsThree()
    # o.template_template_getConfig()
    o.api_product_query()
    # o.weChat_getAppId()
    # o.file_getList_016()
    # o.article_getListByProject()
    # o.article_getDetail()
    # o.articleCategory_get()
    # o.articleCategory_getList()
    # o.articleCategory_getSubList()
    # o.contact_getByOpenId()
    # o.productLine_category_getCategoryTreeList()
    # o.article_browse()
    #o.file_getListForWeChat()
    # o.article_getRecommendedList()
    # o.weChat_get()
    # o.weChat_getDef()
    # o.article_share()
    # o.contact_getContactStatus()
    # o.article_getLikeStatus()
    # o.article_like()
    # o.article_shareRecord()
    # o.file_downloadWithEmail()
    # o.article_getListByIds()
    # o.article_getTrees()
    o.api_productLine_query()

    # o.edm_sendEmail()
    #o.file_getList()
































