# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 22:49
# @Author  : yanfali
# @File    : inheritanc_and_type_check.py
# @Software: 继承与类型检查
""""""
"""一、继承的概念
继承Inheritance
复用父类的公开属性和方法
扩展出新的属性和方法"""

"""二、继承的实现
语法: class 类名(父类列表)
默认父类是object
python 支持多继承"""
class Human:
    """人类"""
    message="这是Human类属性"

    #构造方法
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #实例方法
    def live(self):
        print("住在地球上")

class Student(Human):

    def stduy(self):
        print("真正学习")

#实例化子类对象
stu=Student("YANFA",18)

#访问属性
print(stu.message) #可以访问父类的类属性。这是Human类属性
print(stu.name,stu.age) #可以访问父类构造方法的属性。 YANFA 18

#访问父类的实例方法
stu.live()  #住在地球上

#访问自己的实例方法
stu.stduy() #真正学习

"""三、类型检查
isinstance(示例，类名)：检查对象是否某个类以及派生的实例
issubclass(类名1，类名2)：检查类与类之间的关系，检查类名1是否是类名2的子类"""

print(isinstance(stu,Student)) #检查实例与类 True
print(issubclass(Student,Human)) #检查类与类 True