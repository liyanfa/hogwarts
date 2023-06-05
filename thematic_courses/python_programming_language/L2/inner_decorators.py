# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 20:14
# @Author  : yanfa
# @user   : yanfa 
# @File    : inner_decorators.py
# @remark: 内置装饰器
""""""
"""一、什么是内置类装饰器
不用实例化，直接调用
提高代码可读性
classmethod -类方法
staticmethod-静态方法"""

"""二、普通方法
定义：第一个参数为self，代表实例本身
调用：要有实例化的过程，通过实例对象.方法名调用"""
#定义
# class Method:
#     def normal_demo(self): #第一个参数为self，代表实例本身
#         """普通方法"""
#         print("这是一个普通方法")
# #调用
# m=Method() #要有实例化的过程
# m.normal_demo()  #通过实例对象.方法名调用


"""三、类方法
定义：
    使用@classmethod装饰器，第一个参数为类本身，通常用cls(class)做区分
    在类内可以直接使用类方法或类变量，无法直接使用实例变量或方法
调用：
    无需实例化，直接通过类名.方法名调用，也可以通过实例名.方法名调用
调用："""
#定义
# class Method:
#     @classmethod
#     def classmethod_demo(cls): #第一个参数为self，代表实例本身
#         """类方法"""
#         print("这是一个类方法")
#
# #调用
# Method.classmethod_demo() #无需实例化，直接通过类名.方法名调用
# m=Method()
# m.classmethod_demo() #也可以通过实例名.方法名调用

"""三、静态方法
定义：
    使用@staticmethod装饰器器，没有和类本身有关的参数
    无法直接使用任何类变量、类方法、实例变量、实例方法
调用：
    无需实例化，直接通过类名.方法名调用，也可以通过实例名.方法名调用"""

#定义
class Method:
    @staticmethod
    def staticmethod_demo(): #第一个参数为self，代表实例本身
        """静态方法"""
        print("这是一个静态方法")
#调用
Method.staticmethod_demo() #无需实例化，直接通过类名.方法名调用
m=Method()
m.staticmethod_demo() #也可以通过实例名.方法名调用


"""四、总结-普通方法、类方法、静态方法
名称	        定义	                 调用	                      关键字	        使用场景
普通方法	至少需要一个参数self	实例名.方法名()	                    无	        方法内部涉及到实例对象属性的操作
类方法	至少需要一个cls参数	类名.方法名() 或者实例名.方法名()	@classmethod	如果需要对类属性，即静态变量进行限制性操作
静态方法	无默认参数	        类名.方法名() 或者实例名.方法名()	@staticmethod	无需类或实例参与
"""

"""五、静态方法实例案例
此方法没有任何和实例、类相关的部分，可以作为一个独立函数使用
某些场景下，从业务逻辑来说又属于类的一部分
例子：简单工厂方法
"""
# static 使用场景
# class HeroFactory:
#     # staticmethod 使用场景，
#     # 方法所有涉及到的逻辑都没有使用实例方法或者实例变量的时候
#     # 伪代码
#     @staticmethod
#     def create_hero(hero):
#         if hero == "ez":
#             return EZ()
#         elif hero == "jinx":
#             return Jinx()
#         elif hero == "timo":
#             return Timo()
#         else:
#             raise Exception("此英雄不在英雄工厂当中")