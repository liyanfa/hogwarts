# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 21:37
# @Author  : yanfali
# @File    : type_annotations.py
# @Software: 类型注解
""""""
"""类型提示功能"""
#用法1、指定入参和返回的类型 通过："""
# def sum(a:int,b:int)->int:
#     return  a+b
#
# print(sum(0.1,5))

# 用法2、为类型起别名
from typing import List
f_list=List[float]

def sum(a:float,b:f_list)->f_list:
    return  [a*num for num in b]
print(sum(1.1,[2.2,3.3]))  #[2.4200000000000004, 3.63]

"""ide中的提示功能-类型检查：
setting-搜索ty pe checker 可以修改提示级别，默认warning"""

"""用法三：指定自定义类型"""
# class Student:
#     name:str
#     age:int
#
# def get_stu(name:str)->Student:
#     return Student()

"""静态代码检查
安装mypy"""

"""类型注解总结：
1、增强代码可读性
2、ide中代码提示
3、静态代码检查"""