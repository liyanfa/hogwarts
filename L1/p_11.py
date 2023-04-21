# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 19:22
# @Author  : yanfa
# @user   : yanfa 
# @File    : p_11.py
# @remark: 函数
""""""

"""一、函数的作用
函数是组织好的，可重复使用的，用来实现单一或者相关联功能的代码段
函数能提高应用的模块性和代码的重复利用率
python 69个内置函数：https://docs.python.org/zh-cn/3.8/library/functions.html
abs()：绝对值。abs(x)，返回一个数的绝对值。 参数可以是一个整数或浮点数。 如果参数是一个复数，则返回它的模
all()：
any()：
ascii()：
bin()：
bool()：
breakpoint()：
bytearray()：
bytes()：
callable()：
chr()：
classmethod()：
compile()：
complex()：
delattr()：
dict()：
dir()：
divmod()：
enumerate()：
eval()：
exec()：
filter()：
float()：
format()：
frozenset()：
getattr()：
globals()：
hasattr()：
hash()：
help()：
hex()：
id()：
input()：
int()：
isinstance()：
issubclass()：
iter()：
len()：
list()：
locals()：
map()：
max()：
memoryview()：
min()：
next()：
object()：
oct()：
open()：
ord()：
pow()：
print()：
property()：
range()：
repr()：
reversed()：
round()：
set()：
setattr()：
slice()：
sorted()：
staticmethod()：
str()：
sum()：
super()：
tuple()：
type()：
vars()：
zip()：
__import__()："""

"""二、函数的定义
def:函数关键字
function_name:函数名称
parameter_list:可选，指定向函数的参数
def function_name([parameter_list]):
    ['''xxx''']
    [function_body]
注意缩进：python通过严格的缩进来判断代码块
    函数体和注释相对def关键字保持一定的缩进，一般4个空格"""

def fun_a(a,b,c):
    """这是一个函数"""
    print(f"传入的参数为{a}{b}{c}")

#打印函数comments内容
print(fun_a.__doc__) #这是一个函数
help(fun_a)

#定义空函数
#1、comments
def fun_demo1():
    """这是一个函数"""
#2、pass占位
def fun_demo2():
    pass

"""三、函数调用"""
#无参数
def fun_demo3():
    """函数"""
    print("这是函数")

fun_demo3()  #这是函数

#有参数
def fun_demo4(a,b,c):
    """这是一个函数"""
    print(f"传入的参数为{a}{b}{c}")

fun_demo4(1,2,3) #传入的参数为123

"""四、函数传递
形式参数：定义函数时，函数名称后面括号中的参数 abc
实际参数：调用函数时，函数名称后面括号中的参数 123"""

"""五、位置函数
数量必须与定义一致
位置必须与定义一致"""
#1、错误例子-数量错误
fun_demo4(1,2)  #TypeError: fun_demo4() missing 1 required positional argument: 'c'
fun_demo4(1,2,3,4)  #TypeError: fun_demo4() takes 3 positional arguments but 4 were given
#2、错误例子-位置传错
def person(name,age):
    print(f"姓名为：{name}")
    if age>=18:
        print(f"{name}已成年")
person(20,"yanfa")  #TypeError: '>=' not supported between instances of 'str' and 'int'
person("yanfa",20) #姓名为：yanfa yanfa已成年


"""六、关键字参数
使用形式参数的名字确定输入的参数值
不需要与形式参数的位置完全一致"""
def fun_demo4(a,b,c):
    """这是一个函数"""
    print(f"传入的参数为{a}{b}{c}")
fun_demo4(a=1,c=3,b=2)  #传入的参数为123

"""七、为参数设置默认值
定义函数时可以指定形式参数的默认值,需要是不可变对象如数字/字符串/元祖，否则默认值会随着调用发生变化
指定默认值的形式参数必须放在所有参数的最后，否则会产生语法错误
param=default_value:可选，指定参数并且为该函数设置默认值为default_value
def function_name(...,[param=default_value]
    [function_body]"""

#1、不传参数
def fun_1(b=0):
    print(f"传入参数为：{b}")
fun_1()  #传入参数为：0

#2、错误示例-默认值不放最后
def fun_2(a,b=1,c):
    print(f"传入参数为：{b}")

#3、错误示例，默认值为空列表
#需要是不可变对象如数字/字符串/元祖，否则默认值会随着调用发生变化
def fun_3(a,b,c=[]):
    c.append(a)
    c.append(b)
    print(f"传入参数为：{a} {b} {c}")
fun_3(1,2) #传入参数为：1 2 [1, 2]
fun_3(3,4) #传入参数为：3 4 [1, 2, 3, 4]

"""函数返回值
return [value]
"""
#1、不传值则返回None
def sum(a,b):
    result=a+b
    return

res=sum(1,2)
print(res) #None

#2、返回一个值
def sum(a,b):
    result=a+b
    return result
res=sum(1,2)
print(res) #3

#3、返回多个值，用逗号分隔，作为元祖
def sum(a,b):
    result=a+b
    return result,a,b
res=sum(1,2)
print(res) #(3, 1, 2)
print(type(res)) #<class 'tuple'>