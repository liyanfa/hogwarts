# -*- coding: utf-8 -*-
# @Time    : 2023/6/27 10:58
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_pytest_for_xdist.py
# @remark: 分布式并发执行测试用例
""""""
from time import sleep

"""一、pytest并行与分布式执行
场景1：
测试用例1000条，一条执行1分钟，一个测试人员执行需要100分钟。通常我们会用人力成本换取时间成本，加几个一起执行，时间就会缩短，
如果10个人一起执行只需要100分钟，这就是一种分布式场景。
场景2：
假设有一个报名系统，对报名总是统计，数据同时进行修改操作的时候有可能出现问题，需要迷你这种
场景，需要多用户并发请求数据。

解决：
使用分布式并发执行测试用例。分布式插件：pytest-xdist

使用方法：进入pypi.python.org 搜索pytest-xdist 查看官方文档
       安装：pip install pytest-xdist （pip install pytest-xdist[psutil] 要使用psutil检测可用CPU数量，请安装psutil附加）
       执行命令：
                pytest -n auto（pytest将生成与可用CPU数量相等的工作进程，并在它们之间随机分布测试。）
                pytest -n 4 （指定cpu数量）   
注意：
用例多的时候效果明显，多进程并发执行，同时支持allure
"""

"""二、分布式执行测试用例原则
1、用例之间是独立的，不要有依赖关系
2、用例执行没有顺序，随机顺序都能正常执行
3、每个用例都能重复运行，运行结果不会影响其他用例
"""
# 例子：单线程执行【5 passed in 5.04s】  并行执行【5 passed in 1.42s】
def test_demo1():
    sleep(1)
    assert True

def test_demo2():
    sleep(1)
    assert True

def test_demo3():
    sleep(1)
    assert True

def test_demo4():
    sleep(1)
    assert True

def test_demo5():
    sleep(1)
    assert True