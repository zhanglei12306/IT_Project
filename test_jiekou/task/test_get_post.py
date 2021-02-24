import pytest
import requests
from test_jiekou.task.basepage import BasePage
from test_jiekou.task.tes_datas import get_datas



class TestApiCase:

    def setup_class(self):
        # 实例化类,生成类的对象
        self.token = BasePage().test_token()
        print("\n:get和 post实现通讯录的增删改查功能开始")

    def teardown_class(self):
        print("\n:get和 post实现通讯录的增删改查功能结束")

    @pytest.mark.parametrize("body", get_datas()[3])
    def test_create(self, body):
        # 创建成员
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        re = requests.post(url, json=body)
        print(re.json())
        assert re.json()['errmsg'] == 'created'

    @pytest.mark.parametrize("user_id", get_datas()[2])
    def test_delete(self, user_id):
        # 删除成员
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={user_id}'
        re = requests.post(url)
        assert re.json()['errmsg'] == 'deleted'

    @pytest.mark.parametrize('body', get_datas()[1])
    def test_update(self, body):
        # 更新成员
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        re = requests.post(url, json=body)
        assert re.json()['errmsg'] == 'updated'

    @pytest.mark.parametrize("user_id", get_datas()[0])
    def test_read_members(self, user_id):
        # 读取成员
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}'
        re = requests.get(url)
        assert re.json()['errmsg'] == 'ok'
if __name__ == '__main__':
    pytest.main()