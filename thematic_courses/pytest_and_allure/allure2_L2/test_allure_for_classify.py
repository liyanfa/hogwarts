# -*- coding: utf-8 -*-
# @Time    : 2023/6/29 11:25
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_allure_for_classify.py
# @remark: allure分类
""""""
import allure

"""
一、报告分类介绍
应用场景：
可以为项目以及项目下不同模块对用例进行分类管理，也可以运行某个类别下的用例
报告展示：
类别会展示在测试报告的Behaviors栏目下
allure提供三个装饰器：
    @allure.epic：敏捷里面的概念，定义史诗，往下是feature
    @allure.feature：功能点的描述，理解成模块，往下是story
    @allure.story：故事，是功能的子集
    
二、allure分类-epic
场景：希望在测试报告中看到用例所在的项目，需要用到epic,相当于定义一个项目的需求，
    由于粒度比较打，在epic下还需要定义略小粒度的用户故事。
解决：@allure.epic

三、allure分类-feature/story
场景：希望在报告中看到测试功能，子功能或场景
解决：@allure.feature、@allure.story
步骤：
    在功能上加@allure.feature("功能名")
    在子功能上加@allure.story("子功能名")
    
四、allure运行epic/feature/story：
（多个用逗号分隔）
1、只运行epic名为'项目1'和'项目2'的测试用例
    --allure-epics=项目1,项目2
2、只运行feature名为'功能模块1'和'功能模块2'的测试用例
    --allure-features=功能模块1,功能模块2
3、只运行story名为'子功能1'和'子功能2'的测试用例
    --allure-stories=子功能1,子功能2
4、运行feature+story的用例，取并集
    --allure-features=功能模块1 --allure-stories=子功能1,子功能2

五、allure epic/feature/story的关系
1、epic：相当于定义一个项目，史诗
2、feature：相当于一个功能模块，相当于testsuite,可以管理很多分支story
3、story：相当于对应这个功能或者模块下的不同场景、不同分支功能
4、epic与feature、feature与story类似父子关系
"""
@allure.epic("项目1")
@allure.feature("功能模块1")
class TestWithEpic1:
    @allure.story("子功能1")
    @allure.title("用例1")
    def test_case1(self):
        print("用例1")

    @allure.story("子功能1")
    @allure.title("用例2")
    def test_case2(self):
        print("用例2")

    @allure.story("子功能2")
    @allure.title("用例1")
    def test_case3(self):
        print("用例1")

@allure.epic("项目1")
@allure.feature("功能模块2")
class TestWithEpic2:
    @allure.story("子功能1")
    @allure.title("用例1")
    def test_case1(self):
        print("用例1")

    @allure.story("子功能1")
    @allure.title("用例2")
    def test_case2(self):
        print("用例2")

    @allure.story("子功能2")
    @allure.title("用例1")
    def test_case3(self):
        print("用例1")

@allure.epic("项目2")
@allure.feature("功能模块3")
class TestWithEpic3:
    @allure.story("子功能1")
    @allure.title("用例1")
    def test_case1(self):
        print("用例1")

    @allure.story("子功能1")
    @allure.title("用例2")
    def test_case2(self):
        print("用例2")

    @allure.story("子功能2")
    @allure.title("用例1")
    def test_case3(self):
        print("用例1")