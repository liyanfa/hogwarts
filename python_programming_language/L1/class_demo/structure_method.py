# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 13:01
# @Author  : yanfa
# @user   : yanfa 
# @File    : structure_method.py
# @remark: 构造方法
# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 21:16
# @Author  : yanfa
# @user   : yanfa
# @File    : class_def.py
# @remark:

#类的声明  不传则默认父类是超类object
class Human:
    """人类"""
    #定义属性（类属性）-相当与全局变量，实例对象共有的属性
    message_a="这是公有类属性"    #公有的类属性
    __message_b="这是私有类属性"  #私有的类属性 __开头

    #构造方法 -自动执行,直接返回该类的实例，如果不行则默认创建一个构造方法
    def __init__(self,name,age):
        # 实例属性(变量)-实例对象自己私有
        self.name=name
        self.age=age
        print("这是构造方法")

print(Human.message_a) #这是类属性

#实例化对象
person=Human("yanfa",18) #这是构造方法
# print(Human.name)  #错误示范 实例属性，不能通过类对象调用

#通过实例访问类属性
print(person.message_a) #这是公有类属性

#通过实例访问实例属性
print(person.name) #yanfa
print(person.age) #18



