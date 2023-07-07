# -*- coding: utf-8 -*-
# @Time    : 2023/6/26 21:04
# @Author  : yanfa
# @user   : yanfa 
# @File    : conftest.py.py
# @remark: 改写hook
from typing import Optional, List

import pytest
import yaml
from _pytest.hookspec import hookspec


def pytest_runtest_setup(item: "Item") -> None:
    print("hook: 前置处理")


def pytest_runtest_call(item: "Item") -> None:
    print("hook: 执行用例")


def pytest_runtest_teardown(item: "Item", nextitem: Optional["Item"]) -> None:
    print("hook: 后置处理")


def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]
) -> None:
    # 参数items是指测试用例集，里面每个代表一个用例item，
    # 每个item有各种参数如name-用例名称、nodeid-用例路径等，可以打debug查看pytest_runtest_teardown,conftest.py
    # 用法1：修改用例编码
    print("hook: 编码处理开始")
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")

        # 用法3：对某个测试用例添加其他逻辑，如添加标签
        if i.name=='test_encode[张三]':
            print("这是测试用例-张三")
    print("hook: 编码处理结束")

    # 用法2：设置执行顺序，如颠倒
    # items.reverse()

# 定义一个命令行参数
def pytest_addoption(parser):
    # group 将下面所有的option都展示在这个group下,
    # 什么是group,pytest -h查看帮助文档中,找到logging：，它下面又有 --log-level=LEVEL，那么这就是一个组

    # 定义一个分组
    mygroup = parser.getgroup("hogwarts")
    # 注册一个命令行参数
    mygroup.addoption(
        '--env',  # 注册一个命令行选项
        default='test',  # 参数默认值
        dest='env',  # 存储的变量，为属性命令，可以使用option对象访问这个值
        help='set your run env'  # 帮助信息，参数的描述信息
    )
    # 注册第二个命令行参数
    mygroup.addoption(
        '--env1',  # 注册一个命令行选项
        default='test1',  # 参数默认值
        dest='env1',  # 存储的变量，为属性命令，可以使用option对象访问这个值
        help='set your run env1'  # 帮助信息，参数的描述信息
    )

# 如何针对传入的不同参数完成不同的逻辑处理
@pytest.fixture(scope='session')
def cmdoption(request):
    # 最简单的或者录入命令行的值
    # return request.config.getoption("--env")
    # 常用，根据env环境标识取对应yml文件的的账号密码进行登录
    myenv=request.config.getoption("--env",default='test')
    if myenv =='online':
        config_path='/Users/yanfa/PycharmProjects/hogwarts/thematic_courses/pytest_and_allure/pytest_L4/pytest_for_plugins/config/online.yml'
    elif myenv=='test':
        config_path = '/Users/yanfa/PycharmProjects/hogwarts/thematic_courses/pytest_and_allure/pytest_L4/pytest_for_plugins/config/test.yml'
    else:
        config_path=""
        print("环境错误")

    # 读取yml文件
    with open(config_path) as f:
        datas=yaml.safe_load(f)
    return myenv,datas
