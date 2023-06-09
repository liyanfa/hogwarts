# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 21:21
# @Author  : yanfa
# @user   : yanfa 
# @File    : pytest_for_mark.py
# @remark: mark：标记测试用例
"""
场景：只执行符合要求的一部分用例
解决：在测试方法上加@pytest.mark.标签名
执行：-m 执行自定义标记的相关用例
pytest -s test_xx.py -m=webtest
pytest -s test_xx.py -m webtest
pytest -s test_xx.py -m "not ios"

注意：使用pytest.ini进行注册
"""
import pytest


def double(a):
    return a*2

# 下面使用内置关键字会警告，需要使用pytest.ini中markers进行注册
@pytest.mark.float
def test_float():
    print("test double float")
    assert 0.2==double(0.1)

@pytest.mark.int
def test_float():
    print("test double int")
    assert 2==double(1)

@pytest.mark.str
def test_float():
    print("test double str")
    assert 'aa'==double('a')