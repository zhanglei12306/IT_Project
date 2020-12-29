import pytest

# 详细的执行过程 pytest test_fixture.py -vs --setup-show
# fixture 是 pytest 的一个外壳函数，可以模拟setup和teardown的操作
# yield 之前的操作相当于 setup，yield 之后的操作相当于teardown
# yield 相当于 return，如果需要返回数据的话，直接放在 yield 后面
# 创建登录的方法
# 如果需要提前登录 传入登录的方法名  fixture相等于setup
# autouse=True 全部的方法都会执行login方法
@pytest.fixture()
def login():
    print('\n登录操作')
    print('\n登录操作后获取token')
    usrname = 'tom'
    password = '123456'
    token = '79456'
    yield [usrname, password, token]              # 相当于teardown
    print('\n退出登录操作')

# def test_case_one(login):
def test_case_one():
    # 直接放入登录方法名  即可获取数据
    print(f'获取登录数据：{login}')
    print('需要提前登录：测试案例一')

def test_case_two(ConnectDB):
    print('不需要提前登录：测试案例二')

# def test_case_three(login):
def test_case_three(ConnectDB):
    print('需要提前登录：测试案例三')

# usefixtures 方法直接传入登录的方法名 也可以实现
# @pytest.mark.usefixtures('login')
def test_case_four():
    print('需要提前登录：测试案例四')