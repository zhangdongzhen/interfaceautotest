# -*- coding: utf-8 -*
import json,urllib2,time
import re
from common.common_function.Read_From_Mysql import Read_From_Mysql
from common.common_function import sql_config
from pages.api.api_most_all import api_most_all
def dd(info,casecount,platname):
    # list1.reverse()
    # info = ''
    # for m in range(0,len(list1)):
    #     info = info + list1[m]+'\n'
    # len1 = len(list1)
    content = platname+u"postman执行结果"+str(casecount)+u"个接口失败:"+'\n'+info
    # print content
    url='https://oapi.dingtalk.com/robot/send?access_token=d8fadace08194f839283edbafdd30ec8f2909ba9fe196db70f562cf7e4bc6fa5' #钉钉群webhoot
    con={"msgtype":"text","text":{"content":content},"at": {"atMobiles": ["18732159800","18732159800"]}}
    jd=json.dumps(con)
    req=urllib2.Request(url,jd)
    req.add_header('Content-Type', 'application/json')
    response=urllib2.urlopen(req)
    # print response,time.ctime()


def getLoginfo(platform_name,serialnum):
    ss  = sql_config.get_loginfo(platform_name, serialnum)
    loginfo = ''
    record=Read_From_Mysql().Select_Datas_From_User(sql_config.get_loginfo(platform_name,serialnum))
    casecount = len(record)
    for row in record:
        failname = row[0]
        requestbody = row[1]
        responsebody = row[2]
        loginfo = loginfo + u'接口：'+failname+'\n'+u'请求体：'+requestbody+'\n'+'响应体：'+responsebody+'\n'

    return loginfo,casecount

	
if __name__ == '__main__':
    # logpath="C:\\dd\\log"
    platform_name = 'HW'
    serialnum = '20190307170747'
    loginfo,casecount= getLoginfo(platform_name,serialnum)
    platname = u'华为产品' #接口测试平台名称
    dd(loginfo,casecount,platname)
