from base.runmethod import RunMethod
from base.get_data import GetData
class RunTest:
    def __init__(self):
        self.runmethod = RunMethod()
        self.data = GetData()
    # 程序执行
    def go_on_run(self):
      rows_count = self.data.get_case_lines()
      for i in range(1,rows_count):
          url = self.data.get_url(i)
          method = self.data.get_run_method(i)
          is_run = self.data.get_is_run(i)
          data = self.data.get_data_for_json()
          header = self.data.get_is_header(i)
          if is_run:
              res = self.runmethod.run_main(method,url,header,data)
      return res
if __name__ == '__main__':
    Run = RunTest()
    Run.go_on_run()
# 看到7-9了

