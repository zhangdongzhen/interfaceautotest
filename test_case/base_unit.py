# -*- coding: utf-8 -*-
#基础单元测试
#完成每个子单元测试需要做的事情
import unittest
from pages.common_pages.driver import brower
from pages.common_pages.base import BasePage
# import cProfile
class BaseUnit(unittest.TestCase):

    #setUp()方法用于测试用例执行前的初始化工作。
    def setUp(self):
        # 性能监控：测试用例执行时间
        # global cp,driver
        # cp = cProfile.Profile()
        # cp.enable()
        self.driver = brower()

    #tearDown()方法与setUp()相呼应，用于测试用例执行之后的善后工作
    def tearDown(self):
        # 性能监控：测试用例执行时间
        BasePage(self.driver).quit()
        # cp.disable()
        # cp.print_stats()


    # def setDown(self):
    #     cp.disable()
    #     cp.print_stats()
    #     self.driver.quit()
