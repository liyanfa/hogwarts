# -*- coding: utf-8 -*-
# @Time    : 2023/6/8 19:43
# @Author  : yanfa
# @user   : yanfa 
# @File    : pytest_for_commond_line.py
# @remark: 常用命令行参数
""""""
"""
1)  --help 查看帮助文档
例子：pytest --help

2)  -x 用例一旦失败（fail/error）,就立即停止执行  
例子：pytest -x thematic_courses/pytest_and_allure/pytest_L2/test_run_case.py 
输出信息：
thematic_courses/pytest_and_allure/pytest_L2/test_run_case.py ..F
!!!!!! stopping after 1 failures !!!!!

3)  --maxfail=num 用例最大失败次数  
例如：pytest -s thematic_courses/pytest_and_allure/pytest_L2/test_run_case.py --maxfail=1  后续就不会执行了【1 failed, 2 passed】
     pytest -s thematic_courses/pytest_and_allure/pytest_L2/test_run_case.py --maxfail=2  失败数只有1继续执行【 1 failed, 3 passed】

4）  -m  标记用例
例子：pytest -s thematic_courses/pytest_and_allure/pytest_L2/test_run_case.py -m "fail"

5）  -v 打印详细日志
例子：pytest -v thematic_courses/pytest_and_allure/pytest_L2/test_run_case.py 
输出信息 [ 25%] [ 50%] [ 75%] [ 100%]

6）  -s 打印输出日志，如print的部分，配合使用-sv
例子：pytest -s thematic_courses/pytest_and_allure/pytest_L2/test_run_case.py 
输出信息:
thematic_courses/pytest_and_allure/pytest_L2/test_run_case.py test_demo01
.test_demo02
.test_demo03
Ftest_demo04

7）  -k 执行包含某个关键字的测试用例
例子：pytest -s thematic_courses/pytest_and_allure/pytest_L2/test_run_case.py -k "demo03"
输出信息：
thematic_courses/pytest_and_allure/pytest_L2/test_run_case.py test_demo03
F

8）  --collect-only 收集用例集，不执行
例子：pytest --collect-only
输出信息：
collected 7 items                                                                                                                                                     

<Module practical_guide/p1_test_framework/test_module.py>
  <Class TestDome>
    <Function test_demo1>
......
======== 7 tests collected in 0.03s ========
"""