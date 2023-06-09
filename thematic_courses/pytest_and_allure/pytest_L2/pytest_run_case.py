# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 21:04
# @Author  : yanfa
# @user   : yanfa 
# @File    : pytest_run_case.py
# @remark: pytest 运行用例
""""""

"""运行多条用例
运行某个/多个 用例包
运行某个/多个 用例模块
运行某个/多个 类
运行某个/多个 方法


执行包下所有的用例：pytest [包名]  或者py.test [包名]
执行单独一个pytest模块：pytest 文件名.py 或者cd到某目录下pytest
运行某个模块里面某个类：pytest 文件名.py::类名
运行某个模块里面某个类里的方法：pytest 文件名.py::类名::方法名
运行某个模块里面某个单独方法：pytest 文件名.py::方法名

"""

"""运行结果分析：
常用：fail/error/pass/xpass/xfail
特殊：waring/deselect
"""