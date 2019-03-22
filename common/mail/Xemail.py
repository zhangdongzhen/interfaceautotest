# encoding: utf-8
import requests
import urllib
import smtplib

import time
import unittest


class SendEmail():
    def sendmail(self,from1,to1,subject1,html1,attach,filename):
        url="http://api.sendcloud.net/apiv2/mail/send"
        MailAPIKey = 'XPUu9gkkbuyxfM26'
        MailAPIUser = 'monitor_sendcloud'
        print subject1
        # params = {
        #     "apiUser":MailAPIUser,
        #     "apiKey": MailAPIKey ,
        #     "from" : "monitor@sendcloud.im",
        #     "to":"monitor@sendcloud.im",
        #     "subject":"ceshi",
        #     "html" :"hello"
        #          }

        files = [
            ("attachments", (urllib.quote(filename), open(attach, 'rb'), 'application/octet-stream'))
        ]
        params = {
            "apiUser":MailAPIUser,
            "apiKey": MailAPIKey ,
            "from" : from1,
            "to":to1,
            "subject":u"Smarket3.0自动化平台测试邮件",
            "html" :html1

                 }
        # headers = {
        #     'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        #     'cache-control': "no-cache"
        # }
        re = requests.post(url,files=files,data = params)
        print re





