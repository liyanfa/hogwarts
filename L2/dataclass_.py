# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 22:10
# @Author  : yanfali
# @File    : dataclass_.py
# @Software: 数据类dataclass

"""一、dataclass 介绍
操作类属性的默认值、类型等
优势：可读性强、操作灵活、轻量
应用场景：创建对象、完美融合平台开发ORM"""

"""案例：场景：如果创建一只猫，信息包括猫的名字、体重、颜色。同时打印这个对象的时候，希望能打印出一个字符串（包含猫的各种信息）应该如何编写代码
问题：
数据修改不方便
代码冗余
解决方案：
使用自定义类实现数据类"""
# class Cat:
#     name:str
#     color:str
#     weight:int
#
#     def __init__(self,name,color,weight):
#         self.name=name
#         self.color=color
#         self.weight=weight
#
#     def __str_(self):
#         """打印对象信息"""
#         return f"猫咪姓名={self.name} 颜色={self.color} 体重={self.weight}"
#
#     def __repr__(self):
#         """以字符返回"""
#         return f"===>>>猫咪姓名={self.name} 颜色={self.color} 体重={self.weight}"
#
# c=Cat("miaomiao","黄色",10)
# print(c) #如果注释__str__方法，则返回<__main__.Cat object at 0x000002DA7DE2FDC8>
# print(c) #如果不注释，才打印想要的对象信息。===>>>猫咪姓名=miaomiao 颜色=黄色 体重=10

"""数据类更优雅的实现方式
使用dataclass创建数据类
实例化的时候自动生成构造函数"""

#1、最简单的dataclass用法
# from dataclasses import dataclass
# @dataclass()
# class Cat:
#     name:str
#     color:str
#     weight:int
#
# if __name__ == '__main__':
#     cat=Cat("miao","蓝色",10)
#     print(cat) #Cat(name='miao', color='蓝色', weight=10)

"""2、field常用方法
参数名	参数功能
default	字段的默认值
default_factory	定义可变量参数的默认值，default 和 default_factory 不能同时存在
init	如果为 true（默认值），该字段作为参数包含在生成的 init() 方法中。False相反。
repr	如果为 true（默认值），该字段包含在生成的 repr() 方法返回的字符串中"""

#1、default/default_factory指定类型和默认值
#注意同一个参数里不能同时存在default和default_factory
# 如children:list=field(default=2,default_factory=list)

# from dataclasses import dataclass,field
# @dataclass()
# class Cat:
#     name: str
#     color: str =field(default="white") #default指定固定类型str/tuple的默认值和类型
#     weight:int=field(default=2)
#     children:list=field(default_factory=list) #指定可变类型list/dict的默认值和类型
# if __name__ == '__main__':
#     cat=Cat("喵喵")
#     print(cat) #Cat(name='喵喵', color='white', weight=2, children=[])

#2、init参数
#如果为 True（默认值），该字段作为参数包含在生成的 init() 方法中。
#如果为 False，该字段不会包含 init() 方法参数中。
# from dataclasses import dataclass,field
# @dataclass()
# class Cat:
#     name: str
#     color: str
#     weight:int=field(default=2,init=False)
# if __name__ == '__main__':
#     cat=Cat("喵喵","蓝色")  #不需要传weight
#     print(cat) #Cat(name='喵喵', color='蓝色', weight=2)

#3、repr参数
#如果为 True（默认值），该字段包含在生成的 repr() 方法返回的字符串中。
#如果为 False，该字段不会包含在生成的 repr() 方法返回的字符串中
from dataclasses import dataclass,field
@dataclass()
class Cat:
    name: str
    color: str
    weight:int=field(default=2,repr=False)
if __name__ == '__main__':
    cat=Cat("喵喵","蓝色")  #不打印weight
    print(cat) #Cat(name='喵喵', color='蓝色')