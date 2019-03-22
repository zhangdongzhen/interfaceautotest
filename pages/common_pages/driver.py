# -*- coding: utf-8 -*-
import os
from selenium import webdriver
import config
#设置驱动获取浏览器对象
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

g_host=""
g_browserType=""

def brower():

    # type: () -> object
    cur_path = os.path.abspath(os.path.dirname(__file__)) #os.path.basename(path):返回所给路径path的最底层路径名或者是文件名；
    # os.path.dirname(__file__):返回脚本的路径
    root_path = os.path.split(cur_path)[0]  #os.path.split(curPath)[0]:path分割成目录
    root_path = os.path.split(root_path)[0]
    driver_path = root_path + "\common\common_function\chromedriver.exe"


    driver = webdriver.Chrome(driver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()  #放大窗口
    return driver


def setromtedriver(host, browserType):
    global g_host
    global g_browserType
    g_host = host
    g_browserType = browserType


def choose_brower():
    #secret
    #global g_driver
    g_driver = None

    if g_browserType=="chrome":
        g_driver = webdriver.Remote(command_executor=g_host,  #为命令执行器，它用于指定脚本执行的主机及端口。
                                  desired_capabilities=DesiredCapabilities.CHROME)   # desired_capabilities:设计能力。 Desired Capabilities 本质上是keyvalue 的对象，它告诉Selenium Server 脚本执行的基本运行环境
    else:
        g_driver = webdriver.Remote(command_executor=g_host,
                                  desired_capabilities=DesiredCapabilities.FIREFOX)
    return g_driver
if __name__ == '__main__':
    driver = brower()

    # for host, browserType in config.getconfig().items():
    #     print(host)
    #     print(browserType)
    #     setromtedriver(host, browserType)
    #     choose_brower()
    #     driver = brower()
