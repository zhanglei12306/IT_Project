import os

import pytest
import yaml

from test_app.tasktwo.page.app import App

def get_data():
    path = os.path.dirname(__file__) + "/task_add_menbers.yml"
    with open(path, encoding='UTF-8') as f:
        datas = yaml.safe_load(f)
        print(datas)
        # 获取文件中key为datas的数据
        add_datas = datas["adds"]
        print(add_datas)
        return add_datas

class TestContacts:
    def setup(self):
        self.app = App()
        self.app.start()
        self.main = self.app.goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name, gender, phone", get_data())
    def test_contact(self, name, gender, phone):
        toast = self.main.goto_contacts().add_member().add_menmebere_info().edit_name(name).edit_gender(gender).edit_phone(phone).click_save().goto_toast()
        assert toast == '添加成功'

