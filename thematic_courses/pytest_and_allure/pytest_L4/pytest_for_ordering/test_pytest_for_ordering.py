# -*- coding: utf-8 -*-
# @Time    : 2023/6/27 10:05
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_pytest_for_ordering.py
# @remark: 自定义用例执行顺序

""""""
import pytest

"""一、pytest常用插件
1、pip install pytest-ordering 控制用例执行顺序
2、pip install pytest-xdist 分布式并发执行测试用例
3、pip install pytest-dependency 控制用例的依赖关系
4、pip install pytest-rerunfailures 失败重试
5、pip install pytest-assume 多重校验
6、pip install pytest-random-order 用例随机执行
7、pip install pytest-html 测试报告
"""

"""二、pytest执行顺序
场景：
对于集成测试，经常会有上下文依赖关系的测试用例。
比如10个步骤，拆成10条case,这时候能知道到底执行到哪步报错。，
而用例默认执行顺序是自上而下，需要控制执行顺序

解决：
可以通过setup/teardown/fixture来解决，也可以使用对应插件。

安装：pip install pytest-ordering （仓库地址https://github.com/ftobia/pytest-ordering）

用法：
    @pytest.mark.first 对应0,不推荐这种写法
    @pytest.mark.last 对应-1,不推荐这种写法
    @pytest.mark.run(order=0) 对应第一个，推荐这种写法
    @pytest.mark.run(order=2) 对应第三个，推荐这种写法

注意：
    1、多个插件装饰器（>2）的时候，有可能会发生冲突
    2、order支持英文/正整数/负整数，执行优先级：0>较小的正数>较大的正数>无标记>较小的负数>较大的负数
    orders_map = {
    'first': 0,
    'second': 1,
    'third': 2,
    'fourth': 3,
    'fifth': 4,
    'sixth': 5,
    'seventh': 6,
    'eighth': 7,
    'last': -1,
    'second_to_last': -2,
    'third_to_last': -3,
    'fourth_to_last': -4,
    'fifth_to_last': -5,
    'sixth_to_last': -6,
    'seventh_to_last': -7,
    'eighth_to_last': -8,
}
"""
#例子 执行顺序0->2->4->无标记->-4->-2 （0>较小的正数>较大的正数>无标记>较小的负数>较大的负数）
@pytest.mark.run(order=4)
def test_demo1():
    print("4")

@pytest.mark.run(order=2)
def test_demo2():
    print("2")

@pytest.mark.run(order=0)
def test_demo3():
    print("0")

def test_demo4():
    print("无标记")

@pytest.mark.run(order=-4)
def test_demo5():
    print("-4")

@pytest.mark.run(order=-2)
def test_demo6():
    print("-2")


