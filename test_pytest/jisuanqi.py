def jisuanqi(a, b, c):
    if c == '+':
        rte = a + b
    elif c == '-':
        rte = a - b
    elif c == '*':
        rte= a * b
    elif c == '/':
        rte = a / b
    else:
        print('升级')
    # print('%d %s %d = %d' % (a, c, b, rte))
    return rte


def jisuanqi2():
    a = int(input('请输入数字:'))
    b = int(input('请输入数字:'))
    c = input('运算符号:')
    q = jisuanqi(a, b, c)
    w = jisuanqi1(q)
    print(q)
    print(w)
jisuanqi2()