

import pytest


@pytest.fixture(params=[1, 2, 3], ids=['r1', 'r2', 'r3'])
def login_one(request):
    data = request.param
    print("\n获取测试数据")
    return data + 4

def test_caseone(login_one):
    # print(login_one)
    print(f"\n测试用例{login_one}")