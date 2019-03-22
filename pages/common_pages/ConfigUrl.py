# -*- coding: utf-8 -*-
# import xlrd
class ConfigUrl():
    def BaseUrl(self):
        #  如果是s2系统，，x,y请输入，2，0
        # 如果是uat系统，下，y请输入:0,0
        # tables=xlrd.open_workbook('../../common/common_function/Url.xlsx')
        # cell=tables.sheet_by_name("url")
        # urlvalue=cell.cell(2,0).value
        # print urlvalue
        return "https://s2-tenant.smarket.net.cn"
if __name__ == '__main__':
    ConfigUrl().BaseUrl()
