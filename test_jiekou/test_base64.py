import json
import base64
import requests

class ApiRequests:

    def send(self, data:dict):
        res = requests.request(data['method'], data['url'], headers=data['headers'])
        if data['encoding'] == 'base64':
            return json.loads(base64.b64decode(res.content))
        # 把加密后的相应信息发给第三方服务，让第三方服务解密并返回解密后的信息
        elif data['encoding'] == 'safasfs':
            return requests.post('url', data=res.content)

