import pytest


def test_one():
    # assert 10 == 100
    # assert False == True
    # assert 600 == 200
    pytest.assume(1 == 2)
    # pytest.assume(False == True)
    pytest.assume(True == True)
    pytest.assume(100 == 200)