# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 10:58
# @Author  : yanfa
# @user   : yanfa 
# @File    : function_inner.py
# @remark:内置函数示例

#next
#通过调用 iterator 的 __next__() 方法获取下一个元素。如果迭代器耗尽，则返回给定的 default，如果没有默认值则触发 StopIteration。
# my_list = [1, 2, 3, 4, 5]
# my_iterator = iter(my_list)
#
# while True:
#     try:
#         next_element = next(my_iterator)
#         print(next_element)
#     except StopIteration:
#         break

#repr(object):一个对象转换为一个可打印的字符串
#eval()：表达式求值，
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Person(name='{self.name}', age={self.age})"
#
# if __name__ == '__main__':
#     person = Person("John", 25)
#     person_str = repr(person)
#     print(person_str)  # 输出：Person(name='John', age=25)
#     print(type(person_str)) #输出：<class 'str'>
#
#     person = eval(person_str)
#     print(person) # 输出：Person(name='John', age=25)
#     print(type(person)) #输出：<class '__main__.Person'>


#sum/min/max/abs
# list=[1,2,3]
# print(sum(list)) #输出：6
# print(min(list)) #输出：1
# print(max(list)) #输出：3
# a=-1
# print(abs(a)) #输出：1
# b=-1.1
# print(abs(a)) #输出：1.1
# c=-(1+2j) #复数
# print(abs(c)) #输出：2.23606797749979

# complex()复数的表示
# 创建实部为4，虚部为-3的复数
# z1 = 4-3j
# z2 = complex(4, -3)


#zip(*iterables) 创建一个聚合了来自每个可迭代对象中的元素的迭代器。
# list1=['a','b','c']
# list2=[1,2,3]
# print(zip(list1,list2)) #输出：<zip object at 0x100dc3800>
# print(list(zip(list1,list2)))#输出：[('a', 1), ('b', 2), ('c', 3)]

#type()
# str1='a'
# bool1=True
# list1=[1,2,3]
# set1={1,2,3}
# tuple1=(1,2,3)
# dict1={'a':1}
# print(type(str1)) #<class 'list'>
# print(type(bool1)) #<class 'bool'>
# print(type(list1)) #<class 'list'>
# print(type(set1)) #<class 'set'>
# print(type(tuple1)) #<class 'tuple'>
# print(type(dict1)) #<class 'dict'>


#map(function, iterable, ...)
# 将一个函数应用到一个或多个可迭代对象中的每个元素，并返回一个新的可迭代对象，其中每个元素是原可迭代对象中对应元素经过函数处理后的结果。
#例子1：将一个列表中的元素全部转换为字符串：
# lst = [1, 2, 3, 4, 5]
# lst_str = list(map(str, lst))
# print(lst_str)  # 输出：['1', '2', '3', '4', '5']
# #例子2：两个列表中的元素按位置相加，并返回一个新的列表
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [10, 20, 30, 40, 50]
# lst_sum = list(map(lambda x, y: x + y, lst1, lst2))
# print(lst_sum)  # 输出：[11, 22, 33, 44, 55]


#bool()
# 1. 将整数转换为布尔值
# print(bool(0))     # False
# print(bool(10))    # True
# print(bool(-10))   # True
#
# # 2. 将浮点数转换为布尔值
# print(bool(0.0))   # False
# print(bool(3.14))  # True
#
# # 3. 将字符串转换为布尔值
# print(bool(''))    # False
# print(bool('foo')) # True
#
# # 4. 将列表、元组、字典等容器类型转换为布尔值
# print(bool([]))    # False


#locals() 返回当前作用域的所有局部变量和它们的值的字典。
#globals() 返回表示当前全局符号表的字典
# def test_func():
#     x = 10
#     y = 20
#     print(locals()) #输出：{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x1001b8cd0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/yanfa/PycharmProjects/hogwarts/function_inner.py', '__cached__': None, 'test_func': <function test_func at 0x100202280>}
#     print(globals()) ##输出：{'x': 10, 'y': 20}
#
# test_func()

#hash()返回一个对象的哈希值，通常用于字典中的键值对查找和比较。该函数只能接受一个参数.函数的参数必须是可哈希的对象，例如数字、字符串、元组等，而不支持不可哈希的对象，例如列表、字典等。如果尝试对不可哈希的对象调用 hash() 函数，会触发 TypeError 异常。
"""哈希值，也称为散列值或摘要，是将任意长度的数据通过哈希算法转换为固定长度的值。哈希算法是一种将数据映射到较小数据集的函数。哈希值通常用于对数据进行唯一标识、验证数据完整性以及快速查找数据。哈希值具有以下特点：

相同的输入数据必定产生相同的哈希值。
不同的输入数据产生的哈希值不同。
哈希值的长度固定。
哈希算法是单向的，即无法通过哈希值还原出原始数据。
常见的哈希算法包括MD5、SHA-1、SHA-256等。在Python中，可以使用hash()函数获取对象的哈希值"""
# hash() 用于获取数字的哈希值
# print(hash(10))
# print(hash(3.14))
# print(hash(-100))
#
# # hash() 用于获取字符串的哈希值
# print(hash('hello'))
# print(hash('world'))
# print(hash('python'))
#
# # hash() 用于获取元组的哈希值
# print(hash((1, 2, 3)))
# print(hash(('apple', 'banana', 'orange')))
# print(hash((1, 2, 'hello', 'world')))

#输出
# 10
# 1231051966567569402
# -100
# 8460651058384799857
# 2697156520147284760
# 8730113997671937973
# 529344067295497451
# 3308440409156982361
# 5876282949419969837

##操作对象属性
# getattr(): 从一个对象中获取指定的属性。如果该属性不存在，则可以提供一个默认值，如果没有提供默认值，则会抛出 AttributeError 异常。
# setattr()：给对象的属性赋值。如果对象中不存在该属性，则会新建该属性。
# hasattr()： 检查对象是否有指定的属性。
class Person:
    name = 'Tom'
    age = 20

p = Person()
print(getattr(p, 'name'))  # Tom
print(getattr(p, 'gender', 'unknown'))  # unknown

setattr(p, 'name', 'Jerry')
setattr(p, 'gender', 'male')

print(p.name)  # Jerry
print(p.gender)  # male

print(hasattr(p, 'name'))  # True
print(hasattr(p, 'gender'))  # False
