# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 21:38
# @Author  : yanfa
# @user   : yanfa 
# @File    : class_method.py
# @remark:类方法
class Human:
    # 类属性
    pop = 0

    # 类方法 可以操作类的详细信息
    @classmethod  # 只能用这个装饰器
    def born(cls):  # cls是class的简写,是指类名本身
        print("这是类方法")
        cls.pop += 1


# 通过类名访问类方法
Human.born()  # 这是类方法
print(Human.pop)  # 1
