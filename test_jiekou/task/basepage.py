import requests
class BasePage:
    def test_token(self):
        # 获取token
        corp_id = 'wwd96e7d6fd6ae016d'
        secret = 'KZxjtIppUrUaW488bW_LOD6RGPG8-VU6kjkvNh71xJM'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={secret}'
        re = requests.get(url)
        if re.json()['errmsg'] == 'ok':
            self.token = re.json()['access_token']
            return self.token
        else:
            print('获取token失败')