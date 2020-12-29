from test_pytest.pythoncode.calculator import Calculator
import os.path
import yaml
import pytest

path = os.path.dirname(__file__) + "/task_new.yml"
with open(path) as f:
    datas = yaml.safe_load(f)
    # 获取文件中key为datas的数据
    add_datas = datas["datas"]
    # sub_datas = datas["sub"]
    # mul_datas = datas["mul"]
    # div_datas = datas["div"]
    # 获取文件中key为myids的数据
    add_ids = datas["myids"]


@pytest.fixture(scope='class')
def get_calc():
    print('\n获取计算器实例')
    calc = Calculator()
    return calc

@pytest.fixture(params=add_datas, ids=add_ids)
def get_datas(request):
    print("\n开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("\n结束计算")