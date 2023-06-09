# -*- coding: utf-8 -*-
# @Time    : 2023/6/8 19:33
# @Author  : yanfa
# @user   : yanfa 
# @File    : pytest_for_lf_ff.py
# @remark: 命令行参数-使用缓存状态

""""""
"""
--lf(--last-failed) 只重新运行故障
--ff(--failed-first) 先运行故障后再执行其他的用例

例子1：
pytest -s thematic_courses/pytest_and_allure/pytest_L2/test_run_case.py --lf
输出：
configfile: pytest.ini
collected 4 items / 3 deselected / 1 selected                                                                                                                         
run-last-failure: rerun previous 1 failure
1 failed, 3 deselected xx

例子2：
pytest -s thematic_courses/pytest_and_allure/pytest_L2/test_run_case.py --ff
输出：
configfile: pytest.ini
collected 4 items                                                                                                                                                     
run-last-failure: rerun previous 1 failure first
1 failed, 3 passed xx
"""
