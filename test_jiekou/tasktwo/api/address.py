
import requests
from test_jiekou.tasktwo.api.basepage import BasePages



class Address(BasePages):

    def add_member(self, body, *args):
        # 创建成员
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        # return requests.post(url, json=body).json()
        return self.send('post', url, json=body)
        # print(re.json())
        # assert re.json()['errmsg'] == 'created'


    def serch_member(self, user_id, *args):
        # 读取成员
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={user_id}'
        # return requests.get(url).json()
        return self.send('get', url)
        # assert re.json()['errmsg'] == 'ok'


    def update_member(self, body, *args):
        # 更新成员
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        # return requests.post(url, json=body).json()
        return self.send('post', url, json=body)
        # assert re.json()['errmsg'] == 'updated'


    def delete_member(self, user_id, *args):
        # 删除成员
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={user_id}'
        # return requests.post(url).json()
        return self.send('get', url)
        # assert re.json()['errmsg'] == 'deleted'
