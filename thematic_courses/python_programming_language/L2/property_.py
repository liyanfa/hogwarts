# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 22:16
# @Author  : yanfali
# @File    : property_.py
# @Software: 封装 property

""""""
"""一、封装的概念
隐藏：属性和实现细节，不允许外部直接访问
暴露：公开方法，实现对内部信息的操作和访问"""

"""二、封装的作用
限制安全的访问和操作，提高数据安全性
可进行数据检查，从而有利于保证对象信息的完整性"""


class Accont:
    """账户"""

    # 普通属性
    bank = "boc"

    """三、封装的实现：隐藏
    保护属性：_属性名
    私有属性：__属性名 被视作_类名__属性名"""
    # 保护属性
    _username = "hogwarts"

    # 私有属性
    __password = "888"

    """四、封装的实现：暴露
    提供数据访问功能(getter)
    计算属性
    语法：使用@property装饰器、语法糖
    调用：实例.方法名"""

    # 暴露 -计算属性
    @property
    def password(self):
        return self.__password

    """五、封装的实现：暴露
    提供数据操作功能(setter)
    语法：使用@计算属性名.setter装饰器
    调用：实例.方法名
    """

    @password.setter
    def password(self, value):
        if len(value) >= 8:
            self.__password = value
        else:
            print("密码长度最少8位")


# print(Accont.bank)
# print(Accont._username) #会提示Access to a protected member _username of a class
# print(Accont.__password) #无法填充，AttributeError: type object 'Accont' has no attribute '__password'

# 打印有哪些属性
print(Accont.__dict__)  # 自动改名为_Accont__password

# 实例化对象
obj = Accont()
# 访问实例的私有属性
print(obj.password)  # 888

# 修改私有属性-满足校验条件
obj.password = "12345678"
print(obj.password)  # 12345678
# 修改私有属性-不满足校验条件
obj.password = "1234"
print(obj.password)  # 会自动过滤非法数据保留原数据。密码长度最少8位 \n 888
