# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 19:47
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_allure_01_for_add_title.py
# @remark: 添加用例标题
""""""
import allure
import pytest

"""
一、allure用法
方法名	                方法参数	                    参数说明
@allure.epic()	        epic描述	            敏捷里面的概念，定义史诗，往下是 feature
@allure.feature()	    模块名称	            功能点的描述，往下是 story
@allure.story()	        用户故事	            用户故事，往下是 title
@allure.title("xx")	    用例的标题	        重命名 html 报告名称
@allure.step()	        操作步骤	            测试用例的步骤
@allure.testcase()	    测试用例的链接地址	    对应功能测试用例系统里面的 case
@allure.issue()	        缺陷	                对应缺陷管理系统里面的链接
@allure.description()   用例描述	            测试用例的描述
@allure.severity()	    用例等级	            blocker，critical，normal，minor，trivial
@allure.link()	        链接	                定义一个链接，在测试报告展现
@allure.attachment()    附件	                报告添加附件

二、添加用例标题
通过@allure.title()自定义标题，支持三种方式：
1、直接@allre.title()

2、@allre.title()支持占位符的方式传递参数，实现测试用例标题参数化，动态生成用例标题

3、@allure.dynamic.title()动态更新测试用例标题

"""


# 例子：
# 方式一：直接@allre.title()
@allure.title("这是标题")
def test_with_title():
    assert True

# 方式二：参数化标题
@allure.title("参数化标题：参数1:{param1} 参数2：{param2}")
@pytest.mark.parametrize("param1,param2,expected", [(1, 1, 2), (1, 3, 3)])
def test_with_title_param(param1, param2, expected):
    assert param1 + param2 == expected

# 方式三：更新标题
@allure.title("老标题")
def test_with_dynamic_title():
    assert True
    allure.dynamic.title("新标题")
