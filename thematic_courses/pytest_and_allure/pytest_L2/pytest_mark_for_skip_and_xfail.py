# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 20:36
# @Author  : yanfa
# @user   : yanfa 
# @File    : pytest_mark_for_skip_and_xfail.py
# @remark:  pytest设置跳过、预期失败用例

"""
mark.skip mark.xfail是pytest的内置标签，可以处理一些特殊的测试用例，不能成功的测试用例
skip：始终跳过该测试用例
skipif:遇到特定情况跳过该测试用例
xfail:遇到特定情况，产生一个期望失败的输出
"""
import sys

import pytest

"""skip使用场景
1/调试时不想运行这个用例
2/标记无法在某些平台上运行的测试功能
3/在某些版本中执行，其他版本中跳过
4/比如，当前的外部资源不可用时跳过，如数据在数据库，如果数据库连接失败，执行了也会报错。

解决1：添加装饰器
@pytest.mark.skip
@pytest.mark.skip(reason='')
@pytest.mark.skipif(expr,reason='')
"""
@pytest.mark.skip
def test_demo1():
    print("没开发完")

@pytest.mark.skip(reason='代码没实现')
def test_demo2():
    return False

@pytest.mark.skipif(sys.platform=="darwin",reason='为mac系统进行跳过')
def test_demo2():
    return True

"""
解决2：代码中添加跳过代码
pytest.skip(reason)
"""
# def check_login():
#     return False
#
# def test_function():
#     print("start")
#     if not check_login():
#         pytest.skip("还未初始化完毕")
#     print("end")

"""xfail使用场景
与skip类似，预期结果为fail，标记用例为fail,主要是提示作用，可以用于标记有缺陷的用例，修复完成后再去掉该装饰器。
用法：
1/添加装饰器@pytest.mark.xfail
2/代码中执行 pytest.xfail(reason='功能尚未完成')"""
@pytest.mark.xfail
def test_demo3():
    print("xfail方法执行")
    # assert 1 == 2 #标记为XFAIL
    assert 1 == 1 #标记为XPASS


def test_demo4():
    print("start")
    pytest.xfail(reason="功能尚未开始")
    print("测试过程")
    assert 1==1   #1 xfailed in 0.02s