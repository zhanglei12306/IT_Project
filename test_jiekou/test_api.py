import requests

class Api:
    data = {
        'method':'get',
        'url':'http://baidu:9999/demo.txt',
        'headers':None,
        'encoding':'base64'
    }
    def send(self, data:dict):
        # 替换
        data['url'] = str(data['url']).replace('baidu', '127.0.0.1')
        re = requests.request(method=data['method'], url=data['url'], headerd=data['headers'])