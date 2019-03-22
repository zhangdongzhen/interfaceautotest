#-*-encoding:utf-8 -*-
import unittest
import time
from common.report import report
# from test import test_support
from common.mail import email_send
class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def clear(self):
        pass

    def getTest(self, arg1, arg2):  # 定义的函数，最终生成的测试用例的执行方法
        self.type=arg1
        print "type:",self.type
        StartTime = time.time()  # time()：返回当前时间的时间戳（1970纪元后经过的浮点秒数），需要import time
        suite = unittest.TestSuite()  # 创建一个测试集合
        # suite = Suit()  # 创建一个测试集合

        # 线上会
        webinar_test = self.Def_List(MyTestCase)  # Def_List 获取指定单元测试中，测试函数列表
        for webinar_tmp in webinar_test:
            suite.addTest(MyTestCase(webinar_tmp))
            # 测试
        # 创建测试报告
        AddSuite = report.AllReport()  # AddSuite = report.AllReport() :实例化AllReport类
        AddSuite.onlyneed_suite(suite)  # onlyneed_suite(suite) ：指定suit的report

        # 发送邮件
        EndTime = time.time()
        PerformTime = EndTime - StartTime
        content = "autoTest"
        SendEmail = email_send.SendEmailModel()  # 实例化SendEmailModel类
        SendEmail.postreport_only(PerformTime, str(content))  # 调用SendEmailModel类中postreport_only方法
    def test_0001(self):
        print "type:",self.type
        print "test_0001"
    def test_0002(self):
        print "type:", self.type
        print "test_0002"
    def test_0003(self):
        print "type:", self.type
        print "test_0003"
    def test_0004(self):
        print "type:", self.type
        print "test_0004"
    def Def_List(self, class_name):  # def_list 获取单元测试中，测试函数列表， #class的名字，不用双引号，直接用

        list = []
        def_name = dir(class_name)  # dir():返回当前范围内的变量、方法和定义的类型列表
        for tmp in def_name:
            def_four = str(tmp)[:4]  # str(tmp)[:4] :索引和切片，从下标为0的元素选择到下标为3的元素，不包括下标4的元素
            if def_four == "test":  # 取方法前四个字母为test的
                list.append(tmp)  # append() 方法向列表的尾部添加一个新的元素。只接受一个参数
        return list

    @staticmethod
    def getTestFunc(arg1, arg2):
        def func(self):
            self.getTest(arg1, arg2)
        return func


def __generateTestCases():
    arglists = [('s2', 's2'), ('uat', 'uat'), ('dell', 'dell'), ('hw', 'hw'), ('hw_uat', 'hw_uat')]
    for args in arglists:
        setattr(MyTestCase, 'test_func_%s_%s' % (args[0], args[1]),
                MyTestCase.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()
if __name__ == '__main__':
    # test_support.run_unittest(MyTestCase)
    unittest.main()
