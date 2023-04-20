# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 20:34
# @Author  : yanfa
# @user   : yanfa 
# @File    : p_13.py
# @remark:匿名函数 lambda
""""""
import math

"""一、匿名函数
没有名字的函数
用lambda表达式创建匿名函数"""

"""二、使用场景
需要一个函数，但是又不想费神去命名这个函数
通常在这个函数只使用一次的场景下
可以指定短小的回调函数"""

"""三、语法
result:调用lambda表达式
[arg1[,arg2,...,argn]]：可选，指定要传递的参数列表
expression：必选，指定一个实现具体功能的表达式
result=lambda[arg1[,arg2,...,argn]]:expression"""

#1、实例-求圆面积
#常规写法
# def area(r):
#     '''计算园面积 r-半径'''
#     result=math.pi*r*r
#     return result
# print(area(10))

#lambda表达式
r=10
result=lambda r:math.pi*r*r
print(result(r))  #314.1592653589793

#不可省略自己的变量，异常-如果不指定r
result=lambda r:math.pi*r*r
print(result)  #<function <lambda> at 0x103ee9d30>

#示例2：对获取到的信息进行排序
book_info=[("python入门",22.5),("java入门",20),("测试入门",25)]
print(book_info) #
# 指定规则排序 lambda x:(x[1])-返回列表中每个元祖的第二个元素
book_info.sort(key=lambda x:(x[1]))
print(book_info) #[('java入门', 20), ('python入门', 22.5), ('测试入门', 25)]