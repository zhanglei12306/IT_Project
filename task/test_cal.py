from pythoncode.calculator import Calculator
import pytest
from task.test_getdatas import get_datas
# from task.log import logger

class TestCalc:

    def setup_class(self):
        # 实例化类,生成类的对象
        self.calc = Calculator()
        print("\nCalculator:计算机开始计算")

    def teardown_class(self):
        print("\nCalculator:计算机结束计算")

    def setup_method(self):
        print("\nCalculator:计算开始")

    def teardown_method(self):
        print("\nCalculator:计算结束")

     # 使用参数化
    @pytest.mark.parametrize("a, b, expect", get_datas()[0], ids=get_datas()[4])
    # 测试add函数
    def test_add(self, a, b, expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect
        # logger.WARNING({f"test_add预期结果：{result}"})

    @pytest.mark.parametrize("a, b, expect", get_datas()[1], ids=get_datas()[4])
    # 测试sub函数
    def test_sub(self, a, b, expect):
        # 调用sub函数,返回的结果保存在result里面
        result = self.calc.sub(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect
        # logger.debug({f"预期结果：{result}"})

    @pytest.mark.parametrize("a, b, expect", get_datas()[2], ids=get_datas()[4])
    # 测试mul函数
    def test_mul(self, a, b, expect):
        # 调用mul函数,返回的结果保存在result里面
        result = self.calc.mul(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect
        # logger.debug({f"预期结果：{result}"})

    @pytest.mark.parametrize("a, b, expect", get_datas()[3], ids=get_datas()[4])
    # 测试div函数
    def test_div(self, a, b, expect):
        # 调用div函数,返回的结果保存在result里面
        result = self.calc.div(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect
        # logger.debug({f"预期结果：{result}"})

if __name__ == '__main__':
    pytest.main()
