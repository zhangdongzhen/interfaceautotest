# -*- coding: utf-8 -*-
from test_case.api_all_Interface import ParametrizedTestCase
import unittest
global s2_success,s2_fail
class TestOne(ParametrizedTestCase):
    def test_something(self):
        s2_success=0
        s2_fail=0
        self.s2_success=s2_success
        self.s2_fail = s2_fail
        self.yaya_0003()


    # def test_something_else(self):
    #     print 'param =', self.param
    #     self.assertEqual(2, 2)
    def yaya_0003(self):
        print self.param
        if self.param=='hw':
            print 'param =hw'
            # self.assertEqual(3,3)
            self.hw_001()
        elif self.param=='dell':
            self.dell_001()
        elif self.param=='hw_uat':
            self.hw_uat_001()
        else:
            print "走到了这里"
            self.s2_001()
            self.s2_002()
            print "self.success:",self.s2_success
    def hw_001(self):
        print "hw_001"
    def hw_uat_001(self):
        print "hw_uat_001"
    def dell_001(self):
        print "dell_001"
    def uat_001(self):
        print "uat_001"
    def s2_001(self):
        print "s2_001"
        self.s2_success=self.s2_success+1
    def s2_002(self):
        print "s2_001"
        self.s2_success=self.s2_success+1


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(TestOne, param='s2'))
    suite.addTest(ParametrizedTestCase.parametrize(TestOne, param='hw'))
    suite.addTest(ParametrizedTestCase.parametrize(TestOne, param='hw_uat'))
    # suite.addTest(ParametrizedTestCase.parametrize(TestOne, param='uat'))
    suite.addTest(ParametrizedTestCase.parametrize(TestOne, param='dell'))
    unittest.TextTestRunner(verbosity=1).run(suite)


