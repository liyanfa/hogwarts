# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 20:30
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_allure_02_for_add_step.py
# @remark: 添加用例步骤
""""""
import allure
import pytest

"""一、allure支持2种方法
方法一：使用装饰器@allure.step定义一个测试步骤，在测试用例中使用
方法二：使用with allure.step()添加测试步骤

"""
# @allure.step
# def simple_step1(param):
#     """定义一个测试步骤"""
#     print(f"步骤1：筛选条件选择：{param}")
#
# @allure.step
# def simple_step2(func):
#     """定义一个测试步骤"""
#     print(f"步骤2：点击搜索，搜索{func}")
#
# @pytest.mark.parametrize("param,func",[("name","名称"),("id","序号")])
# @allure.title("搜索功能-{func}")
# def test_step_in_method1(param,func):
#     simple_step1(param)
#     simple_step2(func)

@allure.title("搜索用例")
def test_step_in_method2():
    with allure.step("步骤一：打开页面"):
        print("打开页面")
    with allure.step("步骤二：录入搜索条件"):
        print("录入搜索条件")
    with allure.step("步骤三：点击搜索"):
        print("打点击搜索")
