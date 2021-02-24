import requests
class BasePage:
    def test_token(self):
        # 获取token
        corp_id = 'wwd'
        secret = 'KZxjtI'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={secret}'
        re = requests.get(url)
        if re.json()['errmsg'] == 'ok':
            self.token = re.json()['access_token']
            return self.token
        else:
            print('获取token失败')