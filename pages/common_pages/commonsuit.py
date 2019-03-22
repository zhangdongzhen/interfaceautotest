# -*- coding: utf-8 -*-
import unittest
import time
import sys


__unittest = True

class Suit(unittest.TestSuite):
    def run(self, result, debug=False):
        failcount = 3  # 失败总运行次数
        class_num = 1
        topLevel = False
        if getattr(result, '_testRunEntered', False) is False:
            result._testRunEntered = topLevel = True

        for test in self:
            case_num = 1
            if result.shouldStop:
                break

            success_flag = True
            while success_flag:
                if _isnotsuite(test):
                    self._tearDownPreviousClass(test, result)
                    self._handleModuleFixture(test, result)
                    self._handleClassSetUp(test, result)
                    result._previousTestClass = test.__class__
                    if (getattr(test.__class__, '_classSetupFailed', False) or
                            getattr(result, '_moduleSetUpFailed', False)):
                        if class_num > failcount:
                            success_flag = False
                        else:
                            time.sleep(5)
                            result._previousTestClass = None
                            print u'类%s第%s次重新初始化执行' % (test.__class__, class_num)
                            class_num += 1
                        continue

                if not debug:
                    test(result)
                else:
                    test.debug()

                if result.result[-1][0] == 1 or result.result[-1][0] == 2:  # 结果为fail和err用例判断
                    if case_num > failcount:
                        success_flag = False
                    else:
                        print u'用例%s第%s次重新执行' % (test, case_num)
                        case_num += 1
                else:
                    success_flag = False

        if topLevel:
            self._tearDownPreviousClass(None, result)
            self._handleModuleTearDown(result)
            result._testRunEntered = False
        return result

def _isnotsuite(test):
    "A crude way to tell apart testcases and suites with duck-typing"
    try:
        iter(test)
    except TypeError:
        return True
    return False