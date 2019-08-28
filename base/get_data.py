from model_excel import OperateExcel
import data_config
from operate_json import OperetionJson
class GetData:
    def __init__(self):
        self.oper_excel = OperateExcel()
    def get_case_lines(self):
        return self.oper_excel.get_nums()
    def get_is_run(self,row,flag=None):
        col = data_config.get_run()
        run_model = self.oper_excel.get_cell_value(row,col)
        if run_model == "yes":
            flag = True
        else:
            flag = False
        return flag
    def get_run_method(self,row):
        col = data_config.get_request_way()
        vaule_method = self.oper_excel.get_cell_value(row,col)
        return vaule_method
    def get_is_header(self,row):
        col = data_config.get_header()
        value_header = self.oper_excel.get_cell_value(row,col)
        if value_header == "yes":
            return data_config.get_header()
        else:
            return None
    # 获取请求url
    def get_url(self,row):
        col = data_config.get_url()
        value_url = self.oper_excel.get_cell_value(row,col)
        return value_url

    # 获取请求数据
    def get_request_data(self,row):
        col = data_config.get_data()
        value_data = self.oper_excel.get_cell_value(row,col)
        if value_data == "":
            return None
        else:
            return value_data
# 看到7-7节课了!!!
    # 通过关键字拿到data数据
    def get_data_for_json(self,row):
        opera_json = OperetionJson()
        request_data = opera_json.get_data()
        return request_data
    # 获取预期结果
    def get_expect_data(self,row):
        col = data_config.get_except_data()
        exepect_data = self.oper_excel.get_cell_value(row,col)
        if exepect_data == "":
            return None
        return exepect_data