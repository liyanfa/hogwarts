# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 20:10
# @Author  : yanfa
# @user   : yanfa 
# @File    : args_and_kwargs.py
# @remark: 函数进阶与参数处理
""""""
"""一、可变参数
可变参数也称为不定长参数
传入参数中实际参数可以是任意多个
常用形式：*args **kwargs"""

"""*args-列表或元祖
接受任意多个实际参数，并将其放入一个元祖中
使用已经存在的列表或元祖作为函数的可变参数，可以在列表名称前加*
传参是*是组合参数为元祖
调用时*是解包"""

def print_language(*args):
    print(args)

#1、调用函数，把不同数量的参数传递进去，用位置函数
print_language("python","go") #存放到一个元祖('python', 'go')
print_language("python","go","java","php") #('python', 'go', 'java', 'php')

#2、等价为print_language("python","go","java","php")
lan=["python","go","java","php"]
# print_language(lan)
print_language(*lan) #('python', 'go', 'java', 'php')

"""**kwargs-字典
接受任意多个类似关键字参数一样显示赋值的实际参数，并将其放到一个字典中
使用已经存在字典作为函数的可变参数，可以在字典的名称前面加**
**-打包的作用
调用时参数前面**表示解包"""
#1、打包
def print_info(**kwargs):
    print(kwargs)
print_info(a=18,b=20) #{'a': 18, 'b': 20}

#2、解包 等价于print_info(a=18,b=20)
params={"a":18,"b":20}
print_info(**params) #解包 {'a': 18, 'b': 20}