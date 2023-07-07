# -*- coding: utf-8 -*-
# @Time    : 2023/6/26 19:21
# @Author  : yanfa
# @user   : yanfa 
# @File    : pytest_for_ini.py
# @remark: pytest.ini配置文件
""""""
"""一、pytest.ini是什么
pytest -h找到[pytest] ini-options in the first pytest.ini|tox.ini|setup.cfg|pyproject.toml file found:

1、pytest.ini是pytest的配置文件
2、可以修改pytest的默认行为
3、不能使用任何中文符号，包括汉字、空格、引号、冒号等等
"""

"""二、pytest.ini能做什么
1、修改用例的命名规则
2、配置日志格式，比代码配置更方便
3、添加标签，防止运行过程中报告警错误
4、指定执行目录
5、排除搜索目录
"""

"""2.1、pytest配置-改变运行规则
1、执行以test_开头和check_开头的文件，后面一定要加*
python_files = test_* check_*
2、执行所有以Test_开头和Check_开头的类
python_classes = Test* Check*
3、执行所有以test_开头和check_开头的方法
python_functions = test_* check_*
"""
# 例子：见check_demo.py

"""2.2、pytest配置-添加默认参数
addopts = -s -v --alluredir=./results
"""

"""2.3、pytest配置-指定/忽略执行目录
1、设置执行路径
testpaths = thematic_courses/pytest_and_allure/pytest_L4
2、忽略某些文件夹/目录
norecursedirs = result logs datas test_demo*
"""
# 例子1：执行pytest 就等同执行pytest -s -v
# 例子2：data下的check_demo1.py不执行，注释掉norecursedirs = data就执行

"""2.4、pytest-日志
https://ceshiren.com/t/topic/13105

[pytest]
;日志开关 true false
log_cli = true
;日志级别
log_cli_level = info
;打印详细日志，相当于命令行加 -vs
addopts = --capture=no
;日志格式
log_cli_format = %(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)
;日志时间格式
log_cli_date_format = %Y-%m-%d %H:%M:%S
;日志文件位置
log_file = ./log/test.log
;日志文件等级
log_file_level = info
;日志文件格式
log_file_format = %(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)
;日志文件日期格式
log_file_date_format = %Y-%m-%d %H:%M:%S
"""

"""总结：
修改用例的命令规则
配置日志格式，比代码配置更方便
指定执行目录
排除搜索目录
添加标签，防止运行过程报警告错误
添加默认参数
"""