# -*- coding: utf-8 -*-
# @Time    : 2023/6/8 20:13
# @Author  : yanfa
# @user   : yanfa 
# @File    : pytest_for_code_run.py
# @remark: python代码执行pytest

""""""
import pytest

"""
1/使用main函数 运行方式 python test_xx.py
例子： python thematic_courses/pytest_and_allure/pytest_L2/pytest_for_code_run.py

2/使用python -m pytest  test_xx.py [其他命令行] 调用pytest，常用于持续集成
例子：python -m pytest thematic_courses/pytest_and_allure/pytest_L2/pytest_for_code_run.py -m "fail"
 """

def test_code1():
    assert 1==1

@pytest.mark.fail
def test_code2():
    assert 1==2

if __name__ == '__main__':
    # 1、运行当前目录下所有符合规则的用例，包括子目录（test_*.py和*_test.py）
    # pytest.main()
    # 2、运行模块中的某条用例 xx.py::test_xx
    # pytest.main(['thematic_courses/pytest_and_allure/pytest_L2/pytest_for_code_run.py::test_code2','-sv'])
    # 3、运行某个标签
    pytest.main(['thematic_courses/pytest_and_allure/pytest_L2/pytest_for_code_run.py','-sv','-m','fail'])
