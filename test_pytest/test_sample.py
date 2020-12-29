def inc(x):
    return x + 1


def test_answer():
    # pytest -vs 文件名(s是带控制台输出结果，也是输出详细)
    print('这是第一条')
    # pytest - V(最高级别信息 - -verbose) 打印详细运行日志信息
    assert inc(3) == 4

def test_demo():
    # pytest -vs 文件名(s是带控制台输出结果，也是输出详细)
    print('这是第二条')
    # pytest - V(最高级别信息 - -verbose) 打印详细运行日志信息
    assert inc(3) == 4

def test_fun():
    # pytest -vs 文件名(s是带控制台输出结果，也是输出详细)
    print('这是第三条')
    # pytest - V(最高级别信息 - -verbose) 打印详细运行日志信息
    assert inc(3) == 4