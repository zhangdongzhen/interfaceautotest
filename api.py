#encoding=utf-8
from flask import Flask
from flask import  request, json, jsonify
from common.common_function import sql_config
from common.common_function import Bl_value
from common.common_function.Read_From_Mysql import Read_From_Mysql
from flask_cors import *
from inter_auto_test_control import ConrollerShowInter
api = Flask(__name__)
CORS(api, supports_credentials=True)

#执行测试用例
#格式是
# caseparams = {'File_Test': ['test_001_file_creat'],
#               'Questionnaire': ['test_004_create_questionnaire']}
@api.route("/v1.0/postman/exec_intercase", methods=['post'])
def exec_interautotest():
    data = request.data
    data = json.loads(data)
    # caseparams = {'File_Test':['test_001_file_creat'],
    #               'Questionnaire':['test_004_create_questionnaire']}
    A = ConrollerShowInter()
    A.SupportTool_Control_inter(data['execUser'],data['platname'])
    return '1'

# #查询所有用例和所属模块
# @api.route("/v1.0/ui/list_testcase", methods=['get'])
# def list_testcase():
#     db = DbHelper()
#     results = db.select_case()
#     return jsonify(results)
#
# #新增用例
# @api.route("/v1.0/ui/add_testcase", methods=['get'])
# def add_testcase():
#     # data = request.data
#     # data = json.loads(data)
#     data = {'casename':'aa','scriptname':'bb','moduleid':1}
#     db = DbHelper()
#     id = db.add_case(data['casename'], data['scriptname'], data['moduleid'])
#     return str(id)
#
# #删除用例
# @api.route("/v1.0/ui/del_testcase", methods=['get'])
# def del_testcase():
#     # data = request.data
#     # data = json.loads(data)
#     data = {'id': 45}
#     db = DbHelper()
#     result = db.del_case(data['id'])
#     return str(result)
#
#
#查询所有执行结果
@api.route("/v1.0/postman/resultList", methods=['get'])
def list_execResult():
    start = request.args.get('start', 0)
    num = request.args.get('num', 10)
    db = Read_From_Mysql()

    results = db.select_datas_by_page(start,num)

    print results
    return jsonify(results)

#查询所有失败的日志
@api.route("/v1.0/postman/errorlog", methods=['get'])
def list_errorlog():
    serialnum = request.args.get('serialnum', '0')
    print serialnum
    start = request.args.get('start', 0)
    num = request.args.get('num', 10)
    db = Read_From_Mysql()

    results = db.Select_Datas_From_table(serialnum,start,num)

    print results
    return jsonify(results)



if __name__ == '__main__':
    api.run(threaded=True, port=5000, host='0.0.0.0')