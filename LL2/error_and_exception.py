# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 20:37
# @Author  : yanfa
# @user   : yanfa 
# @File    : error_and_exception.py
# @remark: 错误与异常
""""""

"""一、错误
1、语法错误
2、逻辑错误
3、系统错误"""

#1、语法错误 如SyntaxError: invalid syntax
# num=1
# if num>1
#     print("num>1")

#2、逻辑错误
num=1
if num>1:
    print("num<1")

#3、系统错误

"""二、异常
❖ 异常即是⼀个事件，该事件会在程序执⾏过程中发⽣，影响了程序的正常执⾏。
❖ 有些是由于拼写、配置、选项等等各种引起的程序错误，有些是由于程序功能处理逻辑不完善引起的漏
洞，这些统称为程序中的异常"""
def div(a,b):
    return a/b
print(3/0)  #ZeroDivisionError: division by zero

"""三、异常和错误的区别
错误与异常都是在程序编译和运⾏时出现的错误
❖ 异常可以被开发⼈员捕捉和处理
❖ 错误⼀般是系统错误，⼀般不需要开发⼈员处理（也⽆法处理），⽐如内存溢出"""

"""四、场景的异常类型
除零异常、名称异常、索引异常、键异常、值异常、属性异常、类型异常"""
#名称异常
num=1
print(name) #NameError: name 'name' is not defined

#索引异常
a=[1,2]
print(a[3]) #IndexError: list index out of range

#键异常
a={"a":1}
print(a["b"]) #KeyError: 'b'

#值异常
num="1"
if num>1:
    print(num)

#类型异常
a='1'
print(a+2) #TypeError: can only concatenate str (not "int") to str

"""五、异常处理
各种异常继承自-》Exception-》BaseException-》object"""

#1、异常捕获
try:
    pass
except Exception as e: #可以指定很细的异常如ValueError，也可以都捕获用Exception
    pass #有异常会执行
else:
    pass #没异常时执行
finally:
    pass #都最终会执行

#2、异常抛出 raise
def raise_num(num):
    if num<100:
        raise ValueError(f"值错误：{num}")
    else:
        print("可输入的数字不能大于等于100")

raise_num(40) #ValueError: 值错误：40



#3、自定义异常
class MyException(Exception):

    def __init__(self,value):
        self.value=value

    def __str__(self):
        return repr(self.value)