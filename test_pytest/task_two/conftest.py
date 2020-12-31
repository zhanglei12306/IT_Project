from test_pytest.pythoncode.calculator import Calculator
import os.path
import yaml
import pytest

path = os.path.dirname(__file__) + "/task_new.yml"
with open(path) as f:
    datas = yaml.safe_load(f)
    # 获取文件中key为datas的数据
    add_datas = datas["datas"]
    sub_datas = datas["sub"]
    mul_datas = datas["mul"]
    div_datas = datas["div"]
    # 获取文件中key为myids的数据
    add_ids = datas["myids"]


@pytest.fixture(scope='class')
def get_calc():
    print('\n获取计算器实例')
    calc = Calculator()
    return calc

# scope为作用域  params为参数列表
@pytest.fixture(params=add_datas, scope='module', ids=add_ids)
def get_add_datas(request):
    print("\n开始计算")
    print(f"\nrequest.param的测试数据是：{request.param}")
    yield request.param
    print("\n结束计算")

@pytest.fixture(params=sub_datas, scope='module', ids=add_ids)
def get_sub_datas(request):
    print("\n开始计算")
    print(f"\nrequest.param的测试数据是：{request.param}")
    yield request.param
    print("\n结束计算")

@pytest.fixture(params=mul_datas, scope='module', ids=add_ids)
def get_mul_datas(request):
    print("\n开始计算")
    print(f"\nrequest.param的测试数据是：{request.param}")
    yield request.param
    print("\n结束计算")

@pytest.fixture(params=div_datas, scope='module', ids=add_ids)
def get_div_datas(request):
    print("\n开始计算")
    print(f"\nrequest.param的测试数据是：{request.param}")
    yield request.param
    print("\n结束计算")