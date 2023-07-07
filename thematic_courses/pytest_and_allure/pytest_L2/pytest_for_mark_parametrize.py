# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 20:09
# @Author  : yanfa
# @user   : yanfa 
# @File    : pytest_for_mark_parametrize.py
# @remark: pytest参数化用例

# 简单示例
# def inc(x):
#     return x+1
#
# def test_answer():
#     assert inc(3)==4
#
# class Test_a():
#     def test_a(self):
#         pass

"""mark:参数化测试函数使用
1/单参数
2/多参数
3/用例重命名
4/笛卡尔积"""


# 传统方法-代码冗余
# search_list=['appium','selenium']
# def test_search1():
#     name='appium'
#     assert name in search_list
#
# def test_search2():
#     name='selenium'
#     assert name in search_list

#第一种 参数化实现用例动态生成-单参数
import pytest
# search_list=['appium','selenium']
#
# @pytest.mark.parametrize('name',['appium','selenium','pytest',''])
# def test_search(name):
#     assert name in search_list

#第二种 多参数 将数据放到元祖和或者列表中
# @pytest.mark.parametrize('username,password',[['zhangsan','1234'],['lisi','5678']])
# @pytest.mark.parametrize('username,password',[('zhangsan','1234'),('lisi','5678')])
# @pytest.mark.parametrize('username,password',(('zhangsan','1234'),('lisi','5678')))
# def test_login(username,password):
#     print(f'用户名：{username},密码：{password}')

#第三种 用例重命名，使用ids参数，名字数与参数个数一致  解决中文问题看conftest.py
# @pytest.mark.parametrize('username,password',[['zhangsan','1234'],['lisi','5678']],ids=["第一个名字","第二个名字"])
# def test_login(username,password):
#     print(f'用户名：{username},密码：{password}')

#第四种 笛卡尔积 由近及远 一层层循环
# 比如两组数据
# m=[1,2,3]
# n=[a,b,c]
# 共有9中组合[1-a,1-b,1-c,2-a,2-b,2-c,3-a,3-b,3-c]
# 使用方法：
@pytest.mark.parametrize("n",["a","b","c"])
@pytest.mark.parametrize("m",[1,2,3])
def test_dika(m,n):
    print(f"笛卡尔积参数化 m={m},n={n}")