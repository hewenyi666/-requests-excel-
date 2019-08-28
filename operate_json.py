import json
class OperetionJson:
    # def __init__(self):
    #     self.value_data = read_data()
    def read_data(self):
        with open("data_json.json",'r') as fp:
            json_data = json.load(fp)
        return json_data
    def get_data(self,id):
        value_data = self.read_data()
        return value_data[id]
if __name__ == '__main__':
    print(OperetionJson().get_data('age'))