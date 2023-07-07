# -*- coding: utf-8 -*-
# @Time    : 2023/6/29 10:49
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_allure_for_add_link.py
# @remark: 添加链接
""""""
import allure

"""应用场景：
将报告与bug管理/测试用例管理系统集成，支持三种@allure.link、@allure.issue、@allure.testcase
"""

# 格式1：添加普通链接 @allure.link(url,name) url-链接 name-链接名称
@allure.link("https://ceshiren.com")
def test_with_link():
    pass

@allure.link("https://ceshiren.com","这是普通链接")
def test_with_link_name():
    pass

# 格式2：添加用例管理系统链接 @allure.testcase(url,name) 会有一个圆柱图标
@allure.testcase("https://ceshiren.com","这是用例管理系统")
def test_with_link_testcase():
    pass

# 格式3：添加bug管理系统链接 @allure.issue(url,name) 会有一个bug图标
# 特殊：通过--allure-link-pattern指定一个模版链接，将url传成bugid
# --allure-link-pattern=issue:https://ceshiren.com/t/topic/{}
# 目标链接：https://ceshiren.com/t/topic/24593
# 执行命令：pytest test_allure_for_add_link.py --alluredir=./report --clean-alluredir --allure-link-pattern=issue:https://ceshiren.com/t/topic/{}
@allure.issue("24593","这是bug管理系统")
def test_with_link_issue():
    pass
