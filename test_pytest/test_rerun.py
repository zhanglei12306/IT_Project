from time import sleep
import pytest

# 要重新运行所有测试失败，请使用--reruns命令行选项，并指定要运行测试的最大次数，使用--reruns-delay命令行选项，其中包含您希望在下一次测试重试开始之前等待的秒数
@pytest.mark.flaky(reruns=5, reruns_deley=1)
def test_rerun_one():
    sleep(0.5)
    assert 1 == 2

def test_rerun_two():
    sleep(0.5)
    assert 2 == 2

def test_rerun_three():
    sleep(0.5)
    assert 3 == 2