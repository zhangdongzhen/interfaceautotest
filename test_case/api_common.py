#-*-encoding:utf-8 -*-
"""
@version:1
@author:刘雅
@file:api_common.py,common总入口
@time:2019/1/1015:32
"""
from base_unit import BaseUnit
from pages.api.api_common_all import Api_Common_All
class Api_Common(BaseUnit):
    # HW平台
    def test_0001(self,type):
        Api_Common_All().run_all_common_inter("HW")
    # S2平台
    def test_0002(self):
        Api_Common_All().run_all_common_inter("S2")
    # UAT平台
    def test_0003(self):
        Api_Common_All().run_all_common_inter("UAT")
    # HW_UAT平台
    def test_0004(self):
        Api_Common_All().run_all_common_inter("HW_UAT")
    # HW_UAT平台
    def test_0005(self):
        Api_Common_All().run_all_common_inter("DELL")

if __name__ == '__main__':
    pass
