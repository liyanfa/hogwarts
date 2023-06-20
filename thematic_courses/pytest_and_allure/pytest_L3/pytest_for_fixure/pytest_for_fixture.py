# -*- coding: utf-8 -*-
# @Time    : 2023/6/19 21:04
# @Author  : yanfa
# @user   : yanfa 
# @File    : pytest_for_fixture.py
# @remark: 测试用例全生命周期管理-fixture

""""""
import pytest

"""一、fixture用法
fixture特点及优势
1/命令灵活：对于setup/teardown可以不起这2个名字
2/数据共享：在conftest.py配置里写方法可以实现数据共享，不需要import导入，可以跨文件共享
3/scope的层次及神奇的yield组合相当于各种setup和teardown
4/实现参数化"""

"""1、fixture在自动化中的应用-基本用法
场景：测试用例执行时，有的用例需要登录才能执行，有的不需要。setup和teardown无法满足，fixture可以。默认scope范围为function
步骤：
1/导入pytest
2/在登录函数上加@pytest.fixture()
3/在要使用的测试方法中传入（登录函数名称），就先登录
4/不传入的就不登录直接执行测试方法"""

# 1.传统 写法冗余
# def login():
#     print("登录")
#
# def test_search():
#     print("搜索")
#
# def test_cart():
#     login()
#     print("购物车")
#
# def test_order():
#     login()
#     print("下单")

# 2.fixture 灵活 尽量避免test开头，以免与测试用例混淆
# @pytest.fixture()
# def login():
#     print("登录")
#
# def test_search():
#     print("搜索")
#
# # 函数名字作为参数传入
# def test_cart(login):
#     print("购物车")
#
# def test_order(login):
#     print("下单")

"""2、fixture在自动化中的应用-作用域
取值          范围      说明
function    函数级     每一个函数或方法都会调用,默认函数级别
class       类级       每个测试类只执行一次
module      模块级     每一个.py文件调用一次
package     包级       每一个python包只调用一次-暂不支持
session     会话级      每次会话只需要运行一次，会话内所有方法/类/模块都共享这个方法
"""
# 如果设置为会话级别，那么整体只会执行一次登录
# @pytest.fixture(scope="session")
# 如果设置为模块级别，那么整体只会执行一次登录
# @pytest.fixture(scope="module")
# 如果设置为类级别，那么TestDemo只会执行一次登录
# @pytest.fixture(scope="class")
# 如果设置为函数级别，所有函数包括TestDemo下的都会执行登录
# @pytest.fixture(scope="function")
# def login():
#     print("完成登录")
#
# def test_search():
#     print("搜索")
#
# # 函数名字作为参数传入
# def test_cart(login):
#     print("购物车")
#
# def test_order(login):
#     print("下单")
#
# class TestDemo:
#     def test_demo1(self,login):
#         print("case1")
#     def test_demo2(self,login):
#         print("case2")

"""3、fixture在自动化中的应用-yield关键字
场景：
你已经可以将测试方法前要执行的或依赖的解决了，测试方法之后销毁清除数据要如何进行呢？

解决：
通过在fixture函数中加入yield关键字，yield是调用第一次返回结果，第二次执行它后面的语句返回

步骤：
在@pytest.fixture(scope=module)
在登录的方法中加yield,之后加销毁清除的步骤
@pytest.fixture
def fixtute_name():
    setup操作
    yield 返回值1,返回值2
    teardown操作
"""
# 1.最简单的用法
# @pytest.fixture(scope="class")
# def login():
#     # setup操作
#     print("完成登录")
#     yield   #相当于return,若无返回只默认为None，所以login=None
#     # teardown操作
#     print("完成登出")
#
#
# # 函数名字作为参数传入
# def test_cart(login):
#     print("购物车")

# 2、通过提取登录的token
# @pytest.fixture(scope="class")
# def login():
#     # setup操作
#     print("完成登录")
#     token='hxnmma'
#
#     yield token  #同return指定返回值,login='hxnmma'
#     # teardown操作
#     print("完成登出")
#
#
# # 函数名字作为参数传入
# def test_cart(login):
#     print(f"token:{login}")
#     print("购物车")

# 、多个返回值
# @pytest.fixture(scope="class")
# def login():
#     # setup操作
#     print("完成登录")
#     name='zhangsan'
#     token = 'hxxxxxauullnmma'
#
#     yield name,token  # 同return指定返回值,login='hxnmma'
#     # teardown操作
#     print("完成登出")
#
# # 函数名字作为参数传入
# def test_cart(login):
#     name, token=login
#     print(f"name:{name}\ntoken:{token}")
#     print("购物车")

"""4、fixture在自动化中的应用-数据共享
场景：
你和其他测试工程师合作一起开发时，公共的模块要在不同文件中，要在大家都访问得到的地方

解决：
使用conftest.py这个文件进行数据共享，并且它可以放在不同的位置起着不同范围的作用

前提：
1/conftest.py文件名是固定的
2/放在项目下是全局的数据共享的地方

执行：
系统执行到参数login时先从本地模块中查找是否有这个名字的变量等
之后在conftest.py中查询是否有

步骤：
将登录模块带@pytest.fixture写在conftest.py
"""
#本目录下conftest.py
# def test_cart(login):
#     name, token=login
#     print(f"name:{name}\ntoken:{token}")
#     print("购物车")

# 输出
# pytest_for_fixture.py::test_cart 完成登录
# PASSED                                  [100%]
# name:zhangsan
# token:hxxxxxauullnmma
# 购物车
# 完成登出

"""5、fixture在自动化中的应用-自动应用autouse
场景：
不想原方法有任何改的，或者全部都自动实现自动应用，没特例，也都不需要返回值时选择自动应用

解决：
使用fixture中参数autouser=True实现,默认为false

步骤：
在方法上面加@pytest.fixture(autouse=True)
"""
#例子：本目录下conftest.py中login的装饰器@pytest.fixture(scope="session",autouse=True)
def test_search():
    print("搜索")

# 不需要将登录函数名字作为参数传入
def test_cart():
    print("购物车")

def test_order():
    print("下单")

#输出
# thematic_courses/pytest_and_allure/pytest_L3/pytest_for_fixure/pytest_for_fixture.py::test_search
# 完成登录
# 搜索
# PASSED
# thematic_courses/pytest_and_allure/pytest_L3/pytest_for_fixure/pytest_for_fixture.py::test_cart
# 购物车
# PASSED
# thematic_courses/pytest_and_allure/pytest_L3/pytest_for_fixure/pytest_for_fixture.py::test_order
# 下单
# PASSED
# 完成登出

"""6、fixture在自动化中的应用-参数化params
场景：
测试离不开数据，为了数据灵活，一般数据都是通过参数传递的

解决：
fixture通过固定参数request传递

步骤：
在fixture中增加@pytest.fixture(params=[1,2,3])
在方法参数写request,方法体里面使用request.params接收参数

注意：request是fixture的内置装饰器
"""
@pytest.fixture(params=[["张三","123456"],["李四","666666"]])
def login(request):
    print(f"登录信息：{request.param}")
    return request.param

# 笛卡尔积
def test_demo1(login):
    print(f"登录信息：{login}")

# 输出
# 登录信息：['张三', '123456']
# PASSED                         [ 50%]登录信息：['张三', '123456']
# 登录信息：['李四', '666666']
# PASSED                         [100%]登录信息：['李四', '666666']
