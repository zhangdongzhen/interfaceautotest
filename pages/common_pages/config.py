# -*- coding: utf-8 -*-
#配置文件代码：
def getconfig():

    #    d = {"http://192.168.109.1:5555/wd/hub": "chrome",
    #      "http://192.168.109.1:5556/wd/hub": "firefox"}
    # return d


    d = {"http://110.249.213.74:5901/wd/hub": "chrome"}
    return d
# 获取接口的地址
def getInterAddress():
    return "../../common/fileconfig/file/plants_all.xlsx"
# 获取接口的地址
def getWriteAddress():
    return "../../common/fileconfig/file/plants_all_write.xlsx"
# 获取对应的index值
def get_Sheet_index(sheet_name):
    if sheet_name=="HW":
        return 0
    elif sheet_name=="DELL":
        return 1
    elif sheet_name=="HW_UAT":
        return 2
    elif sheet_name=="UAT":
        return 3
    else:
        return 4
# 获取第一个sheet页值
def getSheet_One_Name():
    return "common"
# 获取excel中行和列
def get_row_col_one():
    return 1,1
