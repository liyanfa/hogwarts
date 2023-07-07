# -*- coding: utf-8 -*-
# @Time    : 2023/6/27 15:34
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_pytest_for_develop_plugins.py
# @remark: pytest开发自己的插件
""""""
import pytest

"""一、pytest编写插件1-修改默认编码
pytest_collection_modifyitems收集上来的测试用例实现定制化功能
解决问题：
    1、自定义用例执行顺序
    2、解决编码问题（中文的测试用例名称容易乱码）
    3、自动添加标签
示例：  测试用例收集完成时，将收集的用例名name和用例标识nodeid的中文信息显示在控制台上-一般放在项目根目录的conftest.py
def pytest_collection_modifyitems(items):
    print("hook: 编码处理开始")
    for i in items:
        i.name=i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid=i.nodeid.encode("utf-8").decode("unicode_escape")
    print("hook: 编码处理结束")
"""
# 例子 配置见conftest.py，如果不处理会乱码
# @pytest.mark.parametrize('name',['张三'])
# def test_encode(name):
#     print(f"name：{name}")
# 输出
# ================ test session starts ======================
# platform darwin -- Python 3.9.6, pytest-7.3.1, pluggy-1.0.0
# rootdir: /Users/yanfa/PycharmProjects/hogwarts
# configfile: pytest.ini
# plugins: ordering-0.6, xdist-3.3.1
# collecting ...
# hook: 编码处理开始
# hook: 编码处理结束
# collected 1 items

# thematic_courses/pytest_and_allure/pytest_L4/pytest_for_plugins/test_pytest_for_develop_plugins.py::test_encode[张三]
# hook: 前置处理
# hook: 执行用例
# name：张三 PASSED
# hook: 后置处理

# =============== 1 passed in 0.01s =================

"""二、pytest编写插件2-添加命令行参数
代码示例：
    def pytest_addoption(parser):
        # group 将下面所有的option都展示在这个group下,
        # 什么是group,pytest -h查看帮助文档中,找到logging：，它下面又有 --log-level=LEVEL，那么这就是一个组
        mygroup = parser.getgroup("hogwarts") 
        group.addoption(
            '--env',        #注册一个命令行选项
            default='test', #参数默认值
            dest = 'env',   #存储的变量，为属性命令，可以使用option对象访问这个值
            help='set your run env' # 帮助信息，参数的描述信息
        )
    
    @pytest.fixture(scope='session'):
    def cmdoption(request):
        return request.config.getoption("--env")
查看是否注册成功：点击conftest.py右键open in terminal找到hogwarts
效果：
    hogwarts:
        --env=ENV             set your run env
"""
# 例子：逻辑见conftest.py，
# 直接执行会取test文件默认值，输出('test', {'username': 152155555555, 'password': 123456})
# 命令行执行：pytest --env=online xxx/xxx/.py 会取online文件值，输出 ('online', {'username': 15266666666, 'password': 123456})
def test_addoption(cmdoption):
    print(cmdoption)


"""三、打包发布
1、打包发布到pypi
    发布到：www.pypi.org
    代码上传到：github
    
2、打包项目构成
    源码包、setup.py、测试包
    说明文档：www.pypi.org 点击help,找到Basics下点击How do I package and publish my code for PyPI?，点击packaging tutorial

3、打包命令
依赖包安装：
    pip install setuptools python的包管理工具，负责安装和发布，尤其是安装拥有依赖关系的包
    pip install wheel 生成*.whl格式的安装包，本质上是一个压缩包
打包命令：
    python setup.py sdist bdist_wheel
查找包：pip list |grep pytest_encode
例子：setup.py见https://ceshiren.com/t/topic/14156

4、发布至https://pypi.org/
见https://packaging.python.org/en/latest/tutorials/packaging-projects/
mac:
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE
"""