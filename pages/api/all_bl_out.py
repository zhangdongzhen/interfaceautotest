#-*-encoding:utf-8 -*-
"""
@version:1
@author:刘雅
@file:取出全部变量类
@time:2019/1/3117:58
"""
# 从common_config表中读取数据
from common.common_function.Read_From_Mysql import Read_From_Mysql
global a
a="emial"
def get_all_bl(type):

    list={}
    # 获取common_config表中的变量
    common_config_sql="select Variable_name,Variable_value from common_config where platform_name='"+type+"';"
    # 获取common_savebl表中的变量
    common_savebl_sql = "select Variable_name,Variable_value from common_savebl where platform_name='" + type + "';"
    # 获取moreplatform_domain表中的变量
    moreplatform_domain_sql="select platform_name,domain from moreplatform_domain where platform_name like '%"+type+"%';"
    print "moreplatform_domain_sql：",moreplatform_domain_sql
    list1 = Read_From_Mysql().Select_Datas_From_User(common_config_sql)
    list2 = Read_From_Mysql().Select_Datas_From_User(common_savebl_sql)
    list3 = Read_From_Mysql().Select_Datas_From_User(moreplatform_domain_sql)
    # 将3个元祖的值都放到一个字典list中
    for i in range(0,len(list1)):
        list[list1[i][0]] = list1[i][1]
    for i in range(0,len(list2)):
        list[list2[i][0]] = list2[i][1]
    for i in range(0, len(list3)):
        list[list3[i][0]] = list3[i][1]
    return list