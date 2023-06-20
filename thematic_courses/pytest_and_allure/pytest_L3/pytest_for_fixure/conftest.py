# -*- coding: utf-8 -*-
# @Time    : 2023/6/20 21:03
# @Author  : yanfa
# @user   : yanfa 
# @File    : conftest.py
# @remark:
import pytest

# 会话层，整个执行过程中只执行一次
# @pytest.fixture(scope="session")
# 自动应用
@pytest.fixture(scope="session",autouse=True)
def login():
    # setup操作
    print("完成登录")
    name='zhangsan'
    token = 'hxxxxxauullnmma'

    yield name,token  # 同return指定返回值,login='hxnmma'
    # teardown操作
    print("完成登出")

@pytest.fixture(scope="session")
def connect_db():
    # setup操作
    print("连接数据库")
    yield
    # teardown操作
    print("断言数据库")