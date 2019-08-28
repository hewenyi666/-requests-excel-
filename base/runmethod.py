import requests
class RunMethod:
    def get_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,headers=header,data=data).json()
        else:
            res = requests.get(url=url, data=data).json()
        return res
    def post_main(self, url, data, header):
        res = None
        if header != None:
            res = requests.post(url=url,headers=header,data=data).json()
        else:
            res = requests.post(url=url, data=data).json()
        return res
    def run_main(self,method,url,header=None,data=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return res