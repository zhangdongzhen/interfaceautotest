# -*- coding: utf-8 -*-

from pages.common_pages.base import BasePage
import os
import time
import subprocess

class Detailfile_Page(BasePage):
    # 切换到新开窗口处
    def switch_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到短信任务详情页面
    # 点击上传文件按钮
    def click_input_file_but(self):
        self.wait_is_visible('x', '/html/body/div/div[1]/div[2]/div[4]/div[2]/div/button[1]')  # 点上传文件按钮
    # 上传.xlsx的文件
    #上传文件
    def upload_file_xlsx(self):
        time.sleep(3)
        # 获取上传文件路径
        cur_path = os.path.abspath(os.path.dirname(__file__))
        con_path = "\common\\fileconfig\\file\export_sms.exe"
        print cur_path
        sp_path = os.path.split(os.path.split(os.path.split(cur_path)[0])[0])[0]
        print sp_path
        """
        eval() 函数用来执行一个字符串表达式，并返回表达式的值,参考地址：http://www.runoob.com/python/python-func-eval.html
        repr() 函数将对象转化为供解释器读取的形式，参考地址：http://www.runoob.com/python/python-func-repr.html
        replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次，
                  参考地址：http://www.runoob.com/python/att-string-replace.html
        """
        zh_path = eval(repr(sp_path + con_path).replace('\\', '\\\\'))
        self.deprint(u"上传的文件地址：" + zh_path)
        subprocess.call(zh_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE)  ##路径中有空格的采取此方法。没有空格的可以用os.system
        time.sleep(5)
        self.deprint("上传成功")
        return u"上传成功，校验文件类型成功"
    # 上传文件，上传图片类型
    def upload_picture(self):
        time.sleep(3)
        # 获取上传文件路径
        cur_path = os.path.abspath(os.path.dirname(__file__))
        con_path = "\common\\fileconfig\\file\export_image.exe"
        print cur_path
        sp_path = os.path.split(os.path.split(os.path.split(cur_path)[0])[0])[0]
        print sp_path
        """
        eval() 函数用来执行一个字符串表达式，并返回表达式的值,参考地址：http://www.runoob.com/python/python-func-eval.html
        repr() 函数将对象转化为供解释器读取的形式，参考地址：http://www.runoob.com/python/python-func-repr.html
        replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次，
                  参考地址：http://www.runoob.com/python/att-string-replace.html
        """
        zh_path = eval(repr(sp_path + con_path).replace('\\', '\\\\'))
        self.deprint(u"上传的文件地址：" + zh_path)
        # self.wait_is_visible('x', '/html/body/div/div[1]/div[2]/div[4]/div[2]/div/button[1]')  # 点上传文件按钮
        # """
        # python subprocess模块使用总结,参考地址：https://www.cnblogs.com/lincappu/p/8270709.html
        # """
        subprocess.call(zh_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE)  ##路径中有空格的采取此方法。没有空格的可以用os.system
        time.sleep(5)
        self.deprint("上传成功")
        return u"上传类型不符，校验文件类型成功"

    # 系统提示：文件夹限制了上传文件类型，选择的上传文件类型不符合限制
    def get_tip_content(self):
        time.sleep(10)
        text=self.find_element_text('x','//*[@id="alertCommon"]/div/div/div[2]/div[3]')
        self.wait_is_visible('x','//*[@id="alertCommon"]/div/div/div[3]/button')
        return text
    # 点击限制上传文件上传的确定按钮
    def click_xz_input(self):
        self.wait_is_visible('x','//*[@id="alertCommon"]/div/div/div[3]/button')
    # 开始点击批量上传按钮
    def click_amount_input(self):
        self.wait_is_visible('x','/html/body/div/div[1]/div[2]/div[4]/div[2]/div/button[2]/img')
    # 点击批量上传的上传文件按钮
    def click_amount_upload(self):
        self.wait_is_visible('x','//*[@id="dropbox"]/div[1]/i')
    # 点击上传文件的再次上传处
    def click_upload_again(self):
        self.wait_is_visible('x','//*[@id="dropbox"]')
    # 点击开始上传按钮
    def click_start_upload(self):
        time.sleep(3)
        self.wait_is_visible('x','//*[@id="uploadFile"]/div/div/div[3]/a[1]')
    # 将第二个图片的文件删除
    def delete_picture(self):
        self.wait_is_visible('x','//*[@id="dropbox"]/div[2]/div[2]/span/a')
    # 关闭上传文件的窗口
    def close_upload_win(self):
        self.wait_is_visible('x','//*[@id="uploadFile"]/div/div/div[1]/span/span')
    # 点击文件标题，进入预览页面
    def click_title_to_view(self):
        self.wait_is_visible('x','/html/body/div/div[1]/div[2]/div[6]/table/tbody[2]/tr[1]/td[5]/div/div[1]/span[1]')
        time.sleep(2)
    # 需要先切换到iframe,再获取内部值
    def switch_to_iframes(self):
        iframe = self.driver.find_elements_by_tag_name("iframe")[0]
        self.driver.switch_to_frame(iframe)
        time.sleep(1)
    # 判断文件的第一行和预期是否一致
    def is_ok(self):
        return self.find_element_text('x','//*[@id="A2"]/span')
    # 点击back按钮
    def click_back_but(self):
        self.driver.back()
        self.driver.refresh()
    # 开始筛选并删除
    def start_search(self,name):
        self.find_element_input('x','/html/body/div/div[1]/div[2]/div[4]/div[1]/div[2]/input',name)
    # 选择全选按钮
    def click_all_select(self):
        self.wait_is_visible('x','/html/body/div/div[1]/div[2]/div[6]/table/tfoot/tr/th/div/div[1]/label[1]')
    # 开始删除文件
    def delete_file(self):
        self.wait_is_visible('x','/html/body/div/div[1]/div[2]/div[6]/table/tfoot/tr/th/div/div[2]/a[3]')
    # 在弹出的对话窗中选择取消/确定按钮
    def click_ok_but(self,num):

        self.wait_is_visible('x','//*[@id="deleteFileDialog"]/div/div/div[3]/button['+num+']')
    # 获取到很抱歉，暂时没有数据呀
    def get_final_data(self):
        time.sleep(2)
        return self.find_element_text('x','/html/body/div/div[1]/div[2]/div[6]/div/div/span')