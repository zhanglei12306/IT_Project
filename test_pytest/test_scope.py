import pytest
'''
fixture的作用域 scope的取值:
function 函数或者方法级别都会被调用
class 类级别调用一次   只要类中的方法传入一个方法名ConnectDB就行
module 模块级别调用一次  任意一个类中的方法需要传入一个方法名ConnectDB
session 是多个文件调用一次
'''
# @pytest.fixture(scope='function')
# @pytest.fixture(scope='class')
# @pytest.fixture(scope='module')
# def ConnectDB():
#     print('\n连接数据库操作')
#     yield
#     print('\n断开数据库操作')

class TestOne:

    def test_a(self, ConnectDB):
        print("\n测试用例a")

    def test_b(self):
        print("\n测试用例b")

class TestTwo:

    def test_c(self):
        print("\n测试用例c")

    def test_d(self):
        print("\n测试用例d")
