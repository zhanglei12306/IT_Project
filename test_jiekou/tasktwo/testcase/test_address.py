import pytest

from test_jiekou.tasktwo.api.address import Address
from test_jiekou.tasktwo.testcase.tes_datas import get_datas


class TestAddress:
    def setup(self):
        self.assress = Address()

    @pytest.mark.parametrize("body", get_datas()[3])
    def test_add_menbers(self, body):
        # 数据清理
        self.assress.delete_member(body['userid'])

        # 创建成员
        re = self.assress.add_member(body)
        print(re)
        assert re['errmsg'] == 'created'
        # 查询成员
        re = self.assress.serch_member(body['userid'])
        print(re)
        # assert re['errmsg'] == 'ok'
        assert re['name'] == body['name']

    @pytest.mark.parametrize('body', get_datas()[1])
    def test_update_menbers(self, body):
        # 查询成员
        re = self.assress.serch_member(body['userid'])
        print(re)
        assert re['errmsg'] == 'ok'
        # 更新成员
        re = self.assress.update_member(body)
        print(re)
        assert re['errmsg'] == 'updated'
        # 查询成员
        re = self.assress.serch_member(body['userid'])
        print(re)
        assert re['name'] == body['name']

