# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 21:16
# @Author  : yanfa
# @user   : yanfa 
# @File    : closure_functions_and_decorators.py
# @remark:闭包函数与装饰器
""""""
import time

"""一、函数引用
函数可以被引用，函数可以被赋值给一个变量
"""
# def hog():
#     print(hog)
# print(hog) #是一个函数对象 <function hog at 0x101032280>
#
# harry=hog #把函数对象赋值给一个变量
# print(harry)  #<function hog at 0x100876280>

"""二、闭包函数
闭包的内部函数中，对外部作用域的变量进行引用
闭包无法修改外部函数的局部变量
闭包可以保存当前的运行环境"""

# def output(grade):
#     def inner(name,gender):
#         print(f"开学啦，姓名是{name},性别是{gender},年级是{grade}") #闭包的内部函数中，对外部作用域的变量进行引用
#     return inner
#
# student=output(1) #闭包可以保存当前的运行环境，grade声明了下面就不用重复声明
# student("张三","男") #开学啦，姓名是张三,性别是男,年级是1
# student("李四","女")
# student("王五","男")

#闭包无法修改外部函数的局部变量
# def output(grade):
#     grade="2"
#     print(f"外函数的年级：{grade}")
#     def inner(name,gender):
#         grade = "1"
#         print(f"内函数的年级：{grade}")
#     return inner
#
# student=output(1) #外函数的年级：2 \n 内函数的年级：1
"""为什么要学习装饰器
行业需求：涉及python技术栈，面试常见题
使用需求：优化代码的可读性，可维护性"""
"""三、装饰器"""
#需求：函数体执行开始和结束打印信息
#第一：没封装时，代码冗余
# def hog():
#     print("霍格沃滋学社")
# def hog2():
#     print("霍格沃滋学社2")
# print("函数开始执行")
# hog()
# print("函数结束执行")
#
# print("函数开始执行")
# hog2()
# print("函数结束执行")

#第二：优化，封装成函数,入参是函数对象func---但是难以理解
# def hog():
#     print("霍格沃滋学社")
# def hog2():
#     print("霍格沃滋学社2")
# def function_tips(func):
#     print("函数开始执行")
#     func()
#     print("函数结束执行")
#
# function_tips(hog) #函数开始执行\n霍格沃滋学社\n函数结束执行
# function_tips(hog2)

#第三、使用装饰器-更简洁
# 第一步：定义2个函数，外函数，内函数
# 第五步：在装饰器执行过程中，会自动传入一个参数，参数就是被装饰函数的函数对象
# def timer(func):
#     def inner():
#         # 第二步：添加装饰器逻辑
#         print("计时开始")
#         func() #第六步：添加被装饰函数的执行逻辑
#         print("计时结束")
#     # 第三步：把内函数的函数对象return
#     return inner

#第四步：装饰器的使用
# @timer
# def hog():
#     print("学社")
# @timer
# def hog2():
#     print("学社2")
# hog() #计时开始\n学社\n计时结束
# hog2() #计时开始\n学社2\n计时结束

#装饰器实战练习-实现一个计时器的装饰器，计算函数执行时间

# def timer(myfunc):
#     def inner():
#         start=time.time()
#         print(f"开始时间：{start}")
#         myfunc()
#         end=time.time()
#         print(f"结束时间：{end}")
#         diff_time=end-start
#         print(f"执行时间：{diff_time}")
#     return inner
#
# @timer
# def myfunc():
#     print("这是我的函数")
#
# myfunc() #开始时间：xx\n这是我的函数\n开始时间：xx\n执行时间：xx

"""四、装饰带参数函数
使用不定长参数*args,**kwargs"""
def timer(myfunc):
    def inner(*args,**kwargs):
        start=time.time()
        print(f"开始时间：{start}")
        myfunc(*args,**kwargs)
        end=time.time()
        print(f"结束时间：{end}")
        diff_time=end-start
        print(f"执行时间：{diff_time}")
    return inner

@timer
def myfunc(name):
    print(f"这是我的函数{name}")

myfunc("张三") #xxx 这是我的函数张三 xxx

@timer
def myfunc(name,age:int,sex):
    print(f"这是我的函数,姓名为{name}，年龄为：{age},性别为：{sex}")

myfunc("张三",18,"男") #xxx 这是我的函数,姓名为张三，年龄为：18,性别为：男 xxx
