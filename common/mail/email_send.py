#-*- coding:UTF-8 -*-
#!/usr/bin/python

import os
from datetime import datetime
from pages.common_pages.base import BasePage
import smtplib
from  common.mail import Xemail
import chardet


class SendEmailModel():


    def PostEmail(self):
        import smtplib  #Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
        # from email_oper.mime.multipart import MIMEMultipart
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.header import Header
        # from email_oper.mime.text import MIMEText
        from email.mime.text import MIMEText  #//导入MIMEText类
        # from email_oper.header import Header
        sender = 'gavin_li@sinobasedm.com'                      #发件人
        receiver = ['huoyan109@126.com','huoyan108@126.com']   #收件人
        subject = "Smarket3.0自动化测试测试邮件"          #邮件主题
        smtpserver = 'smtp.exmail.qq.com'                      #不同的邮件，有不同端口
        username = 'gavin_li@sinobasedm.com'                  #进入邮箱的账户名
        password = 'Abc@123'                           #进入邮箱的密码
        fileHTML = r"..\\Smarket3.0_TestReport.html"
        fileProgramLog = "D:\Info.txt"
        fileTestLogFail = "D:\TestLogFail.txt"
        fileTestLogPass = "D:\TestLogPass.txt"
        msgRoot = MIMEMultipart()
        msgRoot['From'] = Header("李鸿飞", 'utf-8')
        msgRoot['To'] =  Header("每一位项目相关人员", 'utf-8')
        subject = 'Python SMTP 邮件自动化测试'
        msgRoot['Subject'] = Header(subject, 'utf-8')

        msgRoot['Python SMTP 邮件自动化测试'] = subject         #主题
        #主要内容
        text_msg = MIMEText("<html><body><p><span style='color: black;'>&nbsp;&nbsp; hello every Receiver:</span></p><p>&nbsp;&nbsp;&nbsp;&nbsp; 附件为本次回归的测试报告，请各位查收。<br/></p><p/>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; 自动化测试小组敬上</p></body></html>",'html',_charset="utf-8")
        msgRoot.attach(text_msg)

        #附件
        att = MIMEText(open(fileHTML, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="Smarket3.0_TestReport.html"'
        msgRoot.attach(att)
        att = MIMEText(open(fileProgramLog, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="Info.txt"'
        msgRoot.attach(att)
        att = MIMEText(open(fileTestLogFail, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="TestLogFail.txt"'
        msgRoot.attach(att)
        att = MIMEText(open(fileTestLogPass, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="TestLogPass"'
        msgRoot.attach(att)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)
            smtp.login(username, password)
            smtp.sendmail(sender, receiver, msgRoot.as_string())
            smtp.quit()
            print "邮件发送成功"
        except smtplib.SMTPException:
            print "Error: 无法发送邮件"

    #邮件内容的设置
    def postreport_only(self,PerformTime,content):

        import smtplib
        content_str=str(content)
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.application import MIMEApplication
        from email.header import Header
        sender = 'abc@sinobasedm.com'  # 发件人
        nowtime = datetime.now().strftime('%H')
        # if nowtime >= "04" and nowtime <= "08":
        # receiver = ('lily_liu@sinobasedm.com','394522655@qq.com', 'paul_ma@sinobasedm.com', 'master_ma@sinobasedm.com',
        #                 'kim_liu@sinobasedm.com', 'manco_wang@sinobasedm.com', 'jason_liang@sinobasedm.com',
        #                 '1946898935@qq.com', 'cara_gao@sinobasedm.com', 'lizzy_li@sinobasedm.com','1511274870@qq.com',
        #                 'andy_yang@sinobasedm.com', 'lisa_xing@sinobasedm.com', 'belle_hu@sinobasedm.com',
        #                 'nina_xiao@sinobasedm.com','xin_liu@sinobasedm.com','smile_geng@sinobasedm.com',
        #                 'merry_you@sinobasedm.com','aimee_wang@sinobasedm.com','aurora_zhang@sinobasedm.com','bella_wang@sinobasedm.com','lilian_chang@sinobasedm.com')
        # areceiver = ('394522655@qq.com', '1946898935@qq.com', 'cara_gao@sinobasedm.com', 'Willie_wang@sinobasedm.com',
        #                 'kevin_liu@sinobasedm.com', 'lizzy_li@sinobasedm.com',
        #                 '1511274870@qq.com', 'andy_yang@sinobasedm.com','xin_liu@sinobasedm.com','smile_geng@sinobasedm.com',
        #                 'lisa_xing@sinobasedm.com', 'nina_xiao@sinobasedm.com', 'merry_you@sinobasedm.com','aimee_wang@sinobasedm.com','aurora_zhang@sinobasedm.com'
        #                 , 'bella_wang@sinobasedm.com', 'lilian_chang@sinobasedm.com')

        # else:
        #     receiver = ('1946898935@qq.com', 'cara_gao@sinobasedm.com','lily_liu@sinobasedm.com')
        #     areceiver = ('1946898935@qq.com', 'cara_gao@sinobasedm.com','lily_liu@sinobasedm.com')

        # receiver = ('cara_gao@sinobasedm.com', 'aurora_zhang@sinobasedm.com','lily_liu@sinobasedm.com')
        areceiver = ('lily_liu@sinobasedm.com','1946898935@qq.com')


        # receiver = ('aurora_zhang@sinobasedm.com')
        # areceiver = ('aurora_zhang@sinobasedm.com')

        receiver = "lily_liu@sinobasedm.com;1946898935@qq.com"

        subject = u"各个平台接口执行结果"  # 邮件主题
        smtpserver = 'smtp.exmail.qq.com'  # 不同的邮件，有不同端口
        username = 'abc@sinobasedm.com'  # 进入邮箱的账户名
        password = 'Sino@123'  # 进入邮箱的密码
        msgRoot = MIMEMultipart()
        msgRoot['From'] = Header("自动化测试平台", 'utf-8')
        msgRoot['To'] = Header("每一位项目相关人员", 'utf-8')
        msgRoot['Cc'] = areceiver
        msgRoot['Subject'] = Header(subject, 'utf-8') #Subject为邮件主题

        """
        主要内容，参考例子：
        msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
        注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'，
        最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。

        text_msg = MIMEText(
            "<html><body><p><span style='color: black;'>&nbsp;&nbsp; hello every Receiver:</span></p>"
            "<p>&nbsp;&nbsp;&nbsp;&nbsp; 本次测试总耗时："+ str(PerformTime) +"秒<br/></p>"
            "<p>&nbsp;&nbsp;&nbsp;&nbsp; 附件为本次回归的测试报告，请各位查收。<br/></p>"
            "<p>&nbsp;&nbsp;&nbsp;&nbsp; 本次回归测试执行用例范围："+ content +"<br/></p>"
            "<p/>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; 自动化测试小组敬上</p></body></html>",
            'html', _charset="utf-8")

        msgRoot.attach(text_msg)
        """
        # 附件
        fileHTML = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "\\report\Smarket3.0_TestReport.html"
        """
        定义文件目录,
        程序中 \ 是转义符，所以关于路径的写法要用/;
        字符串引号外加r可以不转义
        """
        result_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "\\report\\reportlog" #report存放文件夹的路径
        lists = os.listdir(result_dir)  #os.listdir(path):返回指定路径下的文件和文件夹列表;
        """
        重新按时间对目录下的文件进行排序,
        #list.sort([func]):该方法没有返回值，但会对列表的对象进行排序,func 可选参数, 如果指定该参数会使用该参数的方法进行排序。
        #sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序
        最后对lists元素，按文件修改时间大小从小到大排序。
        获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
        但是lambda fn这些的用法 不会，有熟练经验的大神可以补充，以便分享
        """
        lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
        #list.sort([func]):该方法没有返回值，但会对列表的对象进行排序,func 可选参数, 如果指定该参数会使用该参数的方法进行排序。
        #sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序
        print(('最新的文件为： ' + lists[-1]))
        fileHTML = os.path.join(result_dir, lists[-1]) #os.path.join()函数：返回值：将多个路径组合后返回
        print (file)
        """
        r:以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式
        rb:以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式
        wb:以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
        """
        f = open(fileHTML, 'rb') #python open() 函数用于打开一个文件，创建一个 file 对象。

        mail_body = f.read()  #f.read()读到文件尾时返回""(空字串)
        f.close()   #f.close() 关闭文件
        msg = MIMEText(mail_body, 'html', 'utf-8')  #MIMEText()发送文本内容 需要引入from email.mime.text import MIMEText
        msgRoot = MIMEMultipart()  #MIMEMultipart() 生成包括多个部分的邮件体
        msgRoot['Subject'] = Header(subject, 'utf-8')  # Subject为邮件主题
        msgRoot.attach(msg)
        msgRoot['From'] = sender

        msgRoot['To'] = ','.join(receiver)#实现抄送
        att = MIMEApplication(open(fileHTML, 'rb').read())
        att.add_header('Content-Disposition', 'attachment', filename=lists[-1])
        msgRoot.attach(att)

        try:
            # smtp = smtplib.SMTP()  #创建一个SMTP对象
            # smtp.connect(smtpserver)   #/通过connect方法链接到smtp主机
            # smtp.login(username, password)
            # #sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
            # # smtp.sendmail(sender, receiver, msgRoot.as_string())  #sendmail中的那个To是list，不是string，否则只能发给第一个人
            #
            # # 发送给多人、同时抄送给多人，发送人和抄送人放在同一个列表中
            # smtp.sendmail(sender, receiver, msgRoot.as_string())
            # smtp.quit()
            send1 = Xemail.SendEmail()  # 实例化SendEmailModel类
            # f_charInfo = chardet.detect(msg)
            msg1 = mail_body.decode('utf-8')
            send1.sendmail(sender, receiver,subject,msg1,fileHTML,lists[-1])
            print "邮件发送成功"
        except smtplib.SMTPException:
            print "Error: 无法发送邮件"


if __name__ == '__main__':

    P = SendEmailModel()
    content = "test_001_loginoffline;test_002_createoffline"
    content = "test_003_offline"
    P.postreport_only("总时间",content)