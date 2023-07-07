# -*- coding: utf-8 -*-
# @Time    : 2023/6/26 20:39
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_pytest_for_plugins.py
# @remark: pytest插件-内置插件hook
""""""

"""一、pytest插件分类
1、外部插件：pip install安装的插件，也叫第三方库
2、本地插件：pytest自动模块发现机制（conftest.py存放的）
3、内置插件：代码内部的_pytest目录加载，也叫hook函数
"""

"""二、pytest hook介绍
1、是一个函数，在系统消息触发时被系统调用
2、自动触发机制
3、hook函数的名称是确定的
4、pytest有很多的勾子函数
5、使用时直接编写函数体

"""

"""三、pytest hook 执行顺序 
【参考https://ceshiren.com/t/topic/8807】
1、用例执行顺序：
大概 开始执行->执行测试用例->结束执行
详细 收集测试用例->收集完测试用例之后->执行前置setup->调用执行测试->执行后置teardown->...->获取测试结果
root
└── pytest_cmdline_main
├── pytest_plugin_registered
├── pytest_configure
│ └── pytest_plugin_registered
├── pytest_sessionstart
│ ├── pytest_plugin_registered
│ └── pytest_report_header
├── pytest_collection
│ ├── pytest_collectstart
│ ├── pytest_make_collect_report
│ │ ├── pytest_collect_file
│ │ │ └── pytest_pycollect_makemodule
│ │ └── pytest_pycollect_makeitem
│ │ └── pytest_generate_tests
│ │ └── pytest_make_parametrize_id
│ ├── pytest_collectreport
│ ├── pytest_itemcollected
│ ├── pytest_collection_modifyitems
│ └── pytest_collection_finish
│ └── pytest_report_collectionfinish
├── pytest_runtestloop
│ └── pytest_runtest_protocol
│ ├── pytest_runtest_logstart
│ ├── pytest_runtest_setup
│ │ └── pytest_fixture_setup
│ ├── pytest_runtest_makereport
│ ├── pytest_runtest_logreport
│ │ └── pytest_report_teststatus
│ ├── pytest_runtest_call
│ │ └── pytest_pyfunc_call
│ ├── pytest_runtest_teardown
│ │ └── pytest_fixture_post_finalizer
│ └── pytest_runtest_logfinish
├── pytest_sessionfinish
│ └── pytest_terminal_summary
└── pytest_unconfigure

2、hook执行顺序 
见源码 /site-packages/_pytest/hookspec.py

pytest_addoption: 添加命令行参数，运行时会先去读取命令行参数
pytest_collection_modifyitems: 收集测试用例，收集后（改编码，改执行顺序等）
pytest_collection_finish: 收集之后的操作
pytest_runtest_setup: 前置操作，在调用pytest_runtest_call之前调用
pytest_runtest_call: 调用执行测试的用例
pytest_runtest_teardown: 后置操作，在调用pytest_runtest_call之后调用
pytest_runtest_makereport: 运行测试用例，返回setup、call、teardown的执行结果

改造脚本见conftest.py，复制hookspec.py中勾子函数，然后函数体写自己的逻辑
from _pytest.hookspec import hookspec

def pytest_runtest_setup(item: "Item") -> None:
    print("hook: 前置处理")

def pytest_runtest_call(item: "Item") -> None:
    print("hook: 执行用例")

def pytest_runtest_teardown(item: "Item", nextitem: Optional["Item"]) -> None:
    print("hook: 后置处理")
"""
# 例子：conftest.py简单改造，然后执行test_hook.py
# 输出
# hook: 前置处理
# hook: 执行用例
# 这是用例的操作 PASSED
# hook: 后置处理
def test_hook():
    print("这是用例的操作")


"""四、总结
1、hook函数名称固定
2、hook函数会被自动执行
3、执行是有先后顺序的
4、pytest定义了很多的hook函数，可以在不同阶段实现不同的功能
"""
