# -*- coding: utf-8 -*-
'''
Created on 2018-07-13
@author: 尤梅枝
'''
import unittest
import HTMLTestRunnerCN
import time
import os

def run():
    suit=unittest.TestSuite(规划规范和对方过后2333顶顶顶顶)
    # 定义测试文件的查找路径
    test_dir= "D:\SmarketAutoTest\\test_case"
    # 定义discover获取文件路径下的所有test用例
    discove=unittest.defaultTestLoader.discover(test_dir,pattern='*case.py',top_level_dir=None)
    # 将所有要执行的测试用例放入suit
    for test_suite in discove:
        for test_case in test_suite:
            suit.addTests(test_case)
            # print suit
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    curPath = os.path.abspath(os.path.dirname(__file__))
    # print curPath
    myfile_path = curPath + "\\common\\report\\reportlog\\"
    #定义生成的报告路径和报告名
    myfile = myfile_path+now+"Smarket3.0_TestReport.html"
    fp = open(myfile, 'wb')
    # 运行套件中的所有用例
    runner=HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u"Smarket3.0自动化测试报告"
    )
    runner.run(suit)
    return suit


if __name__ == "__main__":
    runtest=run()
    # print runtest