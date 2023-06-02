# -*- coding: utf-8 -*-
# @Time    : 2023/5/31 13:04
# @Author  : yanfa
# @user   : yanfa 
# @File    : g1_pytest_test_framework.py
# @remark: pytest测试框架
"""一、简介：全功能python测试工具，兼容unittest框架，支持三百多种插件，支持简单的单测和复杂的功能测试，
可以结合request进行接口测试，结合selenium/appium实现自动化功能测试，结合allure2集成到jenkins实现持续集成"""
import pytest

"""二、安装
pip install -U pytest
查看版本pytest --version"""

"""三、用例识别和运行
用例编写规范：
1/测试文件以test_开头或以_test结尾
2/测试类以Test开头，不能待__init__方法
3/测试函数以test_开头
4/断言使用assert即可
"""

"""四、运行参数
pytest --help
pytest -v: 打印详细日志信息，一般调试时使用
pytest -s: 控制台输出结果，将print输出，一般调试时使用
pytest -k: 只执行包含某关键字的参数用例，支持 pytest -k "类名/方法名"，也支持逻辑关系 pytest -k "类名 and not 方法名"。注意window是-k后面的字符串参数需要双引号
pytest -m [标记名]: 将运行@pytest.mark.[标记名]下标记的参数用例
pytest -x: 遇到用例失败就停止
pytest --maxfail=[num]: 用例失败个数达到阀值停止运行
"""

"""五、运行模式
1/执行文件或模块 pytest xx.py
2/执行类 pytest xx.py::类名
3/执行方法 pytest xx.py::类名::方法名
"""

"""六、pytest框架结构
执行用例前后会执行setup/teardown完成前后置，按照用例运行级别可以分为以下几类
模块级：（setup_module/teardown_module）在模块始末调用
函数级：（setup_function/teardown__function）在函数始末调用，在类外部
类级：（setup_class/teardown__class）在类始末调用，在类中
方法级：（setup_method/teardown_method）在方法始末调用，在类中
方法级：（setup/teardown）在方法始末调用，在类中
调用顺序：setup_module-》setup_class-》setup_method-》setup-》teardown-》teardown_method-》teardown__class-》teardown_module
见test_module.py
"""

"""七、pytest fixtures
使用pytest.fixture装饰器来装饰一个方法，被装饰的方法名可以做为一个参数传递到参测试方法中。
可以用这种方式来完成测试之前的初始化，也可以返回数据给测试函数。
1/将fixture做为函数参数
通常用setup/teardown进行资源初始化，但是如果有这样一个场景，用例1和3依赖登陆，用例3不依赖登陆，那样就行不通，可以用装饰器功能。
例如在登陆功能加上装饰器@pytest.fixture后，将这个用例方法名以参数形式传到方法里面，这个方法就会先执行登陆，再执行自身的用例步骤，
如果不传者不执行登陆，直接执行已有步骤。
2/指定范围内共享
"""
@pytest.fixture()
def login():
    print("登陆")
    return ('yanfa',123)

@pytest.fixture()
def op():
    print("登陆后的操作")

def test_case1(login,op):
    print(login)
    print("test case1 需要登陆")

def test_case2():
    print("test case2 不需要登陆")

def test_case3(login):
    print(login)
    print("test case3 需要登陆")