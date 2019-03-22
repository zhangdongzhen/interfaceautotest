# -*- coding: utf-8 -*-
from datetime import datetime
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.select import Select
import sys
from pages.common_pages.ConfigUrl import ConfigUrl
import win32con
import win32gui
import os
#print sys.getdefaultencoding()#sys.getdefaultencoding(): 获取系统当前编码，一般默认为ascii。
from random import randint   #random:随机的意思
type=sys.getfilesystemencoding()
reload(sys)
sys.setdefaultencoding('utf8')
#print type
import time

#页面操作基础类
class BasePage(object):
    base_url=ConfigUrl().BaseUrl()
    #__init__()方法对参数进行初始化
    def __init__(self,selenium_driver,base_url=base_url,parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout=30
        self.parent = parent
        self.url=""
    def _open(self,url):
        self.url = self.base_url + url
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.timeout)
    def _open_uat(self,url):
    #     此方法用于uat的登陆
        url="https://uat-tenant.smarket.net.cn"
        self.url=url
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.timeout)
    def open(self):
        self._open(self.url)
    def open_uat(self):
         # 此方法用于uat的登陆
        self._open_uat(self.url)
    #退出浏览器
    def quit(self):
        self.driver.quit()
    #关闭当前页
    def close(self):
        self.driver.close()
    """
    #定位元素并单击,对单击操作做扩展
    driver.implicitly_wait() :隐形等待，设定时间是秒
    find_element_by_xpath():按xpath定位元素
    find_element_by_class_name():按name定位元素
    find_element_by_id():按id定位元素
    find_element_by_link_text（）:按文本链接定位
    find_element_by_tag_name():html 本质就是tag来定义实现不同的功能，每一个元素都是一个tag。

    """
    def element_click(self,method,location):

        if method =="x":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_xpath(location).click()
        if method =="class":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_class_name(location).click()
        if method == "id":
            self.driver.find_element_by_id(location).click()
        if method == "name":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_name(location).click()
        if method == "link":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_link_text(location).click()
        if method == "tag":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_tag_name(location).click()
        if method == "Plink":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_partial_link_text(location).click()
        if method == "css":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_css_selector(location).click()
    # #定位元素并输入值，输入操作做扩展
    # def element_value_input(self,method,location,value):
    #     global driver
    #     if method =="x":
    #         self.driver.find_element_by_xpath(location).send_keys(value)
    #     if method =="class":
    #         self.driver.find_element_by_class_name(location).send_keys(value)
    #     if method == "id":
    #         self.driver.find_element_by_id(location).send_keys(value)
    #     if method == "name":
    #         self.driver.find_element_by_name(location).send_keys(value)
    #     if method == "link":
    #         self.driver.find_element_by_link_text(location).send_keys(value)
    #     if method == "tag":
    #         self.driver.find_element_by_tag_name(location).send_keys(value)
    #     if method == "Plink":
    #         self.driver.find_element_by_partial_link_text(location).send_keys(value)
    #     if method == "css":
    #         self.driver.find_element_by_css_selector(location).send_keys(value)
    #发现元素并单击
    def find_element_click(self,method,location):
        if method =="x":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_xpath(location).click()
        if method =="class":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_class_name(location).click()
        if method == "id":
            self.driver.find_element_by_id(location).click()
        if method == "name":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_name(location).click()
        if method == "link":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_link_text(location).click()
        if method == "tag":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_tag_name(location).click()
        if method == "Plink":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_partial_link_text(location).click()
        if method == "css":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_css_selector(location).click()
    # 发现元素，返回文本值
    def find_element_text(self,method,location):
        if method =="x":
            self.driver.implicitly_wait(3)
            text = self.driver.find_element_by_xpath(location).text
            return text
        if method =="class":
            self.driver.implicitly_wait(3)
            text = self.driver.find_element_by_class_name(location).text
            return text
        if method == "id":
            text = self.driver.find_element_by_id(location).text
            return text
        if method == "name":
            self.driver.implicitly_wait(3)
            text = self.driver.find_element_by_name(location).text
            return text
        if method == "link":
            self.driver.implicitly_wait(3)
            text = self.driver.find_element_by_link_text(location).text
            return text
        if method == "tag":
            self.driver.implicitly_wait(3)
            text = self.driver.find_element_by_tag_name(location).text
            return text
        if method == "Plink":
            self.driver.implicitly_wait(3)
            text = self.driver.find_element_by_partial_link_text(location).text
            return text
        if method == "css":
            self.driver.implicitly_wait(3)
            text = self.driver.find_element_by_css_selector(location).text
            return text
    #通过输入框的属性获取属性值
    def find_element_AttributeText(self,method,location,attributeName):
        if method == "x":
            attributeValue = self.driver.find_element_by_xpath(location).get_attribute(attributeName)
            return attributeValue
        if method =="class":
            attributeValue = self.driver.find_element_by_class_name(location).get_attribute(attributeName)
            return attributeValue
        if method == "id":
            attributeValue = self.driver.find_element_by_id(location).get_attribute(attributeName)
            return attributeValue
        if method == "name":
            attributeValue = self.driver.find_element_by_name(location).get_attribute(attributeName)
            return attributeValue
        if method == "link":
            attributeValue = self.driver.find_element_by_link_text(location).get_attribute(attributeName)
            return attributeValue
        if method == "tag":
            attributeValue = self.driver.find_element_by_tag_name(location).get_attribute(attributeName)
            return attributeValue
        if method == "Plink":
            attributeValue = self.driver.find_element_by_partial_link_text(location).get_attribute(attributeName)
            return attributeValue
        if method == "css":
            attributeValue = self.driver.find_element_by_css_selector(location).get_attribute(attributeName)
            return attributeValue
    #发现元素，并输入值
    def find_element_input(self,method,location,value):
        if method =="x":
            # self.driver.find_element_by_xpath(location).clear()
            self.driver.find_element_by_xpath(location).send_keys(value)
        if method =="class":
            self.driver.find_element_by_class_name(location).send_keys(value)
        if method == "id":
            self.driver.find_element_by_id(location).send_keys(value)
        if method == "name":
            self.driver.find_element_by_name(location).send_keys(value)
        if method == "link":
            self.driver.find_element_by_link_text(location).send_keys(value)
        if method == "tag":
            self.driver.find_element_by_tag_name(location).send_keys(value)
        if method == "Plink":
            self.driver.find_element_by_partial_link_text(location).send_keys(value)
        if method == "css":
            # self.driver.find_element_by_css_selector(location).clear()
            self.driver.find_element_by_css_selector(location).send_keys(value)
    #显性等待
    """
    显性等待，
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # 显性等待（2），https://www.cnblogs.com/yoyoketang/p/6517477.html 可参考
    # element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_css_selector(css_path))
    """
    # def dominant_wait(self,method,location):
    #     if method == "x":
    #         element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, location)))
    #         element.click()
    #     if method == "css":
    #         element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, location)))
    #         element.click()
    # # 一直等待某元素可见，默认超时10秒，ui需要import selenium.webdriver.support.ui as ui
    # # def wait_is_visible(self,method,location):
    # #
    # #     isFind = False
    # #     for n in range(0, 20):
    # #         time.sleep(0.5)
    # #         # 如果找个元素，打印内容，同时break跳出循环
    # #         element = None
    # #         if method == "x":
    # #             self.driver.implicitly_wait(3)
    # #             element = self.driver.find_element_by_xpath(location)
    # #         if method == "class":
    # #             self.driver.implicitly_wait(3)
    # #             element = self.driver.find_element_by_class_name(location)
    # #         if method == "id":
    # #             element = self.driver.find_element_by_id(location)
    # #         if method == "name":
    # #             self.driver.implicitly_wait(3)
    # #             element = self.driver.find_element_by_name(location)
    # #         if method == "link":
    # #             self.driver.implicitly_wait(3)
    # #             element = self.driver.find_element_by_link_text(location)
    # #         if method == "tag":
    # #             self.driver.implicitly_wait(3)
    # #             element = self.driver.find_element_by_tag_name(location)
    # #         if method == "Plink":
    # #             self.driver.implicitly_wait(3)
    # #             element = self.driver.find_element_by_partial_link_text(location)
    # #         if method == "css":
    # #             self.driver.implicitly_wait(3)
    # #             element = self.driver.find_element_by_css_selector(location)
    # #
    # #         if element:
    # #             # print "找到了"
    # #             element.click()
    # #             isFind = True
    # #             break
    # #     if isFind != True:
    # #         print "没找到元素"
    # # 一直等待某个元素消失，默认超时10秒
    # def is_not_visible(locator, timeout=10):
    #     try:
    #         ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
    #         return True
    #     except TimeoutException:
    #         return False
    # #句柄的获得
    # def switch_handle(self,value):
    #     try:
    #         if value == "0":
    #             asd = driver.window_handles
    #             driver.switch_to_window(asd[0])
    #         if value == "-1":
    #             # -1就是当前的窗口
    #             qwe = driver.window_handles
    #             driver.switch_to_window(qwe[-1])
    #         if value == "-2":
    #             qwe = driver.window_handles
    #             driver.switch_to_window(qwe[-2])
    #     except IOError:
    #             print "handle值有误！"
    #按一定格式获取当前时间，需要from datetime import datetime
    def deprint(self,content):
        dt = datetime.now()
        print datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')+"："+content
    #按YYYY-MM-DD HH:MM:SS格式获取当前时间，并返回
    def nowtime(self):
        dt = datetime.now()
        time=datetime.strftime(dt,'%Y-%m-%d %H:%M:%S')
        return time
        # print time
    #按一定格式获取当前时间，需要from datetime import datetime
    def printime(self):
        dt = datetime.now()
        strnow = datetime.strftime(dt, '%Y-%m-%d %H_%M_%S')
        return strnow
    def select_value(self,location,value):
        sel = self.driver.find_element_by_xpath(location)
        Select(sel).select_by_value(value)

    #20秒内每间隔0.5秒寻找一次元素，并click
    def wait_is_visible(self, method, location):
        #print  "wait_is_visible"
        isFind = False  #布尔类型
        for n in range(0, 40):  #rang（）数组，从0开始遍历
            # 如果找个元素，打印内容，同时break跳出循环
            # text = '开始执行循环第:' + str((n + 1) * 0.5)
            text = str((n + 1) * 1) +u'秒'
            # self.deprint(text)
            element = None #定义变量，默认的为空
            time.sleep(1)  # 遍历一次就休息1秒
            try:
                if method == "x":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_xpath(location)
                elif method == "class":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_class_name(location)
                elif method == "id":
                    element = self.driver.find_element_by_id(location)
                elif method == "name":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_name(location)
                elif method == "link":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_link_text(location)
                elif method == "tag":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_tag_name(location)
                elif method == "Plink":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_partial_link_text(location)
                elif method == "css":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_css_selector(location)
            except:
                # print "没找到"

                time.sleep(0.5)  # 遍历一次就休息0.5秒
                continue
            if element != None :
                # print "找到了"
                # print element.get_attribute('ng-hide')
                # if element.get_attribute('ng-hide')==True:
                element.click()
                isFind = True
                break
        if isFind != True:
            # print "没找到元素:"+location
            val =u'查找元素:' + location +u'超时:' +text

            self.deprint(val)
        return isFind

    # 20秒内每间隔0.5秒寻找一次元素,并输入value
    def element_value_input(self,method,location,value):
        isFind = False
        for n in range(0, 40):
            # 如果找个元素，打印内容，同时break跳出循环
            # text = '开始执行循环第:' + str((n + 1) * 0.5)
            text = str((n + 1) * 0.5) + u'秒'
            #self.deprint(text)
            time.sleep(1)  # 遍历一次就休息0.5秒
            element = None
            try:
                if method == "x":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_xpath(location)
                if method == "class":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_class_name(location)
                if method == "id":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_id(location)
                if method == "name":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_name(location)
                if method == "link":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_link_text(location)
                if method == "tag":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_tag_name(location)
                if method == "Plink":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_partial_link_text(location)
                if method == "css":
                    self.driver.implicitly_wait(30)
                    element = self.driver.find_element_by_css_selector(location)
            except:
                time.sleep(0.5)  # 遍历一次就休息0.5秒
                continue
            if element:
                # print "找到了"
                element.send_keys(value)
                isFind = True
                break
        if isFind != True:
            return "没找到元素"

    #滚动条
    def scrollbar(self,value):
        self.deprint("开始执行滚动条，请等待")
        time.sleep(1)
        if value == "top":
            js = "var q=document.documentElement.scrollTop=0"
            self.driver.execute_script(js)
        elif value == "bottom":
            js = "var q=document.documentElement.scrollTop=1000000"
            self.driver.execute_script(js)
        else:
            js = "var q=document.documentElement.scrollTop=" + value + ""
            self.driver.execute_script(js)
    # print "滚动条执行完毕"

    #万能验证码
    def verirynumber(self):

        veriry = randint(1000, 9999)  # random.randint(a,b)用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
        print(u"生成的随机数：%d" % veriry)  # %d,整数;%s,表示格化式一个对象为字符

        number = repr(input("请输入随机数：")).decode('utf-8').encode(type)  # repr(): Python 内置函数,函数将对象转化为供解释器读取的形式。
        # Python decode() 方法以 encoding 指定的编码格式解码字符串。默认编码为字符串编码
        # Python encode() 方法以 encoding 指定的编码格式编码字符串。

        number = int(number)

        if number == veriry:
            print (u"登录成功！").decode('utf-8').encode(type)
        elif number == 132741:
            print(u"登录成功！").decode('utf-8').encode(type)
        else:
            print(u"验证码输入有误！")

    # 循环遍历元素获取其文本值
    def for_get_element_text(self,method,location,method2,secondele):
        divele=""
        labeltext=""
        if method=='x':
            divele = self.driver.find_element_by_xpath(location)

        elif method=='id':
            divele = self.driver.find_element_by_id(location)
            # labeltext = divele.find_elements_by_tag_name('label')
        elif method=='class':
            divele = self.driver.find_element_by_class_name(location)
            # labeltext = divele.find_elements_by_tag_name('label')
        elif method=='link':
            divele = self.driver.find_element_by_link_text(
                location)
            # labeltext = divele.find_elements_by_tag_name('label')
        elif method=='Plink':
            divele = self.driver.find_element_by_partial_link_text(
                location)
        time.sleep(5)
        if method2=='x':
            labeltext = divele.find_elements_by_xpath(secondele)
        elif method2=='id':
            labeltext = divele.find_elements_by_id(secondele)
        elif method2=='class':
            labeltext = divele.find_elements_by_class_name(secondele)
        elif method2=='link':
            labeltext = divele.find_elements_by_link_text(secondele)
        elif method2=='tag':
            labeltext = divele.find_elements_by_tag_name(secondele)
        return labeltext

    # 循环获取对应元素并点击
    def for_get_click(self,name,text):
        for i in range(0, len(text)):
            if name == text[i].text:
                text[i].click()
                break
    # 循环获取对应元素文本并返回文本值
    def for_get_text(self,name,spanele):
        time.sleep(3)
        text = ""
        # divele = self.driver.find_element_by_class_name('fans-group-box')
        # spanele = divele.find_elements_by_tag_name('span')
        for i in range(0, len(spanele)):
            if name == spanele[i].text:
                text = spanele[i].text
                break
            else:
                text = "未找到"
        return text
    # 上传图片/文件方法
    def upload_picture_or_file(self,uploadtype,uploadfilexpath,filepath,ljcode,ljname):
        # 说明：con_path：\common\\fileconfig\\file\import.xlsx，请按照此路径填写，替换import.xlsx即可；不要自己更改路径格式，如有更改，可能会影响到后续代码；
        # ljcode:可以用auto3获取，默认使用#32770，如运行不通，在做修改
        # ljname:打开的对话框左上角的名称，一般为u'打开'
        time.sleep(3)
        # 点击上传文件按钮，uploadtype：为类型，x/name/class等；uploadfilexpath：为具体的值
        self.wait_is_visible(uploadtype, uploadfilexpath)
        # 此处必须加休息时间，不加会报错
        time.sleep(3)
        cur_path = os.path.abspath(os.path.dirname(__file__))
        con_path = filepath
        sp_path = os.path.split(os.path.split(cur_path)[0])[0]
        zh_path = eval(repr(sp_path + con_path).replace('\\', "\\"))
        # win32gui
        # dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
        dialog = win32gui.FindWindow(ljcode, ljname)  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, zh_path)  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
if __name__ == '__main__':
    A = BasePage(1)
    A.verirynumber()