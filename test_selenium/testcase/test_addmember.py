import os

import pytest
import yaml

from test_selenium.page.main_page import MainPage

def get_data():
    path = os.path.dirname(__file__) + "/task_data.yml"
    with open(path, encoding='UTF-8') as f:
        datas = yaml.safe_load(f)
        # 获取文件中key为datas的数据
        add_datas = datas["adds"]
        return add_datas


class TestAddMember:
    def setup_class(self):
        # 实例化 MainPage类
        self.main = MainPage()

    def teardown_class(self):
        pass

    # 添加人员
    @pytest.mark.parametrize('name, acctid, phone', get_data())
    def test_add_members(self, name, acctid, phone):
        result = self.main.goto_cntacts().add_members(name, acctid, phone).get_list()
        assert '18272673585' in result

    def test_add_members_fail(self):
        result = self.main.goto_cntacts().add_members_fail('15565050138').get_list()
        assert '15565050138' in result

    # 添加部门
    def test_add_department(self):
        result = self.main.goto_cntacts_department().add_departments().add_department().get_list_department()
        assert '销售部' in result