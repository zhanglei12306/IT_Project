import pytest


@pytest.fixture(scope='session')
def ConnectDB():
    print('\n连接数据库操作')
    yield
    print('\n断开数据库操作')