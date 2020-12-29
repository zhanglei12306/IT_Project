import pytest

# 控制哦用力的执行顺序
# @pytest.mark.run(order=2)
# @pytest.mark.second
def test_foo():
    assert True

# @pytest.mark.run(order=1)
# @pytest.mark.first
def test_bar():
    assert True

def test_foo3():
    assert True

def test_bar4():
    assert True