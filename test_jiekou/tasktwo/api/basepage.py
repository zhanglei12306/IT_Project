import requests
class BasePages:


    def __init__(self):
        # 获取token
        corp_id = 'wwd86e8d6fd7ae016d'
        secret = 'KZxjtIppUrUaW488bW-VU6kjkvNh71xJM'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={secret}'
        re = requests.get(url).json()
        self.token = re["access_token"]
        self.request_session = requests.Session()
        self.request_session.params = {'access_token': self.token}

    def send(self, *args, **kwargs):
        return self.request_session.request(*args, **kwargs).json()
