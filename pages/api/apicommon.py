# -*- coding: utf-8 -*-
# import requests
import time
import random
import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#定义全局变量
#前台登陆的session
global forntSession
#后台管理登陆的session
global bakSess
#时间
global timestampHeader
import requests
from pages.api.api_quester_common import api_quester_common
# 获取bakSess
def get_bakSess(url,email,password,Identifi_field,platform_name):

    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0100&command%5Btype%5D=2&command%5Bcmd%5D=account.login&command%5Bsess%5D=&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5Bemail%5D="+email+"&command%5Bbody%5D%5Bpassword%5D="+password+"&command%5Bbody%5D%5BclientType%5D=1&command%5Bbody%5D%5BclientBrand%5D=Netscape&command%5Bbody%5D%5BclientVersion%5D=5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F71.0.3578.98%20Safari%2F537.36"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "5e28ab0e-c5e5-6adc-42dd-be62c76a5874"
    }
    return api_quester_common().post_request_bigScree("POST",url,payload,headers,Identifi_field,platform_name,"session")
# 获取loginSess
def get_loginSess(url,tenantId,schemaId,memberFormId,memberSchemaId,unique,password,Identifi_field,platform_name):
    # print "payload:",payload
    # payload = "{\"tenantId\":\""+tenantId+"\",\"schemaId\":\"482\",\"memberFormId\":\"873\",\"memberSchemaId\":\"482\",\"unique\":\"15960167982\",\"token\":\"\",\"password\":\"4297F44B13955235245B2497399D7A93\",\"checkCode\":\"\",\"loginType\":\"\",\"url\":\"https://hwyhw.smarket.net.cn/f/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberId=873&memberFormId=873&trackId=0&memberSchemaId=482&configId=37066&weChatId=9418&backUrl=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ff%2Fa4193c73ac8d7e3b81b384bea132c40a%2Fhtml%2FEventDetail.html%3FinstanceId%3D9445\",\"browseInfo\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36\",\"browser\":\"Chrome\",\"version\":\"71.0.3578.98\",\"os\":\"Windows\",\"equipment\":\"电脑端\",\"resolution\":\"1920X1080\",\"referenceUrl\":\"https://hwyhw.smarket.net.cn/f/a4193c73ac8d7e3b81b384bea132c40a/html/EventDetail.html?instanceId=9445\",\"referenceTitle\":\"\",\"sessionId\":\"7fa15a6f75e585ed7544c6953f555543\"},\"globalUserId\":\"1bf522f38f2e647bd6b46a4527b509df\"}"
    # payload = '{"tenantId":"547","schemaId":"482","memberFormId":"873","memberSchemaId":"482","unique":"15960167982","token":"","password":"4297F44B13955235245B2497399D7A93","checkCode":"","loginType":"","url":"https://hwyhw.smarket.net.cn/f/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberId=873&memberFormId=873&trackId=0&memberSchemaId=482&configId=37066&weChatId=9418&backUrl=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ff%2Fa4193c73ac8d7e3b81b384bea132c40a%2Fhtml%2FEventDetail.html%3FinstanceId%3D9445","browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36","browser":"Chrome","version":"71.0.3578.98","os":"Windows","equipment":"电脑端","resolution":"1920X1080","referenceUrl":"https://hwyhw.smarket.net.cn/f/a4193c73ac8d7e3b81b384bea132c40a/html/EventDetail.html?instanceId=9445","referenceTitle":"","sessionId":"7fa15a6f75e585ed7544c6953f555543"},"globalUserId":"1bf522f38f2e647bd6b46a4527b509df"}'
    # print "payload:",payload
    # 字典
    payload = {}
    payload["tenantId"] = tenantId
    payload["schemaId"] = schemaId
    payload["memberFormId"] = memberFormId
    payload["memberSchemaId"] = memberSchemaId
    payload["unique"] = unique
    payload["password"] = password
    payload["checkCode"] = ""
    payload["loginType"] = ""
    payload["url"] = "https://hwyhw.smarket.net.cn/f/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberId=873&memberFormId=873&trackId=0&memberSchemaId=482&configId=37066&weChatId=9418&backUrl=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ff%2Fa4193c73ac8d7e3b81b384bea132c40a%2Fhtml%2FEventDetail.html%3FinstanceId%3D9445"
    payload["browseInfo"] = {"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36","browser":"Chrome","version":"71.0.3578.98","os":"Windows","equipment":"电脑端","resolution":"1920X1080","referenceUrl":"https://hwyhw.smarket.net.cn/f/a4193c73ac8d7e3b81b384bea132c40a/html/EventDetail.html?instanceId=9445","referenceTitle":"","sessionId":"7fa15a6f75e585ed7544c6953f555543"}
    payload["globalUserId"] = "1bf522f38f2e647bd6b46a4527b509df"
    print "payload:",payload
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "a4c630f5-0612-0e08-a914-9e8e8ad37d07"
    }
    return api_quester_common().post_request_seminarId("POST", url, payload, headers,Identifi_field,platform_name,"session","memberId")
# 获取global_topicId
def get_global_topicId(type,url,tenantId,nodeId,bakSess,Identifi_field):
    print "bakSess;",bakSess
    payload = "command%5Bsize%5D=0&command%5Bsess%5D="+bakSess+"&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=topic.create&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BnodeId%5D="+nodeId+"&command%5Bbody%5D%5BmoduleId%5D=0&command%5Bbody%5D%5BinstanceId%5D=0&command%5Bbody%5D%5BschemaId%5D=0&command%5Bbody%5D%5Btype%5D=2&command%5Bbody%5D%5Btitle%5D=%E5%BE%AE%E8%AE%A8%E8%AE%BAid%E6%8E%A5%E5%8F%A31547713980&command%5Bbody%5D%5BpostIdentity%5D=1&command%5Bbody%5D%5BpostIdentityExtra%5D=0&command%5Bbody%5D%5BtrackId%5D=0&command%5Bbody%5D%5BreplyIdentity%5D=1&command%5Bbody%5D%5BenableCheck%5D=0&command%5Bbody%5D%5BenableLike%5D=1&command%5Bbody%5D%5BenableDelete%5D=1&command%5Bbody%5D%5BenableAttachment%5D=1"
    print "payload:",payload
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "e757a272-a660-d7fe-ab45-e4faf2b9c031"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers,Identifi_field,type,"content")
# 获取微讨论topicId
def get_topicId(type,url,tenantId,nodeId,bakSess,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Bsess%5D="+bakSess+"&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=topic.create&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BnodeId%5D="+nodeId+"&command%5Bbody%5D%5BmoduleId%5D=0&command%5Bbody%5D%5BinstanceId%5D=0&command%5Bbody%5D%5BschemaId%5D=0&command%5Bbody%5D%5Btype%5D=2&command%5Bbody%5D%5Btitle%5D=1"+createTime+"&command%5Bbody%5D%5BpostIdentity%5D=1&command%5Bbody%5D%5BpostIdentityExtra%5D=0&command%5Bbody%5D%5BtrackId%5D=0&command%5Bbody%5D%5BreplyIdentity%5D=1&command%5Bbody%5D%5BenableCheck%5D=0&command%5Bbody%5D%5BenableLike%5D=1&command%5Bbody%5D%5BenableDelete%5D=1&command%5Bbody%5D%5BenableAttachment%5D=1"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "672e95e2-81a7-4757-d8b1-42441e32decb"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"content")
# 获取微讨论子版id
def get_sectionId(type,url,tenantId,nodeId,bakSess,Identifi_field,global_topicId):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bcmd%5D=forum.section.create&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BnodeId%5D="+nodeId+"&command%5Bbody%5D%5BmoduleId%5D=&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BtopicId%5D="+global_topicId+"&command%5Bbody%5D%5BsectionName%5D=%E5%AD%90%E7%89%88id"
    print "payload:",payload
    print "url:",url
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "853b81b9-12c3-f609-971d-7267d568f658"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"content")
# 获取线下会的seminarId和instanceId
def get_seminarId(type,url,tenantId,bakSess,Identifi_field,memberFormId,memberFormName):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=seminar.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5Bname%5D=%E6%B5%8B%E8%AF%95%E4%BC%9A%E8%AE%AE2"+createTime+"&command%5Bbody%5D%5BtargetRegisterCount%5D=&command%5Bbody%5D%5BtargetParticipantCount%5D=&command%5Bbody%5D%5BstartTime%5D=1548118800&command%5Bbody%5D%5BendTime%5D=1863682338&command%5Bbody%5D%5Bregion%5D%5Bcity%5D=%E5%8C%97%E4%BA%AC&command%5Bbody%5D%5Bregion%5D%5BcityId%5D=110100&command%5Bbody%5D%5Bregion%5D%5Bcountry%5D=%E4%B8%AD%E5%9B%BD&command%5Bbody%5D%5Bregion%5D%5BcountryId%5D=0&command%5Bbody%5D%5Bregion%5D%5Bprovince%5D=%E5%8C%97%E4%BA%AC&command%5Bbody%5D%5Bregion%5D%5BprovinceId%5D=110000&command%5Bbody%5D%5Baddress%5D=%E5%8C%97%E4%BA%AC&command%5Bbody%5D%5BweChatType%5D=custom&command%5Bbody%5D%5BweChatId%5D=9418&command%5Bbody%5D%5BsceneName%5D=business&command%5Bbody%5D%5BopenMember%5D=1&command%5Bbody%5D%5BmemberFormId%5D="+memberFormId+"&command%5Bbody%5D%5BmemberFormName%5D=%E9%BB%98%E8%AE%A4%E6%B3%A8%E5%86%8C%E8%A1%A8%E5%8D%95&command%5Bbody%5D%5BmemberTrackId%5D=0&command%5Bbody%5D%5Bintroduction%5D=&command%5Bbody%5D%5Bmodules%5D%5B0%5D%5Bname%5D=inviterManage&command%5Bbody%5D%5Bmodules%5D%5B0%5D%5BdisplayName%5D=%E4%BC%9A%E8%AE%AE%E9%82%80%E8%AF%B7&command%5Bbody%5D%5Bmodules%5D%5B0%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B0%5D%5BisSub%5D=1&command%5Bbody%5D%5Bmodules%5D%5B0%5D%5Border%5D=0.5&command%5Bbody%5D%5Bmodules%5D%5B0%5D%5Bicon%5D=inviterManage&command%5Bbody%5D%5Bmodules%5D%5B0%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B1%5D%5Bname%5D=guest&command%5Bbody%5D%5Bmodules%5D%5B1%5D%5BdisplayName%5D=%E5%8F%82%E4%BC%9A%E5%98%89%E5%AE%BE&command%5Bbody%5D%5Bmodules%5D%5B1%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B1%5D%5BisSub%5D=1&command%5Bbody%5D%5Bmodules%5D%5B1%5D%5Border%5D=1&command%5Bbody%5D%5Bmodules%5D%5B1%5D%5Bicon%5D=guest&command%5Bbody%5D%5Bmodules%5D%5B1%5D%5BisEnable%5D=1&command%5Bbody%5D%5Bmodules%5D%5B2%5D%5Bname%5D=agenda&command%5Bbody%5D%5Bmodules%5D%5B2%5D%5BdisplayName%5D=%E4%BC%9A%E8%AE%AE%E6%97%A5%E7%A8%8B&command%5Bbody%5D%5Bmodules%5D%5B2%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B2%5D%5BisSub%5D=1&command%5Bbody%5D%5Bmodules%5D%5B2%5D%5Bicon%5D=agenda&command%5Bbody%5D%5Bmodules%5D%5B2%5D%5Border%5D=2&command%5Bbody%5D%5Bmodules%5D%5B2%5D%5BisEnable%5D=1&command%5Bbody%5D%5Bmodules%5D%5B3%5D%5Bname%5D=registration&command%5Bbody%5D%5Bmodules%5D%5B3%5D%5BdisplayName%5D=%E6%8A%A5%E5%90%8D%E8%A1%A8%E5%8D%95&command%5Bbody%5D%5Bmodules%5D%5B3%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B3%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B3%5D%5Bicon%5D=registform&command%5Bbody%5D%5Bmodules%5D%5B3%5D%5Border%5D=2.5&command%5Bbody%5D%5Bmodules%5D%5B3%5D%5BisEnable%5D=1&command%5Bbody%5D%5Bmodules%5D%5B4%5D%5Bname%5D=trackingCode&command%5Bbody%5D%5Bmodules%5D%5B4%5D%5BdisplayName%5D=%E6%B8%A0%E9%81%93%E8%BF%BD%E8%B8%AA%E4%BB%A3%E7%A0%81&command%5Bbody%5D%5Bmodules%5D%5B4%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B4%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B4%5D%5Bicon%5D=invert&command%5Bbody%5D%5Bmodules%5D%5B4%5D%5Border%5D=3&command%5Bbody%5D%5Bmodules%5D%5B4%5D%5BisEnable%5D=1&command%5Bbody%5D%5Bmodules%5D%5B5%5D%5Bname%5D=signingPoint&command%5Bbody%5D%5Bmodules%5D%5B5%5D%5BdisplayName%5D=%E7%AD%BE%E5%88%B0%E7%82%B9&command%5Bbody%5D%5Bmodules%5D%5B5%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B5%5D%5BisSub%5D=1&command%5Bbody%5D%5Bmodules%5D%5B5%5D%5Bicon%5D=signin&command%5Bbody%5D%5Bmodules%5D%5B5%5D%5Border%5D=4&command%5Bbody%5D%5Bmodules%5D%5B5%5D%5BisEnable%5D=1&command%5Bbody%5D%5Bmodules%5D%5B6%5D%5Bname%5D=interaction&command%5Bbody%5D%5Bmodules%5D%5B6%5D%5BdisplayName%5D=%E4%BA%92%E5%8A%A8%E7%8E%AF%E8%8A%82&command%5Bbody%5D%5Bmodules%5D%5B6%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B6%5D%5BisSub%5D=1&command%5Bbody%5D%5Bmodules%5D%5B6%5D%5Bicon%5D=interact&command%5Bbody%5D%5Bmodules%5D%5B6%5D%5Border%5D=7&command%5Bbody%5D%5Bmodules%5D%5B6%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B7%5D%5Bname%5D=bigScreenManage&command%5Bbody%5D%5Bmodules%5D%5B7%5D%5BdisplayName%5D=%E5%A4%A7%E5%B1%8F%E7%AE%A1%E7%90%86&command%5Bbody%5D%5Bmodules%5D%5B7%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B7%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B7%5D%5Bicon%5D=screen&command%5Bbody%5D%5Bmodules%5D%5B7%5D%5Border%5D=7.1&command%5Bbody%5D%5Bmodules%5D%5B7%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B8%5D%5Bname%5D=rights&command%5Bbody%5D%5Bmodules%5D%5B8%5D%5BdisplayName%5D=%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%86&command%5Bbody%5D%5Bmodules%5D%5B8%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B8%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B8%5D%5Bicon%5D=rights&command%5Bbody%5D%5Bmodules%5D%5B8%5D%5Border%5D=7.2&command%5Bbody%5D%5Bmodules%5D%5B8%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B9%5D%5Bname%5D=subSeminar&command%5Bbody%5D%5Bmodules%5D%5B9%5D%5BdisplayName%5D=%E5%88%86%E4%BC%9A%E5%9C%BA&command%5Bbody%5D%5Bmodules%5D%5B9%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B9%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B9%5D%5Bicon%5D=subEvent&command%5Bbody%5D%5Bmodules%5D%5B9%5D%5Border%5D=7.5&command%5Bbody%5D%5Bmodules%5D%5B9%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B10%5D%5Bname%5D=edm&command%5Bbody%5D%5Bmodules%5D%5B10%5D%5BdisplayName%5D=%E9%82%AE%E4%BB%B6%E4%BB%BB%E5%8A%A1&command%5Bbody%5D%5Bmodules%5D%5B10%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B10%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B10%5D%5Bicon%5D=edm&command%5Bbody%5D%5Bmodules%5D%5B10%5D%5Border%5D=7.6&command%5Bbody%5D%5Bmodules%5D%5B10%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B11%5D%5Bname%5D=sms&command%5Bbody%5D%5Bmodules%5D%5B11%5D%5BdisplayName%5D=%E7%9F%AD%E4%BF%A1%E4%BB%BB%E5%8A%A1&command%5Bbody%5D%5Bmodules%5D%5B11%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B11%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B11%5D%5Bicon%5D=sms&command%5Bbody%5D%5Bmodules%5D%5B11%5D%5Border%5D=7.7&command%5Bbody%5D%5Bmodules%5D%5B11%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B12%5D%5Bname%5D=material&command%5Bbody%5D%5Bmodules%5D%5B12%5D%5BdisplayName%5D=%E7%B4%A0%E6%9D%90%E5%BA%93&command%5Bbody%5D%5Bmodules%5D%5B12%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B12%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B12%5D%5Bicon%5D=source&command%5Bbody%5D%5Bmodules%5D%5B12%5D%5Border%5D=8&command%5Bbody%5D%5Bmodules%5D%5B12%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B13%5D%5Bname%5D=appMonitor&command%5Bbody%5D%5Bmodules%5D%5B13%5D%5BdisplayName%5D=%E7%AD%BE%E5%88%B0%E8%AE%BE%E5%A4%87%E7%9B%91%E6%8E%A7&command%5Bbody%5D%5Bmodules%5D%5B13%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B13%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B13%5D%5Bicon%5D=appmonitor&command%5Bbody%5D%5Bmodules%5D%5B13%5D%5Border%5D=8.3&command%5Bbody%5D%5Bmodules%5D%5B13%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B14%5D%5Bname%5D=article&command%5Bbody%5D%5Bmodules%5D%5B14%5D%5BdisplayName%5D=%E6%96%87%E7%AB%A0&command%5Bbody%5D%5Bmodules%5D%5B14%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B14%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B14%5D%5Bicon%5D=article&command%5Bbody%5D%5Bmodules%5D%5B14%5D%5Border%5D=9&command%5Bbody%5D%5Bmodules%5D%5B14%5D%5BisEnable%5D=0&command%5Bbody%5D%5BweChatQrCodeUrl%5D=http%3A%2F%2Fhwyhw.smarket.net.cn%2Fcontent%2Findex.php%3FmappingId%3Df7d8e440a75469d6b0ca009caf33c09b&command%5Bbody%5D%5BtopicId%5D=&command%5Bbody%5D%5BwapTopicId%5D=&command%5Bbody%5D%5BinviteId%5D=&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    print "payload:",payload
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "f3f572e3-8e78-43db-3d04-5734587124e5"
    }
    return api_quester_common().post_request_seminarId("POST", url, payload, headers, Identifi_field, type,"seminarId","instanceId")
 # 获取线下会的开启大屏管理模块
def seminarId_setModule(type,url,tenantId,bakSess,Identifi_field,seminarId):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=seminar.setModule&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BseminarId%5D="+seminarId+"&command%5Bbody%5D%5Bmodules%5D%5B0%5D%5Bname%5D=inviterManage&command%5Bbody%5D%5Bmodules%5D%5B0%5D%5BdisplayName%5D=%E4%BC%9A%E8%AE%AE%E9%82%80%E8%AF%B7&command%5Bbody%5D%5Bmodules%5D%5B0%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B0%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B0%5D%5Border%5D=101&command%5Bbody%5D%5Bmodules%5D%5B0%5D%5Bicon%5D=eventinvite&command%5Bbody%5D%5Bmodules%5D%5B0%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B1%5D%5Bname%5D=guest&command%5Bbody%5D%5Bmodules%5D%5B1%5D%5BdisplayName%5D=%E5%8F%82%E4%BC%9A%E5%98%89%E5%AE%BE&command%5Bbody%5D%5Bmodules%5D%5B1%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B1%5D%5BisSub%5D=1&command%5Bbody%5D%5Bmodules%5D%5B1%5D%5Border%5D=102&command%5Bbody%5D%5Bmodules%5D%5B1%5D%5Bicon%5D=guest&command%5Bbody%5D%5Bmodules%5D%5B1%5D%5BisEnable%5D=1&command%5Bbody%5D%5Bmodules%5D%5B2%5D%5Bname%5D=agenda&command%5Bbody%5D%5Bmodules%5D%5B2%5D%5BdisplayName%5D=%E4%BC%9A%E8%AE%AE%E6%97%A5%E7%A8%8B&command%5Bbody%5D%5Bmodules%5D%5B2%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B2%5D%5BisSub%5D=1&command%5Bbody%5D%5Bmodules%5D%5B2%5D%5Border%5D=103&command%5Bbody%5D%5Bmodules%5D%5B2%5D%5Bicon%5D=agenda&command%5Bbody%5D%5Bmodules%5D%5B2%5D%5BisEnable%5D=1&command%5Bbody%5D%5Bmodules%5D%5B3%5D%5Bname%5D=registration&command%5Bbody%5D%5Bmodules%5D%5B3%5D%5BdisplayName%5D=%E6%8A%A5%E5%90%8D%E8%A1%A8%E5%8D%95&command%5Bbody%5D%5Bmodules%5D%5B3%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B3%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B3%5D%5Border%5D=104&command%5Bbody%5D%5Bmodules%5D%5B3%5D%5Bicon%5D=registform&command%5Bbody%5D%5Bmodules%5D%5B3%5D%5BisEnable%5D=1&command%5Bbody%5D%5Bmodules%5D%5B4%5D%5Bname%5D=trackingCode&command%5Bbody%5D%5Bmodules%5D%5B4%5D%5BdisplayName%5D=%E6%B8%A0%E9%81%93%E8%BF%BD%E8%B8%AA%E4%BB%A3%E7%A0%81&command%5Bbody%5D%5Bmodules%5D%5B4%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B4%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B4%5D%5Border%5D=105&command%5Bbody%5D%5Bmodules%5D%5B4%5D%5Bicon%5D=invert&command%5Bbody%5D%5Bmodules%5D%5B4%5D%5BisEnable%5D=1&command%5Bbody%5D%5Bmodules%5D%5B5%5D%5Bname%5D=signingPoint&command%5Bbody%5D%5Bmodules%5D%5B5%5D%5BdisplayName%5D=%E7%AD%BE%E5%88%B0%E7%82%B9&command%5Bbody%5D%5Bmodules%5D%5B5%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B5%5D%5BisSub%5D=1&command%5Bbody%5D%5Bmodules%5D%5B5%5D%5Border%5D=106&command%5Bbody%5D%5Bmodules%5D%5B5%5D%5Bicon%5D=signin&command%5Bbody%5D%5Bmodules%5D%5B5%5D%5BisEnable%5D=1&command%5Bbody%5D%5Bmodules%5D%5B6%5D%5Bname%5D=interaction&command%5Bbody%5D%5Bmodules%5D%5B6%5D%5BdisplayName%5D=%E4%BA%92%E5%8A%A8%E7%8E%AF%E8%8A%82&command%5Bbody%5D%5Bmodules%5D%5B6%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B6%5D%5BisSub%5D=1&command%5Bbody%5D%5Bmodules%5D%5B6%5D%5Border%5D=108&command%5Bbody%5D%5Bmodules%5D%5B6%5D%5Bicon%5D=interact&command%5Bbody%5D%5Bmodules%5D%5B6%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B7%5D%5Bname%5D=bigScreenManage&command%5Bbody%5D%5Bmodules%5D%5B7%5D%5BdisplayName%5D=%E5%A4%A7%E5%B1%8F%E7%AE%A1%E7%90%86&command%5Bbody%5D%5Bmodules%5D%5B7%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B7%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B7%5D%5Border%5D=109&command%5Bbody%5D%5Bmodules%5D%5B7%5D%5Bicon%5D=screen&command%5Bbody%5D%5Bmodules%5D%5B7%5D%5BisEnable%5D=1&command%5Bbody%5D%5Bmodules%5D%5B8%5D%5Bname%5D=rights&command%5Bbody%5D%5Bmodules%5D%5B8%5D%5BdisplayName%5D=%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%86&command%5Bbody%5D%5Bmodules%5D%5B8%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B8%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B8%5D%5Border%5D=110&command%5Bbody%5D%5Bmodules%5D%5B8%5D%5Bicon%5D=rights&command%5Bbody%5D%5Bmodules%5D%5B8%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B9%5D%5Bname%5D=appMonitor&command%5Bbody%5D%5Bmodules%5D%5B9%5D%5BdisplayName%5D=%E7%AD%BE%E5%88%B0%E8%AE%BE%E5%A4%87%E7%9B%91%E6%8E%A7&command%5Bbody%5D%5Bmodules%5D%5B9%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B9%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B9%5D%5Border%5D=110&command%5Bbody%5D%5Bmodules%5D%5B9%5D%5Bicon%5D=appmonitor&command%5Bbody%5D%5Bmodules%5D%5B9%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B10%5D%5Bname%5D=subSeminar&command%5Bbody%5D%5Bmodules%5D%5B10%5D%5BdisplayName%5D=%E5%88%86%E4%BC%9A%E5%9C%BA&command%5Bbody%5D%5Bmodules%5D%5B10%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B10%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B10%5D%5Border%5D=111&command%5Bbody%5D%5Bmodules%5D%5B10%5D%5Bicon%5D=subevent&command%5Bbody%5D%5Bmodules%5D%5B10%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B11%5D%5Bname%5D=edm&command%5Bbody%5D%5Bmodules%5D%5B11%5D%5BdisplayName%5D=%E9%82%AE%E4%BB%B6%E4%BB%BB%E5%8A%A1&command%5Bbody%5D%5Bmodules%5D%5B11%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B11%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B11%5D%5Border%5D=112&command%5Bbody%5D%5Bmodules%5D%5B11%5D%5Bicon%5D=edm&command%5Bbody%5D%5Bmodules%5D%5B11%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B12%5D%5Bname%5D=sms&command%5Bbody%5D%5Bmodules%5D%5B12%5D%5BdisplayName%5D=%E7%9F%AD%E4%BF%A1%E4%BB%BB%E5%8A%A1&command%5Bbody%5D%5Bmodules%5D%5B12%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B12%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B12%5D%5Border%5D=113&command%5Bbody%5D%5Bmodules%5D%5B12%5D%5Bicon%5D=sms&command%5Bbody%5D%5Bmodules%5D%5B12%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B13%5D%5Bname%5D=material&command%5Bbody%5D%5Bmodules%5D%5B13%5D%5BdisplayName%5D=%E7%B4%A0%E6%9D%90%E5%BA%93&command%5Bbody%5D%5Bmodules%5D%5B13%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B13%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B13%5D%5Border%5D=114&command%5Bbody%5D%5Bmodules%5D%5B13%5D%5Bicon%5D=source&command%5Bbody%5D%5Bmodules%5D%5B13%5D%5BisEnable%5D=0&command%5Bbody%5D%5Bmodules%5D%5B14%5D%5Bname%5D=article&command%5Bbody%5D%5Bmodules%5D%5B14%5D%5BdisplayName%5D=%E6%96%87%E7%AB%A0&command%5Bbody%5D%5Bmodules%5D%5B14%5D%5Btype%5D=optional&command%5Bbody%5D%5Bmodules%5D%5B14%5D%5BisSub%5D=0&command%5Bbody%5D%5Bmodules%5D%5B14%5D%5Border%5D=115&command%5Bbody%5D%5Bmodules%5D%5B14%5D%5Bicon%5D=article&command%5Bbody%5D%5Bmodules%5D%5B14%5D%5BisEnable%5D=0&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F72.0.3626.121+Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=72.0.3626.121&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1920X1080&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Fsde%2Fseminar.html%23%2FSeminar%2FBigScreen%2FManage&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D="
    print "payload:",payload
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "f3f572e3-8e78-43db-3d04-5734587124e5"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"desc")
# 获取线下会的通道id
def get_seminarId_passageId(type,url,tenantId,bakSess,seminar_instanceId,seminarId,Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=seminar.signingPoint.getList&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BinstanceId%5D="+seminar_instanceId+"&command%5Bbody%5D%5BseminarId%5D="+seminarId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "49c3efbb-9c20-25cb-9173-ecdc89dd8075"
    }
    return api_quester_common().post_request_passageId("POST", url, payload, headers, Identifi_field, type,"passageId")
 # 获取线下会的通道
def get_seminarId_signingPointId(type,url,tenantId,bakSess,seminar_instanceId,seminarId,Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=seminar.signingPoint.getList&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BinstanceId%5D="+seminar_instanceId+"&command%5Bbody%5D%5BseminarId%5D="+seminarId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "49c3efbb-9c20-25cb-9173-ecdc89dd8075"
    }
    return api_quester_common().post_request_signingPointId("POST", url, payload, headers, Identifi_field, type,"signingPointId")
# 获取luckDrawid
def get_luckDrawid(type,url,tenantId,bakSess,Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bcmd%5D=luckyDraw.create2&command%5Bver%5D=1000&command%5Bbody%5D%5Btitle%5D=%E6%88%91%E6%98%AF%E5%88%AE%E5%88%AE%E5%8D%A1&command%5Bbody%5D%5Btype%5D=1&command%5Bbody%5D%5BstartTime%5D=1553011200&command%5Bbody%5D%5BendTime%5D=1868760875&command%5Bbody%5D%5BenableShare%5D=0&command%5Bbody%5D%5BshareTitle%5D=&command%5Bbody%5D%5BshareDesc%5D=&command%5Bbody%5D%5BshareCover%5D=&command%5Bbody%5D%5Bfreq%5D=1000000&command%5Bbody%5D%5Bprecondition%5D=1&command%5Bbody%5D%5Bidentity%5D=1&command%5Bbody%5D%5BattentionWeChat%5D=0&command%5Bbody%5D%5BneedUserInfo%5D=0&command%5Bbody%5D%5BguaranteedFlag%5D=&command%5Bbody%5D%5BisShared%5D=0&command%5Bbody%5D%5BisPermanent%5D=false&command%5Bbody%5D%5BmoduleType%5D=&command%5Bbody%5D%5BschemaId%5D=&command%5Bbody%5D%5BregisterFormId%5D=&command%5Bbody%5D%5BtrackId%5D=&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Burl%5D=&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Bcmd%5D=&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Burl%5D=&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Bcmd%5D=&command%5Bbody%5D%5BattachId%5D=&command%5Bbody%5D%5BisPublicCopy%5D=0&command%5Bbody%5D%5BisPublicRef%5D=0&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BmeetingType%5D=&command%5Bbody%5D%5BmeetingInstanceId%5D=&command%5Bbody%5D%5BweChatId%5D=&command%5Bbody%5D%5BweChatName%5D=&command%5Bbody%5D%5BattachWXAccount%5D=&command%5Bbody%5D%5BpreviewImg%5D=&command%5Bbody%5D%5BtemplateCategoryId%5D=7&command%5Bbody%5D%5BtemplateDevice%5D=wap&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "d7c10ad9-9fa3-36b4-3f95-adf072cbdbbc"
    }
    return api_quester_common().post_request_bigScree("POST", url, payload, headers, Identifi_field, type,"luckyDrawId")
# 获取签到大屏id
def get_bigScreen_templateId(type,url,bakSess,seminar_instanceId,nodeId,tenantId,Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=template.template.getList&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BinstanceId%5D="+seminar_instanceId+"&command%5Bbody%5D%5BmoduleId%5D=3&command%5Bbody%5D%5BnodeId%5D="+nodeId+"&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BcategoryId%5D=117&command%5Bbody%5D%5BisRemoveDefault%5D=false&command%5Bbody%5D%5Bdevice%5D="
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "20fdf5d8-5ac8-de4e-2fbd-8ff74b49fd32"
    }
    return api_quester_common().post_request_bigScreen_templateId("POST", url, payload, headers, Identifi_field, type)
# 获取签到大屏configId
def get_bigScreen_configId(type,url,bakSess,tenantId,bigScreen_templateId,Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=template.template.setConfig&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5Bconfig%5D%5Btitle%5D=%E5%A4%A7%E5%B1%8F%E7%AD%BE%E5%88%B0WAP%E6%A8%A1%E6%9D%BFV2&command%5Bbody%5D%5Bconfig%5D%5Bdesc%5D=%E5%A4%A7%E5%B1%8F%E7%AD%BE%E5%88%B0WAP%E6%A8%A1%E6%9D%BFV2&command%5Bbody%5D%5Bconfig%5D%5Bdevice%5D=wap&command%5Bbody%5D%5Bconfig%5D%5BpreviewCoverImage%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ff%2F6770207988262a430a1d23cd617d86b1%2F&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Btitle%5D=%E7%AD%BE%E5%88%B0%E9%A1%B5%E9%9D%A2&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bdesc%5D=this%20is%20the%20complete%20page&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bname%5D=sign&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5BformalUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ff%2F6770207988262a430a1d23cd617d86b1%2Fhtml%2Fsign.html&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5BsettingUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ff%2F6770207988262a430a1d23cd617d86b1%2Fhtml%2Fsign_setting.html&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5BisDefault%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B0%5D%5BattrName%5D=background&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B0%5D%5BdisplayName%5D=%E8%83%8C%E6%99%AF&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B0%5D%5Btype%5D=body&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B0%5D%5BdefaultUrl%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B0%5D%5BreplaceUrl%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B0%5D%5BdefaultText%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B0%5D%5BreplaceText%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B0%5D%5BisUse%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B0%5D%5BisShow%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B0%5D%5Bstyle%5D%5Bbackground-image%5D=url('https%3A%2F%2Fhwyhw.smarket.net.cn%2Ff%2F6770207988262a430a1d23cd617d86b1%2Fimages%2Fpage_bg.jpg')&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B0%5D%5Bstyle%5D%5Bbackground-color%5D=%23265b9c&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B0%5D%5Bstyle%5D%5Bbackground-size%5D=100%25%20100%25&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B1%5D%5BattrName%5D=title&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B1%5D%5BdisplayName%5D=%E6%A0%87%E9%A2%98&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B1%5D%5Btype%5D=div&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B1%5D%5BdefaultUrl%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B1%5D%5BreplaceUrl%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B1%5D%5BdefaultText%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B1%5D%5BreplaceText%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B1%5D%5BisUse%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B1%5D%5BisShow%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B1%5D%5Bstyle%5D%5Bcolor%5D=%23ffffff&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B2%5D%5BattrName%5D=signButton&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B2%5D%5BdisplayName%5D=%E6%8C%89%E9%92%AE&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B2%5D%5Btype%5D=p&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B2%5D%5BdefaultUrl%5D=%E7%AD%BE%E5%88%B0%E4%B8%8A%E5%A2%99&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B2%5D%5BreplaceUrl%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B2%5D%5BdefaultText%5D=%E7%AD%BE%E5%88%B0%E4%B8%8A%E5%A2%99&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B2%5D%5BreplaceText%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B2%5D%5BisUse%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B2%5D%5BisShow%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B2%5D%5Bstyle%5D%5Bbackground-color%5D=%23e0af56&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B2%5D%5Bstyle%5D%5Bborder-radius%5D=.06rem&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bextra%5D%5B2%5D%5Bstyle%5D%5Bcolor%5D=%23503402&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B0%5D%5Bid%5D=10822&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Btitle%5D=%E7%AD%BE%E5%88%B0%E6%88%90%E5%8A%9F%E9%A1%B5%E9%9D%A2&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bdesc%5D=this%20is%20the%20complete%20page&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5BformalUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ff%2F6770207988262a430a1d23cd617d86b1%2Fhtml%2FSignSuccess.html&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bname%5D=signSuccess&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5BsettingUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ff%2F6770207988262a430a1d23cd617d86b1%2Fhtml%2FSignSuccess_setting.html&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5BisDefault%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B0%5D%5BattrName%5D=background&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B0%5D%5BdisplayName%5D=%E8%83%8C%E6%99%AF&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B0%5D%5Btype%5D=body&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B0%5D%5BdefaultUrl%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B0%5D%5BreplaceUrl%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B0%5D%5BdefaultText%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B0%5D%5BreplaceText%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B0%5D%5BisUse%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B0%5D%5BisShow%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B0%5D%5Bstyle%5D%5Bbackground-image%5D=url('https%3A%2F%2Fhwyhw.smarket.net.cn%2Ff%2F6770207988262a430a1d23cd617d86b1%2Fimages%2Fpage_bg.jpg')&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B0%5D%5Bstyle%5D%5Bbackground-color%5D=%23265b9c&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B0%5D%5Bstyle%5D%5Bbackground-size%5D=100%25%20100%25&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B1%5D%5BattrName%5D=title&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B1%5D%5BdisplayName%5D=%E6%A0%87%E9%A2%98&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B1%5D%5Btype%5D=div&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B1%5D%5BdefaultUrl%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B1%5D%5BreplaceUrl%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B1%5D%5BdefaultText%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B1%5D%5BreplaceText%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B1%5D%5BisUse%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B1%5D%5BisShow%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B1%5D%5Bstyle%5D%5Bcolor%5D=%23ffffff&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B2%5D%5BattrName%5D=btnBackground&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B2%5D%5BdisplayName%5D=%E6%8F%90%E7%A4%BA%E4%BF%A1%E6%81%AF%E8%83%8C%E6%99%AF&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B2%5D%5Btype%5D=div&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B2%5D%5BdefaultUrl%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B2%5D%5BreplaceUrl%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B2%5D%5BdefaultText%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B2%5D%5BreplaceText%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B2%5D%5BisUse%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B2%5D%5BisShow%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B2%5D%5Bstyle%5D%5Bbackground-color%5D=%23e0af56&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B3%5D%5BattrName%5D=mesg&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B3%5D%5BdisplayName%5D=%E6%8F%90%E7%A4%BA%E4%BF%A1%E6%81%AF&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B3%5D%5Btype%5D=p&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B3%5D%5BdefaultUrl%5D=%E6%81%AD%E5%96%9C%E6%82%A8%EF%BC%8C%E7%AD%BE%E5%88%B0%E6%88%90%E5%8A%9F%EF%BC%81&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B3%5D%5BreplaceUrl%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B3%5D%5BdefaultText%5D=%E6%81%AD%E5%96%9C%E6%82%A8%EF%BC%8C%E7%AD%BE%E5%88%B0%E6%88%90%E5%8A%9F%EF%BC%81&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B3%5D%5BreplaceText%5D=&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B3%5D%5BisUse%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B3%5D%5BisShow%5D=1&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bextra%5D%5B3%5D%5Bstyle%5D%5Bcolor%5D=%23e0af56&command%5Bbody%5D%5Bconfig%5D%5Bhtml%5D%5B1%5D%5Bid%5D=10823&command%5Bbody%5D%5Bconfig%5D%5Bdependencies%5D%5B%5D=&command%5Bbody%5D%5Bconfig%5D%5Bdependencies%5D%5B%5D=..%2F..%2F..%2F..%2F..%2Fpackage.json&command%5Bbody%5D%5Bconfig%5D%5Buid%5D=6770207988262a430a1d23cd617d86b1&command%5Bbody%5D%5Bconfig%5D%5BcategoryId%5D=17&command%5Bbody%5D%5Bconfig%5D%5BversionNum%5D=v2&command%5Bbody%5D%5Bconfig%5D%5BtenantId%5D=&command%5Bbody%5D%5Bconfig%5D%5BmoduleId%5D=&command%5Bbody%5D%5Bconfig%5D%5BinstanceId%5D=&command%5Bbody%5D%5Bconfig%5D%5BtemplateId%5D="+bigScreen_templateId+"&command%5Bbody%5D%5Bconfig%5D%5BisDefault%5D=0&command%5Bbody%5D%5Bconfig%5D%5BdefaultType%5D=&command%5Bbody%5D%5Bconfig%5D%5BformalUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ff%2F6770207988262a430a1d23cd617d86b1%2Fhtml%2Fsign.html&command%5Bbody%5D%5Bconfig%5D%5Bplatform%5D=v2&command%5Bbody%5D%5Bconfig%5D%5BisEnable%5D="
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "5a608232-78af-8163-b548-4a166615b467"
    }
    return api_quester_common().post_request_bigScree("POST", url, payload, headers, Identifi_field, type,"configId")
# 获取多次签到点的id
def get_signingPointIds(type,url,bakSess,tenantId,seminarId,seminar_instanceId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=seminar.signingPoint.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BseminarId%5D="+seminarId+"&command%5Bbody%5D%5BinstanceId%5D="+seminar_instanceId+"&command%5Bbody%5D%5BgroupId%5D=0&command%5Bbody%5D%5BsigningPointName%5D="+createTime+"&command%5Bbody%5D%5Btype%5D=accessControl&command%5Bbody%5D%5BlimitType%5D=unlimited&command%5Bbody%5D%5BuserTypes%5D=&command%5Bbody%5D%5Bremark%5D=&command%5Bbody%5D%5BcheckInNumber%5D=-1"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "1d030f8a-ec0e-c10b-bf9d-f5f504abcf44"
    }
    return api_quester_common().post_request_acture("POST", url, payload, headers, Identifi_field, type)
# 获取大屏id，此大屏可允许同一用户多次签到
def get_bigScreenId(type,url,bakSess,seminarId,signingPointIds,bigScreen_configId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=seminar.bigScreen.createCheckIn&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BseminarId%5D="+seminarId+"&command%5Bbody%5D%5Bname%5D=y"+createTime+"&command%5Bbody%5D%5Bscale%5D=narrow&command%5Bbody%5D%5BgroupId%5D=0&command%5Bbody%5D%5BsigningPointId%5D="+signingPointIds+"&command%5Bbody%5D%5BsigningPoint%5D=20190321093559&command%5Bbody%5D%5BcheckInByWeChat%5D=on&command%5Bbody%5D%5BregOnSite%5D=off&command%5Bbody%5D%5BregFormId%5D=&command%5Bbody%5D%5BregFormName%5D=%E8%AF%B7%E9%80%89%E6%8B%A9%E6%8A%A5%E5%90%8D%E8%A1%A8%E5%8D%95&command%5Bbody%5D%5BonTheWallField%5D=regInfo&command%5Bbody%5D%5BconfigId%5D="+bigScreen_configId+"&command%5Bbody%5D%5BcheckInConfigId%5D=57707&command%5Bbody%5D%5Bremark%5D=&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F72.0.3626.121+Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=72.0.3626.121&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1920X1080&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Funiportal%2Flogin.html&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D="
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "dbd9d41a-8fd3-6744-e463-588a480bd97e"
    }
    return api_quester_common().post_request_bigScree("POST", url, payload, headers, Identifi_field, type,"id")
# 获取productLine
def get_productLine(type,url,bakSess,tenantId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "{\"command\":{\"size\":0,\"orn\":\"02-0001-00000001\",\"dst\":\"01-0401-00000001\",\"type\":2,\"sess\":\""+bakSess+"\",\"seq\":0,\"ver\":1000,\"body\":{\"productLineName\":\""+createTime+"\",\"thumbnail\":\"\",\"orderNum\":100,\"tenantId\":\""+tenantId+"\"},\"cmd\":\"productLine.create\"}}"
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "0a923aaa-91ec-5f91-a227-173cd3d17ddb"
    }
    return api_quester_common().post_request_bigScree("POST", url, payload, headers, Identifi_field, type,"productLine")
# 获取webinarId和instanceId
def get_webinarId_and_instanceId(type,url,bakSess,tenantId,memberFormId,schemaId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=webinar.event.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5Btitle%5D=%E4%BC%9A%E8%AE%AE"+createTime+"&command%5Bbody%5D%5Bsponsor%5D=%E4%B8%AB%E4%B8%AB&command%5Bbody%5D%5Bintro%5D=&command%5Bbody%5D%5BitemValues%5D%5B%5D=&command%5Bbody%5D%5BwebCastProvider%5D=gensee&command%5Bbody%5D%5BregistrationFormId%5D="+memberFormId+"&command%5Bbody%5D%5BschemaId%5D="+schemaId+"&command%5Bbody%5D%5BstartTime%5D=1548211127&command%5Bbody%5D%5BendTime%5D=1548214727&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    print payload
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "1fa4e618-b31e-340d-2e71-ceec7e3fb3c7"
    }
    return api_quester_common().post_request_seminarId("POST", url, payload, headers, Identifi_field, type,"webinarId","instanceId")
# 获取customFormId
def get_customFormId(type,url,bakSess,tenantId,seminarId,Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=seminar.register.getList&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BseminarId%5D="+seminarId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "a489afd1-f5dc-6339-8d92-d45878559d40"
    }
    print "url:",url
    print "payload:",payload
    return api_quester_common().post_request_get_registerFormId("POST",url,payload,headers,Identifi_field,type,"registerFormId")
# 线下会开启报名表单
def get_open_offline_meetingthe_form(type,url,bakSess,tenantId,seminar_instanceId,customFormId,Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=customForm.start&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BinstanceId%5D="+seminar_instanceId+"&command%5Bbody%5D%5BcustomFormId%5D="+customFormId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "0acc59e9-f90c-d7a7-e2e3-6ceea0f666b9"
    }
    return api_quester_common().post_request_successful("POST",url,payload,headers,Identifi_field,type,"desc")
# 获取问卷ID,questionid—wj
def get_questionid(type,url,bakSess,tenantId,Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=questionary.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BstartTime%5D=&command%5Bbody%5D%5BendTime%5D=&command%5Bbody%5D%5BquestionaryBankId%5D=&command%5Bbody%5D%5BmeetingType%5D=&command%5Bbody%5D%5BmeetingInstanceId%5D=&command%5Bbody%5D%5Bdesc%5D=&command%5Bbody%5D%5BshareDesc%5D=&command%5Bbody%5D%5Btitle%5D=6eb2cafc-a08c-dcea-b4dc-c8c37615daea&command%5Bbody%5D%5Btype%5D=1&command%5Bbody%5D%5BisPermanent%5D=1&command%5Bbody%5D%5BattachId%5D=0&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BmoduleType%5D=&command%5Bbody%5D%5Bidentity%5D=1&command%5Bbody%5D%5BschemaId%5D=&command%5Bbody%5D%5BtrackId%5D=0&command%5Bbody%5D%5BregisterFormId%5D=&command%5Bbody%5D%5BattachWXAccount%5D=0&command%5Bbody%5D%5BattentionWeChat%5D=0&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Burl%5D=&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Bcmd%5D=&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Burl%5D=&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Bcmd%5D=&command%5Bbody%5D%5BshareTitle%5D=1111111111111111111&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "672a2853-d65a-7ca1-1150-a858cb7e122a"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"content")
# 获取guestId
def get_guestId(type,url,bakSess,tenantId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=guest.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BguestTypeId%5D=186&command%5Bbody%5D%5Bglobal%5D=&command%5Bbody%5D%5Bname%5D=%E5%98%89%E5%AE%BE"+createTime+"&command%5Bbody%5D%5Bgender%5D=%E7%94%B7&command%5Bbody%5D%5Benterprise%5D=%E4%BC%A0%E5%AA%92%E5%85%AC%E5%8F%B8&command%5Bbody%5D%5Bduty%5D=&command%5Bbody%5D%5Bdemartment%5D=&command%5Bbody%5D%5BimageMapId%5D=&command%5Bbody%5D%5Bphone%5D=&command%5Bbody%5D%5Bemail%5D=&command%5Bbody%5D%5Bintro%5D=&command%5Bbody%5D%5BisPublic%5D=%E6%98%AF"
    print "payload:",payload
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "80cb47e5-e11d-5f14-187f-699ce0d8d370"
    }
    return api_quester_common().post_request_bigScree("POST", url, payload, headers, Identifi_field, type,"guestId")
# 获取productLineId
def get_productLineId(type,url,bakSess,tenantId,Identifi_field):
    payload = "{\"command\":{\"size\":0,\"orn\":\"02-0001-00000001\",\"dst\":\"01-0401-00000001\",\"type\":2,\"sess\":\""+bakSess+"\",\"seq\":0,\"ver\":1000,\"body\":{\"start\":0,\"num\":10000000,\"withDeleted\":0,\"tenantId\":\""+tenantId+"\"},\"cmd\":\"productLine.getList\"}}"
    print "payload:",payload
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "c0950b18-ca3a-2876-42d7-ce3ff2faeee1"
    }
    return api_quester_common().post_request_productLineId("POST", url, payload, headers, Identifi_field, type,"productLineId")
# 获取webinarId_DianBo和webinar_instanceId_DianBo
def get_webinarId_DianBo_and_webinar_instanceId_DianBo(type,url,bakSess,tenantId,schemaId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=webinar.demand.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5Btitle%5D=%E7%82%B9%E6%92%AD%E4%BC%9A%E8%AE%AE"+createTime+"&command%5Bbody%5D%5Bsponsor%5D=22&command%5Bbody%5D%5Bintro%5D=%3Cp%3E%E4%BC%9A%E8%AE%AE%E7%AE%80%E4%BB%8B%3C%2Fp%3E&command%5Bbody%5D%5BitemValues%5D%5B%5D=&command%5Bbody%5D%5BwebCastProvider%5D=gensee&command%5Bbody%5D%5BregistrationFormId%5D=876&command%5Bbody%5D%5BschemaId%5D="+schemaId+"&command%5Bbody%5D%5BstartTime%5D=1548259200&command%5Bbody%5D%5BendTime%5D=1548345540&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "47b441c1-660d-4758-682b-6b80de48f752"
    }
    return api_quester_common().post_request_seminarId("POST", url, payload, headers, Identifi_field, type, "webinarId","instanceId")
# 线下会日程创建获取agendaId
def get_agendaId(type,url,bakSess,seminarId,Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=seminar.agenda.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BseminarId%5D="+seminarId+"&command%5Bbody%5D%5Bname%5D=%E6%97%A5%E7%A8%8B1548322960&command%5Bbody%5D%5Baddress%5D=%E5%8C%97%E4%BA%AC&command%5Bbody%5D%5BagendaDate%5D=1548056480&command%5Bbody%5D%5BstartTime%5D=1548056480&command%5Bbody%5D%5BendTime%5D=1549050480&command%5Bbody%5D%5Bremark%5D="
    print "payload:",payload
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "ff82365d-6fca-53de-cc99-cd2e63e75edd"
    }
    return api_quester_common().post_request_bigScree("POST", url, payload, headers, Identifi_field, type, "agendaId")
# 获取栏目ID,categoryId
def get_categoryId(type,url,bakSess,tenantId,nodeId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=articleCategory.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BmoduleId%5D=0&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BparentArticleCategoryId%5D=&command%5Bbody%5D%5Btitle%5D=%E6%A0%8F%E7%9B%AE1548381486"+createTime+"&command%5Bbody%5D%5Bsummary%5D=&command%5Bbody%5D%5Bdescription%5D=&command%5Bbody%5D%5BshareDescState%5D=true&command%5Bbody%5D%5BcoverImageMappingId%5D=&command%5Bbody%5D%5BcategoryMethodId%5D=&command%5Bbody%5D%5BisEnableRecommend%5D=0&command%5Bbody%5D%5BrecommendConfig%5D%5BrecommendScheme%5D=1&command%5Bbody%5D%5BrecommendConfig%5D%5BsupplementScheme%5D=1&command%5Bbody%5D%5BrecommendConfig%5D%5BsupplementContent%5D=1&command%5Bbody%5D%5BarticleCategoryId%5D=&command%5Bbody%5D%5BisShared%5D=0&command%5Bbody%5D%5BisEnabled%5D=1&command%5Bbody%5D%5BshareState%5D=1&command%5Bbody%5D%5BsubCategoryCount%5D=0&command%5Bbody%5D%5BcoverImageUrl%5D=&command%5Bbody%5D%5BshareTitle%5D=&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BnodeId%5D="+nodeId+""
    print  "payload:",payload
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "9af8d585-c6b0-1613-3ddb-2019b6bb2df6"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"content")
# 获取文件夹id，fileId
def get_rootFileId(type,url,bakSess,tenantId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bcmd%5D=file.get&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BmoduleType%5D=&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BfileId%5D=0"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "7e0a7233-e16e-19ce-ed10-b97ddc29e7a8"
    }
    return api_quester_common().post_request_bigScree("POST", url, payload, headers, Identifi_field, type, "rootFileId")
# 获取文件夹id，fileId
def get_FolderId(type,url,bakSess,tenantId,rootFileId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bcmd%5D=file.createFolder&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BmoduleId%5D=&command%5Bbody%5D%5BfolderId%5D="+rootFileId+"&command%5Bbody%5D%5BallowUploadFlag%5D=0&command%5Bbody%5D%5BallowUpload%5D=0&command%5Bbody%5D%5BisRelease%5D=1&command%5Bbody%5D%5BisOpenApplyDown%5D=0&command%5Bbody%5D%5BlimitType%5D=&command%5Bbody%5D%5BdownEmailTaskName%5D=&command%5Bbody%5D%5BdownEmailTaskId%5D=&command%5Bbody%5D%5BapplyEmailTaskName%5D=&command%5Bbody%5D%5BapplyEmailTaskId%5D=&command%5Bbody%5D%5BshareTitle%5D=&command%5Bbody%5D%5Bdescription%5D=&command%5Bbody%5D%5BshareImgMappingId%5D=&command%5Bbody%5D%5BweChatId%5D=0&command%5Bbody%5D%5BauthorisedType%5D=0&command%5Bbody%5D%5Bname%5D=%E6%96%87%E4%BB%B6%E5%A4%B9"+createTime
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "c9fa5914-ea3a-200b-d760-5299771b6a6c"
    }
    return api_quester_common().post_request_bigScree("POST", url, payload, headers, Identifi_field, type, "fileId")
    # 获取pollId值
def get_pollId(type, url, bakSess, tenantId, Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=poll.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BattachWXAccountQrCode%5D=&command%5Bbody%5D%5Bfreq%5D=0&command%5Bbody%5D%5Bdesc%5D=&command%5Bbody%5D%5BisPermanent%5D=1&command%5Bbody%5D%5BisPublicCopy%5D=0&command%5Bbody%5D%5BisPublicRef%5D=0&command%5Bbody%5D%5BshareTitle%5D=&command%5Bbody%5D%5BshareDesc%5D=&command%5Bbody%5D%5BshareCover%5D=&command%5Bbody%5D%5BshareCoverUrl%5D=&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BcompleteAction%5D=-1&command%5Bbody%5D%5BcompleteTip%5D=&command%5Bbody%5D%5BcompleteLink%5D=http%3A%2F%2F&command%5Bbody%5D%5BcompleteLuckyDrawId%5D=0&command%5Bbody%5D%5BcompleteActionType%5D=-1&command%5Bbody%5D%5BfollowTip%5D=&command%5Bbody%5D%5Btitle%5D=%E6%8A%95%E7%A5%A8&command%5Bbody%5D%5BshowTitle%5D=1&command%5Bbody%5D%5BattachId%5D=0&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BmoduleType%5D=&command%5Bbody%5D%5BisShared%5D=0&command%5Bbody%5D%5Bidentity%5D=1&command%5Bbody%5D%5BschemaId%5D=0&command%5Bbody%5D%5BregisterFormId%5D=0&command%5Bbody%5D%5BtrackId%5D=0&command%5Bbody%5D%5BattachWXAccount%5D=0&command%5Bbody%5D%5BattachWxAccountName%5D=&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Burl%5D=&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Bcmd%5D=&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Burl%5D=&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Bcmd%5D=&command%5Bbody%5D%5BweChatQrCodeUrl%5D=images%2F953331b9.img-code-default.gif&command%5Bbody%5D%5BisCertifiedService%5D=false&command%5Bbody%5D%5BdateTime%5D%5BstartDate%5D=&command%5Bbody%5D%5BdateTime%5D%5BendDate%5D=&command%5Bbody%5D%5BmeetingType%5D=&command%5Bbody%5D%5BmeetingInstanceId%5D=&command%5Bbody%5D%5BmeetingName%5D=&command%5Bbody%5D%5BstartTime%5D=&command%5Bbody%5D%5BendTime%5D=&command%5Bbody%5D%5BattentionWeChat%5D=0&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F71.0.3578.98%20Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=71.0.3578.98&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1920X1080&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ftool%2Fvote%2Findex.html%23%2F&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D="
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "15d87266-1f7d-cfd6-bae4-620a2f00aa0b"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"content")
# 获取邮件任务id,taskId
def get_taskId(type, url, bakSess, nodeId, Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=edm.task.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BnodeId%5D="+nodeId+"&command%5Bbody%5D%5BmoduleId%5D=&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5Bname%5D=%E9%82%AE%E4%BB%B6"+createTime+"&command%5Bbody%5D%5Btitle%5D=%E9%82%AE%E4%BB%B6&command%5Bbody%5D%5Btype%5D=1&command%5Bbody%5D%5BsenderName%5D=%E4%B8%AB%E4%B8%AB&command%5Bbody%5D%5BisExecuteAdd%5D=1&command%5Bbody%5D%5BisExecuteSend%5D=1&command%5Bbody%5D%5BisRelate%5D=0"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "17dff3df-5b31-9319-0e02-81ef0833ce70"
    }
    return api_quester_common().post_request_bigScree("POST", url, payload, headers, Identifi_field, type,"id")
# 填写邮件内容
def get_task_content(type, url, bakSess, taskId, Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=edm.task.updateContent&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtaskId%5D="+taskId+"&command%5Bbody%5D%5Btitle%5D=%E9%82%AE%E4%BB%B6%E6%A0%87%E9%A2%98&command%5Bbody%5D%5Btype%5D=1&command%5Bbody%5D%5BsenderName%5D=%E4%B8%AB%E4%B8%AB&command%5Bbody%5D%5BsenderEmail%5D=&command%5Bbody%5D%5Breply%5D=&command%5Bbody%5D%5Bhtml%5D=%3Cp%3E%E4%BD%A0%E5%A5%BD%3C%2Fp%3E"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "1aa44b2a-9aef-f89a-02a6-ca306869d153"
    }

    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type, "desc")
# 获取自定义表单id
def get_registerFormId(type, url, bakSess, tenantId, Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=customForm.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BcompleteActionType%5D=0&command%5Bbody%5D%5BisPermanent%5D=1&command%5Bbody%5D%5Bleads%5D=0&command%5Bbody%5D%5BneedLogin%5D=0&command%5Bbody%5D%5Btitle%5D=%E8%A1%A8%E5%8D%95&command%5Bbody%5D%5BtopMenu%5D=0&command%5Bbody%5D%5Btype%5D=1&command%5Bbody%5D%5BcustomFormId%5D=&command%5Bbody%5D%5BformId%5D=&command%5Bbody%5D%5BluckyDrawId%5D=&command%5Bbody%5D%5BmoduleType%5D=&command%5Bbody%5D%5BstartTime%5D=&command%5Bbody%5D%5BendTime%5D=&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BisShared%5D=0&command%5Bbody%5D%5Bidentity%5D=1&command%5Bbody%5D%5BschemaId%5D=&command%5Bbody%5D%5BregisterFormId%5D=&command%5Bbody%5D%5BattachWXAccount%5D=&command%5Bbody%5D%5BmeetingType%5D=&command%5Bbody%5D%5BmeetingInstanceId%5D=&command%5Bbody%5D%5BisPublicCopy%5D=1&command%5Bbody%5D%5BisPublicRef%5D=1&command%5Bbody%5D%5BshareTitle%5D=%E8%A1%A8%E5%8D%95&command%5Bbody%5D%5BshareDesc%5D=&command%5Bbody%5D%5BshareCover%5D=&command%5Bbody%5D%5BshareCoverUrl%5D=&command%5Bbody%5D%5BcompleteAction%5D=&command%5Bbody%5D%5BisReSubmit%5D=0&command%5Bbody%5D%5BattentionWeChat%5D=0&command%5Bbody%5D%5BcallbackConfig%5D=&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F71.0.3578.98%20Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=71.0.3578.98&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1360X768&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ftool%2Fcustomform%2Findex.html%23%2F&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D=&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "92bb9d83-8c00-620e-85e6-971fb2ed84a5"
    }

    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type, "content")
# 获取随机试卷的id值
def get_questionid_sjsj(type, url, bakSess, tenantId, Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=questionary.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BstartTime%5D=&command%5Bbody%5D%5BendTime%5D=&command%5Bbody%5D%5BquestionaryBankId%5D=54&command%5Bbody%5D%5BmeetingType%5D=&command%5Bbody%5D%5BmeetingInstanceId%5D=&command%5Bbody%5D%5Bdesc%5D=&command%5Bbody%5D%5BshareDesc%5D=&command%5Bbody%5D%5Btitle%5D=%E9%9A%8F%E6%9C%BA%E8%AF%95%E5%8D%B7"+createTime+"&command%5Bbody%5D%5Btype%5D=3&command%5Bbody%5D%5BisPermanent%5D=1&command%5Bbody%5D%5BattachId%5D=0&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BmoduleType%5D=&command%5Bbody%5D%5Bidentity%5D=1&command%5Bbody%5D%5BschemaId%5D=&command%5Bbody%5D%5BtrackId%5D=0&command%5Bbody%5D%5BregisterFormId%5D=&command%5Bbody%5D%5BattachWXAccount%5D=0&command%5Bbody%5D%5BattentionWeChat%5D=0&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Burl%5D=&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Bcmd%5D=&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Burl%5D=&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Bcmd%5D=&command%5Bbody%5D%5BshareTitle%5D=%E9%9A%8F%E6%9C%BA%E8%AF%95%E5%8D%B7&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F71.0.3578.98%20Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=71.0.3578.98&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1360X768&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ftool%2Fquestionaire%2Findex.html%23%2F&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D=&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "311d95ce-9a45-5e76-31a5-65025f3dc582"
    }

    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type, "content")
# 开启线下会报名表单
def get_seminar_customForm_start(type, url, bakSess, tenantId,seminar_instanceId,customFormId, Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=customForm.start&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BinstanceId%5D="+seminar_instanceId+"&command%5Bbody%5D%5BcustomFormId%5D%5B%5D="+customFormId+"&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F71.0.3578.98%20Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=71.0.3578.98&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1360X768&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Fsde%2Fseminar.html%23%2FSeminar%2FHome%2FHome&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D="
    print "payload:",payload
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "cf841859-f07b-36b6-30ae-8cf63652f0ab"
    }

    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type, "desc")
# 线下会报名接口
def get_customForm_action(type, url, loginSess, customFormId,seminarId_instanceId,Identifi_field):
    payload = "{\"sess\":\""+loginSess+"\",\"customFormId\":\""+customFormId+"\",\"linkId\":\"8175\",\"instanceId\":\""+seminarId_instanceId+"\",\"globalUserId\":\"2abf91380710762d7c609a8019909ad0\",\"url\":\"https://hwyhw.smarket.net.cn/f/34758dc860857df9a0b4f2b94a015051/html/customForm.html?customFormId=4054&instanceId=11582&linkId=8175&configId=42406&weChatId=9418\",\"referenceUrl\":\"https://hwyhw.smarket.net.cn/f/a4193c73ac8d7e3b81b384bea132c40a/html/EventDetail.html?instanceId=11582\",\"ver\":\"v2.0.1\",\"items\":[{\"fieldName\":\"name\",\"value\":\"杨\"},{\"fieldName\":\"mobile\",\"value\":\"18332118317\"},{\"fieldName\":\"email\",\"value\":\"947300891@qq.com\"},{\"fieldName\":\"identityNum\",\"value\":\"130421199101367\"},{\"fieldName\":\"username\",\"value\":\"Y\"},{\"fieldName\":\"avatar\",\"value\":{\"fileName\":\"\",\"mapId\":\"\"}},{\"fieldName\":\"province\",\"value\":[],\"otherValue\":\"\"},{\"fieldName\":\"jobNumber\",\"value\":\"\"},{\"fieldName\":\"enterprise\",\"value\":\"\"},{\"fieldName\":\"department\",\"value\":[],\"otherValue\":\"\"},{\"fieldName\":\"position\",\"value\":[],\"otherValue\":\"\"},{\"fieldName\":\"gender\",\"value\":[],\"otherValue\":\"\"},{\"fieldName\":\"industry\",\"value\":[],\"otherValue\":\"\"}],\"signPointItems\":[]}"
    payload={"sess":"fb2c3f02c0d02e3a9bd97a571600681e","customFormId":"4054","linkId":"8175","instanceId":"11582","globalUserId":"2abf91380710762d7c609a8019909ad0","url":"https://hwyhw.smarket.net.cn/f/34758dc860857df9a0b4f2b94a015051/html/customForm.html?customFormId=4054&instanceId=11582&linkId=8175&configId=42406&weChatId=9418","referenceUrl":"https://hwyhw.smarket.net.cn/f/a4193c73ac8d7e3b81b384bea132c40a/html/EventDetail.html?instanceId=11582","ver":"v2.0.1","items":[{"fieldName":"name","value":"杨"},{"fieldName":"mobile","value":"18332118317"},{"fieldName":"email","value":"947300891@qq.com"},{"fieldName":"identityNum","value":"130421199101367"},{"fieldName":"username","value":"Y"},{"fieldName":"avatar","value":{"fileName":"","mapId":""}},{"fieldName":"province","value":[],"otherValue":""},{"fieldName":"jobNumber","value":""},{"fieldName":"enterprise","value":""},{"fieldName":"department","value":[],"otherValue":""},{"fieldName":"position","value":[],"otherValue":""},{"fieldName":"gender","value":[],"otherValue":""},{"fieldName":"industry","value":[],"otherValue":""}],"signPointItems":[]}
    # 字典
    payload = {}
    payload["sess"] = loginSess
    payload["customFormId"] = customFormId
    payload["linkId"] = 8175
    payload["instanceId"] = seminarId_instanceId
    payload["globalUserId"] = "2abf91380710762d7c609a8019909ad0"
    payload["url"] = "https://hwyhw.smarket.net.cn/f/34758dc860857df9a0b4f2b94a015051/html/customForm.html?customFormId=4054&instanceId=11582&linkId=8175&configId=42406&weChatId=9418"
    payload["referenceUrl"]="https://hwyhw.smarket.net.cn/f/a4193c73ac8d7e3b81b384bea132c40a/html/EventDetail.html?instanceId=11582"
    payload["ver"] = "v2.0.1"
    payload["items"] = {"fieldName":"name","value":"杨"},{"fieldName":"mobile","value":"18332118317"},{"fieldName":"email","value":"947300891@qq.com"},{"fieldName":"identityNum","value":"130421199101367"},{"fieldName":"username","value":"Y"},{"fieldName":"avatar","value":{"fileName":"","mapId":""}},{"fieldName":"province","value":[],"otherValue":""},{"fieldName":"jobNumber","value":""},{"fieldName":"enterprise","value":""},{"fieldName":"department","value":[],"otherValue":""},{"fieldName":"position","value":[],"otherValue":""},{"fieldName":"gender","value":[],"otherValue":""},{"fieldName":"industry","value":[],"otherValue":""}
    payload["signPointItems"] = ""
    headers = {
        'cache-control': "no-cache",
        'postman-token': "bb510807-1f03-ff97-3bec-1703df8ab46c"
    }

    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type, "desc")

# 获取参会人员信息，contactId
def get_contactId(type,url,bakSess,tenantId,seminarId_instanceId,seminarId,Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=seminar.contact.getList&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BinstanceId%5D="+seminarId_instanceId+"&command%5Bbody%5D%5BseminarId%5D="+seminarId+"&command%5Bbody%5D%5Border%5D=1&command%5Bbody%5D%5Bconditions%5D=&command%5Bbody%5D%5Btags%5D=&command%5Bbody%5D%5BkeyWord%5D=&command%5Bbody%5D%5Bstart%5D=0&command%5Bbody%5D%5Bnum%5D=20&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20WOW64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F68.0.3440.15%20Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=68.0.3440.15&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1366X768&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Fsde%2Fseminar.html%23%2FSeminar%2FHome%2FHome&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D="
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "5a884f2d-2d3c-df72-fc50-0b44172a85d2"
    }
    return api_quester_common().post_request_productLineId("POST", url, payload, headers, Identifi_field, type,"mc_contactId")
# 设置参会人为普通参会人员，contactId
def set_contactId(type,url,bakSess,tenantId,seminarId_instanceId,seminarId,Identifi_field,contactId):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=seminar.contact.update&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BinstanceId%5D="+seminarId_instanceId+"&command%5Bbody%5D%5BseminarId%5D="+seminarId+"&command%5Bbody%5D%5Bfields%5D%5Busername%5D=&command%5Bbody%5D%5Bfields%5D%5BidentityNum%5D=&command%5Bbody%5D%5Bfields%5D%5Bemail%5D=1064265199%40qq.com&command%5Bbody%5D%5Bfields%5D%5Bmobile%5D=15960167982&command%5Bbody%5D%5Bfields%5D%5Bname%5D=%E6%9F%B3%E6%97%A6%E6%97%A6&command%5Bbody%5D%5Bfields%5D%5Benterprise%5D=&command%5Bbody%5D%5Bfields%5D%5Bavatar%5D=&command%5Bbody%5D%5Bfields%5D%5Bprovince%5D=&command%5Bbody%5D%5Bfields%5D%5BjobNumber%5D=&command%5Bbody%5D%5Bfields%5D%5Bdepartment%5D=%E9%94%80%E5%94%AE%E9%83%A8&command%5Bbody%5D%5Bfields%5D%5Bposition%5D=&command%5Bbody%5D%5Bfields%5D%5Bgender%5D=&command%5Bbody%5D%5Bfields%5D%5Bm_one%5D=&command%5Bbody%5D%5BsubSeminars%5D%5B%5D=2868&command%5Bbody%5D%5Bcategory%5D=%E6%99%AE%E9%80%9A%E5%8F%82%E4%BC%9A%E4%BA%BA%E5%91%98&command%5Bbody%5D%5BisCreate%5D=0&command%5Bbody%5D%5BcontactId%5D="+contactId+"&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F72.0.3626.121+Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=72.0.3626.121&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1920X1080&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=http%3A%2F%2Fhwuat.smarket.net.cn%2Fsde%2Fseminar.html%3FseminarId%3D2861%26instanceId%3D11879&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D="
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "5a884f2d-2d3c-df72-fc50-0b44172a85d2"
    }
    print "url:",url
    print "payload:",payload
    return api_quester_common().post_request_acture("POST", url, payload, headers, Identifi_field, type)
# 设置参会人为普通参会人员第一步，contactId
def contact_isSignUp(type,url,bakSess,tenantId,seminarId_instanceId,seminarId,Identifi_field,contactId):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=seminar.contact.isSignUp&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BinstanceId%5D="+seminarId_instanceId+"&command%5Bbody%5D%5BseminarId%5D="+seminarId+"&command%5Bbody%5D%5Bfields%5D%5Busername%5D=&command%5Bbody%5D%5Bfields%5D%5BidentityNum%5D=&command%5Bbody%5D%5Bfields%5D%5Bemail%5D=1064265199%40qq.com&command%5Bbody%5D%5Bfields%5D%5Bmobile%5D=15960167982&command%5Bbody%5D%5Bfields%5D%5Bname%5D=%E6%9F%B3%E6%97%A6%E6%97%A6&command%5Bbody%5D%5Bfields%5D%5Benterprise%5D=&command%5Bbody%5D%5Bfields%5D%5Bavatar%5D=&command%5Bbody%5D%5Bfields%5D%5Bprovince%5D=&command%5Bbody%5D%5Bfields%5D%5BjobNumber%5D=&command%5Bbody%5D%5Bfields%5D%5Bdepartment%5D=%E9%94%80%E5%94%AE%E9%83%A8&command%5Bbody%5D%5Bfields%5D%5Bposition%5D=&command%5Bbody%5D%5Bfields%5D%5Bgender%5D=&command%5Bbody%5D%5Bfields%5D%5Bindustry%5D=&command%5Bbody%5D%5BsubSeminars%5D%5B%5D=3440&command%5Bbody%5D%5Bcategory%5D=%E6%99%AE%E9%80%9A%E5%8F%82%E4%BC%9A%E4%BA%BA%E5%91%98&command%5Bbody%5D%5BisCreate%5D=0&command%5Bbody%5D%5BcontactId%5D="+contactId+"&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F72.0.3626.121+Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=72.0.3626.121&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1920X1080&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Fsde%2Fseminar.html%3FseminarId%3D3439%26instanceId%3D16121&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D="
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "5a884f2d-2d3c-df72-fc50-0b44172a85d2"
    }
    print "url:",url
    print "payload:",payload
    return api_quester_common().post_request_bigScree("POST", url, payload, headers, Identifi_field, type,"isSignUp")
# 设置问卷选项,questionarywj_setItems
def get_questionarywj_setItems(type, url, bakSess, questionid_sjsj,tenantId, Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=questionary.setItems&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BmoduleId%5D=&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BmoduleId2%5D=8&command%5Bbody%5D%5BinstanceId2%5D=11700&command%5Bbody%5D%5BquestionaryId%5D="+questionid_sjsj+"&command%5Bbody%5D%5Bfields%5D%5B0%5D%5Bid%5D=25488&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BmoduleId%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BinstanceId%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BmoduleId2%5D=8&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BinstanceId2%5D=11700&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BfieldName%5D=name&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BextendFieldId%5D=3837&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BdisplayName%5D=%E5%A7%93%E5%90%8D&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BfieldType%5D=TEXT&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BfileLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BtextLimitType%5D=UNCHECK&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BtextRegularExpression%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BtextLength%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BtextRegularId%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BlistOptionType%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BlistDictId%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BlistLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BmaxOptionId%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BdateLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5Bdeleted%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BisSystemed%5D=1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5Brequired%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BerrorMessage%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BdisplayType%5D=1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BisLogin%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BisFormed%5D=1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BextraConfig%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BsaveFieldName%5D=tool_questionnaire_extra_text.f_1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BfieldLevel%5D=1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BisSendSms%5D=1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BotherOption%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BotherIsRequire%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BotherIsFillIn%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BcanEditFields%5D%5B%5D=required&command%5Bbody%5D%5Bfields%5D%5B0%5D%5Bstatus%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BcustomerDisplayName%5D=%E5%A7%93%E5%90%8D&command%5Bbody%5D%5Bfields%5D%5B1%5D%5Bid%5D=25489&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BmoduleId%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BinstanceId%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BmoduleId2%5D=8&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BinstanceId2%5D=11700&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BfieldName%5D=mobile&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BextendFieldId%5D=3838&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BdisplayName%5D=%E6%89%8B%E6%9C%BA&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BfieldType%5D=TEXT&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BfileLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BtextLimitType%5D=SYSTEM&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BtextRegularExpression%5D=%5E1(3%7C4%7C5%7C6%7C7%7C8%7C9)%5Cd%7B9%7D%24&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BtextLength%5D=11&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BtextRegularId%5D=10&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BlistOptionType%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BlistDictId%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BlistLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BmaxOptionId%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BdateLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5Bdeleted%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BisSystemed%5D=1&command%5Bbody%5D%5Bfields%5D%5B1%5D%5Brequired%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BerrorMessage%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BdisplayType%5D=1&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BisLogin%5D=1&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BisFormed%5D=1&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BextraConfig%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BsaveFieldName%5D=tool_questionnaire_extra_text.f_2&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BfieldLevel%5D=1&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BisSendSms%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BotherOption%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BotherIsRequire%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BotherIsFillIn%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BregularExpression%5D=%5E1(3%7C4%7C5%7C6%7C7%7C8%7C9)%5Cd%7B9%7D%24&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BcanEditFields%5D%5B%5D=errorMessage&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BcanEditFields%5D%5B%5D=required&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BcanEditFields%5D%5B%5D=isSendSms&command%5Bbody%5D%5Bfields%5D%5B1%5D%5Bstatus%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BschemaTextLength%5D=11&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BcustomerDisplayName%5D=%E6%89%8B%E6%9C%BA&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Bid%5D=25488&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BmoduleId%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BinstanceId%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BmoduleId2%5D=8&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BinstanceId2%5D=11700&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfieldName%5D=name&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BextendFieldId%5D=3837&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BdisplayName%5D=%E5%A7%93%E5%90%8D&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfieldType%5D=TEXT&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfileLimitType%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BtextLimitType%5D=UNCHECK&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BtextRegularExpression%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BtextLength%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BtextRegularId%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BlistOptionType%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BlistDictId%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BlistLimitType%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BmaxOptionId%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BdateLimitType%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Bdeleted%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BisSystemed%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Brequired%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BerrorMessage%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BdisplayType%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BisLogin%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BisFormed%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BextraConfig%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BsaveFieldName%5D=tool_questionnaire_extra_text.f_1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfieldLevel%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BisSendSms%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BotherOption%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BotherIsRequire%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BotherIsFillIn%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BcanEditFields%5D%5B%5D=required&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Bstatus%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BcustomerDisplayName%5D=%E5%A7%93%E5%90%8D&command%5Bbody%5D%5Bitems%5D%5B1%5D%5Bid%5D=25489&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BmoduleId%5D=0&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BinstanceId%5D=0&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BmoduleId2%5D=8&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BinstanceId2%5D=11700&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BfieldName%5D=mobile&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BextendFieldId%5D=3838&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BdisplayName%5D=%E6%89%8B%E6%9C%BA&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BfieldType%5D=TEXT&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BfileLimitType%5D=&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BtextLimitType%5D=SYSTEM&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BtextRegularExpression%5D=%5E1(3%7C4%7C5%7C6%7C7%7C8%7C9)%5Cd%7B9%7D%24&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BtextLength%5D=11&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BtextRegularId%5D=10&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BlistOptionType%5D=&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BlistDictId%5D=0&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BlistLimitType%5D=&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BmaxOptionId%5D=0&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BdateLimitType%5D=&command%5Bbody%5D%5Bitems%5D%5B1%5D%5Bdeleted%5D=0&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BisSystemed%5D=1&command%5Bbody%5D%5Bitems%5D%5B1%5D%5Brequired%5D=0&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BerrorMessage%5D=&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BdisplayType%5D=1&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BisLogin%5D=1&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BisFormed%5D=1&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BextraConfig%5D=&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BsaveFieldName%5D=tool_questionnaire_extra_text.f_2&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BfieldLevel%5D=1&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BisSendSms%5D=0&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BotherOption%5D=&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BotherIsRequire%5D=&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BotherIsFillIn%5D=&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BregularExpression%5D=%5E1(3%7C4%7C5%7C6%7C7%7C8%7C9)%5Cd%7B9%7D%24&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BcanEditFields%5D%5B%5D=errorMessage&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BcanEditFields%5D%5B%5D=required&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BcanEditFields%5D%5B%5D=isSendSms&command%5Bbody%5D%5Bitems%5D%5B1%5D%5Bstatus%5D=0&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BschemaTextLength%5D=11&command%5Bbody%5D%5Bitems%5D%5B1%5D%5BcustomerDisplayName%5D=%E6%89%8B%E6%9C%BA&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F72.0.3626.121+Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=72.0.3626.121&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1920X1080&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ftool%2Fquestionaire%2Findex.html%23%2F&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D="
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "db8a869b-48e8-9f7a-ab12-8da204d93448"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type, "desc")
# 获取问卷选项item值
def get_questionid_item(type,url,bakSess,questionid_sjsj, tenantId,Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=questionary.get&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BquestionaryId%5D="+questionid_sjsj+"&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20WOW64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F68.0.3440.15%20Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=68.0.3440.15&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1366X768&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ftool%2Fquestionaire%2Findex.html%23%2FQuestionaire%2F%3Aaction%3FquestionaryId%3D1751%26action%3DSetItems&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D=&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "19b0e8f8-d9e8-631c-ffec-7a3d60178fda"
    }
    return api_quester_common().post_request_productLineId("POST", url, payload, headers, Identifi_field, type,"itemId")




# 获取luckDrawid
def get_dicId_dicname(type,url,tenantId,bakSess,Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=dic.getList&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5Bkeyword%5D=&command%5Bbody%5D%5Btype%5D=-1&command%5Bbody%5D%5BisCascade%5D=-1&command%5Bbody%5D%5Bstart%5D=0&command%5Bbody%5D%5Bnum%5D=20&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "fcbb8353-d5e0-f756-c100-ec6226607d57"
    }
    return api_quester_common().post_request_intwo_outtwo("POST", url, payload, headers, Identifi_field, type,"dicId","name")

#获取门禁多次签到接口的通道值
def get_passagesId(type,url,bakSess,tenantId,seminarId,instanceId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=seminar.signingPoint.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BseminarId%5D="+seminarId+"&command%5Bbody%5D%5BinstanceId%5D="+instanceId+"&command%5Bbody%5D%5BgroupId%5D=0&command%5Bbody%5D%5BsigningPointName%5D=%E7%AD%BE%E5%88%B0"+createTime+"&command%5Bbody%5D%5Btype%5D=accessControl&command%5Bbody%5D%5BlimitType%5D=unlimited&command%5Bbody%5D%5BuserTypes%5D=&command%5Bbody%5D%5Bremark%5D=&command%5Bbody%5D%5BcheckInNumber%5D=-1&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F71.0.3578.98%20Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=71.0.3578.98&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1920X1080&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Fsde%2Fseminar.html%23%2FSeminar%2FHome%2FHome&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D="
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "cbfec25c-f418-4165-b3a7-a96ba32c8789"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type, "content")
#文件夹内上传图片
def get_file_upload(type,url,bakSess,Identifi_field):
    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[size]\"\r\n\r\n0\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[orn]\"\r\n\r\n02-0001-00000001\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[dst]\"\r\n\r\n01-0300\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[type]\"\r\n\r\n2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[cmd]\"\r\n\r\nfile.upload\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[sess]\"\r\n\r\n"+bakSess+"\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[seq]\"\r\n\r\n0\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[ver]\"\r\n\r\n1000\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[body]\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"[object Object].jpg\"\r\nContent-Type: false\r\n\r\n\r\n-----011000010111000001101001--"
    headers = {
        'content-type': "multipart/form-data; boundary=---011000010111000001101001",
        'cache-control': "no-cache",
        'postman-token': "5aef2600-61e8-7e4d-c1ad-bdaee2ad9f2a"
    }
    return api_quester_common().post_request_bigScree("POST", url, payload, headers, Identifi_field, type,"mappingId")



#微讨论下面的帖子id-postId的接口
def get_forum_post_postId(type,url,bakSess,tenantId,nodeId,global_topicId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bcmd%5D=forum.post.create&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BnodeId%5D="+nodeId+"&command%5Bbody%5D%5BmoduleId%5D=0&command%5Bbody%5D%5BinstanceId%5D=0&command%5Bbody%5D%5BtopicId%5D="+global_topicId+"&command%5Bbody%5D%5BenableReply%5D=1&command%5Bbody%5D%5BisAnonymous%5D=1&command%5Bbody%5D%5Btitle%5D=%E5%8F%91%E5%B8%961"+createTime+"&command%5Bbody%5D%5Bcontent%5D=%3Cp%3E%E5%8F%91%E5%B8%96%E5%95%A6%3C%2Fp%3E&command%5Bbody%5D%5BsectionId%5D=169&command%5Bbody%5D%5BpostId%5D=0&command%5Bbody%5D%5Bactivity%5D=1"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "6380841a-92a1-56b4-5c0f-3dfe5743122e"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"content")
#获取获取questionid—sj试卷
def get_questionid_sj(type,url,tenantId,bakSess,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=questionary.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BstartTime%5D=&command%5Bbody%5D%5BendTime%5D=&command%5Bbody%5D%5BquestionaryBankId%5D=&command%5Bbody%5D%5BmeetingType%5D=&command%5Bbody%5D%5BmeetingInstanceId%5D=&command%5Bbody%5D%5Bdesc%5D=&command%5Bbody%5D%5BshareDesc%5D=&command%5Bbody%5D%5Btitle%5D=%E8%AF%95%E5%8D%B7"+createTime+"&command%5Bbody%5D%5Btype%5D=3&command%5Bbody%5D%5BisPermanent%5D=1&command%5Bbody%5D%5BattachId%5D=0&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BmoduleType%5D=&command%5Bbody%5D%5Bidentity%5D=1&command%5Bbody%5D%5BschemaId%5D=&command%5Bbody%5D%5BtrackId%5D=0&command%5Bbody%5D%5BregisterFormId%5D=&command%5Bbody%5D%5BattachWXAccount%5D=0&command%5Bbody%5D%5BattentionWeChat%5D=0&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Burl%5D=&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Bcmd%5D=&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Burl%5D=&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Bcmd%5D=&command%5Bbody%5D%5BshareTitle%5D=%E8%AF%95%E5%8D%B7&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F71.0.3578.98%20Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=71.0.3578.98&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1920X1080&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ftool%2Fquestionaire%2Findex.html%23%2F&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D=&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "1728442c-1725-38a5-1917-05cf0f601992"
    }

    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"content")
#获取获取PLQID,评论区iD
def get_PLQID(type,url,tenantId,bakSess,nodeId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bcmd%5D=topic.create&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BnodeId%5D="+nodeId+"&command%5Bbody%5D%5BmoduleId%5D=0&command%5Bbody%5D%5BinstanceId%5D=0&command%5Bbody%5D%5BschemaId%5D=0&command%5Bbody%5D%5Btype%5D=3&command%5Bbody%5D%5Btitle%5D=%E8%AF%84%E8%AE%BA%E5%8C%BA"+createTime+"&command%5Bbody%5D%5BpostIdentity%5D=1&command%5Bbody%5D%5BpostIdentityExtra%5D=0&command%5Bbody%5D%5BtrackId%5D=0&command%5Bbody%5D%5BreplyIdentity%5D=1&command%5Bbody%5D%5BenableCheck%5D=0&command%5Bbody%5D%5BenableLike%5D=1&command%5Bbody%5D%5BenableDelete%5D=1&command%5Bbody%5D%5BenableAttachment%5D=1"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "ef6aa072-ad6c-55d4-1ed5-765dcce38030"
    }

    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"content")
#试卷-跳转到结果页保存按钮
def get_questionary_update(type,url,tenantId,bakSess,questionid_sj,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=questionary.update&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BquestionaryId%5D="+questionid_sj+"&command%5Bbody%5D%5Btitle%5D=%E8%AF%95%E5%8D%B720190129192320&command%5Bbody%5D%5Btype%5D=3&command%5Bbody%5D%5BshowTitle%5D=0&command%5Bbody%5D%5Bdesc%5D=&command%5Bbody%5D%5Btemplate%5D=&command%5Bbody%5D%5BisPermanent%5D=1&command%5Bbody%5D%5BcompleteAction%5D=http%3A%2F%2F&command%5Bbody%5D%5BcompleteActionType%5D=-1&command%5Bbody%5D%5BshareTitle%5D=%E8%AF%95%E5%8D%B7&command%5Bbody%5D%5BshareCover%5D=&command%5Bbody%5D%5BshareDesc%5D=&command%5Bbody%5D%5Bfreq%5D=&command%5Bbody%5D%5BfollowTip%5D=&command%5Bbody%5D%5BattachId%5D=0&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BisShared%5D=0&command%5Bbody%5D%5Bidentity%5D=1&command%5Bbody%5D%5BtrackId%5D=0&command%5Bbody%5D%5BattentionWeChat%5D=0&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Burl%5D=&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Bcmd%5D=&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Burl%5D=&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Bcmd%5D=&command%5Bbody%5D%5BisPublicCopy%5D=0&command%5Bbody%5D%5BisPublicRef%5D=0&command%5Bbody%5D%5BstartTime%5D=&command%5Bbody%5D%5BendTime%5D=&command%5Bbody%5D%5BmeetingType%5D=&command%5Bbody%5D%5BmeetingInstanceId%5D=&command%5Bbody%5D%5BregisterFormId%5D=&command%5Bbody%5D%5BattachWXAccount%5D=0&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F71.0.3578.98%20Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=71.0.3578.98&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1920X1080&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ftool%2Fquestionaire%2Findex.html%23%2F&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D=&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "e0627615-1479-f0ec-6978-a37983f6a465"
    }

    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"desc")
#获取线下会分会场id
def get_subSeminarId(type,url,tenantId,bakSess,seminarId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=seminar.subSeminar.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5Bname%5D=%E5%88%86%E4%BC%9A%E5%9C%BA"+createTime+"&command%5Bbody%5D%5BstartTime%5D=1548765000&command%5Bbody%5D%5BendTime%5D=1864483199&command%5Bbody%5D%5Bhotel%5D=%E5%8C%97%E4%BA%AC&command%5Bbody%5D%5BpermissionType%5D=disabled&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BseminarId%5D="+seminarId+"&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F71.0.3578.98%20Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=71.0.3578.98&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1920X1080&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Fsde%2Fseminar.html%23%2FSeminar%2FMenu%2FList&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D="
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "5d9fffd9-4ec9-3a7c-0b4c-13ef61538cd9"
    }

    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"content")
#获取试卷添加题目
def get_questionarysj_setItems(type,url,tenantId,bakSess,questionaryId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=questionary.setItems&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BquestionaryId%5D="+questionaryId+"&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfieldType%5D=LIST&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfieldLevel%5D=4&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BitemId%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Bquestion%5D=%E5%8D%95%E9%80%89%E9%A2%981&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfieldName%5D=%E5%8D%95%E9%80%89%E6%A1%86&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BregularExpression%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BisCommon%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Btype%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Bkey%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Bnecessary%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Banswer%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BtotalScore%5D=10&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BleadsGrade%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BleadsGradeTitle%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BenableRegular%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5Bfocus%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5Btitle%5D=A&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5BpicMapId%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5BpicUrl%5D=%2F%2Fcdn.smarket.net.cn%2Fimages%2Fimg-pic-default.gif&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5BisFillIn%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5BisOther%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5Btext%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5Bscore%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5BscoreTitle%5D=%E4%B8%8D%E5%BE%97%E5%88%86&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5B%24%24hashKey%5D=object%3A465&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5BisChecked%5D=false&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5BoptionId%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5Bfocus%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5Btitle%5D=B&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5BpicMapId%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5BpicUrl%5D=%2F%2Fcdn.smarket.net.cn%2Fimages%2Fimg-pic-default.gif&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5BisFillIn%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5BisOther%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5Btext%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5Bscore%5D=10&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5BscoreTitle%5D=%E5%BE%97%E5%88%86&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5B%24%24hashKey%5D=object%3A469&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5BisChecked%5D=true&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5BoptionId%5D=2&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F71.0.3578.98%20Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=71.0.3578.98&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1920X1080&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ftool%2Fquestionaire%2Findex.html%23%2F&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D=&command%5Bbody%5D%5BtenantId%5D="+tenantId+""

    headers = {
        'cookie': "SMARKET_MEMBER_SESS=;",
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "5dff405d-cb13-e175-72b3-2d29218042b0"
    }

    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"desc")
#获取articleCategoryId值
def get_articleCategoryId(type,url,tenantId,bakSess,nodeId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=articleCategory.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BmoduleId%5D=0&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BparentArticleCategoryId%5D=&command%5Bbody%5D%5Btitle%5D=%E6%96%87%E7%AB%A0id"+createTime+"&command%5Bbody%5D%5Bsummary%5D=&command%5Bbody%5D%5Bdescription%5D=&command%5Bbody%5D%5BshareDescState%5D=true&command%5Bbody%5D%5BcoverImageMappingId%5D=&command%5Bbody%5D%5BcategoryMethodId%5D=235683&command%5Bbody%5D%5BisEnableRecommend%5D=0&command%5Bbody%5D%5BrecommendConfig%5D%5BrecommendScheme%5D=1&command%5Bbody%5D%5BrecommendConfig%5D%5BsupplementScheme%5D=1&command%5Bbody%5D%5BrecommendConfig%5D%5BsupplementContent%5D=1&command%5Bbody%5D%5BarticleCategoryId%5D=&command%5Bbody%5D%5BisShared%5D=0&command%5Bbody%5D%5BisEnabled%5D=1&command%5Bbody%5D%5BshareState%5D=1&command%5Bbody%5D%5BsubCategoryCount%5D=0&command%5Bbody%5D%5BcoverImageUrl%5D=&command%5Bbody%5D%5BshareTitle%5D=&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BnodeId%5D="+nodeId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "9d4f14fc-38c2-a522-00b5-82043a640ed8"
    }

    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"content")
#文件夹内获取上传图片的文件id
def get_file_create(type,url,bakSess, tenantId,seminarId_instanceId,FolderId,Identifi_field):
    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[size]\"\r\n\r\n0\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[orn]\"\r\n\r\n02-0001-00000001\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[dst]\"\r\n\r\n01-0401-00000001\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[type]\"\r\n\r\n2\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[sess]\"\r\n\r\n"+bakSess+"\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[seq]\"\r\n\r\n0\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[cmd]\"\r\n\r\nfile.create\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[ver]\"\r\n\r\n1000\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[body][tenantId]\"\r\n\r\n"+tenantId+"\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[body][moduleType]\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[body][instanceId]\"\r\n\r\n"+seminarId_instanceId+"\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[body][folderId]\"\r\n\r\n"+FolderId+"\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[body][mapId]\"\r\n\r\n4ce51d8e992e4dd0c2fc2a01889871a9\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[body][name]\"\r\n\r\n1529633926(1).jpg\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[body][size]\"\r\n\r\n64274\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[body][iconMapId]\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[body][descInfo]\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"command[body][ext]\"\r\n\r\njpg\r\n-----011000010111000001101001--"
    headers = {
        'content-type': "multipart/form-data; boundary=---011000010111000001101001",
        'cache-control': "no-cache",
        'postman-token': "ab204800-727a-9d97-1193-0fef0d561fb8"
    }
    return api_quester_common().post_request_bigScree("POST", url, payload, headers, Identifi_field, type, "fileId")
#获取留言板的主贴id
def get_LYBZTId(type,url,bakSess,tenantId,nodeId,topicId,Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bcmd%5D=post.create&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BnodeId%5D="+nodeId+"&command%5Bbody%5D%5BtopicId%5D="+topicId+"&command%5Bbody%5D%5BenableReply%5D=1&command%5Bbody%5D%5BisAnonymous%5D=1&command%5Bbody%5D%5Bcontent%5D=%E5%A4%A7%E5%AE%B6%E5%A5%BD&command%5Bbody%5D%5BpostId%5D=0&command%5Bbody%5D%5BmoduleId%5D=0&command%5Bbody%5D%5BinstanceId%5D=0"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "ea3a142c-3f2f-4ea1-a9c8-9bec3b33abba"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"content")
#获取只有姓名和手机的表单id
def get_customFormid_nameand_phone(type,url,bakSess,tenantId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=customForm.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BcompleteActionType%5D=0&command%5Bbody%5D%5BisPermanent%5D=1&command%5Bbody%5D%5Bleads%5D=0&command%5Bbody%5D%5BneedLogin%5D=0&command%5Bbody%5D%5Btitle%5D=%E5%8F%AA%E6%9C%89%E5%A7%93%E5%90%8D%E5%92%8C%E6%89%8B%E6%9C%BA%E5%8F%B7%E7%9A%84%E8%A1%A8%E5%8D%95"+createTime+"&command%5Bbody%5D%5BtopMenu%5D=0&command%5Bbody%5D%5Btype%5D=1&command%5Bbody%5D%5BcustomFormId%5D=&command%5Bbody%5D%5BformId%5D=&command%5Bbody%5D%5BluckyDrawId%5D=&command%5Bbody%5D%5BmoduleType%5D=&command%5Bbody%5D%5BstartTime%5D=&command%5Bbody%5D%5BendTime%5D=&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BisShared%5D=0&command%5Bbody%5D%5Bidentity%5D=1&command%5Bbody%5D%5BschemaId%5D=&command%5Bbody%5D%5BregisterFormId%5D=&command%5Bbody%5D%5BattachWXAccount%5D=&command%5Bbody%5D%5BmeetingType%5D=&command%5Bbody%5D%5BmeetingInstanceId%5D=&command%5Bbody%5D%5BisPublicCopy%5D=1&command%5Bbody%5D%5BisPublicRef%5D=1&command%5Bbody%5D%5BshareTitle%5D=%E5%8F%AA%E6%9C%89%E5%A7%93%E5%90%8D%E5%92%8C%E6%89%8B%E6%9C%BA%E5%8F%B7%E7%9A%84%E8%A1%A8%E5%8D%95&command%5Bbody%5D%5BshareDesc%5D=&command%5Bbody%5D%5BshareCover%5D=&command%5Bbody%5D%5BshareCoverUrl%5D=&command%5Bbody%5D%5BcompleteAction%5D=&command%5Bbody%5D%5BisReSubmit%5D=0&command%5Bbody%5D%5BattentionWeChat%5D=0&command%5Bbody%5D%5BcallbackConfig%5D=&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20WOW64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F68.0.3440.15%20Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=68.0.3440.15&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1366X768&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ftool%2Fcustomform%2Findex.html%23%2F&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D=&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "125eb172-8851-cd14-54f3-6131938fdaef"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, Identifi_field, type,"content")
#获取自定义注册表单id
def get_zdyresterFormId(type,url,bakSess,tenantId,schemaId,Identifi_field):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Bdst%5D=01-0401-00000001&command%5Born%5D=02-0001-00000001&command%5Btype%5D=2&command%5Bsess%5D="+bakSess+"&command%5Bcmd%5D=form.create&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BschemaId%5D="+schemaId+"&command%5Bbody%5D%5Btitle%5D=%E8%A1%A8%E5%8D%95"+createTime+"&command%5Bbody%5D%5Bfields%5D%5B0%5D%5Bid%5D=3837&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BschemaId%5D="+schemaId+"&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BfieldName%5D=name&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BdisplayName%5D=%E5%A7%93%E5%90%8D&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BfieldType%5D=TEXT&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BfileLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BtextLimitType%5D=UNCHECK&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BlistOptionType%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BlistDictId%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BdateLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BorderId%5D=1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5Bdeleted%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BisSystemed%5D=1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BisShow%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5Brequired%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5Benabled%5D=1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BerrorMessage%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BtextRegularExpression%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BtextLength%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BtextRegularId%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BlistLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BmaxOptionId%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BisOverWrite%5D=1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BisRecordHistory%5D=1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BisExport%5D=1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BisLogin%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BisFormed%5D=1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BmemberFieldName%5D=mbr_member.realname&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BidentFieldName%5D=mbr_identification.realname&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BdefaultFieldId%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BisSendSms%5D=1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BversionNumber%5D=1&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BfieldId%5D=2&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BregularName%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BregularExpression%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BregularDescription%5D=&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BschemaTextLimitType%5D=UNCHECK&command%5Bbody%5D%5Bfields%5D%5B0%5D%5B%24%24hashKey%5D=object%3A124&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BtextDefaultRegType%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5Bid%5D=3838&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BschemaId%5D="+schemaId+"&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BfieldName%5D=mobile&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BdisplayName%5D=%E6%89%8B%E6%9C%BA&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BfieldType%5D=TEXT&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BfileLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BtextLimitType%5D=SYSTEM&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BlistOptionType%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BlistDictId%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BdateLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BorderId%5D=2&command%5Bbody%5D%5Bfields%5D%5B1%5D%5Bdeleted%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BisSystemed%5D=1&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BisShow%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5Brequired%5D=1&command%5Bbody%5D%5Bfields%5D%5B1%5D%5Benabled%5D=1&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BerrorMessage%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BtextRegularExpression%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BtextLength%5D=11&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BtextRegularId%5D=10&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BlistLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BmaxOptionId%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BisOverWrite%5D=1&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BisRecordHistory%5D=1&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BisExport%5D=1&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BisLogin%5D=1&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BisFormed%5D=1&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BmemberFieldName%5D=mbr_member.mobile&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BidentFieldName%5D=mbr_identification.mobile&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BdefaultFieldId%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BisSendSms%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BversionNumber%5D=2&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BfieldId%5D=4&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BregularName%5D=mobile&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BregularExpression%5D=%5E1(3%7C4%7C5%7C6%7C7%7C8%7C9)%5Cd%7B9%7D%24&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BregularDescription%5D=%E6%89%8B%E6%9C%BA%E5%8F%B7%E7%A0%81&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BschemaTextLimitType%5D=SYSTEM&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BisPhoneCode%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BschemaErrorMessage%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5B%24%24hashKey%5D=object%3A125&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BtextDefaultRegType%5D=mobile&command%5Bbody%5D%5Bfields%5D%5B2%5D%5Bid%5D=3839&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BschemaId%5D="+schemaId+"&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BfieldName%5D=email&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BdisplayName%5D=%E9%82%AE%E7%AE%B1&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BfieldType%5D=TEXT&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BfileLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BtextLimitType%5D=SYSTEM&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BlistOptionType%5D=&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BlistDictId%5D=&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BdateLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BorderId%5D=3&command%5Bbody%5D%5Bfields%5D%5B2%5D%5Bdeleted%5D=0&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BisSystemed%5D=1&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BisShow%5D=0&command%5Bbody%5D%5Bfields%5D%5B2%5D%5Brequired%5D=0&command%5Bbody%5D%5Bfields%5D%5B2%5D%5Benabled%5D=1&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BerrorMessage%5D=&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BtextRegularExpression%5D=&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BtextLength%5D=&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BtextRegularId%5D=11&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BlistLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BmaxOptionId%5D=0&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BisOverWrite%5D=1&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BisRecordHistory%5D=1&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BisExport%5D=1&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BisLogin%5D=1&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BisFormed%5D=1&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BmemberFieldName%5D=mbr_member.email&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BidentFieldName%5D=mbr_identification.email&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BdefaultFieldId%5D=0&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BisSendSms%5D=1&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BversionNumber%5D=1&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BfieldId%5D=3&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BregularName%5D=email&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BregularExpression%5D=%5E(%5Cw)%2B(.%7C-%5Cw%2B)*%40(.%7C-%7C%5Cw)%2B((%5C.%5Cw%2B)%2B)%24&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BregularDescription%5D=%E9%82%AE%E7%AE%B1%E6%A0%BC%E5%BC%8F&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BschemaTextLimitType%5D=SYSTEM&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BschemaErrorMessage%5D=0&command%5Bbody%5D%5Bfields%5D%5B2%5D%5B%24%24hashKey%5D=object%3A126&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BtextDefaultRegType%5D=email&command%5Bbody%5D%5Bfields%5D%5B3%5D%5Bid%5D=3846&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BschemaId%5D="+schemaId+"&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BfieldName%5D=password&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BdisplayName%5D=%E5%AF%86%E7%A0%81&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BfieldType%5D=TEXT&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BfileLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BtextLimitType%5D=SYSTEM&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BlistOptionType%5D=&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BlistDictId%5D=&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BdateLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BorderId%5D=10&command%5Bbody%5D%5Bfields%5D%5B3%5D%5Bdeleted%5D=0&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BisSystemed%5D=1&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BisShow%5D=0&command%5Bbody%5D%5Bfields%5D%5B3%5D%5Brequired%5D=1&command%5Bbody%5D%5Bfields%5D%5B3%5D%5Benabled%5D=1&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BerrorMessage%5D=&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BtextRegularExpression%5D=&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BtextLength%5D=&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BtextRegularId%5D=16&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BlistLimitType%5D=&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BmaxOptionId%5D=0&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BisOverWrite%5D=1&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BisRecordHistory%5D=1&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BisExport%5D=1&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BisLogin%5D=0&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BisFormed%5D=1&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BmemberFieldName%5D=&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BidentFieldName%5D=mbr_identification.pwd&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BdefaultFieldId%5D=0&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BisSendSms%5D=1&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BversionNumber%5D=1&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BfieldId%5D=5&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BregularName%5D=password&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BregularExpression%5D=%5E.%7B6%2C20%7D%24&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BregularDescription%5D=%E5%AF%86%E7%A0%81&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BschemaTextLimitType%5D=SYSTEM&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BschemaErrorMessage%5D=0&command%5Bbody%5D%5Bfields%5D%5B3%5D%5B%24%24hashKey%5D=object%3A131&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BtextDefaultRegType%5D=password"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "09594c57-b3e6-0cb4-d95c-9272daf7a553"
    }

    return api_quester_common().post_request_bigScree("POST", url, payload, headers, Identifi_field, type,"formId")
# 获取标签属性值
def get_tag_field_getList(type,url,bakSess,tenantId,Identifi_field):
    payload = "command%5Bsize%5D=0&command%5Bdst%5D=01-0401-00000001&command%5Born%5D=02-0001-00000001&command%5Btype%5D=2&command%5Bsess%5D="+bakSess+"&command%5Bcmd%5D=tag.field.getList&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BisEnable%5D=-1&command%5Bbody%5D%5BisShowTag%5D=1&command%5Bbody%5D%5Btype%5D=all&command%5Bbody%5D%5Border%5D=id&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "5209229d-b6e8-1202-5377-186b6e23b2b8"
    }
    return api_quester_common().tag_field_getList("POST", url, payload, headers, Identifi_field, type, "tagSchemaId","tagFieldId","fieldName","displayName","tagId",)

# 获取后台登录session
def get_most_account_login(type,domain,email,password,Identifi_field):

    path="/content/index.php"
    print "domain:", domain + path
    payload="command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0100&command%5Btype%5D=2&command%5Bcmd%5D=account.login&command%5Bsess%5D=&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5Bemail%5D="+email+"&command%5Bbody%5D%5Bpassword%5D="+password+"&command%5Bbody%5D%5BclientType%5D=1&command%5Bbody%5D%5BclientBrand%5D=Netscape&command%5Bbody%5D%5BclientVersion%5D=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F71.0.3578.98+Safari%2F537.36"
    headers = {
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "aa379846-dbff-5b3a-c6ff-dc03f9c5a871"
    }
    return api_quester_common().post_request_get_customFormId("POST", domain+path, payload, headers, Identifi_field, type, "session")
# 华为uat类型的后台登录session
def hw_uat_get_most_account_login(type,domain,email,password,Identifi_field):

    path="/account/login"
    print "domain:", domain + path
    payload={
        "size":"0",
        "orn":"02-0001-00000001",
        "dst":"01-0100",
        "type":"2",
        "cmd":"account.login",
        "sess":"",
        "seq":"0",
        "ver":1000,
        "email":email,
        "password":password,
        "clientType":1,
        "clientBrand":"Netscape",
        "clientVersion":"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "67239a78-0da0-4d37-96f6-dba74e1598e9"
    }
    return api_quester_common().post_request_get_customFormId("POST", domain+path, payload, headers, Identifi_field, type, "session")
# 获取前台登录session
def get_most_member_login(type,domain,tenantId,schemaId,memberFormId,memberSchemaId,unique,password,Identifi_field):
    path="/member/login"
    print "domain:", domain + path
    # 字典
    # payload = {"tenantId":str(tenantId),"schemaId":str(schemaId),"memberFormId":str(memberFormId),"memberSchemaId":str(memberSchemaId),"unique":str(unique),"token":"","password":str(password),"checkCode":"","loginType":"","url":"https://hwyhw.smarket.net.cn/f/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberId=873&memberFormId=873&trackId=0&memberSchemaId=482&configId=37066&weChatId=9418&backUrl=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ff%2Fa4193c73ac8d7e3b81b384bea132c40a%2Fhtml%2FEventDetail.html%3FinstanceId%3D9445","browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36","browser":"Chrome","version":"71.0.3578.98","os":"Windows","equipment":"电脑端","resolution":"1920X1080","referenceUrl":"https://hwyhw.smarket.net.cn/f/a4193c73ac8d7e3b81b384bea132c40a/html/EventDetail.html?instanceId=9445","referenceTitle":"","sessionId":"7fa15a6f75e585ed7544c6953f555543"},"globalUserId":"1bf522f38f2e647bd6b46a4527b509df"}
    payload={}
    payload["tenantId"] = tenantId
    payload["schemaId"] = schemaId
    payload["memberFormId"] = memberFormId
    payload["memberSchemaId"] = memberSchemaId
    payload["unique"] = unique
    payload["password"] = password
    payload["checkCode"] = ""
    payload["loginType"] = ""
    payload["url"] = "https://hwyhw.smarket.net.cn/f/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberId=873&memberFormId=873&trackId=0&memberSchemaId=482&configId=37066&weChatId=9418&backUrl=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ff%2Fa4193c73ac8d7e3b81b384bea132c40a%2Fhtml%2FEventDetail.html%3FinstanceId%3D9445"
    payload["browseInfo"] = {
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "browser": "Chrome", "version": "71.0.3578.98", "os": "Windows", "equipment": "电脑端", "resolution": "1920X1080",
        "referenceUrl": "https://hwyhw.smarket.net.cn/f/a4193c73ac8d7e3b81b384bea132c40a/html/EventDetail.html?instanceId=9445",
        "referenceTitle": "", "sessionId": "7fa15a6f75e585ed7544c6953f555543"}
    payload["globalUserId"] = "1bf522f38f2e647bd6b46a4527b509df"
    # payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:", payload
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "a4c630f5-0612-0e08-a914-9e8e8ad37d07"
    }
    return api_quester_common().post_request_bigScree("POST", domain + path, payload, headers, Identifi_field, type,"session")
# 绑定微信和参会人员
def get_most_seminar_contact_setContactToWechat(type,domain,seminarId,contactId,wechatId,bakSsess,Identifi_field):
    path="/seminar/contact/setContactToWechat"
    print "domain:", domain + path
    payload={
          "seminarId": seminarId,
          "contactId": contactId,
          "wechatId": wechatId,
          "openId": "o_sUFt2z1cgjIO47gTGRf2sUUKTg",
          "sess":""+bakSsess+""
     }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "c48b3082-8a70-2af0-c4cc-a978dce71cee"
    }
    return api_quester_common().Is_successful("POST", domain+path, payload, headers, Identifi_field, type)
# api_member_password_update修改前台登录用户的密码-jch
def get_most_api_member_password_update(type,domain,tenantId,member_password,loginSess):
    path="/api/member/password/update"
    print "domain:",domain+path
    payload='{ "tenantId": "'+tenantId+'","oldPwd": "'+member_password+'","newPwd": "'+member_password+'","sess": "'+loginSess+'"}'
    print "payload:",payload
    headers = {
    'content-type': "application/json",
    'cookie': "SMARKET_MEMBER_SESS=;",
    'cache-control': "no-cache",
    'postman-token': "c1028c29-1026-66bc-086a-4e4c6f681d32"
    }
    return api_quester_common().Is_successful("POST", domain+path, payload, headers,type,type)
#api_member_contacts_simple_signin 注册用户简单登录(通过OpenId或账号密码登录)
def get_api_member_contacts_simple_signin(type,domain,tenantId,unique,password, memberFormId):
    path="/api/member/contacts/simple/signin"
    print "domain:",domain+path
    payload={"tenantId":int(tenantId),"formId": int(memberFormId),"unique":unique,"password":password,"verify":"","globalUserId":""}
    # payload={}
    # payload["tenantId"]=int(tenantId)
    # payload["formId"] = 873
    # payload["unique"] = unique
    # payload["password"] = password
    # payload["verify"] = ""
    # payload["globalUserId"] = ""
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload；", payload
    headers = {
        'Content-Type': "application/json",
        'cookie': "MARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "73ec62f7-097e-4190-a5f0-d58e20730984"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#member_identification_UpdateAvatar 修改注册用户头像
def get_member_identification_UpdateAvatar(type,domain,tenantId,schemaId,loginSess):
    path="/member/identification/UpdateAvatar"
    print "domain:",domain+path
    payload={
        "tenantId":tenantId,
        "schemaId":schemaId,
        "mapping":{
            "fileName": "1.jpg",
            "mapping": "0dc75571265fd288aa520bd7e449fcf5"
        },
        "sess":""+loginSess+""
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload；",payload
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "9c114a84-c91b-4eaa-bb8d-b95e32af084b"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#member_update更新用户信息
def get_member_update(type,domain,memberFormId,loginSess):
    path="/member/update"
    print "domain:", domain + path
    payload={
        "memberFormId": int(memberFormId),
        "sess": str(loginSess),
        "formData": [
            {
                "fieldName": "name",
                "value": "yaya"
            }
        ]
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "016ff562-689e-4a2c-8490-744e0c62e03e"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#articleCategory_get获取文章列表
def get_articleCategory_get(type,domain,loginSess,tenantId,nodeId):
    path = "/articleCategory/get"
    print "domain:", domain + path
    payload={
        "sess": ""+loginSess+"",
        "id":0,
        "instanceId":"",
        "tenantId":tenantId,
        "nodeId":nodeId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "625cfd27-d873-48db-8a9c-22416edd7858"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#comment_getList评论列表
def get_comment_getList(type,domain,tenantId,topicId,loginSess):
    path = "/comment/getList"
    print "domain:", domain + path
    payload={
        "tenantId":tenantId,
        "subVersionId":"108122",
        "commentId":0,
        "start":0,
        "num": 15,
        "topicId": topicId,
        "sess": ""+loginSess+"",
        "openId": "",
        "cookieId":"6011594ff2ae3ad38866d2b437df1d29",
        "globalUserId":"6011594ff2ae3ad38866d2b437df1d29"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "6c50cbb9-2806-4fe1-8519-250a561c4f50"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#获取微讨论的详情
def get_forum_getForumInfo(type,domain,global_topicId,tenantId):
    path = "/forum/getForumInfo"
    print "domain:", domain + path
    payload={
        "topicId": global_topicId,
        "tenantId": tenantId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "346c61fe-0314-4142-b960-87affaa7226e"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#forum_getReplyList/获取微论坛的回复列表
def get_forum_getReplyList(type,domain,global_topicId,loginSess):
    path = "/forum/getReplyList"
    print "domain:", domain + path
    payload = {
        "topicId":global_topicId,
        "openId": "",
        "cookieId": "",
        "start": 0,
        "num": 10,
        "isAll": 1,
        "sess": ""+loginSess+""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "648c2e87-ebdf-4a9e-9111-57746b7e4e1c"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#forum_post_create/微论坛发贴回复
def get_forum_post_create(type,domain,topicId,sectionId):
    path = "/forum/post/create"
    print "domain:", domain + path
    payload={
    "content": "<p>hello</p>",
    "postId": "",
    "topicId":topicId,
    "sess": "",
    "sectionId":sectionId,
    "title": "1",
    "attachments": [],
    "cookieId": "6011594ff2ae3ad38866d2b437df1d29",
    "browseInfo": {
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "browser": "Chrome",
        "version": "70.0.3538.110",
        "os": "Windows",
        "equipment": "pc",
        "resolution": "1360X768",
        "referenceUrl": "http://hwuat.smarket.net.cn/topic/index.html",
        "referenceTitle": "",
        "sessionId": "00277a0b9d591de8030333d95de3473e"
    },
    "enableReply": 1,
    "isAnonymous": 0,
    "signUserId": "",
    "globalUserId": "6011594ff2ae3ad38866d2b437df1d29"
}
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "a287ad3a-58e5-435e-b215-a8fe108f645f"
    }
    return api_quester_common().Is_successful_getvalue("POST", domain + path, payload, headers, type, type,"content")
#forum_post_get/微论坛帖子详情
def get_forum_post(type,domain,tenantId,nodeId,postId):
    path = "/forum/post/get"
    print "domain:", domain + path
    payload ={
        "tenantId":tenantId,
        "nodeId":nodeId,
        "moduleId":"1",
        "instanceId": 0,
        "postId":postId,
        "memberId": 0,
        "openId": "otqO01CM74B9qQ2ZFwGiglaZFxzg",
        "cookieId": 0
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "c4ac2288-b302-4102-9b8a-c669f11e141c"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# article_browse 文章浏览
def get_most_article_browse(type,domain,articleId):
    path="/article/browse"
    print "domain:",domain+path
    payload = {}
    payload["articleId"] = articleId
    payload["sess"] = ""
    payload["globalUserId"] = "6011594ff2ae3ad38866d2b437df1d29"
    payload["openId"] = ""
    payload["url"] = "https://hwuat.smarket.net.cn/f/27bfd3aaa163a0b75e40770732dbbaa3/html/info.html?articleId=107612&configId=33193"
    payload["referenceUrl"] = ""
    payload["equipment"] = {"ua":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36","browser":{"name":"Chrome","version":"70.0.3538.110","major":"70"},"engine":{"name":"WebKit","version":"537.36"},"os":{"name":"Windows","version":"10"},"device":{},"cpu":{"architecture":"amd64"}}
    payload["pageTitle"]="班车路线"
    payload["weChatId"]="9605"
    payload["resolution"]="1920*1080"
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "24f22422-016d-8c64-993d-544387d9c146"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# forum_post_getMainPost 获取微讨论的主贴列表
def get_most_forum_post_getMainPost(type,domain,global_topicId):
    path="/forum/post/getMainPost"
    print "domain:", domain + path
    payload={"topicId":global_topicId,"start": "0","num": 10,"sectionId": "-1","cookieId": "39e5bd2a4a1c363d09b9fdd09323b3d8","openId": "","orderBy": 1,"isHot": -1}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "2bb54177-63eb-eb64-fd2e-b12596dad9d7"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# forum_post_getMainPostNumber/微论坛主贴和回帖统计
def get_most_forum_post_getMainPostNumber(type,domain,global_topicId):
    path="/forum/post/getMainPostNumber"
    print "domain:", domain + path
    payload={"topicId":global_topicId}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "308a2d32-32fd-b7cc-2d1c-6ca483638667"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# forum_post_getPersonalPostList/微论坛查看个人或者他人帖子信息
def get_most_forum_post_getPersonalPostList(type,domain,loginSess):
    path="/forum/post/getPersonalPostList"
    print "domain:", domain + path
    payload={"memberId": 13056,"start": 0,"num": 100,"sess":loginSess}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "a1fb1843-40ee-5faa-df01-58b65992964f"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# forum_post_getReplyPost/获取微讨论的主贴ID
def get_most_forum_post_getReplyPost(type,domain,pos):
    path="/forum/post/getReplyPost"
    print "domain:", domain + path
    payload={"postId":pos ,"start": "0","num": 10,"cookieId": "39e5bd2a4a1c363d09b9fdd09323b3d8","openId": ""}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "00de6bce-2487-8807-b15f-a7e5058fad9a"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# forum_post_like / 微论坛给帖子点赞
def get_most_forum_post_like(type, domain,postId,loginSess):
    path="/forum/post/like"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = {}
    payload["postIds"] = [int(postId)]
    payload["cookieId"] =createTime
    payload["openId"] = ""
    payload["sess"] = str(loginSess)
    payload["browseInfo"] = {"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","browser":"Chrome","version":"66.0.3359.181","os":"Windows","equipment":"pc","resolution":"1366X768","referenceUrl":"https://f.smarket.net.cn/s/template/69a1e37d00c97c5cad5fa347e5e3a931/html/index.html?topicId=1441&configId=253066","referenceTitle":"","sessionId":"ec69f3edd1c9908cb8cfeb1e4528488e"}
    payload["globalUserId"]=createTime

    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "paylos:", payload
    # payload={"postIds":postId,"cookieId":"{{$guid}}","openId":"","sess":loginSess,"browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","browser":"Chrome","version":"66.0.3359.181","os":"Windows","equipment":"电脑端","resolution":"1366X768","referenceUrl":"https://f.smarket.net.cn/s/template/69a1e37d00c97c5cad5fa347e5e3a931/html/index.html?topicId=1441&configId=253066","referenceTitle":"","sessionId":"ec69f3edd1c9908cb8cfeb1e4528488e"},"globalUserId":"{{$guid}}"}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "f2b41b71-748e-52a1-c58b-8d940548da01"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)



# forum_post_update/更新帖子内容
def get_most_forum_post_update(type,domain,tenantId,nodeId,section_create):
    path="/forum/post/update"
    print "domain:", domain + path
    payload={
      "tenantId": tenantId,"nodeId": nodeId,"moduleId": "","instanceId": "","sectionId": section_create,"enableReply": 1,"title": "帖子","attachements": [],
      "content": "突突突突突突拖拖","postId": 0,"activity": "","cookieId": "","openId": "6663"
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "813efdd8-2d38-50ae-ca08-c1598191b53f"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# forum_section_getList/获取某个微论坛的子版列表
def get_most_forum_section_getList(type, domain, global_topicId):
    path="/forum/section/getList"
    print "domain:", domain + path
    payload={"topicId": global_topicId,"keyword": ""}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "c1a4994c-13af-2634-b861-61678794b1fa"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# article_browseRecord / 文章浏览
def get_most_article_browseRecord(type, domain, articleId,bakSess):
    path="/article/browseRecord"
    print "domain:", domain + path
    payload={
        "articleId": articleId,"globalUserId": "","openId": "","url": "","referenceUrl": "","sess": bakSess,"pageTitle": "测试",
        "equipment": "","weChatId": "","resolution": ""}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "f9f19283-5d87-a433-99e9-103d69da09b1"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# forum_stat_homePage/微论坛帖子列表
def get_most_forum_stat_homePage(type, domain, section_create,global_topicId):
    path="/forum/stat/homePage"
    print "domain:", domain + path
    payload={"status": 1,"activity": -1,"sectionId": section_create,"topicId": global_topicId,"keyword": "","orderBy": 1,"start": 0,"num": 10}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "f6114b5c-319e-1a7a-befd-75a658d10b4a"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#article_Collection/文章收藏
def get_article_Collection(type,domain,articleId,bakSess):
    path="/article/Collection"
    print "domain:", domain + path
    payload={"articleId":articleId,"status": 1,"globalUserId": "","openId": "","url": "","referenceUrl": "","sess": ""+bakSess+""}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "d63e0495-e126-4676-88e7-dec8020b9d88"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#forum_post_deletePost/删除自己发的帖子
def get_forum_post_deletePost(type,domain,topicId,pos):
    path="/forum/post/deletePost"
    print "domain:", domain + path
    payload={"topicId":topicId,"postIds":[pos]}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "ea01879b-1e48-4d8d-bc34-f2dd628771eb"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#file_create/该接口为后台接口，后期即将移除，请不要继续使用，上传文件
def get_file_create_upload(type,domain,tenantId,FolderId,bakSess):
    path = "/file/create"
    print "domain:", domain + path
    payload = {
        "tenantId": tenantId,
        "instanceId": "",
        "moduleType": "",
        "folderId":FolderId,
        "mapId": "1a8674072979ff40f575751995aa2c9f",
        "name": "1.jpg",
        "size": 19325,
        "iconMapId": "",
        "descInfo": "",
        "sortNum": "1",
        "mapName": "",
        "sess":""+bakSess+""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "ea01879b-1e48-4d8d-bc34-f2dd628771eb"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful_getvalue_02("POST", domain + path, payload, headers, type, type,"fileId")
#article_getDetail/获取文章详情
def get_article_getDetail(type,domain,articleId):
    path = "/article/getDetail"
    print "domain:", domain + path
    payload = {"withStat": 0,"articleId":articleId,"withTemplate": 1,"isScroll": 0,"withTag": 0}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "0f722efd-cf4c-480f-9083-721a5bdf9ddd"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful_getvalue_02("POST", domain + path, payload, headers, type, type,"topicId")
#article_getLikeStatus/获取此用户是否允许继续点赞,articleId和cookieId是必填字段,openId不传就以cookieId查询用户身份,传openId则cookieId和openId满足其一即可返回此用户的点赞状态
def get_article_getLikeStatus(type,domain,articleId,bakSess):
    path = "/article/getLikeStatus"
    print "domain:", domain + path
    payload = {"articleId":articleId,"globalUserId": "","openId": "","sess": ""+bakSess+""}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "e06db854-9b8d-4e12-8a47-10cca1067be4"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#article_getList/该接口即将过期不在维护，使用article_getListByProject替代
def get_article_getList(type,domain,tenantId,loginSess,categoryId):
    path = "/article/getList"
    print "domain:", domain + path
    payload = {
        "tenantId":tenantId,
        "moduleId":0,
        "instanceId": "",
        "articleCategoryId":categoryId,
        "title": "",
        "isRecommend": -1,
        "isStick": -1,
        "start": 0,
        "num": 5,
        "withStat": 1,
        "typeId": "",
        "sess": ""+loginSess+""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "2b3660ff-4501-4efc-8a83-a80bbe82024b"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#article_getListByIds/根据文章id数组获取文章列表信息
def get_article_getListByIds(type,domain,articleId):
    path = "/article/getListByIds"
    print "domain:", domain + path
    payload = {  "articleIds": [articleId],"withStat": 1,"withTemplate": "1"}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "e06db854-9b8d-4e12-8a47-10cca1067be4"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#article_getListByProject/获取文章列表
def get_article_getListByProject(type,domain,tenantId,categoryId):
    path = "/article/getListByProject"
    print "domain:", domain + path
    payload = {
    "tenantId":tenantId,
    "moduleId": 1,
    "instanceId": 12,
    "articleCategoryId":"",
    "title": "",
    "isRecommend": -1,
    "isStick": -1,
    "start": 0,
    "num": 20,
    "withStat": 1,
    "withTemplate": 1,
    "getAll": 1,
    "typeId": "",
    "searchColumns": [],
    "tags": [],
    "article": 1,
    "categoryId": categoryId,
    "startTime": "2015-12-02 16:47:41",
    "endTime": "2015-12-02 16:47:41"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "675c64fd-773d-4d28-ac1e-df6154416453"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#file_update/该接口为后台接口，后期即将移除，请不要继续使用，修改文件
def get_file_update(type,domain,tenantId,fileIds,mappingId,FolderId,bakSess):
    path = "/file/update"
    print "domain:", domain + path
    payload={
        "tenantId":tenantId,
        "moduleType": "",
        "instanceId": "",
        "fileId": fileIds,
        "size": 1223,
        "name": "welcome.jpg",
        "mapId":mappingId,
        "iconMapId":mappingId,
        "descInfo": "desccrition",
        "upperFileId":FolderId,
        "mapName": "",
        "sortNum": "1",
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "69c2da7b-e405-4717-8cd8-6073cd29d9d1"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#questionary_get/获取问卷信息
def get_questionary(type,domain,questionid_wj):
    path = "/questionary/get"
    print "domain:", domain + path
    payload ={
        "questionaryId": questionid_wj,
        "globalUserId": "60833f5d0335c945182342472d7499c7",
        "browseInfo": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "browser": "Chrome",
            "version": "69.0.3497.100",
            "os": "Windows",
            "equipment": "pc",
            "resolution": "1920X1080",
            "referenceUrl": "",
            "referenceTitle": ""
        }
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "fa103cd9-0b3c-4de6-992f-972e29e9e1f3"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# articleCategory_getSubList/获取文章分组列表
def get_most_articleCategory_getSubList(type,domain,categoryId):
    path="/articleCategory/getSubList"
    print "domain:", domain + path
    payload= {"articleCategoryId": categoryId, "_cache_with_cached": "1","_cache_refresh": "1","_cache_timeout":"60"}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "305f45c9-d945-9289-c41c-254ffff394eb"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# questionary_getList/获取问卷列表
def get_most_questionary_getList(type,domain,tenantId):
    path="/questionary_getList"
    print "domain:", domain + path
    payload = {"tenantId": tenantId,"moduleType": "","instanceId": "","attachId": "","name": "","status": -1,"start": 0,"num": 12,"type": 0}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "1eaa6de7-2e11-f130-816d-c4826b066766"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# questionary_reAction/提交试卷
def get_most_questionary_reAction(type,domain,questionid_wj,questionid_item):
    path = "/questionary/reAction"
    print "domain:", domain + path
    payload = {
        "questionaryId": questionid_wj,
        "globalUserId": "544fbf14b96536d1e966ac92e3e98a34",
        "referenceUrl": "",
        "headImgUrl": "",
        "openId": "",
        "nickname": "",
        "gender": "",
        "city": "",
        "province": "",
        "country": "",
        "preview": "",
        "instanceId": "",
        "options": [
            {
                "itemId": questionid_item,
                "options": [

                ]
            }
        ]
    }
    headers ={
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "ce974ca2-634b-b6d4-0050-d766ce747d2e"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful_status("POST", domain + path, payload, headers, type, type)
# article_getTrees/查询文章列表
def get_most_article_getTrees(type,domain,bakSess,tenantId,categoryId):
    path = "/article/getTrees"
    print "domain:", domain + path
    payload = {
    "sess":""+bakSess+"",
    "tenantId": ""+tenantId+"",
    "moduleId": "1",
    "instanceId": "38503",
    "articleCategoryId": ""+categoryId+"",
    "startTime": "2018-03-09",
    "endTime": "2018-06-20",
    "start": 0,
    "num": 20,
    "typeId": "2"
  }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "fbc62d8b-9f65-11d7-63b3-778fb174d2db"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#collect_add/收藏信息
def get_most_collect_add(type,domain,loginSess):
    path = "/collect/add"
    print "domain:", domain + path
    payload = {
    "referer": "http://shizaibuzhidao.com",
    "origin": "http://mtiyouyuan.com",
    "instanceId": "",
    "moduleId": "",
    "r": [
        {
        "application": "luckDraw",
        "cookieId": "dont know",
        "openId": "buxiang",
        "sites": "buyongdecaoshu",
        "type": "",
        "objectId": "20"
        }
    ],
    "sess":loginSess
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "a0491964-822c-aed2-c85d-ae3ecc424b17"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful_getvalue("POST", domain + path, payload, headers, type, type,"content")
# collect_cancel/取消收藏信息
def get_most_collect_cancel(type,domain,collectionid,loginSess):
    path = "/collect/cancel"
    print "domain:", domain + path
    payload = {
        "r":collectionid,
        "sess": loginSess
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "6fb8b12c-f1c2-d4a2-5569-06dbe4b4b75e"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# collect_search/查询收藏的信息列表
def get_most_collect_search(type,domain,loginSess):
    path = "/collect/search"
    print "domain:", domain + path
    payload = {
    "start": 1,
    "num": 1,
    "sort": 1,
    "r": {
    "application": "luckDraw",
    "cookieId": "cookieId",
    "openId": "openId",
    "type": "",
    "objectId": "20"
    },
    "sess": loginSess,
    "_cache_with_cached": "1",
    "_cache_refresh": "1",
    "_cache_timeout": "60"
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "9bc1388e-7e26-6871-d009-e82f045d040d"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# articleCategory_getList/获取栏目列表
def get_most_articleCategory_getList(type,domain,tenantId,categoryId):
    path = "/articleCategory/getList"
    print "domain:", domain + path
    payload = {
    "tenantId": tenantId,
    "moduleId": "",
    "instanceId": "",
    "isEnabled": -1,
    "articleCategoryId": ""+categoryId+""
    }
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "b98e0e58-0f96-bf24-3bd6-960a5676d353"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# article_share/文章分享
def get_most_article_share(type,domain,articleId,wechatId):
    path="/article/share"
    print "domain:", domain + path
    payload = {
            "url":"https://hwuat.smarket.net.cn/f/27bfd3aaa163a0b75e40770732dbbaa3/html/info.html?articleId="+articleId+"&configId=38114&weChatId="+wechatId+"&scope=snsapi_userinfo&retCode=0&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwcm92aWRlcklkIjoib3RZemV0MU9RcTV3SC0wekNzRWI2X2FPaGR5ZyIsIm5hbWUiOm51bGwsIm5pY2tuYW1lIjoiXHU3YTBiXHU1MjFhIFx1ZTA1MCIsImF2YXRhciI6Imh0dHA6XC9cL3RoaXJkd3gucWxvZ28uY25cL21tb3BlblwvdmlfMzJcL0RZQUlPZ3E4M2VySXVtY0h1OTRpYldmdG9wbHBUcnN6Slg3UVc4OXJDUEJOWTU0SlNNZEpBdjBoaWNJUktpYURrUUNYY1Vvd1ZEZktZS0xvZFpWWEFMbTJnXC8xMzIiLCJlbWFpbCI6bnVsbCwicHJvdmlkZXIiOiJ3ZWNoYXQiLCJ0ZW5hbnRJZCI6IjUxOSIsInNiYXNlVG9rZW4iOiJhMGIzM2QzMTZlODE5ODhiN2ZjODZiZTk4Mzc2OTMzMyIsIm9yaWdpbmFsIjpbXSwidW5pb25JZCI6Im9oMV9Ld3BkLTF0cWsyNmgxVkE2RTNoOXVaUW8ifQ.cspezDgX5umiWievMtNiwJJnxWO-qDRQU-pDazqs0G0","globalUserId":"5709b38974561c2191bc607dbb485b94"
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "2fc8e8e6-93eb-64b8-7c39-73581836e75a"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# file_folder_getInsOfFileList/获取实例下的文件列表
def get_most_file_folder_getInsOfFileList(type,domain,tenantId):
    path="/file/folder/getInsOfFileList"
    print "domain:", domain + path
    payload ={"tenantId": tenantId,"instanceId": "","start": 0,"num": 20,"searchCondition": "","loadType": 0}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "483ad0b8-aefd-95b9-bccc-7ea04959ac84"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# questionary_exam_action/用户答题
def get_most_questionary_exam_action(type,domain,questionid_sj):
    path="/questionary/exam/action"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={"globalUserId":createTime,"city":"","country":"","gender":"","groupId":"","groupid":"","headImgUrl":"","headimgurl":"","language":"","nickname":"","openId":"","openid":"","authCode":"","province":"","remark":"","sex":"","subscribe":"","subscribeTime":"","subscribe_time":"","name":"","memberId":"","unique":"","uniqueType":"","session":"","needWechat":"false","questionaryId":questionid_sj,"referenceUrl":"","options":[{"fieldName":"name","value":"gaoming"},{"fieldName":"mobile","value":"13393213135"},{"id":"168960","selected":[1]},{"id":"168961","selected":[2]}],"url":"https://f.smarket.net.cn/s/template/dd13c38de8fadfd8c5714e225f798a21/view/answer.html?questionaryId=6224&configId=251344","preview":0,"sess":"","browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","browser":"Chrome","version":"66.0.3359.181","os":"Windows","equipment":"pc","resolution":"1366X768","referenceUrl":"","referenceTitle":"","sessionId":"6c0257bde285d60356ae4a070101d6f3"}}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "3ecfc208-650c-bb9b-4abe-e30c1f68ee6b"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_guest_getList/获取会议嘉宾列表
def get_most_seminar_guest_getList(type,domain,tenantId,seminarId):
    path="/seminar/guest/getList"
    print "domain:", domain + path
    payload={"tenantId": tenantId, "seminarId": seminarId}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "9948e192-f0f7-fa50-d4a0-db84bb747d34"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_guest_getGroupList/获取嘉宾列表
def get_most_seminar_guest_getGroupList(type,domain,tenantId,seminarId):
    path="/seminar/guest/getGroupList"
    print "domain:", domain + path
    payload={"tenantId": tenantId, "seminarId": seminarId}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "aac13f1d-2ce8-56a7-335c-bb14aa4ac809"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_guest_field_Get/获取嘉宾字段列表
def get_most_api_seminar_guest_field_Get(type,domain,tenantId):
    path="/api/seminar/guest/field/get"
    print "domain:", domain + path
    payload = {"tenantId": tenantId}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "6be7eb93-13b0-7954-7f44-ab938e7d8cd2"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# guest_get/获取全局嘉宾信息
def get_most_guest_get(type,domain,tenantId,guestId):
    path="/guest/get"
    print "domain:", domain + path
    payload = {"tenantId": tenantId,"guestId": guestId}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "17ec0888-5f04-d572-1a5a-6b2b30f52de3"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# guest_getList/取租户嘉宾列表
def get_most_guest_getList(type,domain,tenantId):
    path = "/guest/getList"
    print "domain:", domain + path
    payload = {
  "tenantId":tenantId,
  "guestTypeId": "285",
  "key": "",
  "orderType": "createTime",
  "start": 0,
  "num": 10
}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "6169247e-4ede-92d0-d847-e0e3d7df6c59"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# questionary_view/浏览问卷
def get_most_questionary_view(type, domain, questionid_wj):
    path="/questionary/view"
    print "domain:", domain + path
    payload={
          "questionaryId": ""+questionid_wj+"",
          "instanceId": "",
          "globalUserId": "60833f5d0335c945182342472d7499c7",
          "sess": "",
          "url": "https://hwuat.smarket.net.cn/f/e2ba9d7e12c7e74fa9ccb58318acc60d/view/PcQuestionnaire.html?questionaryId=1399&configId=38184",
          "referenceUrl": "",
          "browseInfo": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "browser": "Chrome",
            "version": "69.0.3497.100",
            "os": "Windows",
            "equipment": "电脑端",
            "resolution": "1920X1080",
            "referenceUrl": "",
            "referenceTitle": ""
           }
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "eadf40bd-932f-dd97-a62b-8e231eff5226"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# questionary_action/提交问卷
def get_most_questionary_action(type, domain, questionid_sj):
    path="/questionary/action"
    print "domain:", domain + path
    payload={
          "globalUserId": "60833f5d0335c945182342472d7499c7","city": "","country": "","gender": "","groupId": "","groupid": "","headImgUrl": "",
          "headimgurl": "","language": "","nickname": "","openId": "","openid": "","authCode": "","province": "","remark": "","sex": "","subscribe": "","subscribeTime": "",
          "subscribe_time": "","name": "","memberId":"","unique": "","uniqueType": "","session": "","needWechat":"",
          "questionaryId":""+questionid_sj+"","referenceUrl": "http://hwuat.smarket.net.cn/tool/questionaire/index.html",
          "options": [{"fieldName": "name","value": "s1"}, {"fieldName": "mobile","value": "15960167982"}],
          "url": "https://hwuat.smarket.net.cn/f/e2ba9d7e12c7e74fa9ccb58318acc60d/view/PcQuestionnaire.html?questionaryId=1399&configId=38184&preview=1",
          "preview": 1,"sess": "",
          "browseInfo": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "browser": "Chrome","version": "69.0.3497.100","os": "Windows","equipment": "电脑端","resolution": "1920X1080",
            "referenceUrl": "http://hwuat.smarket.net.cn/tool/questionaire/index.html","referenceTitle": "","sessionId": "590bd757114273ec5157138628b7dae5"
          }
        }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "2ef43418-7401-efe8-6309-b5ea11b50c94"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# article/like-文章点赞
def get_most_article_like(type, domain,articleId,wechatId,loginSess):
    path="/article/like"
    print "domain:", domain + path
    payload={"articleId":articleId,"globalUserId":"6011594ff2ae3ad38866d2b437df1d29","openId":"","sess":"","weChatId":wechatId,
             "resolution":"1920*1080","url":"https://hwuat.smarket.net.cn/f/27bfd3aaa163a0b75e40770732dbbaa3/html/info.html?articleId=107612&configId=33193","referenceUrl":"","browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
             "browser":"Chrome","version":"70.0.3538.110","os":"Windows","equipment":"电脑端","resolution":"1920X1080","referenceUrl":"",
              "referenceTitle":"","sessionId":"\""+loginSess+"\""}}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "5b434528-b0d4-40d3-79a6-71ff8928f6c4"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# comment_create/新增文章评论
def get_most_comment_create(type, domain, tenantId,nodeId,article_topicId):
    path="/comment/create"
    print "domain:", domain + path
    payload={"topicId":article_topicId,"tenantId":tenantId,"nodeId":nodeId,"moduleId":"0","instanceId":"0","isAnonymous":0,"content":"good","commentId":0,"openId":"","cookieId":"6011594ff2ae3ad38866d2b437df1d29","subVersionId":"109316","sess":"","title":"文章1","weChatId":0,"browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36","browser":"Chrome","version":"70.0.3538.110","os":"Windows","equipment":"电脑端","resolution":"1360X768","referenceUrl":"","referenceTitle":"","sessionId":"\"00277a0b9d591de8030333d95de3473e\""},"url":"https://hwuat.smarket.net.cn/f/27bfd3aaa163a0b75e40770732dbbaa3/html/info.html?articleId=109316&configId=39259","referenceUrl":"","globalUserId":"6011594ff2ae3ad38866d2b437df1d29"}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "daa22308-9ebe-1ff8-710f-773ae648e1aa"
    }
    return api_quester_common().Is_successful_getvalue("POST", domain + path, payload, headers, type, type,"content")
# comment_front_delete/删除评论 内容
def get_most_comment_front_delete(type, domain,topicid,content):
    path="/comment/front/delete"
    print "domain:", domain + path
    payload={"topicId":topicid,"openId":"","cookieId":"6011594ff2ae3ad38866d2b437df1d29","commentId":content,"sess":"","globalUserId":"6011594ff2ae3ad38866d2b437df1d29"}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "a860cebd-ec8c-b841-b93f-25adf2c8d580"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# comment_like/点赞评论内容
def get_most_comment_like(type, domain, content,loginSess):
    path="/comment/like"
    print "domain:", domain + path
    payload={"commentIds":[int(content)],"memberId":0,"openId":"","cookieId":"6011594ff2ae3ad38866d2b437df1d29","sess":"","globalUserId":"6011594ff2ae3ad38866d2b437df1d29","browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36","browser":"Chrome","version":"70.0.3538.110","os":"Windows",
            "equipment":"电脑端","resolution":"1920X1080","referenceUrl":"","referenceTitle":"","sessionId":str(loginSess)}}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "913a1ce8-a856-b5a7-9b9b-d5da3c2b4491"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# article_getListByTag/获取租户下文章列表，可通过标签筛选
def get_most_article_getListByTag(type, domain,tenantId):
    path="/article/getListByTag"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "tagName": "",
        "start": "0",
        "num": "10"
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "6c315149-1f89-18f2-6ed4-2d699d460164"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# article_getListForProject/获取文章列表
def get_most_article_getListForProject(type, domain, tenantId,categoryId,seminarId_instanceId):
    path="/article/getListForProject"
    print "domain:", domain + path
    payload={
          "tenantId": tenantId,"moduleId": 3,"instanceId": int(seminarId_instanceId),"articleCategoryId": int(categoryId),"title": "","isRecommend": -1,"isStick": -1,
          "start": 0,"num": 20,"withStat": 1,"withTemplate": 1,"getAll": 1,"typeId": "","searchColumns": [],"tagsInfo": [{"fieldName": ["tagA"]}]
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "124c4ed6-18c3-52ea-0e64-e6298b9126b9"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# article_getRecommendedList/获取栏目的子栏目中推荐的文章列表
def get_most_article_getRecommendedList(type, domain,categoryId):
    path="/article/getRecommendedList"
    print "domain:", domain + path
    payload= {"articleCategoryId": categoryId,"start": 0,"num": 5}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "f947b69f-1887-1a71-1c2e-16148ada2773"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# article_getSharedList/获取分享文章列表
def get_most_article_getSharedList(type, domain, tenantId,nodeId,bakSess):
    path="/article/getSharedList"
    print "domain:", domain + path
    payload={"tenantId": tenantId,"nodeId": nodeId,"moduleId": -2,"instanceId": -1,"title": "","searchTenantId": -1,"searchModuleId": -1,"searchInstanceId": -1,
        "articleCategoryId": -1,"onlyOthers": 0,"start": 0,"num": 20,"sess":bakSess}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "053e2529-917d-a573-26e3-d48d0aaf2be3"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# file_getListForWeChat/获取微信下的文件
def get_most_file_getListForWeChat(type, domain,fileIds):
    path="/file/getListForWeChat"
    print "domain:", domain + path
    payload={
    "fileIds": [
      fileIds
    ]
  }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "59bfa750-5c2f-1217-caaf-79bcdc077b5a"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# poll_get/获取投票
def get_most_poll_get(type,domain,pollId):
    path="/poll/get"
    print "domain:", domain + path
    payload={"pollId": pollId}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "327f2641-a9cf-9e84-adaf-4f561f2872d3"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_agenda_get/获取会议日程信息
def get_most_seminar_agenda_get(type,domain,seminarId,agendaId):
    path="/seminar/agenda/get"
    print "domain:", domain + path
    payload ={"seminarId":seminarId,"agendaId":agendaId}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "e338f66e-d040-cf14-b088-403857a82569"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_agenda_getGroupList/获取会议日程按天分组
def get_most_seminar_agenda_getGroupList(type,domain,seminarId):
    path = "/seminar/agenda/getGroupList"
    print "domain:", domain + path
    payload = {"seminarId": seminarId}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "e338f66e-d040-cf14-b088-403857a82569"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# poll_action/提交投票
def get_most_poll_action(type,domain,pollId):
    path="/poll/action"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = {
    "globalUserId": createTime,
    "city": "",
    "country": "",
    "gender": "",
    "groupId": "",
    "groupid": "",
    "headImgUrl": "",
    "headimgurl": "",
    "language": "",
    "nickname": "",
    "openId": "",
    "openid": "",
    "authCode": "",
    "province": "",
    "remark": "",
    "sex": "",
    "subscribe": "",
    "subscribeTime": "",
    "subscribe_time": "",
    "name": "",
    "memberId": "",
    "unique": "",
    "uniqueType": "",
    "session": "",
    "needWechat": "",
    "pollId": pollId,
    "referenceUrl": "",
    "options": [
        {
            "fieldName": "name",
            "value": "邢英丽"
        },
        {
            "fieldName": "mobile",
            "value": "15201232181"
        }
    ],
    "url": "https://f.smarket.net.cn/s/template/2d8786076af18578c93bd945f0681953/view/vote.html?pollId=2319&configId=251376",
    "preview": 0,
    "sess": "",
    "browseInfo": {
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        "browser": "Chrome",
        "version": "66.0.3359.181",
        "os": "Windows",
        "equipment": "电脑端",
        "resolution": "1366X768",
        "referenceUrl": "",
        "referenceTitle": "",
        "sessionId": "ec69f3edd1c9908cb8cfeb1e4528488e"
    }
}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "d45abb32-53a3-42ac-bf57-6fd73e33fda9"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# poll_getList/获取投票列表
def get_most_poll_getList(type,domain,tenantId,seminarId_instanceId):
    path="/poll/getList"
    payload ={
      "tenantId":tenantId,
      "instanceId":seminarId_instanceId,
      "attachId": "4813",
      "name": "",
      "status": 1,
      "start": 0,
      "num": 10000
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "af0a5aa3-dc8e-4277-9ea3-60049db20980"
        }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# poll_HasParticipation/浏览投票
def get_most_poll_HasParticipation(type,domain,pollId):
    path = "/poll/HasParticipation"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload ={
  "pollId":pollId,
  "globalUserId":createTime,
  "openId": "",
  "referenceUrl": "",
  "url": "",
  "sess": ""
}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "92a0e1a6-2dc0-4696-9c22-93a017bdaf0c"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# poll_sendCheckCode/投票发送验证码
def get_most_poll_sendCheckCode(type,domain,pollId):
    path = "/poll/sendCheckCode"
    print "domain:", domain + path
    payload ={
  "pollId": pollId,
  "mobile": "133932133135"
}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "5fe082df-9c24-4e50-8a76-68df2947a790"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#poll_start/该接口为后台接口，后期即将移除，请不要继续使用，开始投票
def get_most_poll_start(type,domain,tenantId,seminarId_instanceId,pollId,bakSess):
    path = "/poll/start"
    print "domain:", domain + path
    payload ={
  "tenantId": tenantId,
  "instanceId": seminarId_instanceId,
  "pollId": pollId,
  "sess": bakSess
}
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "94bfe8b7-f1c6-4cac-a84c-38b6e21e35bf"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#poll_stat_getResult/获取每个投票选项的结果数量
def get_poll_stat_getResult(type, domain,pollId):
    path = "/poll/stat/getResult"
    print "domain:", domain + path
    payload = {"pollId": pollId,"itemId": "5"}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "35bb0955-8c62-4a84-a0e8-b104f1e34cbf"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#poll_stat_getTotal/返回总投票数
def get_poll_stat_getTotal(type, domain,pollId):
    path = "/poll/stat/getTotal"
    print "domain:", domain + path
    payload = {"pollId": pollId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "5205166d-f796-40cc-ad58-9066382d02b8"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#poll_tool_checkRegistration/报名前验证
def get_poll_tool_checkRegistration(type, domain,pollId,seminarId_instanceId,loginSess):
    path = "/poll/tool/checkRegistration"
    print "domain:", domain + path
    payload = {
        "pollId": pollId,
        "cookieId": "",
        "instanceId": seminarId_instanceId,
        "openId": "oG80v1StB4PwxMWiPFbNyPe1bz14",
        "sess": loginSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "dbe56efd-22d6-48c2-b31c-99aebe9e99bd"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#poll_view/浏览投票
def get_poll_view(type, domain,pollId):
    path = "/poll/view"
    print "domain:", domain + path
    payload = {
        "pollId":pollId,
        "globalUserId": "",
        "openId": "",
        "referenceUrl": "",
        "url": "",
        "sess": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "d74ab5b2-67b5-4392-8c2b-77b500f1bbde"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#product_crossLine_getList/获取租户下的某一分类的多产品线下的产品列表
def get_product_crossLine_getList(type, domain,tenantId):
    path = "/product/crossLine/getList"
    print "domain:", domain + path
    payload = {
        "tenantId": tenantId,
        "keyword": "",
        "start": 0,
        "num": 10,
        "isNew": "0",
        "categoryId": "0",
        "withSoldOut": "0"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "5a7b685c-f5cf-47b4-8526-46a026c2e298"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#product_get/获取产品详细信息
def get_product_get(type, domain,productLine):
    path = "/product/get"
    print "domain:", domain + path
    payload = {"productId": productLine}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "163a9fb4-9b3e-470f-9fda-2d106210661e"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#product_getList/获取产品线下产品列表
def get_product_getList(type, domain,bakSess,productLineId,tenantId):
    path = "/product/getList"
    print "domain:", domain + path
    payload = {
    "command": {
        "size": 0,
        "orn": "02-0001-00000001",
        "dst": "01-0401-00000001",
        "type": 2,
        "sess":bakSess,
        "seq": 0,
        "ver": 1000,
        "body": {
            "productLineId":productLineId,
            "keyword": "",
            "start": 0,
            "isNew": 0,
            "num": 18,
            "withSoldOut": 1,
            "tenantId":tenantId
        },
        "cmd": "product.getList"
    }
}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "ccd08b64-c342-47ac-8a9d-b491e698f7d8"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#productLine_category_getCategoryTreeList/获取产品线分类树
def get_productLine_category_getCategoryTreeList(type, domain,productLineId):
    path = "/productLine/category/getCategoryTreeList"
    print "domain:", domain + path
    payload = {"productLineId":productLineId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "383a3c67-312d-46dc-a3db-04db637581a8"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#productLine_category_getConfigInfo/获取某产品线下具体某个字典值的配置信息
def get_productLine_category_getConfigInfo(type, domain,productLineId):
    path = "/productLine/category/getConfigInfo"
    print "domain:", domain + path
    payload = {"productLineId":productLineId,"dicValueId": 1}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "7efeb961-09e1-4a94-8839-4b7584676eb2"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#productLine_category_getDetailList/获取产品线分类详细列表
def get_productLine_category_getDetailList(type, domain,productLineId):
    path = "/productLine/category/getDetailList"
    print "domain:", domain + path
    payload = {  "productLineId": productLineId,"dicId": ""}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "dd7ae81a-b65e-43b0-8889-f6b953e84447"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# productLine_category_getList/获取产品线下产品分类的子分类信息
def get_most_productLine_category_getList(type, domain, productLineId,dicId):
    path="/productLine/category/getList"
    print "domain:", domain + path
    payload={
        "productLineId": ""+productLineId+"",
        "dicId": ""+dicId+""
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "43185da5-0e71-88dc-c6fc-b481ca86dbd3"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# productLine_field_get/获取某个产品线的字段列表
def get_most_productLine_field_get(type, domain, productLineId):
    path="/productLine/field/get"
    print "domain:", domain + path
    payload={
         "productLineId": ""+productLineId+""
           }
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "6179d72e-5c89-0de2-cb23-62f8e9406a96"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# productLine_get/获取产品线的信息
def get_most_productLine_get(type, domain, productLineId):
    path="/productLine/get"
    print "domain:", domain + path
    payload={
         "productLineId": ""+productLineId+""
           }
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "f8b58fba-46b2-1e1f-7f81-c8e4dc18b347"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# productLine_getList/获取租户下产品线列表
def get_most_productLine_getList(type, domain, tenantId):
    path="/productLine/getList"
    print "domain:", domain + path
    payload={
        "tenantId": ""+tenantId+"",
        "withDeleted": 1,
        "num": 10,
        "start": 0
           }
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "4da0d4f2-d2cc-5175-0043-60436f5afd98"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# weChat_get/该接口为后台接口，后期即将移除，请不要继续使用，获取微信信息
def get_most_weChat_get(type, domain, wechatId,bakSess):
    path="/weChat/get"
    print "domain:", domain + path
    payload={
        "weChatId": ""+wechatId+"",
        "sess": ""+bakSess+""
           }
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "17a53f9d-aafb-5910-4541-6a4c4d0960e3"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# weChat_getAppId/获取微信信息
def get_most_weChat_getAppId(type, domain, wechatId):
    path="/weChat/getAppId"
    print "domain:", domain + path
    payload={
        "weChatId": ""+wechatId+"",
           }
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "8ff2cc5b-1e67-60a3-2ff3-0e5a432aa33f"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# weChat_getConfig/做微信签名用，获取jssdk配置
def get_most_weChat_getConfig(type, domain, wechatId):
    path="/weChat/getConfig"
    print "domain:", domain + path
    payload={
        "weChatId": int(wechatId),
        "jsApiList": [
        "stopRecord",
        "onVoiceRecordEnd",
        "uploadVoice",
        "startRecord"
    ],
        "url": "http://uao.so/907bb3d9ec",
        "onDebug": "false"
           }
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "21ca1a81-9c04-010f-ea36-3cc97418e4d1"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# weChat_getDef/获取各平台默认微信号的配置信息
def get_most_weChat_getDef(type, domain):
    path="/weChat/getDef"
    print "domain:", domain + path
    payload={
           }
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "66efca79-5a7a-22ea-f2ee-c2560cd71eb5"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# weChat_getDefWx/获取各平台默认微信号的配置信息
def get_most_weChat_getDefWx(type, domain):
    path="/weChat/getDefWx"
    print "domain:", domain + path
    payload={
        "_cache_with_cached": "1",
        "_cache_refresh": "1",
        "_cache_timeout": "60"
           }
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "67e3c3af-32f5-6f79-f82a-8428d4fa07c6"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_product_get/获取产品详情
def get_most_api_product_get(type, domain,tenantId,productLine):
    path="/api/product/get"
    print "domain:", domain + path
    payload={
        "tenantId": ""+tenantId+"",
        "productId": ""+productLine+""
           }
    headers = {
     'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "31495218-17e2-f02b-db92-5997b467de90"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_productLine_category_config_get/获取某产品线下具体某个字典值的配置信息
def get_most_api_productLine_category_config_get(type, domain, tenantId, productLineId):
    path="/api/productline/category/config/get"
    print "domain:", domain + path
    payload={"tenantId": tenantId,"productLineId": productLineId,"dicValueId": "484363"}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "f21fd14b-8a3c-d28d-ab1b-756e9b784169"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# api_productLine_category_query/获取产品线分类树
def get_most_api_productLine_category_query(type, domain, tenantId,productLineId,dicId):
    path="/api/productline/category/query"
    print "domain:",domain+path
    payload={"tenantId": tenantId,"productLineId": productLineId,"dicId": dicId}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "9aeed18b-f24d-d24a-9553-8a122c58790d"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# api_productLine_field_get/获取某个产品线的字段列表
def get_most_api_productLine_field_get(type, domain, tenantId, productLineId):
    path="/api/productline/field/get"
    print "domain:",domain+path
    payload={"tenantId": tenantId,"productLineId": productLineId}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "ea213fc5-7331-b9db-ef40-538c67f3567e"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_event_interaction_check/检查什么情况下可以继续投票、答问卷，会场开放过程中可以答
def get_most_webinar_event_interaction_check(type, domain,webinarId_instanceId):
    path="/webinar/event/interaction/check"
    print "domain:",domain+path
    payload={"instanceId":webinarId_instanceId}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "98cde85d-0da4-ab7f-276f-9e10ba0e6e72"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_event_interaction_pollResult/答完问卷后置接口，记录互动结果
def get_most_webinar_event_interaction_pollResult(type, domain, loginSess,pollId):
    path="/webinar/event/interaction/pollResult"
    print "domain:",domain+path
    payload={"globalUserId":"d8b6470260f9903c2bbd93243637acba","city":"","country":"","gender":"","groupId":"","groupid":"","headImgUrl":"","headimgurl":"","language":"","nickname":"","openId":"","openid":"","authCode":"","province":"","remark":"","sex":"","subscribe":"","subscribeTime":"","subscribe_time":"","memberId":"null","unique":"","session":loginSess,"needWechat":"false","pollId":pollId,"referenceUrl":"http://f.smarket.net.cn/s/template/ddaae85fe48ff1372217f0db2def1676/html/meeting.html?instanceId=47019&webinarId=7356&customFormId=15968&trackId=2:74&linkId=32246&signUpNotify=true","options":[{"fieldName":"name","value":"柳旦旦"},{"fieldName":"enterprise","value":"sino"},{"fieldName":"mobile","value":"18032257279"}],"url":"https://f.smarket.net.cn/s/template/2d8786076af18578c93bd945f0681953/view/vote.html?pollId="+pollId+"&configId=272175","preview":0,"sess":loginSess,"enteredId":"265680","browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36","browser":"Chrome","version":"68.0.3440.106","os":"Windows","equipment":"电脑端","resolution":"1920X1080","referenceUrl":"http://f.smarket.net.cn/s/template/ddaae85fe48ff1372217f0db2def1676/html/meeting.html?instanceId=47019&webinarId=7356&customFormId=15968&trackId=2:74&linkId=32246&signUpNotify=true","referenceTitle":"","sessionId":loginSess}}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "ee3bad51-1aeb-5af8-d2f0-a50f57f8b656"
        }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_open_attend/修改参会人数,并返回登录人的地址
def get_most_webinar_open_attend(type, domain, tenantId, webinarId_instanceId):
    path="/webinar/open/attend"
    print "domain:",domain+path
    payload={"tenantId": tenantId,"instanceId": webinarId_instanceId}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "5dec72d6-3ff9-4496-2194-b776de7b2fcb"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#  webinar_open_checkRegistration/查询用户是否可以报名接口
def get_most_webinar_open_checkRegistration(type, domain, tenantId, webinarId_instanceId):
    path="/webinar/open/checkRegistration"
    print "domain:",domain+path
    payload={
          "tenantId": tenantId,
          "instanceId": webinarId_instanceId,
          "includeFormData": "true",
          "cookieId": "39e5bd2a4a1c363d09b9fdd09323b3d8",
          "openId": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "497eb1da-6295-403f-8aa4-9a8fb3838949"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_open_getApplicantInfo/获取会议信息
def get_most_webinar_open_getApplicantInfo(type, domain, webinarId_instanceId,bakSess):
    path="/webinar/open/getApplicantInfo"
    print "domain:",domain+path
    payload={
        "instanceId": webinarId_instanceId,
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "9ee1091f-9b48-445a-8107-bb267b993e0d"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_open_getAttendList/获取已报名的会议列表
def get_most_webinar_open_getAttendList(type, domain, tenantId,bakSess):
    path="/webinar/open/getAttendList"
    print "domain:",domain+path
    payload={
        "tenantId": tenantId,
        "start": 0,
        "num": 12,
        "videoType": "1",
        "includeExtends": "1",
        "includeGuest": "0",
        "orderBy": "createTime",
        "sort": "desc",
        "sess":bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "5daafc0d-e888-4294-8d90-060d0299cbc6"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# webinar_open_getCustomFormInfo/获取自定义表单
def get_most_webinar_open_getCustomFormInfo(type, domain, tenantId, webinarId_instanceId,customFormId):
    path="/webinar/open/getCustomFormInfo"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "instanceId": webinarId_instanceId,
        "customFormId":customFormId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "4f040162-ac68-48bf-917c-580305431104"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_bigScreen_forBigScreenWall_checkIn/有问题，微信签到
def get_most_seminar_bigScreen_forBigScreenWall_checkIn(type,domain,contactId,loginSess,bigScreenId):
    path="/seminar/bigScreen/forBigScreenWall/checkIn"
    print "domain:", domain + path
    payload ={
      "openId":"{{openId}}",
      "nickName": "gaoming",
      "headImgUrl": "",
      "bigScreenId":bigScreenId,
      "contactId":contactId,
      "sess": loginSess
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "48a7555b-ad05-400f-9cee-0e32c1b462c1"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_bigScreen_forBigScreenWall_checkIn/有问题，微信签到
def get_HW_UAT_most_seminar_bigScreen_forBigScreenWall_checkIn(type,domain,contactId,loginSess,bigScreenId):
    path="/seminar/bigScreen/forBigScreenWall/checkIn"
    print "domain:", domain + path
    payload ={
      "openId":"{{openId}}",
      "nickName": "gaoming",
      "headImgUrl": "",
      "bigScreenId":"731",
      "contactId":"478620",
      "sess": loginSess
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "48a7555b-ad05-400f-9cee-0e32c1b462c1"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_open_getDemandInfo/得到一个点播会议的详情信息
def get_most_webinar_open_getDemandInfo(type,domain,tenantId,webinarId_instanceId):
    path="/webinar/open/getDemandInfo"
    print "domain:", domain + path
    payload ={
        "tenantId": tenantId,
        "instanceId": webinarId_instanceId
      }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "cdc4f33c-226a-40ef-942c-c6aaaf191f8e"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_open_getServerTime/获取服务器时间
def get_most_webinar_open_getServerTime(type,domain,tenantId):
    path="/webinar/open/getServerTime"
    print "domain:", domain + path
    payload ={
        "tenantId": tenantId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "9b43075a-b29a-4539-92f3-fd1438fd2db9"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_open_getVideoTimeLine/获取视频信息
def get_most_webinar_open_getVideoTimeLine(type,domain,tenantId):
    path="/webinar/open/getVideoTimeLine"
    print "domain:", domain + path
    payload ={
        "videoId": "",
        "tenantId":tenantId
      }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "96aa01e1-4cda-42af-8798-40782dfe9ec1"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_open_getWebinarInfo/获取会场详细信息
def get_most_webinar_open_getWebinarInfo(type,domain,tenantId,webinarId_instanceId):
    path="/webinar/open/getWebinarInfo"
    print "domain:", domain + path
    payload={
        "instanceId": webinarId_instanceId,
        "tenantId": tenantId,
        "includeCustomField": 0
      }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "9e454247-f3e7-4af2-bbea-abf8f681448d"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_open_getWebinarList/获取直播会议列表
def get_most_webinar_open_getWebinarList(type,domain,tenantId):
    path="/webinar/open/getWebinarList"
    print "domain:", domain + path
    payload ={
        "tenantId": tenantId,
        "startTime": "",
        "status": 3,
        "keyword": "",
        "orderBy": "createTime",
        "videoType": "1",
        "start": 0,
        "num": 12,
        "includeGuest": "true"
      }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "c7caa4d6-8569-4456-b3fd-316e95e8d88b"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#customForm_action/线上会报名
def get_most_customForm_action(type,domain,loginSess,customFormId,webinarId_instanceId):
    path="/customForm/action"
    print "domain:", domain + path
    payload={
        "sess": loginSess,
        "customFormId": customFormId,
        "linkId": "7231",
        "instanceId": webinarId_instanceId,
        "globalUserId": "6011594ff2ae3ad38866d2b437df1d29",
        "url": "https://hwuat.smarket.net.cn/f/39dc846dd6e88089d3990c165e4fad03/view/customForm.html?instanceId=10015&webinarId=530&customFormId=3582&trackId=2:74&linkId=7231&configId=38947&returnUrl=http%3A%2F%2Fhwuat.smarket.net.cn%2Ff%2Fddaae85fe48ff1372217f0db2def1676%2Fhtml%2Fmeeting.html%3FinstanceId%3D10015%26webinarId%3D530%26customFormId%3D3582%26trackId%3D2%3A74%26linkId%3D7231%26signUpNotify%3Dtrue#",
        "referenceUrl": "https://hwuat.smarket.net.cn/f/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberId=878&memberFormId=878&trackId=0&memberSchemaId=318&configId=38461&backUrl=https%3A%2F%2Fhwuat.smarket.net.cn%2Ff%2F39dc846dd6e88089d3990c165e4fad03%2Fview%2FcustomForm.html%3FinstanceId%3D10015%26webinarId%3D530%26customFormId%3D3582%26trackId%3D2%3A74%26linkId%3D7231%26configId%3D38947%26returnUrl%3Dhttp%253A%252F%252Fhwuat.smarket.net.cn%252Ff%252Fddaae85fe48ff1372217f0db2def1676%252Fhtml%252Fmeeting.html%253FinstanceId%253D10015%2526webinarId%253D530%2526customFormId%253D3582%2526trackId%253D2%253A74%2526linkId%253D7231%2526signUpNotify%253Dtrue",
        "ver": "v2.0.1",
        "items": [
            {
                "fieldName": "name",
                "value": "eric"
            },
            {
                "fieldName": "mobile",
                "value": "15960167982"
            },
            {
                "fieldName": "email",
                "value": "1946898935@qq.com"
            },
            {
                "fieldName": "avatar",
                "value": {
                    "fileName": "",
                    "mapId": ""
                }
            },
            {
                "fieldName": "province",
                "value": [],
                "otherValue": ""
            },
            {
                "fieldName": "enterprise",
                "value": ""
            },
            {
                "fieldName": "department",
                "value": [],
                "otherValue": ""
            },
            {
                "fieldName": "position",
                "value": [],
                "otherValue": ""
            },
            {
                "fieldName": "gender",
                "value": [],
                "otherValue": ""
            },
            {
                "fieldName": "industry",
                "value": [
                    ""
                ],
                "otherValue": ""
            },
            {
                "fieldName": "f_3",
                "value": ""
            },
            {
                "fieldName": "m_wenben",
                "value": ""
            },
            {
                "fieldName": "m_liebiao",
                "value": [],
                "otherValue": ""
            },
            {
                "fieldName": "m_wenjian",
                "value": {
                    "fileName": "",
                    "mapId": ""
                }
            },
            {
                "fieldName": "m_shijian",
                "value": ""
            },
            {
                "fieldName": "m_file",
                "value": {
                    "fileName": "",
                    "mapId": ""
                }
            }
        ]
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "6abd5fc4-5c00-48ca-bb17-e944feb86bed"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_open_join/人员参会接口
def get_most_webinar_open_join(type,domain,loginSess,webinar_instanceId,tenantId):
    path="/webinar/open/join"
    print "domain:", domain + path
    payload={"sess":loginSess,"tenantId":tenantId,"instanceId":webinar_instanceId,"joinType":"1","cookieId":"9f2d77f59e6021ced3426596a46919cf","openId":"","url":"http://hwyhw.smarket.net.cn/f/ddaae85fe48ff1372217f0db2def1676/html/meeting.html?instanceId=15356&webinarId=1428&customFormId=5188&trackId=2:74&linkId=10443&signUpNotify=true","referenceUrl":"","globalUserId":"a2798c714589d500e3605c31b3817437"}

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "a6b5399f-70aa-8ad1-1c75-065d592aff7b"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:", payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_project_shenWan_GetWebinar/获取会议信息
def get_most_webinar_project_shenWan_GetWebinar(type,domain,webinarId_instanceId):
    path="/webinar/project/shenWan/GetWebinar"
    print "domain:", domain + path
    payload={
      "webinarId": webinarId_instanceId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "ad634a23-58ca-4439-965e-d19d7afe97cc"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_project_shenWan_GetListByIds/跟进会议id数组 获取会议列表
def get_most_webinar_project_shenWan_GetListByIds(type,domain,seminarId):
    path="/webinar/project/shenWan/GetListByIds"
    print "domain:", domain + path
    payload={"ids":[seminarId]}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "54848651-22ce-454e-833c-cbc4d7d0acde"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#webinar_project_shenWan_GetDemandList/获取已发布的点播列表
def get_webinar_project_shenWan_GetDemandList(type, domain,tenantId):
    path = "/webinar/project/shenWan/GetDemandList"
    print "domain:", domain + path
    payload = {"tenantId": tenantId,"keyword": "","start": 0,"num": 10}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "f2bec045-4e74-49b7-a5c2-ebe5bc57af55"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#webinar_open_trackingCode_getList/根据实例编号获取该实例的渠道追踪代码
def get_webinar_open_trackingCode_getList(type, domain,tenantId,webinarId_instanceId):
    path = "/webinar/open/trackingCode/getList"
    print "domain:", domain + path
    payload = {    "tenantId": tenantId,"instanceId": webinarId_instanceId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "d937ba60-3b74-4e82-b1d0-5bb5e23a2051"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#webinar_open_recordVideoViewCount/记录并获取点播视频的播放次数
def get_webinar_open_recordVideoViewCount(type, domain,tenantId,webinarId,videoId):
    path = "/webinar/open/recordVideoViewCount"
    print "domain:", domain + path
    payload = {  "tenantId" : tenantId,"webinarId": webinarId,"videoId"  : videoId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "03d82dda-2a71-4a9d-8b5c-33c07b14cca9"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#questionary_exam_repeatAction/用户重复回答试题保留最后一次结果
def get_questionary_exam_repeatAction(type, domain,loginSess,questionid_sj):
    path = "/questionary/exam/repeatAction"
    print "domain:", domain + path
    payload = {
        "sess": loginSess,
        "questionaryId": questionid_sj,
        "openId": "xxxwewex",
        "globalUserId": "1488088356",
        "referenceUrl": "source",
        "nickName": "naonao",
        "headImgUrl": "http://testf.smarket.net.cn/t/template/1759447356/images/img-success.png",
        "gender": 1,
        "city": "Wuhan City",
        "provice": "Hubei province",
        "country": "China",
        "options": [
            {
                "id": 1,
                "selected": [
                    1,
                    2
                ]
            }
        ],
        "preview": 0,
        "isRepeat": 1
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "9fa366e6-d354-4e27-8df5-8a7984f4d678"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#试卷添加题目
def get_toolb_add_title(type,domain,bakSess,questionid_sj,tenantId):
    path = "/toolb/index.php"
    print "domain:", domain + path
    # createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=questionary.setItems&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BquestionaryId%5D="+questionid_sj+"&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfieldType%5D=LIST&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfieldLevel%5D=4&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BitemId%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Bquestion%5D=%E5%8D%95%E9%80%89%E9%A2%981&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfieldName%5D=%E5%8D%95%E9%80%89%E6%A1%86&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BregularExpression%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BisCommon%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Btype%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Bkey%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Bnecessary%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Banswer%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BtotalScore%5D=10&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BleadsGrade%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BleadsGradeTitle%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BenableRegular%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5Bfocus%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5Btitle%5D=A&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5BpicMapId%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5BpicUrl%5D=%2F%2Fcdn.smarket.net.cn%2Fimages%2Fimg-pic-default.gif&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5BisFillIn%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5BisOther%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5Btext%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5Bscore%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5BscoreTitle%5D=%E4%B8%8D%E5%BE%97%E5%88%86&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5B%24%24hashKey%5D=object%3A3897&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B0%5D%5BisChecked%5D=false&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5Bfocus%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5Btitle%5D=B&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5BpicMapId%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5BpicUrl%5D=%2F%2Fcdn.smarket.net.cn%2Fimages%2Fimg-pic-default.gif&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5BisFillIn%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5BisOther%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5Btext%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5Bscore%5D=10&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5BscoreTitle%5D=%E5%BE%97%E5%88%86&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5B%24%24hashKey%5D=object%3A3901&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Boptions%5D%5B1%5D%5BisChecked%5D=true&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'cookie': "SMARKET_MEMBER_SESS=;",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "6241493e-0701-4e1d-95df-5f35288ebd57"
    }
    # payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers,type, type)
#questionary_exam_user_GenerateExam/生成试卷
def get_questionary_exam_user_GenerateExam(type,domain,questionid_sj):
    path = "/questionary/exam/user/GenerateExam"
    print "domain:", domain + path
    payload = {"sess": "","questionaryId": int(questionid_sj),"openId": "","globalUserId":"39e5bd2a4a1c363d09b9fdd09323b3d8","isSave": 1}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "17db3b3e-fa5d-4cc3-bfa5-3a46c6328921"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#webinar_open_getWebinarListAdvanced/获取直播会议列表（高级查询功能）,有问题
def get_webinar_open_getWebinarListAdvanced(type,domain,tenantId):
    path = "/webinar/open/getWebinarListAdvanced"
    print "domain:", domain + path
    payload = {
        "tenantId": str(tenantId),
        "startDate": "",
        "status": 3,
        "keyword": "",
        "orderby": "createTime",
        "start": 0,
        "num": 12,
        "fieldsDisplay": [
            "aa",
            "numberTest"
        ],
        "fieldsCondition": [
            {
                "fieldName": "numberTest",
                "fieldComparison": "=",
                "fieldValue": 23,
                "includeNull": "true"
            }
        ],
        "videoType": "1"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "17eddc3e-6d2d-447d-a4ca-ea1365908788"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful_status("POST", domain + path, payload, headers, type, type)
#questionary_exam_user_getAnswers/获取某人试卷的试题记录
def get_questionary_exam_user_getAnswers(type,domain,questionid_wj):
    path = "/questionary/exam/user/getAnswers"
    print "domain:", domain + path
    payload = {"questionaryId": questionid_wj, "openId": "{{openId}}", "globalUserId": "1111", "isSave": 1,
               "isGenerated": 1}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "5773e120-4f13-45e0-a606-3ff500e7bcca"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#questionary_exam_user_getSingleResult/获取某人的答题记录
def get_questionary_exam_user_getSingleResult(type,domain,questionid_sj,tenantId):
    path = "/questionary/exam/user/getSingleResult"
    print "domain:", domain + path
    payload = {"questionaryId": questionid_sj,"examResultId": 86,"tenantId":tenantId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "5773e120-4f13-45e0-a606-3ff500e7bcca"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#问卷设置短信发送验证码
def get_setting_Verification_code(type,domain,bakSess,questionid_wj,tenantId):
    path = "/toolb/index.php"
    print "domain:", domain + path
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=questionary.setItems&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BquestionaryId%5D="+questionid_wj+"&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Bid%5D=3841&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BschemaId%5D=482&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfieldName%5D=mobile&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BdisplayName%5D=%E6%89%8B%E6%9C%BA&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfieldType%5D=TEXT&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfileLimitType%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BtextLimitType%5D=SYSTEM&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BlistOptionType%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BlistDictId%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BdateLimitType%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BorderId%5D=2&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Bdeleted%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BisSystemed%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BisShow%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Brequired%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Benabled%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BerrorMessage%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BtextRegularExpression%5D=%5E1(3%7C4%7C5%7C7%7C8)%5Cd%7B9%7D%24&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BtextLength%5D=11&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BtextRegularId%5D=10&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BlistLimitType%5D=&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BmaxOptionId%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BisOverWrite%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BisRecordHistory%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BisExport%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BisLogin%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BisFormed%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BmemberFieldName%5D=mbr_member.mobile&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BidentFieldName%5D=mbr_identification.mobile&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BdefaultFieldId%5D=0&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BisSendSms%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BversionNumber%5D=2&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfieldId%5D=4&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BfieldLevel%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BcanEditFields%5D%5B%5D=errorMessage&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BcanEditFields%5D%5B%5D=required&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BcanEditFields%5D%5B%5D=isSendSms&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BtextDefaultRegType%5D=mobile&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BregularExpression%5D=%5E1(3%7C4%7C5%7C7%7C8)%5Cd%7B9%7D%24&command%5Bbody%5D%5Bitems%5D%5B0%5D%5Bdescription%5D=%E6%89%8B%E6%9C%BA%E5%8F%B7%E7%A0%81+&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BextendFieldId%5D=3841&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BschemaTextLength%5D=11&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BdisplayType%5D=1&command%5Bbody%5D%5Bitems%5D%5B0%5D%5BcustomerDisplayName%5D=%E6%89%8B%E6%9C%BA&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'cookie': "SMARKET_MEMBER_SESS=;",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "930bb483-4f84-4489-a56c-01253f0996f2"
    }
    # payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().post_request_successful("POST", domain + path, payload, headers, type, type,"desc")
# questionary_sendCheckCode/问卷发送验证码
def get_most_questionary_sendCheckCode(type, domain,questionid_wj,tenantId):
    path="/questionary/sendCheckCode"
    print "domain:", domain + path
    payload={
        "questionaryId": int(questionid_wj),
        "mobile": "15960167982",
        "tenantId": int(tenantId)
           }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "486428dc-8f71-ad55-4159-62d4b2f86642"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# shortUrl_getList/获取短地址
def get_most_shortUrl_getList(type, domain):
    path="/shortUrl/getList"
    print "domain:", domain + path
    payload={
        "withCreate": 0,
        "realUrlList": [
        "http://www.baidu.com/"
  ]
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "a9ca571c-004b-6800-f083-d27ddd34e872"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_webinar_contacts_get/获取报名人信息/返回报名人状态
def get_most_api_webinar_contacts_get(type, domain,tenantId,webinarId_instanceId,loginSess):
    path="/api/webinar/contacts/get"
    print "domain:", domain + path
    payload={
    "tenantId":""+tenantId+"",
    "webinarId":""+webinarId_instanceId+"",
    "sess":""+loginSess+"",
    "includeRegisterData":"false"
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "fbd007b5-e8bf-96d9-aaf7-57eff139ba1e"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# shortUrl_urlStats/获取短网址的统计信息
def get_most_shortUrl_urlStats(type, domain):
    path="/shortUrl/urlStats"
    print "domain:", domain + path
    payload={
    "shortUrl": "http://hwuat.smarket.net.cn/u/4F0IXJp"
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "950e2d3b-e1c0-b11d-9649-c822916fdd70"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_webinar_demand_get/获取点播信息
def get_most_api_webinar_demand_get(type, domain,tenantId,webinarId):
    path="/api/webinar/demand/get"
    print "domain:", domain + path
    payload={
    "tenantId":""+tenantId+"",
    "webinarId":""+webinarId+"",
    "includeFormField":"true"
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "3ad43c1d-376d-dd3f-076f-ddb6641c2662"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_webinar_query/获取会议列表
def get_most_api_webinar_query(type, domain,tenantId):
    path="/api/webinar/query"
    print "domain:", domain + path
    payload={
     "tenantId": ""+tenantId+"",
        "videoType": 1,
        "startTime": "",
        "status": 3,
        "keyword": "",
        "sort": {
            # "createTime": "desc"
        },
        "includeGuest": 0,
      "liveState":-1,
      "isSelectSignUp": 0,
      "sess": "",
      "tags": [
        {
          "wzbqsx": [
            "睡觉"
          ]
        },
        {
          "dsfxwyrdx": [
            "1-10"
          ]
        }
      ],
      "isAndTag": 0,
        "start": 0,
        "num": 50
           }
    headers = {
         'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "0535667e-c2cb-35c6-0af0-addf9dfc0b92"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# questionary_tool_checkRegistration/报名前验证
def get_most_questionary_tool_checkRegistration(type,domain,questionid_wj,webinarId_instanceId,loginSess):
    path="/questionary/tool/checkRegistration"
    print "domain:", domain + path
    payload={
    "questionnaireId": 1932,
    "cookieId": "39e5bd2a4a1c363d09b9fdd09323b3d8",
    "instanceId": webinarId_instanceId,
    "openId": "otqO01CM74B9qQ2ZFwGiglaZFxzg",
    "sess": loginSess
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "54f36c6a-e9a6-6c1f-2676-e94ee0c8e4da"
    }

    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# questionary_stat_getResultByAnswerRecord/获取[常规问卷、leads问卷、非随机试卷]答题记录列表(此接口项目使用)
def get_most_questionary_stat_getResultByAnswerRecord(type, domain,bakSess,questionid_wj):
    path="/questionary/stat/getResultByAnswerRecord"
    print "domain:", domain + path
    payload={
    "sess": ""+bakSess+"",
    "questionaryId": ""+questionid_wj+"",
    "hideTestData": 1,
    "completeItemsOptions": {
    # "{{id1}}": [
    #
    # ],
    # "{{id2}}": [
    #
    # ]
    },
    "identityId": 0,
    "keyword": "",
    "start": 0,
    "num": 20
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "18ed870c-bde6-9bce-23d7-366f11012079"
    }

    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_bigScreen_get/获取大屏详细信息
def get_most_seminar_bigScreen_get(type, domain,createCheckIn):
    path="/seminar/bigScreen/get"
    print "domain:", domain + path
    payload={
     "id": ""+createCheckIn+""
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "d4a63989-4789-490b-f408-6cd2ba42b835"
    }

    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_bigScreen_getListByGroup/获取大屏列表
def get_most_seminar_bigScreen_getListByGroup(type, domain,seminarId):
    path="/seminar/bigScreen/getListByGroup"
    print "domain:", domain + path
    payload={
        "groupId": "0",
        "seminarId": ""+seminarId+""
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "046956dc-6c27-a9f3-b8af-da07e67b0651"
    }

    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_bigScreen_getPollPreset/获取投票大屏预设信息
def get_most_seminar_bigScreen_getPollPreset(type, domain,tenantId,seminarId,createCheckIn,pollId):
    path="/seminar/bigScreen/getPollPreset"
    print "domain:", domain + path
    payload= {
        "tenantId": tenantId,
        "seminarId": seminarId,
        "screenId": createCheckIn,
        "pollId": pollId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "6e24499f-3da0-4ad9-81f9-e7a1c87814d9"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_bigScreen_updateCheckIn/更新签到大屏信息
def get_most_seminar_bigScreen_updateCheckIn(type,domain,seminarId,createCheckIn,signingPointId):
    path="/seminar/bigScreen/updateCheckIn"
    print "domain:", domain + path
    payload={
          "seminarId":seminarId,
          "id": createCheckIn,
          "name": "签到大屏(1)",
          "scale": "narrow",
          "groupId": "1",
          "signingPointId": signingPointId,
          "signingPoint": "普通签到点",
          "checkInByWeChat": "on",
          "checkInStatus": "on",
          "status": "on",
          "onTheWallField": "regInfo",
          "regOnSite": "on",
          "regFormId": "1",
          "regFormName": "asd",
          "interval": "3",
          "loop": "on",
          "isControl": "1",
          "url": "http://www.baidu.com"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "6f359c66-67cb-4541-9813-7ceb96a46711"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_bigScreen_updateLottery/该接口为后台接口，后期即将移除，请不要继续使用，更新留言大屏信息
def get_most_seminar_bigScreen_updateLottery(type,domain,seminarId,createCheckIn,topicId,bakSess):
    path="/seminar/bigScreen/updateLottery"
    print "domain:", domain + path
    payload={
          "seminarId": seminarId,
          "id": createCheckIn,
          "name": "大屏帖子_测试",
          "scale": "narrow",
          "topicId":topicId,
          "groupId": "0",
          "configId": "1",
          "messageConfigId": "1",
          "loop": "on",
          "interval": "3",
          "status": "on",
          "url": "",
          "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "c6b217e0-4f3b-4cbe-90dc-7c123004cd93"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# seminar_bigScreen_updateMessage/该接口为后台接口，后期即将移除，请不要继续使用，更新大屏消息
def get_most_seminar_bigScreen_updateMessage(type, domain, seminarId, createCheckIn,topicId, bakSess):
    path="/seminar/bigScreen/updateMessage"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
          "seminarId": seminarId,
          "id": createCheckIn,
          "name": "y"+createTime,
          "scale": "narrow",
          "topicId": topicId,
          "groupId": "148",
          "configId": "252065",
          "messageConfigId": "252064",
          "loop": "on",
          "interval": "3",
          "status": "on",
          "url": "",
            "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "13547471-f520-4ece-a854-5397ad37108f"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_bigScreen_updatePoll/更新投票大屏
def get_most_seminar_bigScreen_updatePoll(type, domain, seminarId, createCheckIn,pollId):
    path="/seminar/bigScreen/updatePoll"
    print "domain:", domain + path
    payload={
          "seminarId": seminarId,
          "id": createCheckIn,
          "name": "接口需要报名勿动",
          "scale": "narrow",
          "groupId": "159",
          "pollId": pollId,
          "pollName": "更新大屏",
          "interval": "3",
          "loop": "on",
          "status": "on",
          "isControl": "1",
          "url": "http://uao.so/spp2987c303100",
          "bigScreenWapUrl": "http://uao.so/swp2987c303101"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "4eede3af-0829-418f-9a2d-56615a7ce9ab"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_canInteraction/投票线下会前调接口，如果会议已结束，返回结果会有错误信息
def get_most_seminar_canInteraction(type, domain,seminarId_instanceId):
    path="/seminar/canInteraction"
    print "domain:", domain + path
    payload={
         "instanceId": seminarId_instanceId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "3d2889e9-4cdb-4a07-a9c2-90a351da0052"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_contact_checkIdCard/检查身份证号是否存在
def get_moost_seminar_contact_checkIdCard(type, domain):
    path="/seminar/contact/checkIdCard"
    print "domain:", domain + path
    payload={
        "idCard": "111111111111112"}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "84ebcdba-7157-4836-8477-0045e725f67d"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_contact_front_checkIn / 参会人签到
def get_most_seminar_contact_front_checkIn(type, domain,tenantId,seminarId,signingPointIds,passageId,loginSess):
    path="/seminar/contact/front/checkIn"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "seminarId": seminarId,
        "signingPointId": signingPointIds,
        "passageId": passageId,
        "sess":loginSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "457023dc-318b-4cbf-b608-dfd08ecfebca"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# seminar_contact_front_editRegContact/通过前台sess更新注册信息,如果有会议id则同时更新报名信息
def get_most_seminar_contact_front_editRegContact(type, domain,seminarId,seminarId_instanceId,loginSess):
    path="/seminar/contact/front/editRegContact"
    print "domain:", domain + path
    payload={
          "items": [
            {"fieldId": "2","key": "name","text": "上帝3123"},
            {"fieldId": "4","key": "mobile","text": "144442121323"},
            {"fieldId": "3","key": "email","text": "shangdi@tiantang31231.com"},
            {"fieldId": "5051","key": "duoxuan","options": [2,4],
                "values": ["a","c"]},
            {"fieldId": "5052","key": "danxuan","options": [6],
              "values": ["单选1"]},
            {"fieldId": "5054","key": "region","options": [1,2],
              "values": ["河北","石家庄"]}],
          "seminarId": seminarId,
          "instanceId": seminarId_instanceId,
          "sess": loginSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "33e6591f-595f-495e-ad14-5454fccc36a8"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_contact_front_getCommonContactInfo / 获取参会人员信息
def get_most_seminar_contact_front_getCommonContactInfo(type, domain, seminarId,unique):
    path="/seminar/contact/front/getCommonContactInfo"
    print "domain:", domain + path
    payload={
          "seminarId":int(seminarId),
          "unique": str(unique)
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "6f21664c-323f-4163-a0cf-ad8a19070523"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_contact_front_getContactInfo/根据会议id和唯一字段获取参会人信息
def get_most_seminar_contact_front_getContactInfo(type,domain,seminarId,email):
    path="/seminar/contact/front/getContactInfo"
    print "domain:", domain + path
    payload={
      "seminarId": int(seminarId),
      "unique": str(email)
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "6f229230-6a18-44a8-aba6-09d33df1d82f"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_contact_front_getRegContact/此接口即将过期不在维护，可使用 member_geneGet 代替
def get_most_seminar_contact_front_getRegContact(type,domain,tenantId,loginSess):
   path="/seminar/contact/front/getRegContact"
   print "domain:", domain + path
   payload ={
            "tenantId": tenantId,
            "sess": loginSess
        }    # suite.addTest(api_most_interface_HW("test_customForm_HasParticipation_180"))
    # suite.addTest(api_most_interface_HW("test_customForm_sendCheckCode_181"))
    # suite.addTest(api_most_interface_HW("test_customForm_user_getRecordByOpenId_182"))
    # suite.addTest(api_most_interface_HW("test_customForm_user_getResultByOpenId_183"))
    # suite.addTest(api_most_interface_HW("test_customForm_view_184"))
    # suite.addTest(api_most_interface_HW("test_de_contact_front_get_185")) #此用例要与用例test_member_login_002同时执行
    # suite.addTest(api_most_interface_HW("test_de_contact_front_getSeminars_186"))
    # suite.addTest(api_most_interface_HW("test_de_contact_getLastSeminarsBySess_187"))
    # suite.addTest(api_most_interface_HW("test_dic_getList_188"))
    # suite.addTest(api_most_interface_HW("test_dic_params_getList_189"))
   headers = {
       'Content-Type': "application/json",
       'cache-control': "no-cache",
       'Postman-Token': "8a2d3780-fe0d-47e4-82e0-8440f86f1770"
   }
   return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_contact_front_regSeminar/标准报名
def get_most_seminar_contact_front_regSeminar(type,domain,loginSess,seminarId_instanceId,seminarId,customFormId,wechatId):
    path="/seminar/contact/front/regSeminar"
    print "domain:", domain + path
    payload={
      "items": [
        {
          "fieldId": "2",
          "key": "name",
          "text": "上帝"
        },
        {
          "fieldId": "3",
          "key": "email",
        "text": "{{timestamp}}@qq.com"
        }
      ],
       "sess": loginSess,
      "instanceId": seminarId_instanceId,
      "seminarId":seminarId,
      "customFormId": customFormId,
      "channel": "",
      "subSeminars": [
        1
      ],
      "openId": "",
      "wechatId": wechatId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "ac13bf58-efdd-4937-a551-955fa7a988e9"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_contact_front_unRegister/参会人取消报名
def get_most_seminar_contact_front_unRegister(type,domain,seminarId,loginSess):
    path="/seminar/contact/front/unRegister"
    print "domain:", domain + path
    payload={

      "seminarId": seminarId,

      "sess":loginSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "d23a9b88-e151-46c7-b6cc-21d53d4b2aea"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_contact_front_updateSelf/更新参会人员信息 如果传递openId和weChatId会做绑定
def get_most_seminar_contact_front_updateSelf(type,domain,tenantId,seminarId,contactId,loginSess):
    path="/seminar/contact/front/updateSelf"
    print "domain:", domain + path
    payload={
      "tenantId": tenantId,
      "seminarId": seminarId,
      "contactId": contactId,
      "openId": "",
      "weChatId": "",
      "sess": loginSess,
      "items": [
        {
          "fieldId": "",
          "key": "name",
          "text": "lixuefeng11"
        },
          {
            "fieldId": "",
            "key": "mobile",
            "text": "13393213135"
          }
      ]
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "c9219ae8-0b12-4940-8453-30a24b1c19b2"
        }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_contact_getContactToWechat/根据openID获取会中联系人信息
def get_most_seminar_contact_getContactToWechat(type,domain,seminarId,wechatId):
    path="/seminar/contact/getContactToWechat"
    print "domain:", domain + path
    payload={
      "seminarId": seminarId,
      "wechatId": wechatId,
      "openId":"otqO01CM74B9qQ2ZFwGiglaZFxzg"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "3d84632d-a771-4c6a-9ce4-e224dd3ee7ae"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_contact_registerNew/会议报名接口(isProject=1时支持表单短信验证
def get_most_seminar_contact_registerNew(type,domain,customFormId,memberFormId):
    path="/seminar/contact/registerNew"
    print "domain:", domain + path
    payload={
      "syncSignUp": 0,
      "token": "",
      "instanceId": 10482,
      "customFormId": customFormId,
      "memberFormId": memberFormId,
      "globalUserId": "",
      "formData": [
                {
                    "fieldName": "name",
                    "value": ""
                },
                {
                    "fieldName": "email",
                    "value": "{{$randomInt}}@qq.com"
                }
            ]
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "e31a900d-a115-45a2-b394-cf215f3ad003"
        }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_contact_update/此接口即将过期不在维护，可使用seminar_contact_front_editRegContact标准格式实现,有问题
def get_most_seminar_contact_update(type,domain,tenantId,seminarId,contactId,bakSess):
    path="/seminar/contact/update"
    print "domain:", domain + path
    # payload={
    #   "tenantId": int(tenantId),
    #   "seminarId": int(seminarId),
    #   "contactId": int(contactId),
    #   "fields": {
    #     "mobile": "15960167982",
    #     "name": "柳旦旦",
    #     "email": "1064265199@qq.com",
    #     "enterprise": "",
    #     "department": "销售部",
    #     "industry ": "制造业",
    #     "position": "",
    #     "region": {
    #       "country": "中国",
    #       "countryId": "1",
    #       "province": "北京",
    #       "provinceId": "1",
    #       "city": "北京",
    #       "cityId": "0"
    #     }
    #   },
    #   "subSeminars": [
    #    5143
    #   ],
    #   "category": "",
    #   "sess": bakSess
    # }
    payload={ "tenantId": int(tenantId), "seminarId": int(seminarId), "contactId": int(contactId), "fields": { "mobile": "15960167982", "name": "柳旦旦",
"email": "1064265199@qq.com", "enterprise": "", "department": "销售部", "industry ": "制造业", "position": "",
"region": { "country": "中国", "countryId": "1", "province": "北京", "provinceId": "1", "city": "北京", "cityId": "0" } }, "subSeminars": [ 5143 ],
"category": "", "sess": str(bakSess)}
    headers = {
    'content-type': "application/json",
    'cookie': "SMARKET_MEMBER_SESS=;",
    'cache-control': "no-cache",
    'postman-token': "22cc26a8-e4b8-9480-f11d-ea505e6e1e25"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# post_create/该接口为后台接口，后期即将移除，请不要继续使用，留言板发帖
def get_most_post_create(type,domain,global_topicId,postId):
    path="/post/create"
    print "domain:", domain + path
    payload={
      "tenantId": "",
      "nodeId": "",
      "moduleId": "",
      "instanceId": "",
      "enableReply": 0,
      "isAnonymous": 1,
      "topicId": global_topicId,
      "content": "h",
      "postId":postId,
      "memberId": 0,
      "openId": "",
      "cookeId": "",
      "nickname": "",
      "createrPic": "",
      "sess": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "933275ef-4128-4c4a-901d-847f6bca959e"
    }
    return api_quester_common().Is_successful_getvalue("POST", domain + path, payload, headers, type, type,"content")
# webinar_open_registration/线上会报名接口
def get_most_webinar_open_registration(type,domain,webinarId_instanceId,bakSess):
    path="/webinar/open/registration"
    print "domain:", domain + path
    payload ={
        "instanceId":str(webinarId_instanceId),
        "channel": "渠道一",
        "items": [
          {
            "key": "name",
            "text": "上帝"
          },
          {
            "key": "city",
            "text": "天堂"
          },
          {
            "key": "mobile",
            "text": "14444444444"
          },
          {
            "key": "email",
            "text": "shangdi@tiantang.com"
          },
          {
            "key": "enterprise",
            "text": "天宫股份有限公司"
          },
          {
            "key": "department",
            "text": "人力资源部"
          },
          {
            "key": "position",
            "text": "总监"
          }
        ],
        "memberId": "",
        "sys_source": "pc",
        "sess": str(bakSess)
      }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "e7939d05-ea90-4fcc-9af9-badb1ff58337"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#questionary_HasParticipation/浏览问卷
def get_questionary_HasParticipation(type,domain,questionid_wj,bakSess):
    path = "/questionary/HasParticipation"
    print "domain:", domain + path
    payload = {
        "questionaryId": questionid_wj,
        "globalUserId": "0903c078acc06f3713f73de9cc562e23",
        "openId": "",
        "referenceUrl": "",
        "url": "",
        "instanceId": "",
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "2ae30bdd-a862-4852-b804-051915f9bbdd"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#post_get/获取贴子信息
def get_post_get(type,domain,tenantId,nodeId,postId,bakSess):
    path = "/post/get"
    print "domain:", domain + path
    payload = {
        "tenantId": tenantId,
        "nodeId": nodeId,
        "moduleId": "",
        "instanceId": "",
        "postId": postId,
        "memberId": 10,
        "openId": "",
        "cookieId": "39e5bd2a4a1c363d09b9fdd09323b3d8",
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "b92ebbaf-2d72-4464-ba5c-0ffabfc88e78"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#post_getListByUser/获取某人的未被删除的发送帖子记录
def get_post_getListByUser(type,domain,topicId,bakSess):
    path = "/post/getListByUser"
    print "domain:", domain + path
    payload = {
        "topicId": topicId,
        "start": 0,
        "num": 10,
        "openId": "otqO01CM74B9qQ2ZFwGiglaZFxzg",
        "cookieId": "39e5bd2a4a1c363d09b9fdd09323b3d8",
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "3c91939e-5b43-4202-85f3-2cfd6b63c6c0"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#post_getMainAndReplyList/获取留言板的发帖的回帖
def get_post_getMainAndReplyList(type,domain,topicId):
    path = "/post/getMainAndReplyList"
    print "domain:", domain + path
    payload = {
        "topicId": topicId,
        "start": 0,
        "num": 10,
        "status": 0,
        "isPreview": 1
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "95bde2c2-e6fc-4987-8d07-c765f38d86e2"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#post_getMainPost/ 获取主贴列表
def get_post_getMainPost(type,domain,topicId):
    path = "/post/getMainPost"
    print "domain:", domain + path
    payload = {
        "topicId": topicId,
        "openId": "",
        "cookieId": "",
        "start": 0,
        "num": 10
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "a087cd9b-9444-4704-a1b9-d96d584689ac"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#post_getMyPost/获取我发的帖子
def get_post_getMyPost(type,domain,topicId,bakSess):
    path = "/post/getMyPost"
    print "domain:", domain + path
    payload = {
        "topicId": topicId,
        "start": 0,
        "num": 10,
        "memberId": 0,
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "d977a41b-8cd7-4b3e-874e-5a452e7cddf8"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#post_getReplyPost/获取某主贴的所有回贴
def get_post_getReplyPost(type,domain,tenantId,nodeId,postId,bakSess):
    path = "/post/getReplyPost"
    print "domain:", domain + path
    payload = {
        "tenantId": tenantId,
        "nodeId": nodeId,
        "moduleId": "",
        "instanceId": "",
        "postId": postId,
        "start": 0,
        "num": 10,
        "memberId": 10,
        "openId": "",
        "cookieId": "39e5bd2a4a1c363d09b9fdd09323b3d8",
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "e3891716-a860-46db-a634-be7a1571aaa8"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#post_like/点赞
def get_post_like(type,domain):
    path = "/post/like"
    print "domain:", domain + path
    payload = {
        "postIds": [],
        "memberId": 0,
        "openId": "",
        "cookieId": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "c2a1e624-8273-4730-9074-b28b0489b5b0"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#post_update/主贴编辑 更新帖子内容
def get_post_update(type,domain,postId,tenantId,nodeId,seminarId_instanceId):
    path = "/post/update"
    print "domain:", domain + path
    payload = {
        "postId": postId,
        "tenantId": tenantId,
        "nodeId": nodeId,
        "moduleId": 1,
        "instanceId": seminarId_instanceId,
        "enableReply": 1,
        "content": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "2dff85f2-bbf1-4fba-a2e1-0c672db92767"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#post_deletePost/删除主贴
def get_post_deletePost(type,domain,tenantId,nodeId,postI,global_topicId):
    path = "/post/deletePost"
    print "domain:", domain + path
    payload = {
        "tenantId": tenantId,
        "instanceId": "0",
        "moduleId": "0",
        "nodeId": nodeId,
        "sess": "",
        "objectInstanceId": "",
        "browseInfo": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "browser": "Chrome",
            "version": "68.0.3440.106",
            "os": "Windows",
            "equipment": "pc",
            "resolution": "1920X1080",
            "referenceUrl": "https://f.smarket.net.cn/s/template/8dfe8a67389875df111a88fb3101a1b0/html/index.html?topicId=1562&configId=259570",
            "referenceTitle": "",
            "sessionId": ""
        },
        "postIds": [
        postI
        ],
        "topicId": global_topicId,
        "cookieId": "",
        "openId": "",
        "globalUserId": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "36edad93-48e8-4b00-8f9e-87fb1fb3035a"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# post_delete/此接口应为后台接口，后期不在开放，请不要调用 删除主贴
def get_most_post_delete(type, domain,postId):
    path="/post/delete"
    print "domain:", domain + path
    payload={
        "postIds": [
            ""+postId+""
        ]
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "7e88d95e-c05c-088a-9883-2110644cfe90"
    }

    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_frontGet/获取会议详情
def get_most_seminar_frontGet(type, domain,seminarId):
    path="/seminar/frontGet"
    print "domain:", domain + path
    payload={
        "seminarId": ""+seminarId+""
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "b0c07c8a-f838-9f26-3ad0-67d9251a3740"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_frontGetList/获取会议列表，无sess调用
def get_most_seminar_frontGetList(type, domain,tenantId):
    path="/seminar/frontGetList"
    print "domain:", domain + path
    payload={
    "tenantId": ""+tenantId+"",
    "key": "我",
    "sceneName": "business",
    "status": "proposed",
    "sortName": "createTime",
    "sortOrder": "asc",
    "conditions": "null",
    "start": 0,
    "num": 10,
    "expandInfo": [
      "agenda",
      "guest",
      "subSeminar"
    ]
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "8f8e2b50-ce1d-0575-8016-e515dd22d8a1"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_registration/线上会报名表单提交
def get_most_webinar_registration(type, domain,loginSess,webinar_BMFormId,webinarId_instanceId):
    path="/webinar/registration"
    print "domain:", domain + path
    payload={"sess":str(loginSess),"customFormId":str(webinar_BMFormId),"linkId":"26812","instanceId":str(webinarId_instanceId),"globalUserId":"39e5bd2a4a1c363d09b9fdd09323b3d8","url":"https://f.smarket.net.cn/s/template/39dc846dd6e88089d3990c165e4fad03/view/customForm.html?instanceId=38369&webinarId=6132&customFormId=13283&trackId=2:74&linkId=26812&configId=246966&returnUrl=http%3A%2F%2Ff.smarket.net.cn%2Fs%2Ftemplate%2Fddaae85fe48ff1372217f0db2def1676%2Fhtml%2Fmeeting.html%3FinstanceId%3D38369%26webinarId%3D6132%26customFormId%3D13283%26trackId%3D2%3A74%26linkId%3D26812%26signUpNotify%3Dtrue#","referenceUrl":"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/accountbind-registed.html?memberFormId=6329&backUrl=https%3A%2F%2Ff.smarket.net.cn%2Fs%2Ftemplate%2F39dc846dd6e88089d3990c165e4fad03%2Fview%2FcustomForm.html%3FinstanceId%3D38369%26webinarId%3D6132%26customFormId%3D13283%26trackId%3D2%3A74%26linkId%3D26812%26configId%3D246966%26returnUrl%3Dhttp%253A%252F%252Ff.smarket.net.cn%252Fs%252Ftemplate%252Fddaae85fe48ff1372217f0db2def1676%252Fhtml%252Fmeeting.html%253FinstanceId%253D38369%2526webinarId%253D6132%2526customFormId%253D13283%2526trackId%253D2%253A74%2526linkId%253D26812%2526signUpNotify%253Dtrue&configId=246874&memberSchemaId=2808","ver":"v2.0.1","items":[{"fieldName":"name","value":"上帝"},{"fieldName":"mobile","value":"13393213111"},{"fieldName":"email","value":"shandi@tiantang.com"}]}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "edca8553-fb62-5c45-7d11-0c603affc2b4"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# contact_bindMember/微信账号与会员绑定
def get_most_contact_bindMember(type, domain,wechatId,schemaId,loginSess):
    path="/contact/bindMember"
    print "domain:", domain + path
    payload={
    "weChatId": ""+wechatId+"",
    "openId": "otqO01CM74B9qQ2ZFwGiglaZFxzg",
    "schemaId": ""+schemaId+"",
    "sess": ""+loginSess+""
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "0fe24d8e-2ea9-6a4d-6920-3cfa9cc1526d"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_frontGetListByIds/根据ids获取会议列表
def get_most_seminar_frontGetListByIds(type, domain,tenantId):
    path="/seminar/frontGetListByIds"
    print "domain:", domain + path
    payload={
    "tenantId": ""+tenantId+"",
    "ids": [
        5968,

        5963

    ]
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "471a41cd-a3ed-323a-95d2-0e0e46643b16"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_frontGetStatusList/获取会议列表--支持按会议状态搜索
def get_most_seminar_frontGetStatusList(type, domain,tenantId):
    path="/seminar/frontGetStatusList"
    print "domain:", domain + path
    payload={
    "tenantId": ""+tenantId+"",
    "keyword": "我",
    "status": [
    "readytolaunch",
    "launched",
    "completed"
    ],
    "start": 0,
    "num": 10
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "a8f80733-02b0-41b4-86be-34f4b68464e3"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_get/ 获取会议详情
def get_most_seminar_get(type, domain,seminarId):
    path="/seminar/get"
    print "domain:", domain + path
    payload={
    "seminarId": ""+seminarId+""
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "361437f7-560d-9596-06e5-2c265b5aa634"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_getListWithFormId/会议列表（获取列表，输出：会议logo 会议名称 会议开始时间 会议地点 默认的报名表单Id）注：会议logo如果不存在，则不返回
def get_most_seminar_getListWithFormId(type, domain,tenantId):
    path="/seminar/getListWithFormId"
    print "domain:", domain + path
    payload={
    "tenantId": ""+tenantId+"",
    "key": "接口自动化测试",
    "start": "0",
    "num": "10"
           }
    headers = {
         'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "668e1cf1-4e8e-9868-3a02-00a73b685fbc"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_register_canRegister/会议是否可以报名 如果有报名返回线下会报名信息，如果没有报名但是有注册返回注册信息，如果没有注册没有报名返回null
def get_most_seminar_register_canRegister(type, domain,seminarId_instanceId,bakSess):
    path="/seminar/register/canRegister"
    print "domain:", domain + path
    payload={
        "instanceId": ""+seminarId_instanceId+"",
        "sess": ""+bakSess+""
           }
    headers = {
         'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "668e1cf1-4e8e-9868-3a02-00a73b685fbc"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_register_canRegisterNew/-会议是否可以报名
def get_most_seminar_register_canRegisterNew(type,domain,seminarId_instanceId,registerFormId):
    path="/seminar/register/canRegisterNew"
    print "domain:", domain + path
    payload ={
      "instanceId": seminarId_instanceId,
      "formId":registerFormId ,
      "globalUserId": "",
      "openId": "",
      "needSignupUrl": "1"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "2dfdb916-2385-49e1-b904-7b72e39f136e"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# contact_getByOpenId/通过openId获取联系人信息
def get_most_contact_getByOpenId(type,domain,wechatId):
    path="/contact/getByOpenId"
    print "domain:", domain + path
    payload ={
        "weChatId": wechatId,
        "openId": "otqO01CM74B9qQ2ZFwGiglaZFxzg",
        "schemaId": "{{schemaId}}"
      }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "fadd7456-3aca-4737-bcb4-36fbe0d49839"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# contact_getContactStatus/查询openId是否已关注微信号
def get_most_contact_getContactStatus(type,domain,wechatId,bakSess):
    path="/contact/getContactStatus"
    print "domain:", domain + path
    payload ={
        "weChatId": wechatId,
        "openIds": [
          "otqO01CM74B9qQ2ZFwGiglaZFxzg",
          "sdfsdgertrtggg"
        ],
        "status": -1,
        "sess": bakSess
      }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "72506735-4692-4bd1-aa21-44930ccbe7a0"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# customForm_action/线下会报名接口
def get_most_customForm_seminar_action(type,domain,customFormId,seminarId_instanceId):
    path="/customForm/action"
    print "domain:", domain + path
    payload ={
      "customFormId":customFormId,
      "globalUserId": "",
      "referenceUrl": "",
      "linkId": "26892",
      "openId": "",
      "nickName": "",
      "name": "",
      "memberId": "",
      "headImage": "",
      "city": "",
      "province": "",
      "country": "",
      "items": [
          {
          "fieldName": "name",
          "value": "高明"
        },
        {
          "fieldName": "mobile",
          "value": "18633873521"
        },
        {
          "fieldName": "avatar",
          "value": {
            "fileName": "username",
            "mapId": "9a644a7fea95749f75f8cafffd055055"
          }
        }
      ],
      "checkCode": "",
      "createTime": "",
      "sess": "",
      "ver": "v2.0.1",
      "enteredId": "",
      "instanceId": seminarId_instanceId,
      "url": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "06e4736e-e3a1-451c-b2fa-3ef8c3f60179"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# customForm_checkRegistration/报名前验证
def get_most_customForm_checkRegistration(type,domain,registerFormId,seminarId_instanceId):
    path="/customForm/checkRegistration"
    print "domain:", domain + path
    payload ={
      "customFormId": registerFormId,
      "moduleType": "3",
      "cookieId": "",
      "instanceId": seminarId_instanceId,
      "openId": "otqO01CM74B9qQ2ZFwGiglaZFxzg",
      "ver": "v2.0.1"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "172ac012-666d-4bd1-8263-875a9f10c798"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_register_getList/获取报名表单列表
def get_most_seminar_register_getList(type,domain,seminarId):
    path="/seminar/register/getList"
    print "domain:", domain + path
    payload ={"seminarId": seminarId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "5341cdd1-db2e-4710-8c33-efea94e02cc2"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_register_getSubList/通过自定义表单id获取报名表单信息
def get_most_seminar_register_getSubList(type,domain,customFormId,seminarId_instanceId):
    path="/seminar/register/getSubList"
    print "domain:", domain + path
    payload ={
      "customFormId": customFormId,
      "instanceId": seminarId_instanceId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "e079010b-c975-41d5-8744-702fa8f21bb6"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# customForm_checkRepeatable/检查表单的不重复字段是否重复
def get_most_customForm_checkRepeatable(type,domain,customFormId):
    path="/customForm/checkRepeatable"
    print "domain:", domain + path
    payload ={
        "customFormId": customFormId,
        "fieldId": "1",
        "fieldValue": "1",
        "_cache_with_cached": "1"
      }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "df74373e-8d9c-49af-9b99-e0f1e4e3b3aa"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# customForm_get/获取自定义表单详情
def get_most_customForm_get(type,domain,customFormId):
    path="/customForm/get"
    print "domain:", domain + path
    payload ={"customFormId": customFormId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "6822bd3d-782a-46e4-9e16-966a3437bdcc"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# customForm_getListByIds/该接口为后台接口，后期即将移除，请不要继续使用，获取表单列表
def get_most_customForm_getListByIds(type,domain,tenantId,bakSess):
    path="/customForm/getListByIds"
    print "domain:", domain + path
    payload ={
      "tenantId": tenantId,
      "customFormIds": [
          "{{customFormIds}}"
      ],
      "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "b9093c34-0666-414a-85bd-1462e1108d11"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# customForm_HasParticipation/记录表单的浏览记录
def get_most_customForm_HasParticipation(type,domain,customFormId):
    path="/customForm/HasParticipation"
    print "domain:", domain + path
    payload ={
      "customFormId":customFormId,
      "globalUserId": "39e5bd2a4a1c363d09b9fdd09323b3d8",
      "linkId": 28908,
      "openId": "",
      "memberId": "",
      "referenceUrl": "",
      "url": "",
      "trackingCode": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "7527cb54-95cb-42c2-acd5-306ac14ff5da"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# customForm_sendCheckCode/自定义表单发送手机修改密码验证码
def get_most_customForm_sendCheckCode(type, domain, customFormId):
    path = "/customForm/sendCheckCode"
    print "domain:", domain + path
    payload = {
      "customFormId": customFormId,
      "mobile": "13393213135",
       "globalUserId": "66e086fb9d9364161895e217dda7b5c8"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "f2e345c1-db8e-4444-ab9f-fa8d33c43aa7"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# customForm_user_getRecordByOpenId/获取粉丝提交表单记录
def get_most_customForm_user_getRecordByOpenId(type, domain, customFormId,loginSess):
    path = "/customForm/user/getRecordByOpenId"
    print "domain:", domain + path
    payload = {

      "customFormId":customFormId,

      "openId": "oG80v1azw6L2LyxcVogDZnQ3pvNs",

      "start": 0,

      "num": 10,

      "sess":loginSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "153a3994-3e59-49c4-b589-7949dac2bc59"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# customForm_user_getResultByOpenId/获取某个OpenId的答表单的记录
def get_most_customForm_user_getResultByOpenId(type, domain, customFormId):
    path = "/customForm/user/getResultByOpenId"
    print "domain:", domain + path
    payload = {
      "openId": "otqO01HFNgV_Z06fEQgxiH6FAaM0-4",
      "customFormId":customFormId,
      "start": 0,
      "num": 10
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "971203e7-fd3e-477a-92b4-34fa3c3564cd"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# customForm_view/记录表单的浏览记录
def get_most_customForm_view(type, domain, customFormId):
    path = "/customForm/view"
    print "domain:", domain + path
    payload = {
      "customFormId": customFormId,
      "globalUserId": "",
      "linkId": 1,
      "openId": 1,
      "memberId": 1,
      "referenceUrl": "",
      "url": "",
      "trackingCode": ""
    }
    headers = {
        'Content-Type': "application/json",

        'cache-control': "no-cache",
        'Postman-Token': "9a096704-529b-4c20-819f-c560fcbe3b4a"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# de_contact_front_get/获取de联系人信息
def get_most_de_contact_front_get(type, domain, loginSess,tenantId):
    path = "/de/contact/front/get"
    print "domain:", domain + path
    payload = {
        "tId": tenantId,
        "sess": loginSess
      }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "b386e872-f99c-4c72-b4b1-f5075d78f751"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# de_contact_front_getSeminars/ 通过前台sess获取联系人最近参加过的会议
def get_most_de_contact_front_getSeminars(type, domain, loginSess,tenantId):
    path = "/de/contact/front/getSeminars"
    print "domain:", domain + path
    payload ={

      "tId": tenantId,

      "sess":loginSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "563646fb-748b-4fdc-baf5-77256a4b8859"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# de_contact_getLastSeminarsBySess/获取参与过的会议
def get_most_de_contact_getLastSeminarsBySess(type, domain, bakSess,contactId,tenantId):
    path = "/de/contact/getLastSeminarsBySess"
    print "domain:", domain + path
    payload ={
      "tenantId": tenantId,
      "contactId": contactId,
      "sortName": "startTime",
      "sortOrder": "desc",
      "start": 0,
      "num": 20,
      "withTag": 0,
      "sess":bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "7a801ebb-a1ba-4c49-ae62-40cf16afa221"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# dic_getList/获取字典列表
def get_most_dic_getList(type, domain,tenantId):
    path = "/dic/getList"
    print "domain:", domain + path
    payload ={
      "tenantId": tenantId,
      "keyword": "黑龙江",
      "type": "-1",
      "isCascade": "-1",
      "start": "0",
      "num": "20"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "d9c50ff9-f1e5-4ab8-bbd7-b8a7f2523f3d"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# dic_params_getList/获取字典值列表
def get_most_dic_params_getList(type, domain,tenantId,dicId):
    path = "/dic/params/getList"
    print "domain:", domain + path
    payload ={
        "tenantId": tenantId,
        "dicId": dicId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "02220dd5-b7a6-4af7-bf7e-9569ffe5a37b"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_signingPoint_checkIn_getCheckInCount/获取某会议下签到点的签到数
def get_seminar_signingPoint_checkIn_getCheckInCount(type, domain,seminarId):
    path="/seminar/signingPoint/checkIn/getCheckInCount"
    print "domain:", domain + path
    payload={
        "seminarId": seminarId,
        "signPoints": []
           }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "c865fd83-bd3e-480a-8a2f-28e6d492e2d7"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#dic_params_getTree/获取字典树形结构
def get_dic_params_getTree(type, domain,tenantId,dicId):
    path="/dic/params/getTree"
    print "domain:", domain + path
    payload={"tenantId": tenantId,"dicId": dicId,"format": "object"}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "a7c613fc-7a97-475f-9c3c-9ad2e370fba8"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_signingPoint_front_getMyCheckInLog/查看自己的签到记录，传openid，globaluserid，cookieid，sess
def get_seminar_signingPoint_front_getMyCheckInLog(type, domain,tenantId,bakSess,seminarId,seminarId_instanceId,signingPointId,passageId):
    path="/seminar/signingPoint/getCheckInLog"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "sess": bakSess,
        "seminarId": seminarId,
        "instanceId": seminarId_instanceId,
        "groupId": 0,
        "signingPointId": signingPointId,
        "passageId": passageId,
        "contactId": 478744,
        "keyWord": "",
        "sort": 1,
        "start": 0,
        "num": 20
           }
    headers = {
        'cookie': "SMARKET_MEMBER_SESS=;",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "cacd1b32-dcda-499b-aa0a-4ac4b5f8dc67"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_signingPoint_getCheckInLog/获取签到历史记录
def get_seminar_signingPoint_getCheckInLog(type, domain,tenantId,seminarId,seminarId_instanceId,signingPointId,passageId,bakSess):
    path="/seminar/signingPoint/getCheckInLog"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "seminarId": seminarId,
        "instanceId": seminarId_instanceId,
        "groupId": -1,
        "signingPointId": signingPointId,
        "passageId": passageId,
        "contactId": " ",
        "keyWord": "",
        "sort": 1,
        "start": 0,
        "num": 20,
        "sess": bakSess
           }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "3d34b1ae-1f09-45cf-9290-6fb5e2308086"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_signingPoint_getNumberSignInPassage/获取会议签到点签到统计信息
def get_seminar_signingPoint_getNumberSignInPassage(type, domain,tenantId,seminarId,seminarId_instanceId,signingPointId,passageId,bakSess):
    path="/seminar/signingPoint/getNumberSignInPassage"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "seminarId": seminarId,
        "instanceId": seminarId_instanceId,
        "groupId": 0,
        "signingPointId": signingPointId,
        "passageId": passageId,
        "sess": bakSess
           }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "a6a2967b-ad77-4167-941c-8edd9d599e11"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#edm_log_create/创建邮件发送任务
def get_edm_log_create(type,domain,taskId):
    path="/edm/log/create"
    print "domain:", domain + path
    payload={
        "params": [
            {
                "taskId": taskId,
                "params": {
                    "sendEmail": "1946898935@qq.com",
                    "sendName": "email",
                    "city": "http://www.baidu.com"
                }
            }
        ]
           }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "fe712aab-9f6a-4b34-b0c3-3ce467e727eb"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_subSeminar_frontGet/获取分会场详细信息
def get_seminar_subSeminar_frontGet(type,domain,subSeminarId):
    path="/seminar/subSeminar/frontGet"
    print "domain:", domain + path
    payload={    "subSeminarId": subSeminarId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "59a5e9b5-a5e9-4314-86f0-bf5751bb89c7"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_subSeminar_getListByType/获取分会场列表
def get_seminar_subSeminar_getListByType(type,domain,seminarId):
    path="/seminar/subSeminar/getListByType"
    print "domain:", domain + path
    payload={    "seminarId": seminarId,"type": "disabled"}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "649dd731-d75a-4fa7-bbeb-7e2fc464f21f"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_topicTemplate_contact_get/获取联系人信息
def get_seminar_topicTemplate_contact_get(type,domain,seminarId_instanceId,email):
    path="/seminar/topicTemplate/contact/get"
    print "domain:", domain + path
    payload={  "instanceId": seminarId_instanceId,"uniqueValue": email}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "782f0b02-bb2e-4ae2-9dd1-da918067d430"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_topicTemplate_contact_getByOpenId/通过微信OpenId获取某会议下的联系人
def get_seminar_topicTemplate_contact_getByOpenId(type,domain,seminarId):
    path="/seminar/topicTemplate/contact/getByOpenId"
    print "domain:", domain + path
    payload={  "seminarId": seminarId,"openId": "otqO01CM74B9qQ2ZFwGiglaZFxzg"}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "3f6decde-c584-44bf-98cc-df0d0ab5b2fb"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#edm_send/邮件发送接口，session验证
def get_edm_send(type,domain,tenantId,bakSess):
    path="/edm/send"
    print "domain:", domain + path
    payload={
        "toEmails": "394522655@qq.com",
        "subject": "shinaide",
        "content": "welcome",
        "fromEmail": "",
        "fromName": "sino",
        "tenantId": tenantId,
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "d83de5d5-f123-42e0-ad6b-4e077a14abf7"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_topicTemplate_contact_getState/通过实例ID和唯一字段获取信息
def get_seminar_topicTemplate_contact_getState(type,domain,seminarId_instanceId,email):
    path="/seminar/topicTemplate/contact/getState"
    print "domain:", domain + path
    payload={"instanceId": seminarId_instanceId,"uniqueValue": email}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "72ab9d9d-25d0-4eb8-81ec-3a3b0c0dc8ba"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#customForm_isFaceImg/检查图片是否包含人脸
def get_customForm_isFaceImg(type,domain,mappingId):
    path="/customForm/isFaceImg"
    print "domain:", domain + path
    payload={"mappingId": mappingId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "265bb1ca-362b-403e-aef6-32451b8df4e2"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_topicTemplate_contact_getStateBySess/获取注册状态，有问题
def get_seminar_topicTemplate_contact_getStateBySess(type,domain,seminarId_instanceId):
    path="/seminar/topicTemplate/contact/getStateBySess"
    print "domain:", domain + path
    payload={"instanceId": seminarId_instanceId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "98923517-6650-4e9c-a22c-9783295acda9"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_topicTemplate_seminar_getFormInfo/获取表单详细信息
def get_seminar_topicTemplate_seminar_getFormInfo(type,domain,seminarId_instanceId,registerFormId):
    path="/seminar/topicTemplate/seminar/getFormInfo"
    print "domain:", domain + path
    payload={    "instanceId": seminarId_instanceId,"formId": registerFormId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "539afb5c-146f-49ab-a7f1-edf26756e9d4"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_topicTemplate_seminar_getWithAllSub/获取会议信息，包括所有的分会场
def get_seminar_topicTemplate_seminar_getWithAllSub(type,domain,seminarId_instanceId):
    path="/seminar/topicTemplate/seminar/getWithAllSub"
    print "domain:", domain + path
    payload={    "instanceId": seminarId_instanceId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "369d3a8d-de88-478d-9fff-ac4f3282d400"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_trackingCode_getList/获取渠道追踪代码列表
def get_seminar_trackingCode_getList(type,domain,seminarId):
    path="/seminar/trackingCode/getList"
    print "domain:", domain + path
    payload={"seminarId": seminarId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "286062e9-191f-41e6-aa46-ffc0be151713"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_bigScreen_forBigScreenWall_getCheckInData/获取大屏签到墙信息
def get_seminar_bigScreen_forBigScreenWall_getCheckInData(type,domain,createCheckIn,signingPointId):
    path="/seminar/bigScreen/forBigScreenWall/getCheckInData"
    print "domain:", domain + path
    payload={    "id": createCheckIn,"signingPointId": signingPointId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "76fb03bf-bc0c-4895-809a-91c32da56b8b"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_bigScreen_forBigScreenWall_getWapCheckInfo/获取大屏手机端签到信息
def get_seminar_bigScreen_forBigScreenWall_getWapCheckInfo(type,domain,createCheckIn,contactId,email):
    path="/seminar/bigScreen/forBigScreenWall/getWapCheckInfo"
    print "domain:", domain + path
    payload={    "bigScreenId": createCheckIn,"contactId": contactId,"uniqueValue":email}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "16f1c654-6954-4237-981b-473a1e8ba8fa"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#field_getList/获取字段列表
def get_field_getList(type,domain,tenantId):
    path="/field/getList"
    print "domain:", domain + path
    payload={"tenantId": tenantId,"fieldType": "seminar"}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "57451fd4-e4d3-48c2-b581-8bf03ef1a634"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_bigScreen_getWapMessageInfo/获取wap签到模板联系人信息
def get_seminar_bigScreen_getWapMessageInfo(type,domain,seminarId,email):
    path="/seminar/bigScreen/forBigScreenWall/getWapMessageInfo"
    print "domain:", domain + path
    payload={  "seminarId": seminarId,"uniqueValue": email}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "bb501f57-b25b-40ac-bfb3-ea7af99037fc"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#file_folder_getReleaseFile/获取公布的文件
def get_file_folder_getReleaseFile(type,domain,fileId):
    path="/file/folder/getReleaseFile"
    print "domain:", domain + path
    payload={"fileId": fileId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "31f81d5d-9f4f-47ba-8062-94a4d1175c2f"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#file_getList/获取文件列表
def get_file_getList(type,domain,tenantId,seminarId_instanceId,FolderId,fileIds):
    path="/file/getList"
    print "domain:", domain + path
    payload={
    "tenantId": tenantId,
    "moduleType": "",
    "instanceId": seminarId_instanceId,
    "folderId": FolderId,
    "name": "",
    "labelname": "",
    "start": 0,
    "num": 20,
    "type": 1,
    "fileIds": fileIds,
    "isShowSys": 0,
    "fileTypes": [],
    "sortType": 1
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "aa8271dd-05a0-4fe6-80e2-4a00fc486be3"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful_getvalue("POST", domain + path, payload, headers, type, type, "content")
#member_changePwd/前台用户修改密码
def get_member_changePwd(type,domain,schemaId,loginSess):
    path="/member/changePwd"
    print "domain:", domain + path
    payload={
    "oldPwd": "4297F44B13955235245B2497399D7A93",
    "newPwd": "4297F44B13955235245B2497399D7A93",
    "schemaId": schemaId,
     "sess": loginSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "95331b10-39ff-4db1-a518-46e8d630095b"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#member_checkUnique/检测用户唯一，检测字段值唯一
def get_member_checkUnique(type,domain,tenantId):
    path="/member/checkUnique"
    print "domain:", domain + path
    payload={
    "memberSchemaId": tenantId,
    "unique": "13393213135",
    "fieldName": "mobil"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "2d50f1ce-bdff-48d8-8ba8-377457743789"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#luckyDraw_client_action/抽奖
def get_luckyDraw_client_action(type,domain,luckyDrawId,bakSess):
    path="/luckyDraw/client/action"
    print "domain:", domain + path
    payload={
    "luckyDrawId": luckyDrawId,
    "cookieId": "cookieId",
    "openId": "wechatOpenId",
    "memberId": 1,
    "nickName": "null",
    "headImgUrl": "www.126.com",
    "memberName": "this is my name",
    "sex": "nan",
    "city": "Shijiazhuang",
    "province": "Hebei",
    "country": "China",
    "url": "",
    "referenceUrl": "",
    "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "aca6bdc4-f7e1-48b8-8604-4fa7d8e9c1af"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#member_form_GetForNewForm/新的表单信息 接受formId 和 memberFormId 按新接口的格式返回
def get_member_form_GetForNewForm(type,domain,registerFormId):
    path="/member/form/GetForNewForm"
    print "domain:", domain + path
    payload={
        "formId": registerFormId,
        "memberFormId": "",
        "sess": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "b01e3be3-9fdf-445c-a6c3-7236a71b0bb4"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#member_form_GetOAuthUrlByWeChatId/通过wechatId获取授权信息
def get_member_form_GetOAuthUrlByWeChatId(type,domain,wechatId):
    path="/member/form/GetOAuthUrlByWeChatId"
    print "domain:", domain + path
    payload={"weChatId": wechatId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "4b3ce6f6-f105-4666-a3ab-ffdb06d6f438"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#member_form_getTemplate/获取表单模板信息
def get_member_form_getTemplate(type,domain,memberFormId):
    path="/member/form/getTemplate"
    print "domain:", domain + path
    payload={"memberFormId": memberFormId,"trackId": ""}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "04e213d8-1984-4700-acae-4753fd0aed51"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#member_form_getUnique/找回密码
def get_member_form_getUnique(type,domain,memberFormId):
    path="/member/form/getUnique"
    print "domain:", domain + path
    payload={"memberFormId": memberFormId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "75647593-032d-4acf-bdc8-659f3b2acaa9"
    }

    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# member_form_search/查询符合条件的表单
def get_most_member_form_search(type, domain,tenantId):
    path="/member/form/search"
    print "domain:", domain + path
    payload={
        "tenantId": ""+tenantId+"",
        "schemaId": "",
        "formId": "",
        "trackId": "",
        "keyword": "",
        "start": "0",
        "num": "12"
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "c8739767-f104-1e57-e7da-8d23421010b1"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type,type)
# member_form_view/注册表单浏览
def get_most_member_form_view(type, domain,memberFormId,loginSess):
    path="/member/form/view"
    print "domain:", domain + path
    payload={
        "memberFormId": ""+memberFormId+"",
        "globalUserId": "39e5bd2a4a1c363d09b9fdd09323b3d8",
        "url": "",
        "referenceUrl": "",
        "trackId": "0",
        "openId": "",
        "sess": ""+loginSess+""
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "5803c4d8-263b-e2ef-9cfb-c0a2d7ad60b2"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type,type)
# api_seminar_Query/获取会议列表
def get_most_api_seminar_Query(type, domain,tenantId):
    path="/api/seminar/query"
    print "domain:", domain + path
    payload={
        "tenantId": int(tenantId),
        "keyword": "测试",
        "seminarStatus": [],
        "expandInfo": [],
        "sort": ["createTime desc"],
        "start": 0,
        "num": 10
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "b0a035e3-624d-bea6-1a65-8997e6308835"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type,type)
# member_geneGet/根据已登录的session获取用户信息
def get_most_member_geneGet(type, domain,loginSess):
    path="/member/geneGet"
    print "domain:", domain + path
    payload={
        "sess": str(loginSess)
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "a0fbf969-96cc-1c9e-813e-344ddb9cbfba"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type,type)
# api_seminar_site_browse/进入访问专题站行为
def get_most_api_seminar_site_browse(type, domain,seminarId,tenantId):
    path="/api/seminar/site/browse"
    print "domain:", domain + path
    payload={
        "seminarId": int(seminarId),
        "tenantId": int(tenantId),
        "sess": "",
        "globalUserId": "aeb77fdace2cca2d90caef190782555c",
        "openId": "",
        "browseInfo": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "browser": "Chrome", "version": "67.0.3396.99", "os": "Windows", "equipment": "电脑端",
            "resolution": "1920X1080",
            "referenceUrl": "https://uat-sde.smarket.net.cn/seminar.html?seminarId=4303&seminarName=%E6%96%B0%E7%BD%91%E5%85%B3%E6%B5%8B%E8%AF%95&instanceId=35686",
            "referenceTitle": "", "sessionId": "75882b67796fd029c505ff0c19600459"}
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "e4b17d1a-4410-e8f0-821b-fa5e183b487b"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type,type)
# api_seminar_site_share/分享专题站行为
def get_most_api_seminar_site_share(type, domain,seminarId,tenantId):
    path="/api/seminar/site/browse"
    print "domain:", domain + path
    payload={
        "seminarId": int(seminarId),
        "tenantId": int(tenantId),
        "sess": "",
        "globalUserId": "aeb77fdace2cca2d90caef190782555c",
        "openId": "",
        "browseInfo": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "browser": "Chrome", "version": "67.0.3396.99", "os": "Windows", "equipment": "电脑端",
            "resolution": "1920X1080",
            "referenceUrl": "https://uat-sde.smarket.net.cn/seminar.html?seminarId=4303&seminarName=%E6%96%B0%E7%BD%91%E5%85%B3%E6%B5%8B%E8%AF%95&instanceId=35686",
            "referenceTitle": "", "sessionId": "75882b67796fd029c505ff0c19600459"}
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "f69c8db7-e626-82d0-c2b8-034d6bfb4532"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type,type)
# api_template_config_get/获取模板信息
def get_most_api_template_config_get(type, domain,tenantId):
    path="/api/template/config/get"
    print "domain:", domain + path
    payload={
        "tenantId": ""+tenantId+"",
        "configId": "2",
        "isAssociate": "1"
           }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "2363374e-fbbf-ef31-a0a5-c15979f51e5f"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type,type)
# member_get/根据已登录的session获取用户信息
def get_most_member_get(type, domain,tenantId,loginSess):
    path="/member/get"
    print "domain:", domain + path
    payload={ "tenantId": int(tenantId),"sess":str(loginSess),"memberId":
["1079888"],"memberIdList": ["1079888"]}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "8a22bf86-efab-9cef-bf90-c0fbf75b8ffb"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type,type)
# api_topic_board_browse/浏览版面
def get_most_api_topic_board_browse(type, domain,topicId,tenantId):
    path="/api/topic/board/browse"
    print "domain:", domain + path
    payload={"browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36","browser":"Chrome","version":"70.0.3538.110","os":"Windows","equipment":"电脑端","resolution":"1360X768","referenceUrl":"http://hwuat.smarket.net.cn/topic/index.html","referenceTitle":"","sessionId":"8824532dea1a0b05a69586bde4e61207"},"topicId":int(topicId),"tenantId":int(tenantId),"sess":"","openId":"","globalUserId":"6011594ff2ae3ad38866d2b437df1d29"}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "6952b167-a8cf-a816-fc8f-56e353047195"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type,type)
# api_topic_browse/浏览主贴
def get_most_api_topic_browse(type, domain,postId,tenantId,loginSess3,loginSess):
    path="/api/topic/browse"
    print "domain:", domain + path
    payload={
        "postId": postId,
        "tenantId": tenantId,
        "sess": loginSess3,
        "globalUserId": "",
        "openId": "",
        "browseInfo": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "browser": "Chrome",
            "version": "69.0.3497.100",
            "os": "Windows",
            "equipment": "电脑端",
            "resolution": "1920X1080",
            "referenceUrl": "http://dev-webinar.smarket.net.cn/webcast.html",
            "referenceTitle": "",
            "sessionId": loginSess
        }
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "0fc2fb05-ccd0-a436-b322-fcbd8d0d6e66"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# api_topic_comment_query / 微讨论 - 微论坛 - 获取子版的评论列表
def get_most_api_topic_comment_query(type,domain,tenantId,topicId,sectionId,loginSess3):
    path="/api/topic/comment/query"
    print "domain:", domain + path
    payload={
          "tenantId": tenantId,
          "topicId": topicId,
          "sectionId": sectionId,
          "globalUserId": "39e5bd2a4a1c363d09b9fdd09323b3d8",
          "openId": "",
          "sess":loginSess3,
          "start": "1",
          "num": "20"
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "3005e24d-1e7b-7ddb-cb65-c2b52f858925"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# api_topic_forum_post_get/获取帖子详情
def get_most_api_topic_forum_post_get(type, domain, pos,tenantId):
    path="/api/topic/forum/post/get"
    print "domain:",domain+path
    payload={
        "postId": pos,
        "globalUserId": "7d2d23eb4d92c79710cc38bb5009ad5e",
        "openId": "",
        "sess":"",
        "tenantId": tenantId
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "94ca1113-8f6c-87b4-1f47-e52795ba6d64"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# member_LookUp/由下向上获取回填信息.实例联系人-模块联系人-注册用户信息.可传前端sess或不传.
def get_most_member_LookUp(type, domain,tenantId,seminarId_instanceId):
    path="/member/LookUp"
    print "domain:",domain+path
    payload={
          "tenantId": tenantId,
          "moduleId": 2,
          "instanceId": seminarId_instanceId,
          "cookieId": "39e5bd2a4a1c363d09b9fdd09323b3d8",
          "openId": ""
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "2c0701a0-38c9-1fa1-b9e7-bdf2cc18b6ad"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# member_schema_field_GetList/获取体系字段
def get_most_member_schema_field_GetList(type, domain, tenantId, schemaId):
    path="/member/schema/field/GetList"
    print "domain:",domain+path
    payload={
          "tenantId": tenantId,
          "schemaId": schemaId,
          "forForm": "0",
          "showPassword": "0"
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "a04046a2-e465-f387-1e5e-8a522d43dc3a"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# member_schema_orderUnique/获取体系的标识字段及顺序
def get_most_member_schema_orderUnique(type,domain,memberSchemaId):
    path="/member/schema/orderUnique"
    print "domain:",domain+path
    payload={
          "memberSchemaId": memberSchemaId
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "d4abedba-1fa0-40da-17c7-394a6103103c"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# member_schema_field_sorting_GetList/获取身份标识字段列表
def get_most_member_schema_field_sorting_GetList(type, domain,tenantId,schemaId):
    path="/member/schema/field/sorting/GetList"
    print "domain:",domain+path
    payload={
        "tenantId": tenantId,
        "schemaId": schemaId,
        "loginIds": [1088668,1088667]
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "95c95053-9a5e-b93c-88e8-2169ee24ca1a"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# member_sendCheckCode/身份认证体系发送手机修改密码验证码(member_sendCheckCode)新加的接口增加前端的控制（有效期和重发时间）
def get_most_member_sendCheckCode(type, domain,unique,memberSchemaId):
    path="/member/sendCheckCode"
    print "domain:",domain+path
    payload={
          "unique": unique,
          "memberSchemaId": memberSchemaId,
          "validTime": 60,
          "intervalTime": 6,
          "action": "login"
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "d338e3c0-6804-5c94-8da4-f2c22dd2d026"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# member_sendVerificationCode/向手机号码发送验证码
def get_most_member_sendVerificationCode(type, domain, memberFormId, loginSess3):
    path="/member/sendVerificationCode"
    print "domain:",domain+path
    payload={
          "memberFormId": memberFormId,
          "key": "15373660240",
          "content": "",
          "smsSign": "",
          "sess":loginSess3
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "735fa365-3a32-3e9e-edc6-b60b87310106"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# member_sendVerificationCodeToMail/向用户邮箱发送验证码
def get_most_member_sendVerificationCodeToMail(type, domain, memberFormId):
    path="/member/sendVerificationCodeToMail"
    print "domain:",domain+path
    payload={
          "memberFormId": memberFormId,
          "unique": "394522655@qq.com"
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "c91cf7cf-6a63-3e6a-09c7-611d7195050f"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# api_topic_forum_post_query/微讨论-微论坛-获取微论坛的主帖列表
def get_most_api_topic_forum_post_query(type, domain, tenantId,topicId,section_create,loginSess3):
    path="/api/topic/forum/post/query"
    print "domain:",domain+path
    payload={
          "tenantId": tenantId,
          "topicId": topicId,
          "sectionId": section_create,
          "activity": "1",
          "status": "5",
          "keyword": "",
          "sort": "5",
          "globalUserId": "39e5bd2a4a1c363d09b9fdd09323b3d8",
          "sess": loginSess3,
          "start": "0",
          "num": "20"
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "70ab3837-3c86-4602-c752-2f8ad2d6ae16"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# member_updateByField/会员修改，只修改给定的字段.需要登录
def get_most_member_updateByField(type, domain,loginSess):
    path="/member/updateByField"
    print "domain:",domain+path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
          "formData": [{"fieldId": 1,"text":"jobNumber:"+createTime+""},
                         {"fieldId": 2,"text":"enterprise:sinobase"}],
          "sess":str(loginSess)
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "0db2421c-d3a4-633f-c0ae-25e18973b4d4"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# api_topic_forum_post_reply_query/微讨论-微论坛-获取微论坛主贴的回帖列表
def get_most_api_topic_forum_post_reply_query(type, domain,tenantId,postId, loginSess3):
    path="/api/topic/forum/post/reply/query"
    print "domain:",domain+path
    payload={
          "tenantId": tenantId,
          "postId": postId,
           "openId": "",
          "globalUserId": "39e5bd2a4a1c363d09b9fdd09323b3d8",
          "sess": loginSess3,
          "start": "0",
          "num": "20"
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "a000d53b-0606-c99b-f333-14fb5059791f"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# api_topic_get/微讨论-获取版面详情
def get_most_api_topic_get(type, domain, tenantId,topicId):
    path="/api/topic/get"
    print "domain:",domain+path
    payload={
          "tenantId": tenantId,
          "topicId": topicId

    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "67e745cf-6abb-990c-04d3-1aa4fd05802d"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_topic_message_Create/发主帖/回帖
def get_most_api_topic_message_Create(type, domain, tenantId, topicId,loginSess3):
    path="/api/topic/message/create"
    print "domain:",domain+path
    payload={
        "tenantId": tenantId,
        "topicId": topicId,
        "content": "我0725111帖子",
        "postId": "",
        "enableReply": 1,
        "sess": loginSess3,
        "globalUserId": "7d2d23eb4d92c79710cc38bb5009ad5e",
        "nickname": "yi",
        "currentUrl": "http://s2-topic.smarket.net.cn/index.html"
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "92c29ae7-e610-f5ea-167c-2376b2c28987"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# api_topic_message_get/微讨论-留言板-获取留言板帖子的详细信息
def get_most_api_topic_message_get(type, domain, tenantId,postId,bakSess):
    path="/api/topic/message/get"
    print "domain:",domain+path
    payload={
          "tenantId": tenantId,
          "postId": postId,
          "sess": bakSess,
          "openId": "",
          "globalUserId": "c2809a8cd02ad645f169d63d26da0cc6"
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "7ca20acc-e89d-b8bf-5af5-dbb45f81aee5"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# api_topic_message_Query/获取主题帖列表以及对应帖子的回复列表
def get_most_api_topic_message_Query(type, domain, topicId,tenantId):
    path="/api/topic/message/query"
    print "domain:",domain+path
    payload={
       "topicId": topicId,
        "status": 2,
        "isHaveReply": 1,
        "openId": "",
        "globalUserId": "",
        "sess": "",
        "tenantId": tenantId,
        "start": 0,
        "num": 20
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "1787361b-e396-90e4-4e12-4f1a69b6a430"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# api_topic_message_reply_Query/某主帖的回复列表
def get_most_api_topic_message_reply_Query(type, domain,postId,loginSess3,tenantId):
    path="/api/topic/message/reply/query"
    print "domain:",domain+path
    payload={
        "postId": postId,
        "sess": loginSess3,
        "openId": "",
        "globalUserId": "c2809a8cd02ad645f169d63d26da0cc6",
        "tenantId":tenantId,
        "start": 0,
        "num": 20
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "77505e1d-cea9-7f39-d988-42850f8b9396"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# api_topic_share/分享主贴
def get_most_api_topic_share(type, domain,topicId,loginSess3,tenantId,loginSess):
    path="/api/topic/share"
    print "domain:",domain+path
    payload={
        "topicId": topicId,
        "tenantId": tenantId,
        "sess": loginSess3,
        "globalUserId": "",
        "openId": "",
        "browseInfo": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "browser": "Chrome",
            "version": "69.0.3497.100",
            "os": "Windows",
            "equipment": "电脑端",
            "resolution": "1920X1080",
            "referenceUrl": "http://dev-webinar.smarket.net.cn/webcast.html",
            "referenceTitle": "",
            "sessionId": loginSess
        }
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "f562ce14-615a-36ee-cb27-912a247a1401"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# member_loginByOpenId/使用openId登录，如果未登录会返回绑定使用的authCode
def get_most_member_loginByOpenId(type, domain,schemaId,wechatId):
    path="/member/loginByOpenId"
    print "domain:",domain+path
    payload={
         "schemaId": schemaId,
         "wechatId": wechatId,
         "openId": "otqO01CM74B9qQ2ZFwGiglaZFxzg",
         "clientType": "",
         "clientBrand": "",
         "clientVersion": "",
         "platform": ""
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "f208af51-7567-61e9-00de-aa00de3d4204"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# luckyDraw_client_actionByBigScreen/大屏抽奖的抽奖操作
def get_most_luckyDraw_client_actionByBigScreen(type, domain,tenantId,luckyDrawId):
    path = "/luckyDraw/client/actionByBigScreen"
    print "domain:", domain + path
    payload ={
      "tenantId": tenantId,
      "luckyDrawId":luckyDrawId,
      "instanceId": 1,
      "awardDetailId": 1,
      "num": 1
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "da220bce-6b4d-4fcf-b3f2-3570c7de6b3a"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# member_identification_sorting_Get/按当前租户的身份标识优先级来获取注册用户的个人信息
def get_most_member_identification_sorting_Get(type, domain,tenantId,loginSess3):
    path = "/member/identification/sorting/Get"
    print "domain:", domain + path
    payload ={
      "tenantId": str(tenantId),
      "sess":str(loginSess3)
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "86239689-7517-4326-b913-5bb042e15c39"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# luckyDraw_client_GetMyRedPacketLog/微信红包抽奖业务专用，通过OpenId获取当前用户的在该场活动的所有抽奖记录
def get_most_luckyDraw_client_GetMyRedPacketLog(type, domain,tenantId,luckyDrawId):
    path = "/luckyDraw/client/GetMyRedPacketLog"
    print "domain:", domain + path
    payload ={
      "tenantId":tenantId,
      "luckyDrawId": luckyDrawId,
      "openId": "oG80v1azw6L2LyxcVogDZnQ3pvNs"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "5e01ebe0-328e-4bb2-9e17-2e34ffb2fd8d"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_customform_browse/记录表单的浏览记录
def get_most_api_customform_browse(type, domain,tenantId,customFormId):
    path = "/api/customform/browse"
    print "domain:", domain + path
    payload ={
          "tenantId":tenantId,
            "customFormId": customFormId,
            "globalUserId": "a2bff28df34edb31b793f8a941dbf147",
            "sess": "",
            "openId": "",
            "linkId": 291825,
            "url": "",
            "channel": 0
        }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "548fb798-e273-41e0-950c-d57c7e9a6f67"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_customform_field_check/检查表单的不重复字段是否重复/不重复
def get_most_api_customform_field_check(type, domain,tenantId,customFormId):
    path = "/api/customform/field/check"
    print "domain:", domain + path
    payload ={
       "tenantId":tenantId,
        "customFormId": customFormId,
        "fieldName": "email",
        "fieldValue": "{{email}}"

    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "4735e12b-f91d-43e3-8289-d01bc37db677"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_customform_submit/自定义表单提交
def get_most_api_customform_submit(type, domain,tenantId,customFormId):
    path = "/api/customform/submit"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = {
        "tenantId": tenantId,
        "customFormId": customFormId,
        "globalUserId": createTime,
        "openId": "",
        "referenceUrl": "",
        "linkId": 29182,
        "formData": [
            {
                "fieldName": "name",
                "value": "linda"
            },
            {
                "fieldName": "mobile",
                "value": "18863142622"
            }
        ]
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "cab01ddc-4b27-4f36-ac56-056c120153e8"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# member_forgetPwd/找回密码
def get_most_member_forgetPwd(type, domain,memberSchemaId,memberFormId):
    path = "/member/forgetPwd"
    print "domain:", domain + path
    payload = {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwcm92aWRlcklkIjowLCJuYW1lIjoiMTMzOTMyMTMxMzUiLCJuaWNrbmFtZSI6IiIsImF2YXRhciI6IiIsImVtYWlsIjoiIiwicHJvdmlkZXIiOiJyZXNldHBhc3N3b3JkIiwic2Jhc2VUb2tlbiI6Ijg2NzU1MDM3ZGIxNzQyOWQwYmU2MWZhMzU1ZjBiZDhmIiwidW5pb25JZCI6bnVsbH0.CSDd78ivXb5ZzZaq_QX3RMswMfo3tJnPxNgBuSg7rMc",
        "memberSchemaId": str(memberSchemaId),
        "memberFormId": str(memberFormId),
        "password": "4297F44B13955235245B2497399D7A93",
        "url": "https://hwuat.smarket.net.cn/f/8cc23f308e063ab95cdf83676152dd16/view/setpassword.html?memberFormId=876&configId=37928&memberSchemaId=318&backUrl=",
        "referenceUrl": "https://hwuat.smarket.net.cn/f/8cc23f308e063ab95cdf83676152dd16/view/findpassword.html?memberFormId=876&configId=37928&memberSchemaId=318&backUrl=",
        "browseInfo": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "browser": "Chrome",
            "version": "70.0.3538.110",
            "os": "Windows",
            "equipment": "电脑端",
            "resolution": "1920X1080",
            "referenceUrl": "https://hwuat.smarket.net.cn/f/8cc23f308e063ab95cdf83676152dd16/view/findpassword.html?memberFormId=876&configId=37928&memberSchemaId=318&backUrl=",
            "referenceTitle": "",
            "sessionId": "3a0e1069f026d91bc048ce8e41819267"
        },
        "globalUserId": "39e5bd2a4a1c363d09b9fdd09323b3d8"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "20cb4a0c-bdd0-487f-aa77-782252ed6332"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:", payload
    return api_quester_common().Is_successful_status("POST", domain + path, payload, headers, type, type)
# member_UpdateIdentityInfo/修改身份信息
def get_most_member_UpdateIdentityInfo(type, domain,tenantId,schemaId,memberFormIda,loginSess):
    path="/member/UpdateIdentityInfo"
    print "domain:", domain + path
    payload ={
        "tenantId": str(tenantId),
        "schemaId": str(schemaId),
        "memberFormId": str(memberFormIda),
        "sess": str(loginSess),
        "url": "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/personalcenter-basic.html?memberFormId={{memberFormIda}}&configId=292114&memberSchemaId=2808",
        "browseInfo": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "browser": "Chrome",
            "version": "68.0.3440.106",
            "os": "Windows",
            "equipment": "电脑端",
            "resolution": "1536X864",
            "referenceUrl": "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/loginsuccess.html?memberFormId=6599&configId=292114&memberSchemaId=2808",
            "referenceTitle": "",
            "sessionId": "0838ddb748479ce00a85f47fe985d236"
        },
        "formData": [
            {
                "fieldName": "name",
                "value": "小小"
            },
            {
                "fieldName": "province",
                "value": [],
                "otherValue": ""
            },
            {
                "fieldName": "jobNumber",
                "value": ""
            },
            {
                "fieldName": "enterprise",
                "value": ""
            },
            {
                "fieldName": "department",
                "value": [],
                "otherValue": ""
            },
            {
                "fieldName": "position",
                "value": [],
                "otherValue": ""
            },
            {
                "fieldName": "gender",
                "value": [],
                "otherValue": ""
            },
            {
                "fieldName": "industry",
                "value": [],
                "otherValue": ""
            },
            {
                "fieldName": "ri",
                "value": ""
            }
        ],
        "globalUserId": "39e5bd2a4a1c363d09b9fdd09323b3d8"
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "6fcf2bcc-8d21-4b2b-8ef3-65f9d2dc7919"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# member_interaction_record/记录一个互动
def get_most_member_interaction_record(type, domain,tenantId,pollId ):
    path="/member/interaction/record"
    print "domain:", domain + path
    payload = {
        "tenantId":tenantId,
        "moduleId": 0,
        "instanceId": 0,
        "contactId": 0,
        "cookieId": "817c4822639dfe314fada85204644011",
        "openId": "",
        "loginId": 0,
        "memberId": 0,
        "actionKey": "form_browse",
        "objId": pollId,
        "objTitle": "测试表单",
        "signUserId": 0,
        "ip": "",
        "objectModuleId": 0,
        "objectInstanceId": "",
        "browseInfo": "string",
        "weChatId": 0,
        "sess":""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "9dc5d0a3-3f63-4260-a553-da30d3e6661e"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#  webinar_event_interaction_questionnaireResult/提交问卷
def get_most_webinar_event_interaction_questionnaireResult(type, domain,webinarId_instanceId,questionid_wj ):
    path="/webinar/event/interaction/questionnaireResult"
    print "domain:", domain + path
    payload =  {
      "instanceId":webinarId_instanceId,
      "questionaryId": questionid_wj,
      "memberId": 1,
      "title": "问卷2",
      "options": []
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "c4163467-63cc-4770-b741-8ca2af225c5b"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# member_member_associate_Logout/让关联微信粉丝或匿名用户的注册用户退出登录
def get_most_member_member_associate_Logout(type, domain,loginSess ):
    path="/member/member/associate/Logout"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload =  {
      "globalUserId": createTime,
      "schemaId": "",
      "sess":str(loginSess)
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "738e5afb-11ae-4d02-a11f-c2fbc85d8044"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# member_login/前台session
def get_most_member_member_login(type, domain,tenantId ,schemaId):
    path="/member/login"
    print "domain:", domain + path
    payload ={
        "tenantId": tenantId,
        "schemaId":schemaId,
        "memberFormId": "873",
        "memberSchemaId": "482",
        "unique": "15960167982",
        "token": "",
        "password": "4297F44B13955235245B2497399D7A93",
        "checkCode": "",
        "loginType": "",
        "url": "https://hwyhw.smarket.net.cn/f/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberId=873&memberFormId=873&trackId=0&memberSchemaId=482&configId=37066&weChatId=9418&backUrl=https%3A%2F%2Fhwyhw.smarket.net.cn%2Ff%2Fa4193c73ac8d7e3b81b384bea132c40a%2Fhtml%2FEventDetail.html%3FinstanceId%3D9445",
        "browseInfo": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "browser": "Chrome",
            "version": "71.0.3578.98",
            "os": "Windows",
            "equipment": "电脑端",
            "resolution": "1920X1080",
            "referenceUrl": "https://hwyhw.smarket.net.cn/f/a4193c73ac8d7e3b81b384bea132c40a/html/EventDetail.html?instanceId=9445",
            "referenceTitle": "",
            "sessionId": "7fa15a6f75e585ed7544c6953f555543"
        },
        "globalUserId": "1bf522f38f2e647bd6b46a4527b509df"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "978c00ff-7534-44ca-aaec-fac3d1104dd4"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# member_form_get/获取表单信息
def get_most_member_form_get(type, domain,memberFormId ,bakSess):
    path="/member/form/get"
    print "domain:", domain + path
    payload ={
      "memberFormId":memberFormId,
      "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "a15f235d-06d4-4d1e-b626-06ff598f99f5"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_member_contacts_register/用户注册
def get_most_api_member_contacts_register(type, domain,tenantId ,memberFormId):
    path="/api/member/contacts/register"
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    print "domain:", domain + path
    payload ={
      "tenantId": int(tenantId),
      "registerFormId": int(memberFormId),
      "formData":[
        {
          "fieldName": "name",
          "value": ""+createTime+" "
        },
        {
          "fieldName": "username",
          "value": "y"+createTime+""
        }
        ,
        {
          "fieldName": "password",
          "value": "4297F44B13955235245B2497399D7A93"
        }
      ],
      "token": "",
      "currentUrl": "",
      "globalUserId": "",
      "verify": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "69788ab0-02dc-45c7-92ed-49e7dba4eaf2"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_questionnaire_browse/记录问卷浏览记录
def get_most_api_questionnaire_browse(type, domain,tenantId ,questionid_wj):
    path="/api/questionnaire/browse"
    print "domain:", domain + path
    payload = {
        "tenantId":tenantId,
        "questionnaireId": questionid_wj,
        "globalUserId": "a2bff28df34edb31b793f8a941dbf147"
      }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "137a810f-d722-408d-a8a7-c023118843e3"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_questionnaire_get/获取问卷信息
def get_most_api_questionnaire_get(type, domain,tenantId ,questionid_wj):
    path="/api/questionnaire/get"
    print "domain:", domain + path
    payload = {
        "tenantId": tenantId,
        "questionnaireId":questionid_wj
     }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "17c1f3ba-1879-4b4a-a2a7-c760a6dc6950"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_questionnaire_query/查询问卷列表/全部
def get_most_api_questionnaire_query(type, domain,tenantId ):
    path="/api/questionnaire/query"
    print "domain:", domain + path
    payload = {
        "tenantId":tenantId,
        "moduleType": 3,
        "attachId": 5288,
        "status":-1,
        "type":-1,
        "start":0,
        "num":50
}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "22e570de-92ce-47e7-b0b8-13591a2acdb1"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_questionnaire_submit/提交问卷
def get_most_api_questionnaire_submit(type, domain,tenantId ,questionid_wj):
    path="/api/questionnaire/submit"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = {
            "tenantId":tenantId,
            "questionnaireId":questionid_wj,
            "globalUserId": createTime,
            "sess": "",
            "openId": "",
            "referenceUrl": "",
            "nickname": "",
            "headImgUrl": "",
            "gender": "",
            "city": "",
            "province": "",
            "country": "",
            "memberId": "",
           "url": "https://f.smarket.net.cn/s/template/e2ba9d7e12c7e74fa9ccb58318acc60d/view/PcQuestionnaire.html?questionaryId=8036&configId=306603",
            "preview": 1,
            "openid": "",
            "authCode": "",
            "remark": "",
            "sex": "",
            "subscribe": "",
            "subscribeTime": "",
            "subscribe_time": "",
            "unique": "",
            "needWechat": "",
            "formData": [{
                "fieldName": "name",
                "value": "Sunny"
            }],
          "browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36","browser":"Chrome","version":"68.0.3440.106","os":"Windows","equipment":"电脑端","resolution":"1920X1080","referenceTitle":"","sessionId":"854800f9fa18d5f2c2313e1735ac1699"}
        }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "0006e097-990c-46dd-919d-789eb7b43fd7"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_app_getconfiginfo/获取App相关的配置信息
def get_most_api_seminar_app_getconfiginfo(type, domain,bakSess ,tenantId):
    path="/api/seminar/app/getconfiginfo"
    print "domain:", domain + path
    payload = { "sess": bakSess,
        "tenantId": tenantId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "0a97796e-5eaa-45e8-aace-033ee8d14f1b"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_app_monitor_getappinfo/获取设备信息
def get_most_api_seminar_app_monitor_getappinfo(type, domain,seminarId):
    path="/api/seminar/app/monitor/getappinfo"
    print "domain:", domain + path
    payload = {       "sess": "000_test_use_only_create_by_jack",
        "seminarId": seminarId,
        "deviceType": "App",
        "deviceNum": "CA15B807-1131-482A-8C8C-D42A45AD700F"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "20c64e91-792b-4910-92f1-82d4bd7069d6"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_app_monitor_getclientalias/获取设备自定义编号GetNumberapp\seminar\monitor
def get_most_api_seminar_app_monitor_getclientalias(type, domain,tenantId,seminarId):
    path="/api/seminar/app/monitor/getclientalias"
    print "domain:", domain + path
    payload={
        "seq": "000_test_use_only_create_by_jack",
        "tenantId": int(tenantId),
        "seminarId": int(seminarId),
        "deviceType": "APP",
        "deviceNum": "456789-98765-ertfg444",
        "unitType": "iphonx",
        "ip": "192.168.8.8"
            }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "5c0d1870-8893-b698-2e6d-5d7f2ccc59d8"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_app_monitor_updateclientinfo/更新设备信息UpdateInfo
def get_most_api_seminar_app_monitor_updateclientinfo(type, domain,seminarId):
    path="/api/seminar/app/monitor/updateclientinfo"
    print "domain:", domain + path
    payload={
         "sess": "000_test_use_only_create_by_jack",
        "seminarId": ""+seminarId+"",
        "deviceType": "APP",
        "deviceNum": "2A336FB3-7C58-42AF-93F6-A6D350EB9FA",
        "clientAlias": "33",
        "responsiblePerson": "我",
        "account": "string",
        "ip": "string",
        "remark": "string"
            }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "ea557940-0bcb-a6ec-a120-df81d5f7e5dc"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_bigscreen_contacts_Get/获取大屏手机端签到信息/服务号租户
def get_most_api_seminar_bigscreen_contacts_Get(type, domain,tenantId,createCheckIn,contactId):
    path="/api/seminar/bigscreen/contacts/get"
    print "domain:", domain + path
    payload={
        "tenantId": ""+tenantId+"",
        "bigScreenId": ""+createCheckIn+"",
        "contactId": ""+contactId+""
            }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "aa6b31a9-a160-b94d-aad1-5600b3ff0cff"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_bigscreen_Get/获取大屏详细信息
def get_most_api_seminar_bigscreen_Get(type, domain,tenantId,createCheckIn):
    path="/api/seminar/bigscreen/get"
    print "domain:", domain + path
    payload={
        "tenantId": ""+tenantId+"",
        "id": ""+createCheckIn+""
            }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "1b821671-d9b5-3193-99d7-b9462f293b16"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_bigscreen_group_query/获取大屏组列表/服务号租户
def get_most_api_seminar_bigscreen_group_query(type, domain,tenantId,seminarId):
    path="/api/seminar/bigscreen/group/query"
    print "domain:", domain + path
    payload={
        "tenantId": ""+tenantId+"",
        "groupId": 160,
        "seminarId": ""+seminarId+""
            }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "8b11be19-0615-ed93-70b2-be08c7644cf0"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_contacts_field_Get/获取联系人字段列表
def get_most_api_seminar_contacts_field_Get(type, domain,tenantId,seminarId):
    path="/api/seminar/contacts/field/get"
    print "domain:", domain + path
    payload={
        "tenantId": ""+tenantId+"",
        "seminarId": ""+seminarId+""
            }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "60d48ace-dfff-d156-6a55-01ed0e5c50d9"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_contacts_Get/线下会根据sess、openid、globalUserId查询报名信息
def get_most_api_seminar_contacts_Get(type, domain,tenantId,seminarId,bakSess):
    path="/api/seminar/contacts/get"
    print "domain:", domain + path
    payload={
        "tenantId": ""+tenantId+"",
        "seminarId": ""+seminarId+"",
        "sess": ""+bakSess+"",
        "withFormData": "0"
            }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "f1eefe03-9eaf-a785-b144-278dc778177d"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_contacts_SignUp/线下会报名(报名时可以新增或更新注册信息)
def get_most_api_seminar_contacts_SignUp(type, domain,tenantId,seminarId,customFormId):
    path="/api/seminar/contacts/signup"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
        "tenantId": ""+tenantId+"",
        "seminarId": ""+seminarId+"",
        "formData": [
            {
                "fieldName": "name",
                "value": createTime
            },
            {
                "fieldName": "email",
                "value": "{{$timestamp}}@qq.com"
            }
        ],
        "globalUserId": createTime,
        "openId": "",
        "customFormId": ""+customFormId+"",
        "channel": "",
        "ip": "",
        "subSeminarIds": "",
        "needRegistration": 0,
        "token": "",
        "memberFormId": "",
        "weChatId": ""
            }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "c4731cbe-4e73-4d17-aa62-37cc590922db"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_contacts_Update/线下会根据sess更新报名信息（可选是否更新注册信息）/更新注册信息
def get_most_api_seminar_contacts_Update(type, domain,tenantId,loginSess3,seminarId):
    path="/api/seminar/contacts/update"
    print "domain:", domain + path
    payload={
        "tenantId": ""+tenantId+"",
        "seminarId": int(seminarId),
        "globalUserId": "1e7f4b94927007fad87ad69b8eb44d65",
        "openId": "",
        "sess": ""+loginSess3+"",
        "formData": [
            {
                "fieldName": "name",
                "value": "sunkaihan"
            },
            {
                "fieldName": "mobile",
                "value": "18630138542"
            }
        ],
        "subSeminarIds": "",
        "needRegistration": 0,
        "token": "",
        "memberFormId": "",
        "weChatId": ""
            }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "e74ae64f-a976-9e7e-6662-cea79119b538"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_customform_subseminar_get/获取报名表单关联的分会场信息
def get_most_api_seminar_customform_subseminar_get(type, domain,tenantId,seminarId,customFormId):
    path="/api/seminar/customform/subseminar/get"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "seminarId": seminarId,
        "customFormId": customFormId
            }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "6d61c804-51c6-6cb6-ed63-dbf41102eb19"
    }
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#file_downloadWithEmail/文章资料下载
def get_file_downloadWithEmail(type,domain,articleId,fileIds,email,tenantId,loginSess):
    path="/file/downloadWithEmail"
    print "domain:", domain + path
    payload={
    "articleId":str(articleId),
    "openId":"",
    "globalUserId":"e7b0306b56427af5f140adb2a40ee915",
    "fileList":[
        str(fileIds)
    ],
    "email":"1946898935@qq.com",
    "forEmailTemp":0,
    "referenceUrl":"https://f.smarket.net.cn/s/template/27bfd3aaa163a0b75e40770732dbbaa3/html/info.html?articleId=228325&configId=246947",
    "moduleType":26,
    "instanceId":"0",
    "extra":{
        "tenantId":tenantId,
        "instanceId":"0",
        "memberId":0,
        "moduleId":"0",
        "openId":"",
        "weChatId":0,
        "objInstanceId":0
    },
    "browseInfo":{
        "userAgent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
        "browser":"Chrome",
        "version":"67.0.3396.79",
        "os":"Windows",
        "equipment":"pc",
        "resolution":"1280X720",
        "referenceUrl":"https://f.smarket.net.cn/s/template/f619f723e83dccccc76a0d20c664b69a/html/list.html?articleCategoryId=102161&configId=246876&pageTitle=%E6%96%87%E7%AB%A0%E9%A2%98%E7%9B%AE__%E6%9C%AC%E5%9C%B0%E6%96%87%E7%AB%A0_%E6%96%87%E7%AB%A0%E7%AE%A1%E7%90%86__Smarket%E6%99%BA%E8%90%A5",
        "referenceTitle":"",
        "sess": loginSess
    }
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "b72e89bd-025b-4e5a-af5e-bd3ee49c6011"
    }

    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#member_identification_information_Get/用户详情页调的接口，区别与getInfo
def get_member_identification_information_Get(type,domain,tenantId,schemaId,memberId):
    path="/member/identification/information/Get"
    print "domain:", domain + path
    payload={"tenantId": tenantId,"schemaId": schemaId,"loginId": memberId,"isTemplate": "0","sess": ""}
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "51bd8bf1-f19b-44ac-8bf3-fd86420cf174"
    }

    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#file_delete/该接口为后台接口，后期即将移除，请不要继续使用，删除文件
def get_file_delete(type,domain,tenantId,fileId,bakSess):
    path="/file/delete"
    print "domain:", domain + path
    payload={"tenantId": tenantId,"moduleType": "","instanceId": "","fileId": [fileId],"sess":bakSess}
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "5842bf82-4d0e-435d-8bb1-a13ace894b20"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#webinar_open_getLuckyDrawRoster/获取会议的中奖名单
def get_webinar_open_getLuckyDrawRoster(type,domain,webinarId,tenantId,webinarId_instanceId):
    path="/webinar/open/getLuckyDrawRoster"
    print "domain:", domain + path
    payload={"webinarId": webinarId,"tenantId": tenantId,"instanceId": webinarId_instanceId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "f1bb671c-fe30-44e1-8ef0-70e245373e03"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#luckyDraw_client_hasParticipate/有问题，该接口为后台接口，后期即将移除，请不要继续使用，检查某个用户是否已经参与过大屏抽奖，--创建线下会，报名会议后参与的抽奖
# 因此接口特殊，故需要每个接口单独配置
def get_luckyDraw_client_hasParticipate(type,domain,tenantId,luckyDrawId,bakSess):
    path="/luckyDraw/client/hasParticipate"
    print "domain:", domain + path
    payload={
        "tenantId": int(tenantId),
        "luckyDrawId": 977,
        "openId": "otqO01CM74B9qQ2ZFwGiglaZFxzg",
        "memberId": 566247,
        "globalUserId": "39e5bd2a4a1c363d09b9fdd09323b3d8",
        "sess": str(bakSess)
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "7186cc84-1938-428e-9270-89b6f4d9164e"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#luckyDraw_client_participate/有问题，大屏抽奖，用户现场主动参与抽奖，如扫码-马叔，手机端有问题
def get_luckyDraw_client_participate(type,domain,tenantId,luckyDrawId,bakSess):
    path="/luckyDraw/client/participate"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "luckyDrawId": luckyDrawId,
        "openId": "oqbfJjlUJYAomlkfZlRGpZAKAVE0",
        "memberId": "{{memberId}}",
        "globalUserId": "",
        "name": "this is a name",
        "mobile": "15960167982",
        "unique": "aa@vv.com",
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "f9e946a8-1775-4e56-b450-b1f68b347e90"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful_status("POST", domain + path, payload, headers, type, type)
#luckyDraw_client_saveUserInfo/收集中奖用户信息
def get_luckyDraw_client_saveUserInfo(type,domain,luckyDrawId):
    path="/luckyDraw/client/saveUserInfo"
    print "domain:", domain + path
    payload={
        "luckyDrawId": luckyDrawId,
        "resultId": 415353,
        "userName": "Zhangsan",
        "userMobile": 13412345678,
        "userAddr": "Hebei,Shijiazhuang",
        "postcode": 105000
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "a1ec9e0e-271f-4175-ae01-814b03d786a1"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#luckyDraw/client/saveUserInfo统计
def get_luckyDraw_client_saveUserInfo_count(type,domain,luckyDrawId):
    path="/luckyDraw/client/saveUserInfo"
    print "domain:", domain + path
    payload={
        "luckyDrawId": luckyDrawId,
        "resultId": 415353,
        "userName": "Zhangsan",
        "userMobile": 13412345678,
        "userAddr": "Hebei,Shijiazhuang",
        "postcode": 105000
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "28937c5e-1c74-4cb6-afab-412aebf8ae4f"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#luckyDraw_client_share/分享后参与情况，使用该接口获取分享资格
def get_luckyDraw_client_share(type,domain,luckyDrawId):
    path="/luckyDraw/client/share"
    print "domain:", domain + path
    payload={
        "luckyDrawId": luckyDrawId,
        "cookieId": "13244234",
        "openId": "oG80v1azw6L2LyxcVogDZnQ3pvNs",
        "sess": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "19486116-0bfc-4f97-82dd-d080e6122983"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#luckyDraw_get/获取抽奖信息
def get_luckyDraw_get(type,domain,luckyDrawId):
    path="/luckyDraw/get"
    print "domain:", domain + path
    payload={"luckyDrawId": luckyDrawId,"hasVirtualAward": "false"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "0bec6aea-60fc-4421-8526-d593b1e96aa9"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#luckyDraw_getAwardDetailList/获取奖品列表信息
def get_luckyDraw_getAwardDetailList(type,domain,luckyDrawId):
    path="/luckyDraw/getAwardDetailList"
    print "domain:", domain + path
    payload={"luckyDrawId": int(luckyDrawId)}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "453d2b36-c4bd-4138-b69a-e1e886eaf1df"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#luckyDraw_redPacket_getLotteryRecord/大屏红包抽奖获取中奖名单
def get_luckyDraw_redPacket_getLotteryRecord(type,domain,tenantId,luckyDrawId):
    path="/luckyDraw/redPacket/getLotteryRecord"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "luckyDrawId": luckyDrawId,
        "start": 0,
        "num": 10,
        "weChatInfo": "oG80v1azw6L2LyxcVogDZnQ3pvNs",
        "sortId": "",
        "drawStatus": "",
        "receiveStatus": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "69e78503-9832-49cb-a479-85ca5a6b73ec"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#luckyDraw_redPacket_pushMessage/前端推送消息到node服务器
def get_luckyDraw_redPacket_pushMessage(type,domain,luckyDrawId,tenantId,bakSess):
    path="/luckyDraw/redPacket/pushMessage"
    print "domain:", domain + path
    payload={
        "roomId": "1116",
        "type": "openState ",
        "luckyDrawId": luckyDrawId,
        "tenantId": tenantId,
        "sess": bakSess,
        "content": "true"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "f8d72110-8e9d-437f-8242-ae129ac8f863"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#luckyDraw_result_getState/获取大屏抽奖的轮次状态，如果未开始的轮次，标记未开始，已开始的，返回中奖名单
def get_luckyDraw_result_getState(type,domain,tenantId,luckyDrawId):
    path="/luckyDraw/result/getState"
    print "domain:", domain + path
    payload={"tenantId": tenantId,"luckyDrawId": luckyDrawId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "dc2d5c92-15cd-484d-87a5-e8817d6fcae9"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#luckyDraw_result_getUserResultList/获取个人的普通抽奖记录
def get_luckyDraw_result_getUserResultList(type,domain,luckyDrawId,bakSess):
    path="/luckyDraw/result/getUserResultList"
    print "domain:", domain + path
    payload={
        "luckyDrawId": luckyDrawId,
        "sess": bakSess,
        "openId": "",
        "cookieId": "",
        "start": 0,
        "num": 20,
        "startTime": "2018-05-31",
        "endTime": "2018-05-31"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "126d7365-8b7d-4fdb-bea2-3ecfab7071a4"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#luckyDraw_view/检测是否参与过抽奖
def get_luckyDraw_view(type,domain,luckyDrawId):
    path="/luckyDraw/view"
    print "domain:", domain + path
    payload={
        "luckyDrawId": luckyDrawId,
        "globalUserId": "",
        "openId": "oG80v1azw6L2LyxcVogDZnQ3pvNs"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "41359d87-c3f6-4fba-9c5f-fc2ed2a87d39"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#topic_get/获取发帖信息
def get_topic_get(type,domain,topicId):
    path="/topic/get"
    print "domain:", domain + path
    payload={"topicIds":[topicId]}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "aac4a456-f3d6-4b43-9154-45faab7db20c"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_productLine_query/获取租户下产品线列表
def get_api_productLine_query(type,domain,tenantId):
    path="/api/productline/query"
    print "domain:", domain + path
    payload={
    "tenantId": tenantId,
    "withDeleted": 0,
    "num": 10,
    "start": 0
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "d45949bc-77c0-4113-b301-093102771301"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_poll_share/分享投票行为
def get_api_poll_share(type,domain,pollId,tenantId):
    path="/api/poll/share"
    print "domain:", domain + path
    payload={
        "pollId": pollId,
        "tenantId": tenantId,
        "sess": "",
        "globalUserId": "aeb77fdace2cca2d90caef190782555c",
        "openId": "",
        "browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36","browser":"Chrome","version":"67.0.3396.99","os":"Windows","equipment":"pc","resolution":"1920X1080","referenceUrl":"","referenceTitle":"","sessionId":"75882b67796fd029c505ff0c19600459"}
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "928e4fbd-a4ac-452f-88f3-5a683121289c"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_poll_browse/浏览投票行为
def get_api_poll_browse(type,domain,pollId,tenantId):
    path="/api/poll/browse"
    print "domain:", domain + path
    payload={
        "pollId": pollId,
        "tenantId": tenantId,
        "sess": "",
        "globalUserId": "aeb77fdace2cca2d90caef190782555c",
        "openId": "",
        "browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36","browser":"Chrome","version":"67.0.3396.99","os":"Windows","equipment":"pc","resolution":"1920X1080","referenceUrl":"","referenceTitle":"","sessionId":"75882b67796fd029c505ff0c19600459"}
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "dbdff2ba-f3f6-49ae-96e4-2c5bae52a622"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_webinar_channel_query/根据会议ID获取该会议的渠道追踪代码
def get_most_api_webinar_channel_query(type, domain, tenantId,webinarId):
    path="/api/webinar/channel/query"
    print "domain:", domain + path
    payload={
          "tenantId": int(tenantId),
          "webinarId": int(webinarId)
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "9dc425ec-9f80-7b7d-5cd2-3780ea883116"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_webinar_contacts_signup/会议报名
def get_api_webinar_contacts_signup(type, domain,loginSess3,tenantId,webinarId,customFormId):
    path="/api/webinar/contacts/signup"
    print "domain:", domain + path
    payload={
        "sess": loginSess3,
        "tenantId": tenantId,
        "webinarId": webinarId,
        "formId": customFormId,
        "channel": "",
        "formData": [
            {"fieldName": "name", "value": "eric"},
            {"fieldName": "mobile", "value": "13315110180"},
            {"fieldName": "email", "value": "eric@sinobasedm.com"}
        ],
        "url": "http://s2-webinar.smarket.net.cn",
        "source": "PC",
        "referenceUrl": "http://www.smarket.net.cn",
        "globalUserId": "7d2d23eb4d92c79710cc38bb5009ad5e",
        "weChatId": 0,
        "browseInfo": {}
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "c155be15-9e55-4c20-ac55-47c6b389f8b4"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_webinar_get/获取直播会议信息
def get_api_webinar_get(type, domain, tenantId,webinarId):
    path="/api/webinar/get"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "webinarId": webinarId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "6bc08a9d-d985-453d-ab47-731e266893fd"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_webinar_interaction_filedownload_create/下载文件互动记录，有问题
def get_api_webinar_interaction_filedownload_create(type, domain, tenantId,loginSess3,webinarId,fileId):
    path="/api/webinar/interaction/filedownload/create"
    print "domain:", domain + path
    payload={
        "tenantId": int(tenantId),
        "sess": loginSess3,
        "webinarId": webinarId,
        "fileId": fileId,
        "title": "Phase I interface"
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "8d118043-6fae-4f7c-aba9-f434104a3156"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_wechat_contacts_check/根据openIds批量查询用户对某个微信号的关注状态/-1 ：返回所有包含关注和未关注的
def get_api_wechat_contacts_check(type, domain, tenantId,wechatId):
    path="/api/wechat/contacts/check"
    print "domain:", domain + path
    payload={
        "tenantId":tenantId,
        "weChatId":wechatId,
        "openIds": ["otYzet6sfobnSyeIdqLBUDk4szQk","otYzet6J_AvPl_suFiDFf9rTAPuY","otYzet0hYSy2cyadVYsUK3sKxOJU"],
        "subscribeStatus": -1
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "946a7c19-5e0b-4ef0-b5a4-ebd26ca59bf8"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_wechat_contacts_get/获取微信粉丝信息/简体
def get_api_wechat_contacts_get(type, domain, tenantId,wechatId,openId):
    path="/api/wechat/contacts/get"
    print "domain:", domain + path
    payload={
        "tenantId":tenantId,
        "weChatId":wechatId,
        "openId":openId,
        "lang": "zh_CN"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "2705abb4-62da-42c8-8d10-93cbc58ca712"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_wechat_get/获取微信信息
def get_api_wechat_get(type, domain, tenantId,wechatId):
    path="/api/wechat/get"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "weChatId": wechatId,
        "isAuthorize": 0
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "e9421eff-0b4c-42cf-8062-2ed4ae2c0ae1"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_wechat_jssdk_config_get/获取微信jssdk配置
def get_api_wechat_jssdk_config_get(type, domain, tenantId,wechatId):
    path="/api/wechat/jssdk/config/get"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "weChatId": wechatId,
        "jsApiList": [
            "stopRecord",
            "onVoiceRecordEnd",
            "uploadVoice",
            "startRecord"
        ],
        "url": "aaa",
        "onDebug": 0
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "2b466248-76ae-428b-8d4d-57233a055bc6"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_article_category_get/获取栏目的详细信息/带模板
def get_api_article_category_get(type, domain, tenantId,articleId):
    path="/api/article/category/get"
    print "domain:", domain + path
    payload={
        "tenantId":tenantId,
        "articleCategoryId":articleId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "7922ed7c-b614-492e-b12e-f9381ad61936"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_common_shorturl_create/公共服务-短链接-生成短链接
def get_api_common_shorturl_create(type, domain):
    path="/api/common/shorturl/create"
    print "domain:", domain + path
    payload={
        "url": "http://uao.so/spm6599c292114",
        "keyword": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "1d6f1cd5-6abb-4585-9baa-c632851fd5e8"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_content_collect_query/查询我收藏的信息
def get_api_content_collect_query(type, domain,tenantId,bakSess):
    path="/api/content/collect/query"
    print "domain:", domain + path
    payload={
        "tenantId": int(tenantId),
        "sess": bakSess,
        "start": 1,
        "num": 50
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "e9ce356d-42f7-4fd4-8b6d-e333387091f5"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_customform_record_query/获取某个OpenId的表单的记录
def get_api_customform_record_query(type, domain,tenantId,customFormId):
    path="/api/customform/record/query"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "customFormId": customFormId,
        "openId": "oG80v1UWrE1J5QwmSUJqvdzqYhI4",
        "start": 0,
        "num": 50
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "c36ac8cc-968e-4ec0-8814-9cab8a331d35"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_customform_share/分享表单行为
def get_api_customform_share(type, domain,tenantId,customFormId):
    path="/api/customform/share"
    print "domain:", domain + path
    payload={
        "customFormId":customFormId,
        "tenantId": tenantId,
        "sess": "",
        "globalUserId": "aeb77fdace2cca2d90caef190782555c",
        "openId": "",
        "browseInfo": {"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36","browser":"Chrome","version":"69.0.3497.100","os":"Windows","equipment":"pc","resolution":"1920X1080","referenceUrl":"https://test-tool.smarket.net.cn//customform/index.html","referenceTitle":"","sessionId":"ee20d80f98bbbf1f9799ca140c007ac2"}
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "2d3749cf-531a-49f2-a200-2c4d2e8abaed"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_dic_get/20180810-根据字典表id获取字典列表及字典值所级联的下级字典表名称
def get_api_dic_get(type, domain,tenantId,dicId):
    path="/api/dic/get"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "dicId": dicId,
        "sorts": "1"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "516d61ec-e556-4f84-9bb5-3a8a546ca9e9"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_dic_gettree/根据字典表id获取字典树形(当前字典值及下级字典值)结构 最多返回两级
def get_api_dic_gettree(type, domain,dicId,tenantId):
    path="/api/dic/gettree"
    print "domain:", domain + path
    payload={
        "dicId": dicId,
        "tenantId": tenantId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "1e5dd1ef-74b9-4ac9-859f-3f0f7b45cf08"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_dic_params_set/新增或修改字典表的值
def get_api_dic_params_set(type, domain,tenantId,dicId,bakSess):
    path="/api/dic/params/set"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
        "tenantId": tenantId,
        "paramId": "",
        "dicId": dicId,
        "name": createTime,
        "cascadeId": "",
        "isDefault": 0,
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "7b15feda-da49-4e75-8a90-fc277af3a51a"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_seminar_field_Get/获取线下会会议属性字段列表
def get_api_seminar_field_Get(type, domain,tenantId):
    path="/api/seminar/field/get"
    print "domain:", domain + path
    payload={"tenantId": tenantId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "7b15feda-da49-4e75-8a90-fc277af3a51a"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#interaction_getCountByType/获取实例的行为记录数量
def get_interaction_getCountByType(type, domain,tenantId,seminarId_instanceId):
    path="/interaction/getCountByType"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "instanceIds": [

            seminarId_instanceId
        ],
        "moduleType": 3,
        "type": "survey_browse"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "a7e4809a-52d0-4666-8439-5d72d28acd7f"
    }

    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#interaction_getDetailList/ 获取租户下一个用户的某类型的互动记录
def get_interaction_getDetailList(type, domain,tenantId,seminarId_instanceId,memberId):
    path="/interaction/getDetailList"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "instanceId": seminarId_instanceId,
        "moduleType": 3,
        "memberId": memberId,
        "type": "post_create",
        "start": 0,
        "num": -1
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "2ab0f671-dd0b-4fe8-aa3c-61543be6a7bd"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#interaction_getFileDownloads/获取租户下载文件记录，如果传递memberWords则获取这个人的下载记录，如果传递fileWords，则获取这个文件的下载记录
def get_interaction_getFileDownloads(type, domain,tenantId):
    path="/interaction/getFileDownloads"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "memberWords": "",
        "fileWords": "yiiqjiekou",
        "start": 0,
        "num": 10
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "34e5ae83-260a-468e-bf9e-04253b538540"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# interaction_getListByMember/获取前台sess对应的互动行为记录
def get_most_interaction_getListByMember(type, domain, tenantId, loginSess3):
    path="/interaction/getListByMember"
    print "domain:", domain + path
    payload={
          "tenantId": tenantId,
          "moduleType": 4,
          "instanceId": -1,
          "type": "survey_submit",
          "start": 0,
          "num": -1,
          "sess": loginSess3
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "316aeb52-330a-b295-977d-b39b38835f02"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# interaction_getStatCountList/该接口为后台接口，后期即将移除，请不要继续使用，获取用户在实例中的（浏览/分享/资料）计数,有问题
def get_most_interaction_getStatCountList(type, domain, tenantId, seminarId_instanceId,bakSess):
    path="/interaction/getStatCountList"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "instanceId": seminarId_instanceId,
        "moduleType": 3,
        "memberId": 157740,
        "type": "project_browse",
        "statType": "url",
        "start": 0,
        "num": 5,
        "sess": bakSess
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "1a4a4e43-77c0-bfc0-6eec-5a0f084e8c4d"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_form_Get/获取报名表单详细信息
def get_most_api_seminar_form_Get(type, domain, tenantId,seminarId):
    path="/api/seminar/form/get"
    print "domain:", domain + path
    payload={
          "tenantId": tenantId,
          "seminarId": seminarId,
          "formId": 875
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "f8e18baa-149a-dc21-ff42-ae6fe333fe56"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_Get/获取线下会议相关信息
def get_most_api_seminar_Get(type, domain, tenantId,seminarId):
    path="/api/seminar/get"
    print "domain:", domain + path
    payload={
          "tenantId": tenantId,
          "seminarId": seminarId
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "18a63c5a-3ad6-082d-e3f4-13c07a1eb5c6"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_signingpoint_interaction_get/线下会获取互动设置的领奖点列表，从来都没有启用过的互动不在返回列表
def get_most_api_seminar_signingpoint_interaction_get(type, domain,tenantId, seminarId):
    path="/api/seminar/signingpoint/interaction/get"
    print "domain:", domain + path
    payload={
          "tenantId": tenantId,
          "seminarId": seminarId
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "7d20714d-5911-d93c-2d84-e01bcdca8bfd"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_signingpoint_Statistics/签到点按通道统计签到人次
def get_most_api_seminar_signingpoint_Statistics(type, domain, tenantId,seminarId,passageId):
    path="/api/seminar/signingpoint/statistics"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "seminarId": seminarId,
        "checkInGroupId": "0",
        "passageId": passageId,
        "signingPointId": ""
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "23671bb1-40d5-33ea-13ee-9ee224d47549"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_seminar_subseminar_Query/获取分会场列表
def get_most_api_seminar_subseminar_Query(type, domain, tenantId, seminarId):
    path="/api/seminar/subseminar/query"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "seminarId": seminarId,
        "start": 0,
        "num": 20
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "4ea3e5ee-7a84-ac33-899b-0224d1ba08da"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_webinar_demand_record/奥点云点播观看次数，写成死值
def get_most_api_webinar_demand_record(type, domain, tenantId, webinarId,videoId):
    path="/api/webinar/demand/record"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "webinarId": webinarId,
        "videoId": videoId
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "da891498-e4ba-d478-f716-0bee29bc337f"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# article_getCollectionList/微信模块获取收藏列表,有问题
def get_most_article_getCollectionList(type, domain,loginSess3):
    path="/article/getCollectionList"
    print "domain:", domain + path
    payload={
          "start": 0,
          "num": 15,
          "sess": loginSess3
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "0c9935e9-f650-af30-c7cf-8ed856534371"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful_status("POST", domain + path, payload, headers, type, type)
# app_seminar_contact_nfc_bind/该接口为APP专用接口，项目不要使用，nfc批量绑定
def get_most_app_seminar_contact_nfc_bind(type,domain, seminarId,bakSess):
    path="/app/seminar/contact/nfc/bind"
    print "domain:", domain + path
    payload={
          "items": [
            {"seminarId": seminarId, "chipNo": "SDD32232332","contactId": 1,"bindTime": "1491374562"}
          ],
          "sess": bakSess
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "8581546c-4f05-ccca-bf68-e72f7dd5b156"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# app_seminar_contact_nfc_getBindRecord/获取绑卡记录，有问题
def get_most_app_seminar_contact_nfc_getBindRecord(type, domain, seminarId, contactId,bakSess):
    path="/app/seminar/contact/nfc/getBindRecord"
    print "domain:", domain + path
    payload={
          "seminarId": seminarId,
          "contactId":contactId,
          "sess": bakSess
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "f682fbd4-1c7c-3454-12e7-8cab38c4b760"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# app_seminar_contact_nfc_getList/该接口为APP专用接口，项目不要使用，获取nfc绑定关系列表
def get_most_app_seminar_contact_nfc_getList(type, domain, seminarId,bakSess):
    path="/app/seminar/contact/nfc/getList"
    print "domain:", domain + path
    payload={
          "seminarId": seminarId,
          "lastModify": "2018-12-26T18:00:00",
          "start": 0,
          "num": 100,
          "sess": bakSess
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "20943209-50a4-32a5-0a6b-f6fbf0ff680e"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# app_seminar_contact_prints_getList/APP获取打印大屏签到信息
def get_most_app_seminar_contact_prints_getList(type, domain, seminarId, signingPointId,loginSess3):
    path="/app/seminar/contact/prints/getList"
    print "domain:", domain + path
    payload={
          "seminarId": seminarId,
          "signPointId":signingPointId,
          "_sess": loginSess3,
          "id": "0",
          "num": "10"
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "aba96f2a-0af3-51db-75e8-e38d0720471f"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# tag_api_thirdTrigger_add/有问题，产品第三方行为触发-马震(华为不用，不监控 )
def get_most_tag_api_thirdTrigger_add(type, domain,tenantId):
    path="/tag/api/thirdTrigger/add"
    print "domain:", domain + path
    payload={
            "tenantId": tenantId,"actionKey": "third_behavior_key","uniqueField": "weChatNum",
            "uniqueFieldValue": "oG80v1WEYqATpSTdxH3-ZKS6Hwn4","objectId": "全局对象唯一id","objectTitle": "全局对象标题",
            "objectType": "表单",
            "triggerTag": [
              {"tagFieldName": "文章标签","tagFieldNameEn": "artitag","tags": ["吃饭"]},
              {"tagFieldName": "标签","tagFieldNameEn": "articletag","tags": []}
            ]
      }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "b80f6057-b7af-eaf8-2f4e-b85a72fa59df"
    }
    return api_quester_common().Is_successful_status("POST", domain + path, payload, headers, type, type)
# app_seminar_contact_prints_getSigningPointInfo/获取会议下签到点缩略信息
def get_most_app_seminar_contact_prints_getSigningPointInfo(type, domain, seminarId,bakSess):
    path="/app/seminar/contact/prints/getSigningPointInfo"
    print "domain:", domain + path
    payload={
        "seminarId": seminarId,
        "sess": bakSess
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "0cfaf4a4-be43-c589-325f-7e0573427019"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# app_seminar_contact_prints_updatePrintLog/更新APP打印大屏签到日志
def get_most_app_seminar_contact_prints_updatePrintLog(type, domain, seminarId,tenantId,seminarId_instanceId,contactId,bakSess):
    path="/app/seminar/contact/prints/updatePrintLog"
    print "domain:", domain + path
    payload={
          "seminarId": int(seminarId),
          "tenantId": int(tenantId),
          "instanceId": int(seminarId_instanceId),
          "checkIdList": [
            {
              "id": "2",
              "contactId": int(contactId),
              "time": "2015-03-20 14:22:33"
            }
          ],
          "_sess": str(bakSess)
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "c8a27dca-8a2a-a7e6-6c7f-3dd55806ed4e"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# tag_application_GetByObject/获取某个应用的标签使用情况-马叔
def get_most_tag_application_GetByObject(type, domain,tenantId,seminarId_instanceId,bakSess):
    path="/tag/application/GetByObject"
    print "domain:", domain + path
    payload={
          "tenantId": tenantId,
          "moduleId": "2",
          "instanceId": seminarId_instanceId,
          "objectId": "7440",
          "objectType": "问卷",
          "sess": bakSess
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=",
        'cache-control': "no-cache",
        'postman-token': "592804b9-4154-cc04-2193-a3bcacc583ff"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# app_seminar_getList/该接口为APP专用接口，项目不要使用，获取会议列表
def get_most_app_seminar_getList(type, domain, tenantId):
    path="/app/seminar/getList"
    print "domain:", domain + path
    payload={
            "tenantId": tenantId,
            "start": 0,
            "num": 10
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "e1916ed0-967c-612c-6cff-598a9eb8680c"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# tag_application_getByOpenId/通过粉丝OpenId来获取用户的标签
def get_most_tag_application_getByOpenId(type, domain, tenantId):
    path="/tag/application/getByOpenId"
    print "domain:", domain + path
    payload={
          "tenantId": tenantId,
          "openId": "otYzet17K03Eh8QAnXN5Y6LjUgpo"
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "b2e1046d-f1ac-3676-90ed-046b9c1cc22c"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# app_seminar_signingPoint_checkIn_create/该接口为APP专用接口，项目不要使用，创建签到信息
def get_most_app_seminar_signingPoint_checkIn_create(type, domain, signingPointId,contactId,seminarId,bakSess):
    path="/app/seminar/signingPoint/checkIn/create"
    print "domain:", domain + path
    payload={
          "isValidateCheckIn": 0,
          "items": [
            {
              "signingPointId": signingPointId,
              "contactId": contactId,
              "checkInType": "搜索",
              "appId": "1",
              "checkInTime": "2016-02-04T11:32:11",
              "seminarId": seminarId,
              "userId": "1",
              "mediaType": "APP",
              "passageId": 1
            },
            {
              "signingPointId": signingPointId,
              "contactId": contactId,
              "checkInType": "二维码",
              "appId": "1",
              "checkInTime": "2016-02-04T11:23:11",
              "seminarId": seminarId,
              "userId": "1",
              "mediaType": "H5",
              "passageId": 1
            }
          ],
          "sess": bakSess
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "b293c174-8443-add9-13ca-dff6b4aa0718"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#app_seminar_signingPoint_checkIn_getList/该接口为APP专用接口，项目不要使用，获取签到历史记录
def get_app_seminar_signingPoint_checkIn_getList(type, domain,seminarId_instanceId,bakSess):
    path="/app/seminar/signingPoint/checkIn/getList"
    print "domain:", domain + path
    payload={
        "seminarId": seminarId_instanceId,
        "lastModify": "2015-10-22T12:00:00",
        "start": 0,
        "num": 100,
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "17dd9634-c2cd-4fd4-bd8e-c1c5c038bf7f"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#app_seminar_signingPoint_checkIn_getListCompressed/获取签到历史记录,压缩版
def get_app_seminar_signingPoint_checkIn_getListCompressed(type, domain,seminarId_instanceId,bakSess):
    path="/app/seminar/signingPoint/checkIn/getListCompressed"
    print "domain:", domain + path
    payload={
        "seminarId": seminarId_instanceId,
        "lastModify": "2015-10-22T12:00:00",
        "start": 0,
        "num": 100,
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "d355763b-8799-4f60-8106-d3c6fc795029"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful_status("POST", domain + path, payload, headers, type, type)
#app_seminar_signingPoint_contact_getList/该接口为APP专用接口，项目不要使用，获取签到点通道下人员
def get_app_seminar_signingPoint_contact_getList(type, domain,seminarId_instanceId,signingPointId,passageId,bakSess):
    path="/app/seminar/signingPoint/contact/getList"
    print "domain:", domain + path
    payload={
        "seminarId": seminarId_instanceId,
        "signingPointId": signingPointId,
        "passageId": passageId,
        "key": "13393213135",
        "start": 0,
        "num": 20,
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "0b346a83-1833-4312-acfc-a5c11436002a"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#account_channel_get/获取实例详情信息
def get_account_channel_get(type, domain,seminarId_instanceId):
    path="/account/channel/get"
    print "domain:", domain + path
    payload={"id": seminarId_instanceId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "15428706-86cc-4f26-9bc6-4fa35fa8ce51"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#account_getAuth/获取验证信息
def get_account_getAuth(type, domain,nodeId,bakSess,seminarId_instanceId):
    path="/account/getAuth"
    print "domain:", domain + path
    payload={  "nodeId": nodeId,"sess": bakSess,"instanceId": seminarId_instanceId}
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "c37a4ee0-9d4b-44ab-b18d-be44934f0856"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#account_getAuthByInstance/该接口为后台接口，后期即将移除，请不要继续使用，通过实例获取验证信息
def get_account_getAuthByInstance(type, domain,seminarId_instanceId,bakSess):
    path="/account/getAuthByInstance"
    print "domain:", domain + path
    payload={"instanceId": seminarId_instanceId,"sess": bakSess}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "23a5ee40-d975-4c23-9079-93c2a50a4261"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#admin_member_identification_query/客户管理-注册用户-根据自定义列表字段查询注册用户列表
def get_admin_member_identification_query(type, domain,tenantId,bakSess):
    path="/admin/member/identification/query"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "keyword": "",
        "formId": "-1",
        "updateTime": "",
        "listConditions": [
            {
                "fieldName": "industry",
                "value": [
                    "zhizaoye",
                    "dianziye"
                ]
            }

        ],
        "start": "1",
        "num": "10",
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=",
        'cache-control': "no-cache",
        'Postman-Token': "3d9aab0c-b00a-4823-a778-4977dcca9a35"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#anonymous_getId/获取一个全局用户Id（cookieId）
def get_anonymous_getId(type, domain):
    path="/anonymous/getId"
    print "domain:", domain + path
    payload={
        "clientType": "iOS",
        "clientBrand": "Mobile Safari",
        "clientVersion": "5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
        "clientIP": "192.168.0.1"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "b28cfbe5-0fa9-481e-a0f0-a5ebe7b3930b"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#anonymous_setInfo/设置匿名用户信息
def get_anonymous_setInfo(type, domain):
    path="/anonymous/setInfo"
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    print "domain:", domain + path
    payload={
        "cookieId": createTime,
        "name": "",
        "mobile": "",
        "addr": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "de7b1c4a-8422-4b80-b9a5-753844bb0c2a"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#tag_application_GetListByType/查询租户下某种对象类型的应用的标签列表
def get_tag_application_GetListByType(type, domain,tenantId,seminarId_instanceId):
    path="/tag/application/GetListByType"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "moduleId": "2",
        "instanceId": seminarId_instanceId,
        "objectType": "questionnaire"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "fdfab733-39a8-48c3-b928-92a6721c1e37"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#tag_field_GetList/？？？？？？
def get_tag_field_GetList(type, domain,tenantId,bakSess):
    path="/tag/field/GetList"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "isEnable": -1,
        "isShowTag": 1,
        "type": "all",
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "86150d02-5c43-4cc0-b8e4-3fec85dec96e"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_article_category_interaction_browse/记录栏目浏览互动行为
def get_api_article_category_interaction_browse(type, domain,tenantId,categoryId,wechatId):
    path="/api/article/category/interaction/browse"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
        "tenantId":tenantId,
        "articleCategoryId":categoryId,
        "source": "source",
        "globalUserId": createTime,
        "sess": "",
        "openId": "",
        "currentUrl": "url",
        "weChatId": wechatId,
        "browseInfo": {
            "userAgent": "Browser Information",
            "browser": "Browser Name",
            "version": "Browser Edition",
            "os": " User operating system name",
            "equipment": "Equipment type",
            "resolution": "Screen resolution (1920 1080 format)",
            "referenceUrl": "referenceUrl",
            "referenceTitle": "referenceTitle",
            "sessionId": "Request Unique Identification"
        }
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "df07fbe9-65d8-44e5-ae7b-26e71abf4030"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_article_category_interaction_share/记录栏目分享互动行为
def get_api_article_category_interaction_share(type, domain,tenantId,categoryId,wechatId):
    path="/api/article/category/interaction/share"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
        "tenantId":tenantId,
        "articleCategoryId":categoryId,
        "source": "source",
        "globalUserId": createTime,
        "sess": "",
        "openId": "",
        "currentUrl": "url",
        "weChatId": wechatId,
        "browseInfo": {
            "userAgent": "Browser Information",
            "browser": "Browser Name",
            "version": "Browser Edition",
            "os": " User operating system name",
            "equipment": "Equipment type",
            "resolution": "Screen resolution (1920 1080 format)",
            "referenceUrl": "referenceUrl",
            "referenceTitle": "referenceTitle",
            "sessionId": "Request Unique Identification"
        }
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "df07fbe9-65d8-44e5-ae7b-26e71abf4030"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#tag_use_getListByType/获取租户可用的标签列表
def get_tag_use_getListByType(type, domain,tenantId,nodeId,seminarId_instanceId):
    path="/tag/use/getListByType"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "nodeId": nodeId,
        "moduleId": "3",
        "instanceId": seminarId_instanceId,
        "type": "questionnaire"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "99726ef4-9e9d-4bf2-9c73-d99cf13184d7"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_article_category_query/项目使用，获取栏目列表/栏目id为空
def get_api_article_category_query(type, domain,tenantId):
    path="/api/article/category/query"
    print "domain:", domain + path
    payload={
        "tenantId":tenantId,
        "articleCategoryId": "",
        "instanceId": "",
        "isEnabled": "0",
        "start": 0,
        "num": 20
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "a5b5d167-16ca-47fe-8f58-1fd63c605438"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_article_get/获取文章详情
def get_api_article_get(type, domain,tenantId,articleId):
    path="/api/article/get"
    print "domain:", domain + path
    payload={
        "tenantId":tenantId,
        "articleId": articleId,
        "globalUserId": "4e2d551d7887de4be21a35717c4e1cb5",
        "sess": "",
        "openId": "",
        "isWithStat":1,
        "isScroll":1,
         "isWithTag":0
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "4ee0b31d-04f8-4752-9752-3416a4d74011"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#template_template_getConfig/获取模板配置
def get_template_template_getConfig(type, domain):
    path="/template/template/getConfig"
    print "domain:", domain + path
    payload={"configId": 48617}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "8bec4f64-4818-467c-a46a-efa8e3ddb3ff"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_article_interaction_create/记录文章的互动记录，包含浏览和分享
def get_api_article_interaction_create(type, domain,tenantId,articleId):
    path="/api/article/interaction/create"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
        "tenantId": str(tenantId),
        "articleId": articleId,
        "source": "source",
        "interactionType": "1",
        "globalUserId": createTime,
        "sess": "",
        "openId": "",
        "mediaId": "",
        "tick": "",
        "currentUrl": "",
        "weChatId": "",
        "browseInfo": {
            "userAgent": "Browser Information",
            "browser": "Browser Name",
            "version": "Browser Edition",
            "os": " User operating system name",
            "equipment": "Equipment type",
            "resolution": "Screen resolution (1920 1080 format)",
            "referenceUrl": "referenceUrl",
            "referenceTitle": "referenceTitle",
            "sessionId": "Request Unique Identification"
        }
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "9d9acd2a-2317-4715-94fa-1cf6793cd7fd"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#templateMessage_batchSend/发送模板消息，微信模板,templateId-为开启的模板id
def get_templateMessage_batchSend(type, domain,wechatId,bakSess):
    path="/templateMessage/batchSend"
    print "domain:", domain + path
    payload={
        "weChatId": wechatId,
        "templateId": "264",
        "targetName": "",
        "messages": [
            {
                "openId": "{{openId}}",
                "data": {
                    "first": {
                        "value": "gongxi!",
                        "color": "#173100"
                    },
                    "keyword1": {
                        "value": "one",
                        "color": "#173100"
                    }
                },
                "url": "http://www.bing.com"
            }
        ],
        "callbackUrl": "http://devswcb.wechat.smarket.net.cn/index.php",
        "callbackCmd": "templateMessage.callBackFunction",
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "bdff7cc1-0219-4c1e-a261-b9cc8ae3aaf6"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#templateMessage_batchSend/发送模板消息，微信模板,templateId-为开启的模板id
def get_HW_UAT_templateMessage_batchSend(type, domain,wechatId,bakSess):
    path="/templateMessage/batchSend"
    print "domain:", domain + path
    payload={
        "weChatId": 9944,
        "templateId": "285",
        "targetName": "",
        "messages": [
            {
                "openId": "{{openId}}",
                "data": {
                    "first": {
                        "value": "gongxi!",
                        "color": "#173100"
                    },
                    "keyword1": {
                        "value": "one",
                        "color": "#173100"
                    }
                },
                "url": "http://www.bing.com"
            }
        ],
        "callbackUrl": "http://devswcb.wechat.smarket.net.cn/index.php",
        "callbackCmd": "templateMessage.callBackFunction",
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "bdff7cc1-0219-4c1e-a261-b9cc8ae3aaf6"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_article_like_check/检查当前用户是否可以对文章点赞
def get_api_article_like_check(type, domain,tenantId,articleId):
    path="/api/article/like/check"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
        "tenantId": tenantId,
        "articleId": articleId,
        "globalUserId": createTime,
        "openId": "",
        "sess": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "bdff7cc1-0219-4c1e-a261-b9cc8ae3aaf6"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# templateMessage_getContactList/获取粉丝列表，发送模板消息用
def get_most_templateMessage_getContactList(type, domain,wechatId):
    path="/templateMessage/getContactList"
    print "domain:", domain + path
    payload={
          "weChatId": wechatId,
          "sex": "",
          "country": "",
          "group": [

          ],
          "start": 0,
          "num": 20
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "24bbb5cb-3bf6-9ecb-6c4e-9530fc9be39e"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_article_query/获取文章列表
def get_most_api_article_query(type, domain, tenantId):
    path="/api/article/query"
    print "domain:", domain + path
    payload={
        "tenantId":tenantId,"instanceId": "","articleIds":"","typeIds": "","articleCategoryId": "","title": "","summary": "",
        "isRecommend": "","hasChildrenCategory": "","isTop": "","isWithStat": "","sort": [1],"tags": "","start": 0, "num": 50
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "39493554-086b-08ad-6306-ce4de66deaf5"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# topic_post_getAllList/获取留言列表根据指定条件
def get_most_topic_post_getAllList(type, domain, seminarId_instanceId,tenantId,bakSess):
    path="/topic/post/getAllList"
    print "domain:", domain + path
    payload={
          "instanceIds": seminarId_instanceId,
          "memberIds": [1119897],
          "start": 0,"num": 10,
          "tenantId": tenantId,
          "status": 0,
          "isPreview": "0",
          "sess":bakSess
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "fdc89464-5a25-d7e3-2908-9d387c54be92"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# topic_stat_homePage/获取讨论版的列表
def get_most_topic_stat_homePage(type, domain, tenantId,seminarId_instanceId,bakSess):
    path="/topic/stat/homePage"
    print "domain:", domain + path
    payload={
          "type": 1,
          "tenantId": tenantId,
          "moduleId": 3,
          "instanceId":seminarId_instanceId,
          "start": 0,
          "num": 10,
          "isHide": 1,
          "sess": bakSess
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "6d50a604-86e9-974b-b8c8-9a649cc6b9d5"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_member_contacts_get/获取注册用户信息
def get_most_api_member_contacts_get(type, domain, tenantId,loginSess2):
    path="/api/member/contacts/get"
    print "domain:", domain + path
    payload={
          "tenantId": int(tenantId),
          "sess": str(loginSess2)
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "baa26301-cc69-5e7b-3e65-b91bf2c6cec5"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# member_register/注册
def get_most_member_register(type, domain, tenantId,schemaId,memberFormId):
    path="/member/register"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={}
    payload["tenantId"]=str(tenantId)
    payload["schemaId"] = str(schemaId)
    payload["memberFormId"] = str(memberFormId)
    payload["url"] = "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/signup.html?memberFormId=6388&configId=254305&memberSchemaId=2808&backUrl="
    payload["referenceUrl"] = "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305"
    payload["token"] = ""
    payload["verify"] = ""
    payload["formData"] = {"fieldName":"name","value":"xingyingli"},{"fieldName":"username","value":"e"+createTime+""},{"fieldName":"password","value":"4297F44B13955235245B2497399D7A93"}
    payload["browseInfo"] = {"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","browser":"Chrome","version":"66.0.3359.181","os":"Windows","equipment":"pc","resolution":"1366X768","referenceUrl":"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305","referenceTitle":"","sessionId":"ec69f3edd1c9908cb8cfeb1e4528488e"}
    payload["globalUserId"] = createTime
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "b16209d3-964d-8e46-7b3b-7acf1b63f631"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful_getvalue_02("POST", domain + path, payload, headers, type, type,"loginId")
# article_shareRecord/分享记录，globalUserId、openId和sess至少填一个
def get_most_article_shareRecord(type, domain,articleId,loginSess3):
    path="/article/shareRecord"
    print "domain:", domain + path
    payload={
          "articleId": int(articleId),
          "tick": "",
          "mediaId": 12044,
          "referenceUrl": "a",
          "url": "",
          "openId": "",
          "globalUserId": "39e5bd2a4a1c363d09b9fdd09323b3d8",
          "sess": str(loginSess3),
          "weChatId": "",
          "resolution": ""
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "63d32aca-3b56-1802-9f94-266e255eb7e0"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# account_changePassword/该接口为后台接口，后期即将移除，请不要继续使用，修改密码
def get_most_account_changePassword(type, domain,bakSess,member_password):
    path="/admin/account/changePassword"
    print "domain:", domain + path
    payload={
        "oldPwd": member_password,
        "newPwd":member_password,
        "sess": bakSess
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "19ec50ba-5897-f63a-c93b-a64339995123"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_member_contacts_password_update/当前注册用户登录后修改密码
def get_most_api_member_contacts_password_update(type, domain,tenantId,member_password,loginSess3):
    path="/api/member/contacts/password/update"
    print "domain:", domain + path
    payload={
          "tenantId": int(tenantId),
          "oldPwd": str(member_password),
          "newPwd": str(member_password),
          "sess":str(loginSess3)
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "e764de25-c78e-9755-0800-fc9558dc22a9"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# admin_member_identification_updatelog_query/客户管理-注册用户-查询注册用户变更记录日志列表
def get_most_admin_member_identification_updatelog_query(type, domain, tenantId,loginId,bakSess):
    path="/admin/member/identification/updatelog/query"
    print "domain:", domain + path
    payload={
          "tenantId":int(tenantId),
          "loginId": int(loginId),
          "start": "1",
          "num": "10",
          "sess":str(bakSess)
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "5dd3d6b5-0f78-f177-7506-fc3a96f2c5d9"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_member_contacts_update/当前注册用户更新自己的信息
def get_most_api_member_contacts_update(type, domain, tenantId,loginSess3):
    path="/api/member/contacts/update"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
          "tenantId": tenantId,
          "formData": [
             {"fieldName": "name","value": createTime},
            {"fieldName": "email","value": ""+createTime+"@qq.com"},
            {"fieldName": "password","value": "4297F44B13955235245B2497399D7A93"}],
          "globalUserId": "",
          "sess":loginSess3
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "fda7a810-6613-07fd-701f-3d0f44bb1da4"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# anonymous_checkSess/验证前台sess
def get_most_anonymous_checkSess(type, domain,loginSess3):
    path="/anonymous/checkSess"
    print "domain:", domain + path
    payload={
            "sess": loginSess3
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "fb65be25-97aa-4284-36a4-b4a313a334b7"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_questionnaire_share/分享问卷行为
def get_most_api_questionnaire_share(type, domain,questionid_sj,tenantId):
    path="/api/questionnaire/share"
    print "domain:", domain + path
    payload={
        "questionnaireId": questionid_sj,
        "tenantId": tenantId,
        "sess": "",
        "globalUserId": "aeb77fdace2cca2d90caef190782555c",
        "openId": "",
        "browseInfo":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36","browser":"Chrome","version":"67.0.3396.99","os":"Windows","equipment":"电脑端","resolution":"1920X1080","referenceUrl":"https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6329&memberSchemaId=2808&backUrl=https%3A%2F%2Ff.smarket.net.cn%2Fs%2Ftemplate%2Fe2ba9d7e12c7e74fa9ccb58318acc60d%2Fview%2FPcQuestionnaire.html%3FquestionaryId%3D7967%26configId%3D302340&configId=246874","referenceTitle":"","sessionId":"c72d4a05eadf94761e782bf8033a4032"}
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "aee43091-652a-673e-8660-13f4c52f9476"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_file_interaction_share/记录文件分享互动行为
def get_most_api_file_interaction_share(type, domain,tenantId,fileIds):
    path="/api/file/interaction/share"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
         "tenantId":tenantId,
        "fileId": fileIds,
        "source": "来源",
        "globalUserId":createTime,
        "sess": "",
        "openId": "",
        "currentUrl": "当前页面的url地址",
        "weChatId": "",
        "browseInfo": {
            "userAgent": "用户浏览器信息",
            "browser": "用户浏览器名称",
            "version": "用户浏览器版本",
            "os": "用户操作系统名称",
            "equipment": "设备类型",
            "resolution": "屏幕分辨率(格式为1920 1080)",
            "referenceUrl": "来源页面url地址(如果当前页面没有来源，此地址为空)",
            "referenceTitle": "来源页面标题(如果当前页面没有来源，此标题为空)",
            "sessionId": "请求唯一标识"
        }
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=",
        'cache-control': "no-cache",
        'postman-token': "058feddc-6a7d-049d-152b-812e4ec17349"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_file_query/查询文件列表（带分页）
def get_most_api_file_query(type, domain, tenantId,fileId,fileIds):
    path="/api/file/query"
    print "domain:", domain + path
    payload={
        "tenantId":tenantId,
        "folderId": fileId,
        "instanceId": "",
        "keyword": "Email",
        "fileIds": fileIds,
        "fileType": ["xls/xlsx"],
        "isFolder": "",
        "sort": [1],
        "start": "0",
        "num": "10"

    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "7e540fba-9550-b360-32f5-89e947dd063a"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_luckydraw_browse/浏览抽奖
def get_most_api_luckydraw_browse(type, domain,luckyDrawId,tenantId,loginSess3):
    path="/api/luckydraw/browse"
    print "domain:", domain + path
    payload={
            "luckyDrawId":luckyDrawId,
            "tenantId": tenantId,
            "sess": loginSess3,
            "globalUserId": "",
            "openId": "",
            "browseInfo": {
              "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
              "browser": "Chrome",
              "version": "69.0.3497.100",
              "os": "Windows",
              "equipment": "电脑端",
              "resolution": "1920X1080",
              "referenceUrl": "http://test-webinar.smarket.net.cn/webcast.html",
              "referenceTitle": "",
              "sessionId": loginSess3
            }
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "45d15842-cc47-e7ac-75e5-738a0a2dc253"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_luckydraw_fieldinfo_query/获取前台显示中奖字段
def get_most_api_luckydraw_fieldinfo_query(type, domain,luckyDrawId,createCheckIn,tenantId):
    path="/api/luckydraw/fieldinfo/query"
    print "domain:", domain + path
    payload= {
         "luckyDrawId": luckyDrawId,
         "bigScreenId": createCheckIn,
         "luckyDrawType": "5",
         "staffWay": "2",
         "identify": "1",
         "memberFormId": "0",
         "meetInstanceId": "0",
         "interactive": "2",
         "instanceId": "38510",
         "toolType": "0",
         "toolId": "-1",
         "toolIdentity": "0",
         "tenantId": tenantId
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "5b10c513-261a-f1fb-157f-84a98b1c9faa"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_luckydraw_fieldinfo_update-设置前台显示中奖字段
def get_most_api_luckydraw_fieldinfo_update(type, domain, luckyDrawId, createCheckIn,tenantId):
    path="/api/luckydraw/fieldinfo/update"
    print "domain:", domain + path
    payload={
            "luckyDrawId": luckyDrawId,
            "showFieldInfo": "mixed",
            "bigScreenId": createCheckIn,
            "tenantId": tenantId
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "6627de41-e7a0-3887-c4fd-fe5d4608477b"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_luckydraw_get/获取抽奖详情
def get_most_api_luckydraw_get(type, domain,tenantId, luckyDrawId):
    path="/api/luckydraw/get"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "luckyDrawId": luckyDrawId
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "db10d2bf-4c5a-e24d-2505-72207dc231c1"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_luckydraw_share/转发(分享)抽奖
def get_most_api_luckydraw_share(type, domain,luckyDrawId,tenantId,loginSess3):
    path="/api/luckydraw/share"
    print "domain:", domain + path
    payload={
            "luckyDrawId":luckyDrawId,
            "tenantId": tenantId,
            "sess": loginSess3,
            "globalUserId": "",
            "openId": "",
            "browseInfo": {
              "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
              "browser": "Chrome",
              "version": "69.0.3497.100",
              "os": "Windows",
              "equipment": "电脑端",
              "resolution": "1920X1080",
              "referenceUrl": "http://test-webinar.smarket.net.cn/webcast.html",
              "referenceTitle": "",
              "sessionId": loginSess3
            }
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "fe9e05b5-20f9-eb00-5035-acbcd52fce1a"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_luckydraw_user_query/获取大屏抽奖用户(1-100条)
def get_api_luckydraw_user_query(type, domain,luckyDrawId,createCheckIn):
    path="/api/luckydraw/user/query"
    print "domain:", domain + path
    payload={
        "staffWay": "4",
        "luckyDrawId": luckyDrawId,
        "staffId": "1",
        "bigScreenId": createCheckIn
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "ecfe9d97-f71d-48c5-a58e-3df9dc4a481e"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_member_contacts_check/检查唯一字段值是不是可用
def get_api_member_contacts_check(type, domain,tenantId,schemaId):
    path="/api/member/contacts/check"
    print "domain:", domain + path
    payload={
        "tenantId": int(tenantId),
        "schemaId": schemaId,
        "fieldName": "email",
        "fieldValue": "123@qq.com"
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=",
        'cache-control': "no-cache",
        'Postman-Token': "81483bd3-f9a1-44ca-bc33-3d8683e50b07"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_member_image_code_get/获取图片验证码
def get_api_member_image_code_get(type, domain,tenantId):
    path="/api/member/image/code/get"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "globalUserId": "204c52fb08ec1ab57e6223a4cc1b1ae3",
        "len": "5",
        "width": "100",
        "height": "50"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "c317e90c-acb1-4763-b3f7-d650300c5f67"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful_code("POST", domain + path, payload, headers, type, type)
#api_product_query/获取产品线下产品列表
def get_api_product_query(type, domain,tenantId,productLineId):
    path="/api/product/query"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "productIds": [
            907,
            867
        ],
        "productLineId": productLineId,
        "keyword": "",
        "isNew": 0,
        "categoryId": "",
        "withSoldOut": 1,
        "conditions": "",
        "isTop": 0,
        "start": 0,
        "num": 10
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "d2fc59ac-973b-4aab-8e07-bc603eff5ae7"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_seminar_app_checkinpoint_userpermit_query/app专用，获取用户签到点权限列表
def get_api_seminar_app_checkinpoint_userpermit_query(type, domain,seminarId,loginSess1,tenantId):
    path="/api/seminar/app/checkinpoint/userpermit/query"
    print "domain:", domain + path
    payload={
        "seminarId": seminarId,
        "sess": loginSess1,
        "tenantId": tenantId
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "0a256943-d452-45f0-b36c-18494f78c0f9"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_seminar_bigscreen_information_push/向NODE服务推送消息
def get_api_seminar_bigscreen_information_push(type, domain,createCheckIn,tenantId):
    path="/api/seminar/bigscreen/information/push"
    print "domain:", domain + path
    payload={
        "roomId": "string",
        "type": "string",
        "bigScreenId": createCheckIn,
        "tenantId": tenantId,
        "content": "mixed"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "379d539d-78fc-449b-a260-bce114221428"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#article_like/点赞，globalUserId、openId和sess至少填一个
def get_article_like(type, domain,articleId,loginSess1):
    path="/article/like"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
        "articleId": articleId,
        "globalUserId": createTime,
        "openId": "",
        "url": "",
        "referenceUrl": "",
        "sess": loginSess1,
        "weChatId": "",
        "resolution": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=",
        'cache-control': "no-cache",
        'Postman-Token': "bc0da218-09d8-4637-9083-596fc23bd7fa"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#seminar_getList/获取会议列表，该接口为APP专用接口，项目不要使用
def get_seminar_getList(type, domain,tenantId):
    path="/app/seminar/getList"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "key": "",
        "sceneName": "",
        "status": "",
        "sortName": "createTime",
        "conditions": [],
        "start": 0,
        "num": 10
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "f3381128-5b13-49f3-ae4e-4dde6d06c316"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#articleCategory_get/获取单个栏目
def get_articleCategory_get_one(type, domain,tenantId,categoryId):
    path="/articleCategory/get"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "id": categoryId,
        "withTemplate": 0
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "074df36a-2879-416c-9066-d03de624ccae"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#interaction_record/记录一个互动
def get_interaction_record(type, domain,tenantId):
    path="/interaction/record"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "moduleId": 0,
        "instanceId": 0,
        "contactId": 0,
        "cookieId": "817c4822639dfe314fada85204644011",
        "openId": "",
        "actionKey": "form_browse",
        "objId": 11880,
        "obj": "",
        "result": "成功",
        "source": "优奥创思",
        "detail": "详情",
        "objResultId": "",
        "url": "",
        "referenceUrl": "",
        "_cache_with_cached": "1",
        "_cache_refresh": "1",
        "_cache_timeout": "60"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "d37d6d6a-2f2d-4b51-93f7-8f18bcef20ec"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#product_crossLine_getListByIdList/根据产品id数组获取产品列表
def get_product_crossLine_getListByIdList(type, domain,productLine):
    path="/product/crossLine/getListByIdList"
    print "domain:", domain + path
    payload={"productIdList": [productLine]}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "04b15785-bb2f-495b-a38b-00cb93b818e7"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_seminar_contacts_Query/根据session获取此用户在某租户下参与过的所有会议
def get_api_seminar_contacts_Query(type, domain,tenantId,bakSess):
    path="/api/seminar/contacts/query"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "sess": bakSess,
        "withTag": "1",
        "needTopic": "0",
        "sortName": "createTime",
        "sortOrder": "asc",
        "start": "1",
        "num": "20"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "64f3fc10-0828-4956-afe6-e96854ce5eda"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#project_getInfoByLang/通过openId获取联系人信息,可返回不同地区语言
def get_project_getInfoByLang(type, domain,wechatId):
    path="/project/getInfoByLang"
    print "domain:", domain + path
    payload={
        "weChatId": wechatId,
        "openId": "oG80v1fgaHwbGrBPBE1b2lLLTPjk",
        "lang": "zh_CN"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "097d5b3f-071c-4e4d-8b04-8d9b8032de03"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#article_getListByTags/获取租户下文章列表，可通过标签筛选
def get_article_getListByTags(type, domain,tenantId):
    path="/article/getListByTags"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "tags": [{"bq": ["1"]}],
        "start": "0",
        "num": "10"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "c16957c3-97e7-4a12-8451-d24a73a1393b"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_shorturl_generate/生成短地址,但是url按现在的url设置，因为路径变更了
def get_api_shorturl_generate(type, domain):
    path="/api/common/shorturl/create"
    print "domain:", domain + path
    payload={
        "url": "https://s2-sde.smarket.net.cn/seminar.html?seminarId=5968&instanceId=46904#/Seminar/Home/Home",
        "keyword": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "e8eca3cc-ae7f-498f-8092-3ce5ab307f0d"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_seminar_app_signingpoint_group_Query/获取会议下的所有签到点信息
def get_api_seminar_app_signingpoint_group_Query(type, domain,seminarId_instanceId):
    path="/api/seminar/app/signingpoint/group/query"
    print "domain:", domain + path
    payload={"seminarId": seminarId_instanceId}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "5ae271a2-7870-4299-8869-f7fde6aee278"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#file_folder_getReleaseFileList/文件夹列表
def get_file_folder_getReleaseFileList(type, domain,FolderId,accKey):
    path="/file/folder/getReleaseFileList"
    print "domain:", domain + path
    payload={
        "folderId": FolderId,
        "start": 0,
        "num": 8,
        "accKey": accKey
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "675e6995-3a4a-4632-804b-5c81a26b085f"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#member_identification_information_GetByOpenId/有问题，通过openId获取注册信息
def get_member_identification_information_GetByOpenId(type, domain,tenantId,openId,unionId):
    path="/member/identification/information/GetByOpenId"
    print "domain:", domain + path
    payload={
        "openId": openId,
        "tenantId": tenantId,
        "unionId": unionId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "581b1a30-f626-401c-8957-6aa90b7bbea9"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#app_seminar_contact_getListCompressed/该接口为APP专用接口，项目不要使用，获取压缩过的会议联系人
def get_app_seminar_contact_getListCompressed(type, domain,seminarId_instanceId,bakSess):
    path="/app/seminar/contact/getListCompressed"
    print "domain:", domain + path
    payload={
        "seminarId": seminarId_instanceId,
        "lastModify": "2015-10-22T12:00:00",
        "start": 0,
        "num": 10,
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "1fa23a27-7bf1-4d05-8672-70771f82dd93"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful_code("POST", domain + path, payload, headers, type, type)
# app_seminar_signingPoint_getGroupList/该接口为APP专用接口，项目不要使用，获取会议下的所有签到点信息
def get_most_app_seminar_signingPoint_getGroupList(type, domain,seminarId_instanceId):
    path="/app/seminar/signingPoint/getGroupList"
    print "domain:", domain + path
    payload= {
            "seminarId": seminarId_instanceId
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "ddb3e2f2-124c-5530-4016-02b3b53d97e9"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# comment_getList/获取评论列表
def get_most_comment_getList(type, domain,tenantId,topicId,bakSess):
    path="/comment/getList"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "subVersionId": "102161",
        "commentId": "0",
        "start": "0",
        "num": "10",
        "topicId": topicId,
        "sess": bakSess
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "3b615a85-1e28-ab9e-7697-e3c8373cdd98"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# app_seminar_contact_field_getCustomFields/该接口为APP专用接口，项目不要使用，获取联系人字段
def get_most_app_seminar_contact_field_getCustomFields(type, domain,seminarId_instanceId):
    path="/app/seminar/contact/field/getCustomFields"
    print "domain:", domain + path
    payload= {
        "seminarId": seminarId_instanceId
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "1430b9a4-1086-15dd-a60f-26b332f04285"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_open_newRegistration/注册用户接口
def get_most_webinar_open_newRegistration(type, domain,tenantId,schemaId,webinarId_instanceId,memberFormId,loginSess):
    path="/webinar/open/newRegistration"
    print "domain:", domain + path
    payload={
          "tenantId": tenantId,
          "schemaId": schemaId,
          "instanceId": webinarId_instanceId,
          "memberFormId":memberFormId,
          "url": "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/signup.html?memberFormId=6329&configId=246874&memberSchemaId=2808&backUrl=https://f.smarket.net.cn/s/template/39dc846dd6e88089d3990c165e4fad03/view/customForm.html?instanceId=38369&webinarId=6132&customFormId=13283&trackId=2:74&linkId=26812&configId=246966&returnUrl=http%3A%2F%2Ff.smarket.net.cn%2Fs%2Ftemplate%2Fddaae85fe48ff1372217f0db2def1676%2Fhtml%2Fmeeting.html%3FinstanceId%3D38369%26webinarId%3D6132%26customFormId%3D13283%26trackId%3D2%3A74%26linkId%3D26812%26signUpNotify%3Dtrue",
          "referenceUrl": "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberId=6329&memberFormId=6329&trackId=0&memberSchemaId=2808&configId=246874&backUrl=https://f.smarket.net.cn/s/template/39dc846dd6e88089d3990c165e4fad03/view/customForm.html?instanceId=38369&webinarId=6132&customFormId=13283&trackId=2:74&linkId=26812&configId=246966&returnUrl=http%3A%2F%2Ff.smarket.net.cn%2Fs%2Ftemplate%2Fddaae85fe48ff1372217f0db2def1676%2Fhtml%2Fmeeting.html%3FinstanceId%3D38369%26webinarId%3D6132%26customFormId%3D13283%26trackId%3D2%3A74%26linkId%3D26812%26signUpNotify%3Dtrue",
          "token": "",
          "verify": "",
          "formData": [{"fieldName": "name","value": "名"},
                       {"fieldName": "mobile","value": "13393213133"},
                       {"fieldName": "email","value": "22{{timestamp}}@qq.com"},
                       {"fieldName": "identityNum","value": ""},
                       {"fieldName": "username","value": ""},
                       { "fieldName": "avatar","value": {"fileName": "","mapId": ""}},
                       {"fieldName": "province","value": [],"otherValue": ""},
                       {"fieldName": "password","value": "EFE6398127928F1B2E9EF3207FB82663"},
                       {"fieldName": "jobNumber","value": ""},
                       {"fieldName": "enterprise","value": ""},
                       {"fieldName": "department","value": [],"otherValue": ""},
                       {"fieldName": "position","value": [],"otherValue": ""},
                       {"fieldName": "gender","value": [],"otherValue": ""},
                       {"fieldName": "industry", "value": [],"otherValue": ""}],
          "browseInfo": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            "browser": "Chrome",
            "version": "66.0.3359.139",
            "os": "Windows",
            "equipment": "电脑端",
            "resolution": "1536X864",
            "referenceUrl": "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberId=6329&memberFormId=6329&trackId=0&memberSchemaId=2808&configId=246874&backUrl=https://f.smarket.net.cn/s/template/39dc846dd6e88089d3990c165e4fad03/view/customForm.html?instanceId=38369&webinarId=6132&customFormId=13283&trackId=2:74&linkId=26812&configId=246966&returnUrl=http%3A%2F%2Ff.smarket.net.cn%2Fs%2Ftemplate%2Fddaae85fe48ff1372217f0db2def1676%2Fhtml%2Fmeeting.html%3FinstanceId%3D38369%26webinarId%3D6132%26customFormId%3D13283%26trackId%3D2%3A74%26linkId%3D26812%26signUpNotify%3Dtrue",
            "referenceTitle": "",
            "sess": loginSess
          },
          "globalUserId": "39e5bd2a4a1c363d09b9fdd09323b3d8"
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "8a0f9158-4732-c3da-8918-4f082c9043c4"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# file_cutImage/裁剪平台图片资源内容
def get_file_cutImage(type, domain, mappingId):
    path="/file/cutImage"
    print "domain:", domain + path
    payload={
          "mapId": mappingId,
          "croods": {
            "x": "1","y": "1","x2": "5", "y2": "5"},
          "covered": "0",
          "sess": ""
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "b992608c-2d29-8717-35ed-19e866351c86"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# member_geneRegister/注册用户
def get_most_member_geneRegister(type, domain,tenantId,schemaId,memberFormId,loginSess):
    path="/member/geneRegister"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
          "tenantId": str(tenantId),
          "schemaId":str(schemaId),
          "memberFormId":str(memberFormId),
          "url": "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/signup.html?memberFormId=6388&configId=254305&memberSchemaId=2808&backUrl=",
          "referenceUrl": "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305",
          "token": "","verify": "",
          "formData": [{"fieldName": "name","value": "13393213121"},
                       {"fieldName": "username", "value": "a"+createTime+"" },
                       {"fieldName": "password","value": "4297F44B13955235245B2497399D7A93"}],
          "browseInfo": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            "browser": "Chrome",
            "version": "66.0.3359.139",
            "os": "Windows",
            "equipment": "电脑端",
            "resolution": "1536X864",
            "referenceUrl": "https://f.smarket.net.cn/s/template/078f097e0e29d7e56d5ad4a84a085df4/view/login.html?memberFormId=6388&memberSchemaId=2808&configId=254305",
            "referenceTitle": "",
              "sess":str(loginSess)
          },
          "globalUserId": "39e5bd2a4a1c363d09b9fdd09323b3d8"
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "bc98cc62-457e-f188-bb2e-90ad3c4b0917"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful_getvalue_02("POST", domain + path, payload, headers, type, type,"memberId")
# app_seminar_contact_getList/该接口为APP专用接口，项目不要使用，获取会议联系人
def get_most_app_seminar_contact_getList(type, domain,webinarId_instanceId,bakSess):
    path="/app/seminar/contact/getList"
    print "domain:", domain + path
    payload={
            "seminarId": webinarId_instanceId,
            "lastModify": "2015-10-22T12:00:00",
            "start": 0,
            "num": 100,
            "sess": bakSess
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "d64d3b20-3353-908f-1cab-ca8e493c4aaf"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# member_getById/获取某个会员信息
def get_most_member_getById(type, domain,tenantId,memberId,bakSess):
    path="/member/getById"
    print "domain:", domain + path
    payload={
          "tenantId": tenantId,
          "memberId": memberId,
          "sess": bakSess
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=",
        'cache-control': "no-cache",
        'postman-token': "f9819d4a-3e8e-4ac6-a865-0733602634ce"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# article_getListByTags
def get_most_article_getListByTags(type, domain, tenantId):
    path="/article/getListByTags"
    print "domain:", domain + path
    payload={
          "tenantId": tenantId,
          "tags": [
            {"bq": ["1"]}],
          "start": "0",
          "num": "10"
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "c3e1b51b-198a-f4b3-f7b0-0c93d091cd62"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# app_seminar_contact_getByUniqueField/根据参会二维码获取会议联系人
def get_most_app_seminar_contact_getByUniqueField(type, domain, seminarId,bakSess):
    path="/app/seminar/contact/getByUniqueField"
    print "domain:", domain + path
    payload={
            "seminarId":int(seminarId),
            "fieldName" : "mobile",
            "fieldValue" : "15960167982",
            "sess": str(bakSess)
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload:",payload
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "a57d6d89-96b5-6975-6fd6-ce192cf200e4"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# member_identification_getList/获取注册用列表,有问题
def get_most_member_identification_getList(type, domain,tenantId,schemaId,bakSess):
    path="/member/identification/getList"
    print "domain:", domain + path
    payload={
          "tenantId": int(tenantId),
          "schemaId": int(schemaId),
          "keyword": "",
          "start": 0,
          "num": 20,
          "formId": -1,
          "sess": str(bakSess)
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=",
        'cache-control': "no-cache",
        'postman-token': "bf18a7fa-3efd-4f2d-0aae-d0c60f6f2e2a"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)

# member_member_setEnable/启用/停用注册用户,马叔
def get_most_member_member_setEnable(type, domain,schemaId,tenantId,bakSess,memberId):
    path="/member/status/set"
    print "domain:", domain + path
    payload={
          "schemaId": schemaId,
          "tenantId": tenantId,
          "memberIds": [
              memberId
          ],
          "isEnabled": 1,
          "sess":bakSess
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "4292e814-1b50-2387-110b-d145238a15f3"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_file_interaction_preview/记录文件预览互动行为
def get_most_api_file_interaction_preview(type, domain,tenantId,fileIds):
    path="/api/file/interaction/preview"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
         "tenantId":tenantId,
        "fileId": fileIds,
        "source": "来源",
        "globalUserId": createTime,
        "sess": "",
        "openId": "",
        "currentUrl": "当前页面的url地址",
        "weChatId": "",
        "browseInfo": {
            "userAgent": "用户浏览器信息",
            "browser": "用户浏览器名称",
            "version": "用户浏览器版本",
            "os": "用户操作系统名称",
            "equipment": "设备类型",
            "resolution": "屏幕分辨率(格式为1920 1080)",
            "referenceUrl": "来源页面url地址(如果当前页面没有来源，此地址为空)",
            "referenceTitle": "来源页面标题(如果当前页面没有来源，此标题为空)",
            "sessionId": "请求唯一标识"
        }
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=",
        'cache-control': "no-cache",
        'postman-token': "407fecaf-e122-83d3-0c56-0c51b121d167"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_member_form_get/获取表单信息
def get_most_api_member_form_get(type, domain, tenantId, memberFormId):
    path="/api/member/form/get"
    print "domain:", domain + path
    payload={
          "tenantId": tenantId,
          "formId": memberFormId,
          "isObtainLink": 2
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "1fe31960-b2fb-98b2-f5e8-ed3aad80965c"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# webinar_open_interaction_fileDownLoad/下载文件互动记录,有问题
def get_most_webinar_open_interaction_fileDownLoad(type, domain,loginSess1,webinarId_instanceId,fileId):
    path="/open/interaction/fileDownLoad"
    print "domain:", domain + path
    payload={"sess":loginSess1,"instanceId":webinarId_instanceId,"fileId":fileId,"title":"戴尔平台报错.txt"}
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=",
        'cache-control': "no-cache",
        'postman-token': "572b35ad-59c7-bb58-99f2-e1a574c8fb66"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_webinar_live_sendmsg-直播发消息(提问)
def get_most_api_webinar_live_sendmsg(type, domain,loginSess3,webinarId,tenantId):
    path="/api/webinar/live/sendmsg"
    print "domain:", domain + path
    payload={
        "sess": loginSess3,
        "openId": "",
        "globalUserId": "",
        "webinarId": webinarId,
        "currentUrl": "",
        "source": "",
        "browseInfo": {
          "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
          "browser": "Chrome",
          "version": "69.0.3497.100",
          "os": "Windows",
          "equipment": "电脑端",
          "resolution": "1920X1080",
          "referenceUrl": "http://test-webinar.smarket.net.cn/webcast.html",
          "referenceTitle": "",
          "sessionId": loginSess3
        },
        "tenantId":tenantId
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "6c30488c-915b-2410-d52f-7a50bd85be09"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# api_webinar_live_site_browse/访问直播会议专题页
def get_most_api_webinar_live_site_browse(type, domain, loginSess3, webinarId, tenantId):
    path="/api/webinar/live/site/browse"
    print "domain:", domain + path
    payload={
        "sess": loginSess3,
        "openId": "",
        "globalUserId": "",
        "webinarId": webinarId,
        "currentUrl": "",
        "source": "",
        "browseInfo": {
          "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
          "browser": "Chrome",
          "version": "69.0.3497.100",
          "os": "Windows",
          "equipment": "电脑端",
          "resolution": "1920X1080",
          "referenceUrl": "http://test-webinar.smarket.net.cn/webcast.html",
          "referenceTitle": "",
          "sessionId": loginSess3
        },
        "tenantId":tenantId
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "1539efd8-bafe-329f-b984-ca8605db5e19"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# member_form_getList/该接口为后台接口，后期即将移除，请不要继续使用，获取体系下的注册表单列表
def get_most_member_form_getList(type, domain,tenantId,memberSchemaId,bakSess):
    path="/member/form/getList"
    print "domain:", domain + path
    payload={
          "tenantId": tenantId,
          "memberSchemaId": memberSchemaId,
          "sess": bakSess,
          "_cache_with_cached":"1",
          "_cache_refresh":"1",
          "_cache_timeout":"60"
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "6d7c6bbf-6f65-af2c-9a2a-2fedcd420932"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# seminar_topicTemplate_seminar_get/获取会议相关信息
def get_most_seminar_topicTemplate_seminar_get(type, domain,seminarId_instanceId):
    path="/seminar/topicTemplate/seminar/get"
    print "domain:", domain + path
    payload={
       "instanceId":seminarId_instanceId
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "6bc09243-bcfa-2b92-8e0c-be118f3c595d"
    }
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_webinar_live_share/直播分享
def get_api_webinar_live_share(type, domain,loginSess3,webinarId,tenantId):
    path="/api/webinar/live/share"
    print "domain:", domain + path
    payload={
    "sess": loginSess3,
    "openId": "",
    "globalUserId": "",
    "webinarId": webinarId,
    "currentUrl": "",
    "source": "",
    "browseInfo": {
      "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
      "browser": "Chrome",
      "version": "69.0.3497.100",
      "os": "Windows",
      "equipment": "pc",
      "resolution": "1920X1080",
      "referenceUrl": "http://test-webinar.smarket.net.cn/webcast.html",
      "referenceTitle": "",
      "sessionId": loginSess3
    },
    "tenantId":tenantId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "b9198aec-d41d-4b25-9f00-80ff60e02f03"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_webinar_demand_share/分享点播
def get_api_webinar_demand_share(type, domain,loginSess3,webinarId,tenantId):
    path="/api/webinar/demand/share"
    print "domain:", domain + path
    payload={
    "sess": loginSess3,
    "openId": "",
    "globalUserId": "",
    "webinarId": webinarId,
    "currentUrl": "",
    "source": "",
    "browseInfo": {
      "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
      "browser": "Chrome",
      "version": "69.0.3497.100",
      "os": "Windows",
      "equipment": "pc",
      "resolution": "1920X1080",
      "referenceUrl": "http://test-webinar.smarket.net.cn/webcast.html",
      "referenceTitle": "",
      "sessionId": loginSess3
    },
    "tenantId":tenantId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "37e09236-1681-4c57-ae4f-16557a3c7e65"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#webinar_demand_site_browse/访问点播专题页面
def get_webinar_demand_site_browse(type, domain,loginSess3,webinarId,tenantId):
    path="/api/webinar/demand/site/browse"
    print "domain:", domain + path
    payload={
    "sess": loginSess3,
    "openId": "",
    "globalUserId": "",
    "webinarId": webinarId,
    "currentUrl": "",
    "source": "",
    "browseInfo": {
      "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
      "browser": "Chrome",
      "version": "69.0.3497.100",
      "os": "Windows",
      "equipment": "pc",
      "resolution": "1920X1080",
      "referenceUrl": "http://test-webinar.smarket.net.cn/webcast.html",
      "referenceTitle": "",
      "sessionId": loginSess3
    },
    "tenantId":tenantId
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "1f22d177-306d-4da0-a590-6c5d4e1257a5"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_webinar_demand_play/播放点播
def get_api_webinar_demand_play(type, domain,loginSess3,webinarId,tenantId):
    path="/api/webinar/demand/play"
    print "domain:", domain + path
    payload={
    "sess": loginSess3,
    "openId": "",
    "globalUserId": "",
    "webinarId": webinarId,
    "currentUrl": "",
    "source": "",
    "browseInfo": {
      "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
      "browser": "Chrome",
      "version": "69.0.3497.100",
      "os": "Windows",
      "equipment": "pc",
      "resolution": "1920X1080",
      "referenceUrl": "http://test-webinar.smarket.net.cn/webcast.html",
      "referenceTitle": "",
      "sessionId": loginSess3
    },
    "tenantId":tenantId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "4b14c116-e20b-4ad6-ba46-034b271f2640"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#member_integral_update/积分变更
def get_member_integral_update(type, domain,tenantId,loginSess1,seminarId_instanceId):
    path="/api/member/integral/update"
    print "domain:", domain + path
    payload={
    	"tenantId": tenantId,
        "sess": loginSess1,
        "moduleId": "10",
        "instanceId": seminarId_instanceId,
        "openId": "oG80v1WEYqATpSTdxH3-ZKS6Hwn4",
        "weChatId": "",
        "actionKey": "survey_submit",
        "integral": "1",
        "timeSpan": "1543489673"
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "1eff6ac3-e05f-423f-aa71-1c632a388081"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#admin_account_create/账号-用户管理添加账号
def get_admin_account_create(type, domain,tenantId,nodeId,password,bakSess):
    path="/admin/account/create"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
        "tenantId": tenantId,
        "nodeId": nodeId,
        "name": "zch",
        "supplierId": "-1",
        "mobile": createTime,
        "email": ""+createTime+"@qq.com",
        "password": password,
        "isDefault": 0,
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "4006af50-cf19-48fc-87a7-065fec0a3f85"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful_getvalue("POST", domain + path, payload, headers, type, type,"content")
#admin_account_update/编辑用户资料
def get_admin_account_update(type, domain,tenantId,nodeId,userid,bakSess):
    path="/admin/account/update"
    print "domain:", domain + path
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload={
        "tenantId": tenantId,
        "nodeId": nodeId,
        "userId": userid,
        "name": "zch",
        "supplierId": "-1",
        "mobile": createTime,
        "email": ""+createTime+"@qq.com",
        "isSendEmail": "1",
        "closeTime": "",
        "status": "0",
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "233b2427-66ce-4a6c-8fcc-42a54eca382c"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#admin_account_disableUser/禁用用户
def get_admin_account_disableUser(type, domain,tenantId,nodeId,userid,bakSess):
    path="/admin/account/disableUser"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "nodeId": nodeId,
        "userId": userid,
        "status": "1",
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "dca737ab-2923-4059-84e3-54adf492efe6"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#admin_account_delete/删除用户
def get_admin_account_delete(type, domain,tenantId,userid,bakSess):
    path="/admin/account/delete"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "userId": userid,
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "e2a36e20-dfe4-4381-92a8-f2d9715af377"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#admin_application_get/获取手机key值
def get_admin_application_get(type, domain,tenantId,bakSess):
    path="/admin/application/get"
    print "domain:", domain + path
    payload={
        "tenantId":int(tenantId),
        "sess":bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "06e53420-a2cd-45d4-893a-8e1ca05b68f2"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#sms_addSmsLog/发送短信
def get_sms_addSmsLog(type, domain,taskId):
    path="/sms/addSmsLog"
    print "domain:", domain + path
    payload={
        "params": [
            {
                "taskId": taskId,
                "params": {
                    "mobile": "13393213135",
                    "name": "aa"
                }
            }
        ]
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "a954c534-71ee-46d6-bd3d-871307281758"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_article_collection_check/检查当前注册用户是否可以收藏该文章
def get_api_article_collection_check(type, domain,tenantId,articleId,loginSess1):
    path="/api/article/collection/check"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "articleId": articleId,
        "sess": loginSess1
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "6f1797ca-1d4a-41f8-b1a7-6fe65fb334be"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_customform_get/获取自定义表单详情
def get_api_customform_get(type, domain,tenantId,customFormId,bakSess):
    path="/api/customform/get"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "customFormId": customFormId,
        "globalUserId": "0903c078acc06f3713f73de9cc562e23",
        "sess": bakSess,
        "openId": "oG80v1ePWq7jnsV_lyACnWt8sFjg"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "5569d671-50c1-4fdf-b77d-f362df947bec"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_file_download_interaction_query/获取注册用户邮件中文章模板关联文件下载的记录
def get_api_file_download_interaction_query(type, domain,tenantId,loginSess1):
    path="/api/file/download/interaction/query"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "start": "0",
        "num": "5",
        "sess": loginSess1
    }
    headers = {
        'Content-Type': "application/json",
        'Cookie': "=SMARKET_MEMBER_SESS",
        'cache-control': "no-cache",
        'Postman-Token': "9f9b3d0b-4ac4-440b-8465-b2b896c8635a"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api_member_form_share/分享注册表单记录互动行为
def get_api_member_form_share(type, domain,tenantId,registerFormId,loginSess1):
    path="/api/member/form/share"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "formId": registerFormId,
        "globalUserId": "0903c078acc06f3713f73de9cc562e23",
        "openId": "",
        "sess": loginSess1
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "5550d4cb-08bd-4893-a14c-cfd3e97f1a02"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#questionary_getResultList/该接口为后台接口，后期即将移除，请不要继续使用，获取从某个实例进来回答问卷的列表
def get_questionary_getResultList(type, domain,tenantId,bakSess):
    path="/questionary/getResultList"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "moduleType": 4,
        "memberId": 1,
        "start": 0,
        "num": -1,
        "withScore": 1,
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "74d7411e-6b53-4a75-ac9d-38e612f0e335"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#member_GetTokenByOpenId/通过openId 获取token
def get_member_GetTokenByOpenId(type, domain,wechatId):
    path="/member/GetTokenByOpenId"
    print "domain:", domain + path
    payload={
        "openId": "oG80v1ePWq7jnsV_lyACnWt8sFjg",
        "unionId": "ok4RIwWTOQ9mQFI_VEOQBfHSiRkY",
        "weChatId": wechatId
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "c3f27354-c143-4a20-b80d-9a2b9b99a71f"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#member_admin_unbindWeChat/用户和微信解绑--数据删除插件使用
def get_member_admin_unbindWeChat(type, domain,tenantId,memberSchemaId,wechatId):
    path="/member/admin/unbindWeChat"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "memberSchemaId": memberSchemaId,
        "weChatId": wechatId,
        "openId": "oG80v1ePWq7jnsV_lyACnWt8sFjg",
        "sess": ""
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "799cdf12-1697-4c0e-b5b3-c40f75978d22"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#account_verifySession/验证session,并获取相应的信息
def get_account_verifySession(type, domain,loginSess1):
    path="/account/verifySession"
    print "domain:", domain + path
    payload={"sess": loginSess1}
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=",
        'cache-control': "no-cache",
        'Postman-Token': "3327308d-2a8f-4275-bf05-7ddf89083f62"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#admin_member_integral_updateitems/批量积分变更
def get_admin_member_integral_updateitems(type, domain,seminarId_instanceId,wechatId,bakSess):
    path="/admin/member/integral/updateItems"
    print "domain:", domain + path
    payload={
    "item": [
      {
        "moduleId": "1",
        "instanceId": seminarId_instanceId,
        "loginId": "",
        "openId": "o_sUFt-1Pn-7oRu9O7exyzxyYMQY",
        "weChatId": wechatId,
        "actionKey": "survey_submit",
        "integral": "1"
      },
     {
        "moduleId": "1",
        "instanceId": seminarId_instanceId,
        "loginId": "",
        "openId": "o_sUFt-1Pn-7oRu9O7exyzxyYMQY",
        "weChatId": "9944",
        "actionKey": "survey_submit",
        "integral": "2"
      }
    ],
    "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "d86c9c88-3261-41fc-aecc-7d75afdd1afe"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api/seminar/signingpoint/query/查询实例下的签到点列表
def get_api_seminar_signingpoint_query(type, domain,tenantId,seminarId_instanceId):
    path="/api/seminar/signingpoint/query"
    print "domain:", domain + path
    payload={
    "tenantId": tenantId,
    "instanceId": seminarId_instanceId,
    "type": "bylist",
    "isAll": "1",
    "fieldId": "0",
    "needLimit": "0"
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=",
        'cache-control': "no-cache",
        'Postman-Token': "3327308d-2a8f-4275-bf05-7ddf89083f62"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#admin/account/userRole/set/编辑后台账号权限
def get_admin_account_userRole_set(type, domain,tenantId,nodeId,bakSess,userId,roleId):
    path="/admin/account/userRole/set"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "nodeId": nodeId,
        "userId": userId,
        "roleIds": [roleId],
        "type": 1,
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "d34a07ab-f33d-430c-a55f-70fc99483ee7"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#admin/tag/trigger/score/getlist/根据租户id获取行为标签触发分值
def get_admin_tag_trigger_score_getlist(type, domain,tenantId,bakSess):
    path="/admin/tag/trigger/score/getlist"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "5bd9f227-7071-4fd2-bd94-f47b043fe3b6"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api/seminar/contacts/ticket/get/获取联系人电子门票图片
def get_api_seminar_contacts_ticket(type, domain,tenantId,contactId,qrCode):
    path="/api/seminar/contacts/ticket/get"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "contactId": contactId,
        "qrCode": qrCode
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "115c812a-6fd7-4970-9791-79420765136f"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api/seminar/contacts/qrcode/browse/参会人签到二维码浏览（次数+1）
def get_api_seminar_contacts_qrcode_browse(type, domain,tenantId):
    path="/api/seminar/contacts/qrcode/browse"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "contactId": "478865",
        "type": "ticket"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "636ff42e-3f33-4939-8778-4286fcd4f04c"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#customForm_reAction自定义表单重复提交，更新之前的提交结果(项目需要用)
def get_customForm_reAction(type, domain,registerFormId):
    path="/customForm/reAction"
    print "domain:", domain + path
    payload={
        "customFormId": registerFormId,
        "globalUserId": "39e5bd2a4a1c363d09b9fdd09323b3d8",
        "referenceUrl": "",
        "linkId": 26892,
        "openId": "",
        "nickName": "",
        "name": "",
        "memberId": "",
        "headImage": "",
        "city": "",
        "province": "",
        "country": "",
        "items": [
            {
                "fieldName": "name",
                "value": "Gaoming"
            },
            {
                "fieldName": "mobile",
                "value": "18633873521"
            },
            {
                "fieldName": "avatar",
                "value": {
                    "fileName": "username",
                    "mapId": "9a644a7fea95749f75f8cafffd055055"
                }
            }
        ],
        "checkCode": "",
        "createTime": "",
        "sess": "",
        "ver": "v2.0.1"
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "a4d03e4d-3941-402e-8f76-cba25fb14875"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api/file/folder/interaction/share/记录文件夹分享互动行为
def get_api_file_folder_interaction_share(type, domain,tenantId,FolderId):
    path="/api/file/folder/interaction/share"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "folderId": FolderId,
        "source": "WAP",
        "globalUserId": "bd032103729e277cbd027d4c9a3b4577",
        "sess": "",
        "openId": "",
        "currentUrl": "",
        "weChatId": "",
        "browseInfo": {
            "userAgent": "",
            "browser": "Wechat",
            "version": "6.5.7",
            "os": " iPhone OS 9_1 ",
            "equipment": "iPhone",
            "resolution": "320X504",
            "referenceUrl": "",
            "referenceTitle": "",
            "sessionId": ""
        }
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "394b5a0f-6448-4cfd-9166-3339fe2c0afd"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#member_integral_get/查询注册用户|微信粉丝积分
def get_member_integral_get(type, domain,tenantId,loginSess1):
    path="/api/member/integral/get"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "sess": loginSess1,
        "openId": "oG80v1WEYqATpSTdxH3-ZKS6Hwn4",
        "timeSpan": "1543489592"
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "e3074aca-8f23-475e-ac7d-e877efaa136b"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#api/member/integral/integrallog/query/查询变更日志
def get_api_member_integral_integrallog_query(type, domain,tenantId,seminarId_instanceId,loginSess1):
    path="/api/member/integral/integrallog/query"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "moduleId": "1",
        "instanceId": seminarId_instanceId,
        "openId": "",
        "num":"1",
        "start": "0",
        "actionKey": "survey_submit",
        "sess":loginSess1,
        "timeSpan": "1543574291"
    }
    headers = {
        'Content-Type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'Postman-Token': "38cd7b47-40bf-43d2-91ad-f95bddb46367"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
#admin_account_password_update/客户管理中修改用户密码
def get_admin_account_password_update(type, domain,tenantId,nodeId,bakSess):
    path="/admin/account/password/update"
    print "domain:", domain + path
    payload={
        "tenantId": tenantId,
        "nodeId": nodeId,
        "userId": 1756,
        "newPwd": "4297F44B13955235245B2497399D7A93",
        "sess": bakSess
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "d4248a33-bdd8-411c-b5e7-5a01306d2ebb"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# 二维码密串登录
def get_most_dimensional_code_string(type,domain,loginToken):
    path="/content/index.php"
    print "domain:", domain+path
    payload={
          "command": { "size": 0,"orn": "orn","dst": "dst","type": "0x0002","cmd": "admin.account.login.tokenLogin","sess": "", "seq": "","ver": "1000",
            "body": {
        "loginToken":loginToken}}
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "e19c203f-7d94-d1cd-b7ad-d1668ef1b163"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful("POST", domain+path, payload, headers, type, type)
# account/getOAuthTokenByOpen/为account/verifyToken提供token
def get_most_account_getOAuthTokenByOpen(type,domain,tenantId,bakSess):
    path="/content/index.php"
    print "domain:", domain+path
    payload={
          "command": {
            "size": 0,
            "orn": "orn",
            "dst": "dst",
            "type": "0x0002",
            "cmd": "account.getOAuthTokenByOpen",
            "sess": "",
            "seq": "",
            "ver": "1000",
            "body": {
        "tenantId":int(tenantId),
        "sess":str(bakSess)
            }}
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "05adb8ff-b893-2364-74a8-b1e36defef28"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print payload
    return api_quester_common().Is_successful_getvalue_02("POST", domain+path, payload, headers, type, type,"token")
# account/verifyToken/为九芝兰提供验证token的接口，九芝兰使用smarket3给它的token来查询租户信息
def get_most_account_verifyToken(type, domain,tokenfor_verifyToken):
    path="/account/verifyToken"
    print "domain:", domain+path
    payload={
          "token":tokenfor_verifyToken
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "f7353d1c-2b72-d2b3-9edf-163b855327da"
    }
    return api_quester_common().Is_successful("POST", domain+path, payload, headers, type, type)
# member/GetTokenByOpenId/通过openId 获取token
def get_most_member_GetTokenByOpenId(type,domain):
    path="/member/GetTokenByOpenId"
    print "domain:", domain+path
    payload={
        "openId":"oG80v1Ve08-xiPDeZ0SaOjwzjJ24",
        "unionId":"ok4RIwWCvVtiRVCS_az7FADhIhEs",
        "nickname":"张三",
        "avatar":"http://thirdwx.qlogo.cn/mmopen/svyiar8ZPUuvUCEefSrVmlv34QInURv1tbpXSXAp0QYoxicq0ew8WWfGCQiaaAUhJO2XeEStjJZYE4zDqMviciaWzCIicG17dW42dic/132"
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "16757de4-db23-be8e-c2bb-a6aab968de8c"
    }
    return api_quester_common().Is_successful_getvalue_02("POST", domain+path, payload, headers, type, type,"token")
# member/bind/绑定第三方 当前实名用户与第三方登录用户绑定
def get_most_member_bind(type, domain, loginSess,tokenfor_memberbind):
    path="/member/bind"
    print "domain:", domain+path
    payload={
        "sess":str(loginSess),
        "token":str(tokenfor_memberbind)
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "2a854816-a6ff-527c-1ea8-bdbb5df5f4d4"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload；", payload
    return api_quester_common().Is_successful("POST", domain+path, payload, headers, type, type)
# member/unbind/解绑第三方 当前实名用户与第三方登录用户解绑
def get_most_member_unbind(type, domain, loginSess):
    path="/member/unbind"
    print "domain:", domain+path
    payload={
        "sess":loginSess,
        "provider":"wechat"
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "b75b369e-888b-d036-5ad6-e38910ce03b1"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload；", payload
    return api_quester_common().Is_successful("POST", domain+path, payload, headers, type, type)
# member_geneUpdate/更新注册用户信息
def get_most_member_geneUpdate(type, domain, loginSess):
    path="/member/geneUpdate"
    print "domain:", domain+path
    payload={
          "formData": [{
            "fieldId": 26,
            "value": ["北京"]
          }],
          "sess": str(loginSess)
    }
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "807eae94-1de7-5101-3846-e7f6c5970077"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload；", payload
    return api_quester_common().Is_successful("POST", domain+path, payload, headers, type, type)
# 线上会创建视频
def get_create_video(type, url, bakSess,webinarId_Dianbo,tenantId,create_video):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload="command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=webinar.demand.video.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BwebinarId%5D="+webinarId_Dianbo+"&command%5Bbody%5D%5Btitle%5D="+createTime+"&command%5Bbody%5D%5Bdescription%5D=&command%5Bbody%5D%5BvideoOrigin%5D=C%3A%5CUsers%5CAdministrator%5CDesktop%5C1.mp4&command%5Bbody%5D%5BmapId%5D=&command%5Bbody%5D%5Btimes%5D=&command%5Bbody%5D%5BorderNum%5D=2&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "807eae94-1de7-5101-3846-e7f6c5970077"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, create_video,type, "desc")
# 线上会获取视频id
def get_videoId(type, url, bakSess,webinarId_Dianbo,tenantId,create_video,video_instanceId):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload="command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=webinar.demand.video.getList&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BwebinarId%5D="+webinarId_Dianbo+"&command%5Bbody%5D%5BinstanceId%5D="+video_instanceId+"&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "807eae94-1de7-5101-3846-e7f6c5970077"
    }
    return api_quester_common().post_request_productLineId("POST", url, payload, headers, create_video,type, "videoId")
# 获取文章id
def get_articleId(type, url, bakSess,articleCategoryId,tenantId,nodeId):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload="command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=admin.article.Create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BmoduleId%5D=0&command%5Bbody%5D%5BarticleCategoryId%5D="+articleCategoryId+"&command%5Bbody%5D%5BlinkUrl%5D=http%3A%2F%2F&command%5Bbody%5D%5BarticleId%5D=&command%5Bbody%5D%5BtypeId%5D=235684&command%5Bbody%5D%5BuseLinkUrl%5D=0&command%5Bbody%5D%5BshareTitle%5D=&command%5Bbody%5D%5BshareDesc%5D=&command%5Bbody%5D%5BshareImageMappingId%5D=&command%5Bbody%5D%5BshareState%5D=2&command%5Bbody%5D%5BisAllowedComment%5D=1&command%5Bbody%5D%5BisAllowedLike%5D=1&command%5Bbody%5D%5BisEnabled%5D=1&command%5Bbody%5D%5BisStick%5D=0&command%5Bbody%5D%5BisRecommend%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BfieldId%5D=0&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BfieldName%5D=title&command%5Bbody%5D%5Bfields%5D%5B0%5D%5Bvalue%5D=hello&command%5Bbody%5D%5Bfields%5D%5B0%5D%5BoptionCategory%5D=1&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BfieldId%5D=0&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BfieldName%5D=content&command%5Bbody%5D%5Bfields%5D%5B1%5D%5Bvalue%5D=%3Cp%3Ehello%3C%2Fp%3E&command%5Bbody%5D%5Bfields%5D%5B1%5D%5BoptionCategory%5D=1&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BfieldId%5D=0&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BfieldName%5D=coverImageMappingId&command%5Bbody%5D%5Bfields%5D%5B2%5D%5Bvalue%5D=&command%5Bbody%5D%5Bfields%5D%5B2%5D%5BoptionCategory%5D=1&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BfieldId%5D=0&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BfieldName%5D=summary&command%5Bbody%5D%5Bfields%5D%5B3%5D%5Bvalue%5D=&command%5Bbody%5D%5Bfields%5D%5B3%5D%5BoptionCategory%5D=1&command%5Bbody%5D%5Bfields%5D%5B4%5D%5BfieldId%5D=0&command%5Bbody%5D%5Bfields%5D%5B4%5D%5BfieldName%5D=pushTime&command%5Bbody%5D%5Bfields%5D%5B4%5D%5Bvalue%5D=1552406400&command%5Bbody%5D%5Bfields%5D%5B4%5D%5BoptionCategory%5D=2&command%5Bbody%5D%5Bfields%5D%5B5%5D%5BfieldId%5D=0&command%5Bbody%5D%5Bfields%5D%5B5%5D%5BfieldName%5D=showImages&command%5Bbody%5D%5Bfields%5D%5B5%5D%5BoptionCategory%5D=2&command%5Bbody%5D%5Bfields%5D%5B6%5D%5BfieldId%5D=0&command%5Bbody%5D%5Bfields%5D%5B6%5D%5BfieldName%5D=typeId&command%5Bbody%5D%5Bfields%5D%5B6%5D%5Bvalue%5D=&command%5Bbody%5D%5Bfields%5D%5B6%5D%5BoptionCategory%5D=2&command%5Bbody%5D%5Bfields%5D%5B7%5D%5BfieldId%5D=0&command%5Bbody%5D%5Bfields%5D%5B7%5D%5BfieldName%5D=fileIds&command%5Bbody%5D%5Bfields%5D%5B7%5D%5BoptionCategory%5D=2&command%5Bbody%5D%5BtenantId%5D="+tenantId+"&command%5Bbody%5D%5BnodeId%5D="+nodeId+""
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "807eae94-1de7-5101-3846-e7f6c5970077"
    }
    return api_quester_common().post_request_get_customFormId("POST", url, payload, headers, "articleId",type, "articleId")
# 获取线上会报名表单id
def get_webinar_BMFormId(type, url, bakSess,webinar_instanceId,tenantId,schemaId,memberFormId):
    payload="command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=customForm.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5Btitle%5D=%E6%88%91%E6%98%AF%E6%B5%8B%E8%AF%95_%E6%8A%A5%E5%90%8D&command%5Bbody%5D%5BinstanceId%5D="+webinar_instanceId+"&command%5Bbody%5D%5Btype%5D=1&command%5Bbody%5D%5BisPermanent%5D=1&command%5Bbody%5D%5BstartTime%5D=&command%5Bbody%5D%5BendTime%5D=&command%5Bbody%5D%5BneedLogin%5D=0&command%5Bbody%5D%5BcompleteActionType%5D=0&command%5Bbody%5D%5BcompleteAction%5D=&command%5Bbody%5D%5Bleads%5D=0&command%5Bbody%5D%5BtopMenu%5D=0&command%5Bbody%5D%5BisShared%5D=0&command%5Bbody%5D%5BmoduleType%5D=2&command%5Bbody%5D%5BnotDisplayedInList%5D=1&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Burl%5D=%5Bwebinarb%5D&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Bcmd%5D=webinar.open.getApplicantInfo&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Burl%5D=%5Bwebinarb%5D&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Bcmd%5D=webinar.open.registration&command%5Bbody%5D%5Bidentity%5D=3&command%5Bbody%5D%5BschemaId%5D="+schemaId+"&command%5Bbody%5D%5BregisterFormId%5D="+memberFormId+"&command%5Bbody%5D%5BtrackId%5D=0&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "807eae94-1de7-5101-3846-e7f6c5970077"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, "webinar_BMFormId",type, "content")
# 设置奖项选项
def set_luckDraw_Items(type, url, bakSess,luckyDrawId,tenantId):
    payload="command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bcmd%5D=luckyDraw.addAwardDetails&command%5Bver%5D=1000&command%5Bbody%5D%5BluckyDrawId%5D="+luckyDrawId+"&command%5Bbody%5D%5Bawards%5D%5B1%5D%5Bname%5D=%E6%9C%AA%E4%B8%AD%E5%A5%96&command%5Bbody%5D%5Bawards%5D%5B1%5D%5Btype%5D=&command%5Bbody%5D%5Bawards%5D%5B1%5D%5BawardId%5D=&command%5Bbody%5D%5Bawards%5D%5B1%5D%5Bdesc%5D=%E8%B0%A2%E8%B0%A2%E5%8F%82%E4%B8%8E&command%5Bbody%5D%5Bawards%5D%5B1%5D%5Bnum%5D=&command%5Bbody%5D%5Bawards%5D%5B1%5D%5Bprobability%5D=10000000&command%5Bbody%5D%5Bawards%5D%5B1%5D%5Btip%5D=perfect&command%5Bbody%5D%5Bawards%5D%5B2%5D%5Bname%5D=%E4%B8%80%E7%AD%89%E5%A5%96&command%5Bbody%5D%5Bawards%5D%5B2%5D%5Btype%5D=1&command%5Bbody%5D%5Bawards%5D%5B2%5D%5BawardId%5D=339&command%5Bbody%5D%5Bawards%5D%5B2%5D%5Bdesc%5D=1111&command%5Bbody%5D%5Bawards%5D%5B2%5D%5Bnum%5D=1&command%5Bbody%5D%5Bawards%5D%5B2%5D%5Bprobability%5D=100000&command%5Bbody%5D%5Bawards%5D%5B2%5D%5Btip%5D=perfect&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "807eae94-1de7-5101-3846-e7f6c5970077"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, "webinar_BMFormId",type, "desc")
# 给对象打标签
def tag_application_SetOnObject(type,domain,tenantId,tagSchemaId,tagFieldId,fieldName,displayName,tagId,bakSess):
    path = "/tag/application/SetOnObject"
    print "domain:", domain + path
    payload = {
  "sess": str(bakSess),
  "tenantId": tenantId,
  "moduleId": "",
  "instanceId": "",
  "objectId": "882",
  "objectType": "zcbd",
  "objectTitle": "xjzcbd",
  "objectModuleId": "",
  "objectInstanceId": "",
  "tags": [
    {
      "tagFieldId": int(tagFieldId),
      "fieldName":fieldName ,
      "displayName": displayName,
      "tags": [
        {
          "tagId": int(tagId),
          "tenantId": int(tenantId),
          "tagSchemaId": int(tagSchemaId),
          "tagFieldId": int(tagFieldId),
          "tagName": "1",
          "checked": "true",
          "isDelete": 0
        }
      ]
    }
  ]
}

    headers = {
        'content-type': "application/json",
        'cookie': "SMARKET_MEMBER_SESS=;",
        'cache-control': "no-cache",
        'postman-token': "3221c8f5-63de-4970-25f9-71f55b820297"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload；", payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# 给对象打标签，只有s2有
def webinar_open_transfer(type,domain):
    path = "/webinar/open/transfer"
    print "domain:", domain + path
    payload = {}
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "ab4e30f4-5fed-992d-ffd6-8a31d8b45dd6"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload；", payload
    return api_quester_common().Is_successful_status("POST", domain + path, payload, headers, type, type)
# 查看自己的签到记录
def seminar_signingPoint_getCheckInLog_contactId(type,domain,tenantId,bakSess,seminarId,seminarId_instanceId,signingPointId,passageId,contactId):
    path = "/seminar/signingPoint/getCheckInLog"
    print "domain:", domain + path
    payload = {
    "tenantId": tenantId,
    "sess":bakSess,
    "seminarId": seminarId,
    "instanceId": seminarId_instanceId,
    "groupId": 0,
    "signingPointId": signingPointId,
    "passageId": passageId,
    "contactId": contactId,
    "keyWord": "",
    "sort": 1,
    "start": 0,
    "num": 20
  }
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "ab4e30f4-5fed-992d-ffd6-8a31d8b45dd6"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload；", payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# 二维码密串登陆
def admin_account_login_tokenLogin(type,domain):
    path = "/admin/account/login/tokenLogin"
    print "domain:", domain + path
    payload={"loginToken": "UO6iktAhql1ShmdgTGnqaxY/CgoZhQsn0HoMRhJVtXVBU9W9AGR1dErT+NJsz3c8CyM+HATtC1rFYgXwttMVWxJMAxZlAmpAG1g3ThKKppY=" }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "eadb5b31-4fb9-f92e-63da-bf52c84a5ebd"
    }
    payload = json.dumps(payload, encoding="utf-8", ensure_ascii=False)
    print "payload；", payload
    return api_quester_common().Is_successful("POST", domain + path, payload, headers, type, type)
# 获取图片验证码
def member_getImageCode(type,domain):
    path = "/member/getImageCode"
    print "domain:", domain + path
    querystring = {"height": "20", "width": "20", "cookieId": "39e5bd2a4a1c363d09b9fdd09323b3d8", "len": "10"}

    headers = {
        'cache-control': "no-cache",
        'postman-token': "4273d3e9-84db-d23b-522f-5896543bf644"
    }
    # querystring = json.dumps(querystring, encoding="utf-8", ensure_ascii=False)
    # print "querystring；", querystring
    return api_quester_common().Is_successful_get("GET", domain + path, querystring, headers, type, type)
# 华为410361账号监控
def sms_balance(type):
    url = "http://114.118.2.242:8090/sms/balance.do"

    payload = "userid=410361&timespan=20190221022357&pwd=A4FFBADA6FCD6889543DA5422656863E"
    headers = {
        "content-type": "application/x-www-form-urlencoded"
    }
    return api_quester_common().Is_successful_hwjiankong("POST", url, payload, headers, type, type,10000)
# 华为400310账号监控
def sms_balance_two(type):
    url = "http://114.118.2.242:8090/sms/balance.do"

    payload = "userid=400310&timespan=20190221022357&pwd=F9C5F84CD1A905A5EC2F8D15FAE5A1AA"
    headers = {
        "content-type": "application/x-www-form-urlencoded"
    }
    return api_quester_common().Is_successful_hwjiankong("POST", url, payload, headers, type, type,2000)
# 获取线上会的互动问卷id
def get_webinar_question_wj(type,url, bakSess, webinarId_instanceId, tenantId,schemaId,registerFormId):
    payload = "command%5Bsize%5D=0&command%5Born%5D=02-0001-00000001&command%5Bdst%5D=01-0401-00000001&command%5Btype%5D=2&command%5Bcmd%5D=questionary.create&command%5Bsess%5D="+bakSess+"&command%5Bseq%5D=0&command%5Bver%5D=1000&command%5Bbody%5D%5BstartTime%5D=&command%5Bbody%5D%5BendTime%5D=&command%5Bbody%5D%5BquestionaryBankId%5D=&command%5Bbody%5D%5BmeetingType%5D=&command%5Bbody%5D%5BmeetingInstanceId%5D=&command%5Bbody%5D%5Bdesc%5D=&command%5Bbody%5D%5BshareDesc%5D=&command%5Bbody%5D%5Btitle%5D=%E9%97%AE%E5%8D%B7&command%5Bbody%5D%5Btype%5D=1&command%5Bbody%5D%5BisPermanent%5D=1&command%5Bbody%5D%5BattachId%5D=0&command%5Bbody%5D%5BinstanceId%5D=&command%5Bbody%5D%5BmoduleType%5D=&command%5Bbody%5D%5Bidentity%5D=1&command%5Bbody%5D%5BschemaId%5D=&command%5Bbody%5D%5BtrackId%5D=0&command%5Bbody%5D%5BregisterFormId%5D=&command%5Bbody%5D%5BattachWXAccount%5D=0&command%5Bbody%5D%5BattentionWeChat%5D=0&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Burl%5D=&command%5Bbody%5D%5BextraConfig%5D%5Binit%5D%5Bcmd%5D=&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Burl%5D=&command%5Bbody%5D%5BextraConfig%5D%5Bpost%5D%5Bcmd%5D=&command%5Bbody%5D%5BshareTitle%5D=%E9%97%AE%E5%8D%B7&command%5Bbody%5D%5B_browseInfo%5D%5BuserAgent%5D=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F72.0.3626.121+Safari%2F537.36&command%5Bbody%5D%5B_browseInfo%5D%5Bbrowser%5D=Chrome&command%5Bbody%5D%5B_browseInfo%5D%5Bversion%5D=72.0.3626.121&command%5Bbody%5D%5B_browseInfo%5D%5Bos%5D=Windows&command%5Bbody%5D%5B_browseInfo%5D%5Bequipment%5D=%E7%94%B5%E8%84%91%E7%AB%AF&command%5Bbody%5D%5B_browseInfo%5D%5Bresolution%5D=1920X1080&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceUrl%5D=http%3A%2F%2Fhwuat.smarket.net.cn%2Ftool%2Fquestionaire%2Findex.html%23%2F&command%5Bbody%5D%5B_browseInfo%5D%5BreferenceTitle%5D=&command%5Bbody%5D%5BtenantId%5D="+tenantId+""
    print "url:",url
    print "payload：",payload
    headers = {
         'cache-control': "no-cache",
        'Postman-Token': "2c209b08-d4ab-4aff-ac21-7ba8f3f9ae96"
    }
    return api_quester_common().post_request_successful("POST", url, payload, headers, type, type,"content")
