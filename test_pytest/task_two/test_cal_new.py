import pytest


class TestCalc:

    # 测试add函数
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_add_datas):
        result = None
        try:
            # 调用add函数,返回的结果保存在result里面
            result = get_calc.add(get_add_datas[0], get_add_datas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_add_datas[2]

    # 测试div函数
    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_div_datas):
        result = None
        try:
            # 调用add函数,返回的结果保存在result里面
            result = get_calc.div(get_div_datas[0], get_div_datas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_div_datas[2]

    # 测试sub函数
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_sub_datas):
        result = None
        try:
            # 调用add函数,返回的结果保存在result里面
            result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_sub_datas[2]

    # 测试mul函数
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, get_mul_datas):
        result = None
        try:
            # 调用add函数,返回的结果保存在result里面
            result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_mul_datas[2]

