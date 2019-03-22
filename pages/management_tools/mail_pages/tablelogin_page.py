# -*- coding: utf-8 -*-

import time
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.off_line_meeting_pages.index_page import IndexPage
from pages.off_line_meeting_pages.new_meeting_page import NewMeetingPage
import random


class TableLogin(BasePage):


    # 新建注册表单(9)的登录页面
    def create_login(self):

        self.deprint('进入登录页面')
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 跳转到登录页面
        time.sleep(6)
        self.element_value_input('x', '//*[@id="con_one_1"]/div[1]/input', '13403211459')  # 在登录页面输入手机号
        self.element_value_input('x', '//*[@id="con_one_1"]/div[3]/input', '123123')  # 在登录页面输入密码
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面#20180809
        self.element_click('x', '//*[@id="con_one_1"]/input')  # 点击登录按钮
        self.deprint('登录成功')
        mailError = self.driver.find_element_by_xpath('//*[@id="con_one_1"]/div[6]').text
        if mailError:
            print "出现问题： ", self.deprint()
            return False

    # 新建注册表单(9)的登录页面---短信的
    def create_login_sms(self):

        self.deprint('进入登录页面')
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 跳转到登录页面
        time.sleep(6)
        self.scrollbar('200')
        self.wait_is_visible('x','/html/body/div[3]/div/div/a')#点击我要报名按钮
        time.sleep(5)
        self.element_value_input('x', '//*[@id="con_one_1"]/div[1]/input', '13393213135')  # 在登录页面输入手机号
        self.element_value_input('x', '//*[@id="con_one_1"]/div[3]/input', '123123')  # 在登录页面输入密码
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄
        self.element_click('x', '//*[@id="con_one_1"]/input')  # 点击登录按钮
        self.deprint('登录成功')
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.scrollbar('200')
        self.wait_is_visible('x','/html/body/div[3]/div/div/a')#点击刷新页面后的我要报名按钮
        # self.close()
        # mailError = self.driver.find_element_by_xpath('//*[@id="con_one_1"]/div[6]').text
        # if mailError:
        #     print "出现问题： ", self.deprint()
        #     return False


    #线下会实例的注册页面
    def register_edm(self):  # 20180808
        time.sleep(10)
        self.driver.implicitly_wait(30)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 跳转到登录页面
        # self.scrollbar("200")
        # 点击注册按钮
        self.wait_is_visible('x', '//*[@id="con_one_1"]/div[7]/div/div[2]/a')
        time.sleep(8)
        self.randome_phone_edm()
        # 点击注册按钮
        self.wait_is_visible('x', '/html/body/div[3]/div[2]/form/div[3]/div[1]/input')
        time.sleep(8)
        # self.find_element_input('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[1]/div/input', 'yaya')
        self.find_element_input('x', '//*[@id="body-box"]/form/div[1]/input', 'yaya'+ self.nowtime())
        time.sleep(1)
        self.random_email_edm()
        time.sleep(1)
        self.random_idcard_edm()
        time.sleep(1)
        self.scrollbar("200")
        self.random_username_edm()
        time.sleep(1)
        self.scrollbar("bottom")
        # 点击立即提交按钮
        self.wait_is_visible('x', '//*[@id="body-box"]/form/input')
        time.sleep(2)
        self.driver.close()

    # 线上会实例的注册页面
    def register_webinar_edm(self):  # 20180808
        time.sleep(10)
        self.driver.implicitly_wait(30)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 跳转到登录页面
        # self.scrollbar("200")
        # 点击注册按钮
        self.wait_is_visible('x', '//*[@id="con_one_1"]/div[7]/div/div[2]/a')
        time.sleep(2)
        self.randome_phone_webinar_edm()
        # 点击注册按钮
        self.wait_is_visible('x', '/html/body/div[3]/div[2]/form/div[3]/div[1]/input')
        time.sleep(8)
        # self.find_element_input('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[1]/div/input', 'yaya')
        self.find_element_input('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[1]/div/input', 'yaya'+ self.nowtime())
        time.sleep(1)
        self.random_email_webinar_edm()
        time.sleep(1)
        self.random_idcard_webinar_edm()
        time.sleep(1)
        self.scrollbar("200")
        self.random_username_webinar_edm()
        time.sleep(1)
        self.scrollbar("bottom")
        # 点击立即提交按钮
        self.wait_is_visible('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[2]/input')
        time.sleep(2)
        self.driver.close()

        # 开始随机生成身份证
    def random_idcard_edm(self):

        ranidcard = self.randomidcard_edm()
        text_idcard = str(random.randint(00000, 99999)) + str(ranidcard)
        if len(text_idcard) != 18 :
            text_idcard = text_idcard +'0'
        self.deprint(u"身份证号" + text_idcard)
        # 在身份证输入框中输入随机生成的身份证
        self.find_element_input('x', '//*[@id="body-box"]/form/div[4]/input', text_idcard)

        # 开始随机生成身份证
    def random_idcard_webinar_edm(self):

        ranidcard = self.randomidcard_edm()
        text_idcard = str(random.randint(00000, 99999)) + str(ranidcard)
        if len(text_idcard) != 18 :
            text_idcard = text_idcard +'0'
        self.deprint(u"身份证号" + text_idcard)
        # 在身份证输入框中输入随机生成的身份证
        self.find_element_input('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[4]/div/input', text_idcard)

    # 开始随机生成用户名
    def random_username_edm(self):
        text_username = 'u' + str(self.randomidcard_edm())
        # 在用户名输入框中输入随机生成的用户名
        self.find_element_input('x', '//*[@id="body-box"]/form/div[5]/input', text_username)

    # 开始随机生成用户名
    def random_username_webinar_edm(self):
        text_username = 'u' + str(self.randomidcard_edm())
        # 在用户名输入框中输入随机生成的用户名
        self.find_element_input('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[5]/div/input', text_username)

    # 返回生成13位的数值
    def randomidcard_edm(self):
        t = time.time()
        return int(round(t * 1000))

    # 输入随机邮箱值
    def random_email_edm(self):
        randomemail = self.randomemail()
        # self.find_element_input('x', '//*[@id="body-box"]/form/div[3]/input', str(randomemail)+ '@qq.com')
        self.find_element_input('x', '//*[@id="body-box"]/form/div[3]/input', '409539914@qq.com')

    # 输入随机邮箱值
    def random_email_webinar_edm(self):
        randomemail = self.randomemail()
        # self.find_element_input('x', '//*[@id="body-box"]/form/div[3]/input', str(randomemail)+ '@qq.com')
        self.find_element_input('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[3]/div/input', '409539914@qq.com')



    # 生成随机手机号码函数
    def randome_phone_edm(self):

        list = ['131', '130', '132', '155', '156', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159',
                '182', '183', '184', '157', '187', '188', '147', '178', '185', '186', '145', '176', '185', '133', '153',
                '180', '181', '189', '177']
        for i in list:
            # 输入随机的手机号
            phone = self.randomphone()
            ranphone = i + str(phone)
            print "ranphone:", ranphone
            time.sleep(5)
            # 点击右边的小眼睛图标
            self.wait_is_visible('x', '/html/body/div[3]/div[2]/form/div[1]/div[1]/i')
            time.sleep(1)
            # 输入随机的手机号码s
            self.find_element_input('x', '/html/body/div[3]/div[2]/form/div[2]/div[1]/input', ranphone)
            # 点击密码框
            self.wait_is_visible('x', '/html/body/div[3]/div[2]/form/div[1]/div[1]/input[2]')
            time.sleep(1)
            try:
                # 判断异常提示窗是否有内容输出
                text = self.find_element_text('x', '/html/body/div[3]/div[2]/form/div[2]/div[2]/p')
                if "已注册" in text:
                    # 说明手机此时已不能报名
                    continue
                else:
                    # 输入注册的密码
                    self.find_element_input('x', '/html/body/div[3]/div[2]/form/div[1]/div[1]/input[2]', '123123')
                    break
            except:
                # 输入注册的密码
                self.find_element_input('x', '/html/body/div[3]/div[2]/form/div[1]/div[1]/input[2]', '123123')
                break

            # 生成随机手机号码函数
    def randome_phone_webinar_edm(self):

        list = ['131', '130', '132', '155', '156', '135', '136', '137', '138', '139', '150', '151', '152',
                '158', '159',
                '182', '183', '184', '157', '187', '188', '147', '178', '185', '186', '145', '176', '185',
                '133', '153',
                '180', '181', '189', '177']
        for i in list:
        # 输入随机的手机号
            phone = self.randomphone()
            ranphone = i + str(phone)
            print "ranphone:", ranphone
            time.sleep(5)
            # 点击右边的小眼睛图标
            self.wait_is_visible('x', '/html/body/div[3]/div[2]/form/div[1]/div[1]/i')
            time.sleep(1)
            # 输入随机的手机号码s
            self.find_element_input('x', '/html/body/div[3]/div[2]/form/div[2]/div[1]/input', ranphone)
            # 点击密码框
            self.wait_is_visible('x', '/html/body/div[3]/div[2]/form/div[1]/div[1]/input[2]')
            time.sleep(1)
            try:
                # 判断异常提示窗是否有内容输出
                text = self.find_element_text('x', '/html/body/div[3]/div[2]/form/div[2]/div[2]/p')
                if "已注册" in text:
                    # 说明手机此时已不能报名
                    continue
                else:
                    # 输入注册的密码
                    self.find_element_input('x', '/html/body/div[3]/div[2]/form/div[1]/div[1]/input[2]',
                                            '123123')
                    break
            except:
                # 输入注册的密码
                self.find_element_input('x', '/html/body/div[3]/div[2]/form/div[1]/div[1]/input[2]', '123123')
                break

    # 获取随机的手机后8位
    def randomphone(self):

        text = random.randint(00000000, 99999999)
        # textle = len(text)
        if text != 8:
            # text = text.zfill(8)   #自动前面补0  到8位
            text = '%08d' % text
        # print text
        return text

        # return text

    #随机生成邮箱
    def randomemail(self):
        return int(time.time())

    #有登录账号的时候，直接跳转的报名页面
    def signup_exist(self):
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取上一个窗口句柄，跳转到线下会会议页面
        self.scrollbar("1000")
        self.wait_is_visible('x','//*[@id="body-box"]/form/input')#点击提交按钮
        self.close()

    # # 线上会实例短信的登录页面
    def webinar_login_sms(self):

        self.deprint('进入登录页面')
        time.sleep(8)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 跳转到登录页面
        self.element_value_input('x', '//*[@id="con_one_1"]/div[1]/input', '13393213135')  # 在登录页面输入手机号
        self.element_value_input('x', '//*[@id="con_one_1"]/div[3]/input', '123123')  # 在登录页面输入密码
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面#20180809
        self.element_click('x', '//*[@id="con_one_1"]/input')  # 点击登录按钮
        self.deprint('登录成功')
        # mailError = self.driver.find_element_by_xpath('//*[@id="con_one_1"]/div[6]').text
        # if mailError:
        #     print "出现问题： ", self.deprint()
        #     return False

    #有登录账号的时候，直接跳转的报名页面
    def signup_exist_sms(self):
        time.sleep(7)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取上一个窗口句柄，跳转到线下会会议页面
        # print u'22222'
        # time.sleep(3)
        self.scrollbar("bottom")
        # target = self.driver.find_element_by_xpath('//*[@id="body-box"]/div[1]/div[2]/div[2]/div[2]/input')
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)
        # self.wait_is_visible('x', '//*[@id="body-box"]/div[1]/div[2]/div[2]/div[2]/input')
        time.sleep(3)
        self.wait_is_visible('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[2]/input')# 点击立即提交按钮
        time.sleep(3)
        self.close()


if __name__ == '__main__':
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        time.sleep(3)
        o.click_menu_bt('9')
        o = IndexPage(dr)#调用线下会的类
        o.click_createunderline()#调用线下会点击首页的创建会议按钮的方法
        o = NewMeetingPage(dr)#调用线下会的类
        o.create_neww_offline()#调用线下会创建会议的方法
        # # S = Edm_offline(dr)
        # S.createofflineEdm()
        # S.startsigning()
        # S.signupoffline()



