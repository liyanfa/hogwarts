# -*- coding: utf-8 -*-
# @Time    : 2023/6/8 20:37
# @Author  : yanfa
# @user   : yanfa 
# @File    : pytest_for_exception.py
# @remark: pytest 异常处理

"""常用异常处理方式
1/ try...except
try:
    可能产生异常的代码块
except[(Error1,Error2,...)][as e]]:
    处理异常的代码块1
except[(Error3,Error4,...)][as e]]:
    处理异常的代码块2
except [Exception]
    处理其他异常
    """
# try:
#     a=int(input("输出被除数："))
#     b=int(input("输出除数："))
#     c=a/b
#     print(f"相除结果为：{c}")
# except (ValueError,ArithmeticError):
#     print("程序发生数字格式异常或算数异常")
# except:
#     print("其他异常")
import pytest

"""
2/ pytest.raise()
可以捕获特定的异常
获取捕获的异常的细节，如异常类型，异常信息
发生异常，后面的代码将不会被执行"""

def test_raise():
    with pytest.raises(ValueError,match='must be 0 or None'):
        raise ValueError("must be 0 or None") #执行成功
        # raise ZeroDivisionError("除数为0") #执行失败，因为捕获和抛出的类型不一致

def test_raise1():
    # 同时抛出多个异常
    with pytest.raises((ValueError,ZeroDivisionError)):
        raise ZeroDivisionError("除数为0") #执行成功

def test_raise2():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("value must be 42")
    # 获取异常类型和信息
    assert exc_info.type is ValueError
    assert exc_info.value.args[0]=="value must be 42"