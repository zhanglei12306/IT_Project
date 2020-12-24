import pytest
def add_fun(a, b):
    return a + b + 10

# @pytest.mark.parametrize("参数名",列表数据)
# 参数名：作为测试用例的参数. 字符串格式，多个参数中间用逗号隔开。
# 列表数据：一组测试数据。list格式，多组数据用元组类型，
# list的每个元素都是一个元组，元组里的每个元素和按参数顺序一一对应。
# 可以添加ids参数指定用例说明(别名)

# @pytest.mark.parametrize("a, b, expected", [(1, 1, 12),(-1 ,-2 ,7),(1000, 1000 ,2010)], ids=["one", "two", "three"])
# def test_add(a, b, expected):
#     assert add_fun(a, b) == expected

#  参数可以组合堆叠使用,这样生成9条用例
# @pytest.mark.parametrize("a", [0, 1, 3], ids=["a", "b", "c"])
# @pytest.mark.parametrize("b", [2, 3, 6], ids=["aa", "bb", "cc"])
# def test_foo(a, b):
#     print(f"测试参数堆叠组合:a->{a},b->{b}" )