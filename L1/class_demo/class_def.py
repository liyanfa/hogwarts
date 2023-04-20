# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 21:16
# @Author  : yanfa
# @user   : yanfa 
# @File    : class_def.py
# @remark:

#类的声明  不传则默认父类是超类object
class Human:
    """人类"""
    #定义属性（类属性）
    message="这是类属性"

    #构造方法 -自动执行,直接返回该类的实例，如果不行则默认创建一个构造方法
    def __init__(self,name,age):
        # 实例属性(变量)
        self.name=name  #通过self绑定到自身
        self.age=age
        print("这是构造方法")



print(Human.message) #这是类属性

#实例化对象
person=Human("yanfa",18) #这是构造方法

#通过实例访问类属性
print(person.message) #这是类属性
#通过实例访问实例属性
print(person.name) #yanfa
print(person.age) #18


