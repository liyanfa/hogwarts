# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 19:22
# @Author  : yanfa
# @user   : yanfa 
# @File    : function_.py
# @remark: 函数
""""""

"""一、函数的作用
函数是组织好的，可重复使用的，用来实现单一或者相关联功能的代码段
函数能提高应用的模块性和代码的重复利用率
python 69个内置函数：https://docs.python.org/zh-cn/3.8/library/functions.html
abs()：绝对值。abs(x)，返回一个数的绝对值。 参数可以是一个整数或浮点数。 如果参数是一个复数，则返回它的模。

all()：迭代元素是否全真。all(iterable)，如果 iterable 的所有元素均为真值（或可迭代对象为空）则返回 True。
 例如：a=[1,2,False] print(all(a))=》False; a=[] print(all(a))=》True
 
any()：迭代元素是否有真。any(iterable)，如果 iterable 的任一元素为真值则返回 True。 如果可迭代对象为空，返回 False。
a=[1,False,False] print(any(a))=》True; a=[] print(any(a))=》False

ascii()：
bin()：将一个整数转变为一个前缀为“0b”的二进制字符串。结果是一个合法的 Python 表达式。
        如果 x 不是 Python 的 int 对象，那它需要定义 __index__() 方法返回一个整数。
        例子：bin(3)=》'0b11'  format(14, 'b')=》'1110'
        
bool()：
breakpoint()：

bytearray()：class bytearray([source[, encoding[, errors]]])。返回一个新的 bytes 数组。 bytearray 类是一个可变序列，包含范围为 0 <= x < 256 的整数。
            它有可变序列大部分常见的方法，见 可变序列类型 的描述；同时有 bytes 类型的大部分方法

bytes()：class bytes([source[, encoding[, errors]]]).返回一个新的“bytes”对象， 
        是一个不可变序列，包含范围为 0 <= x < 256 的整数。bytes 是 bytearray 的不可变版本 - 它有其中不改变序列的方法和相同的索引、切片操作

callable()：是否可调用。callable(object)。如果参数 object 是可调用的就返回 True，否则返回 False。 
            如果返回 True，调用仍可能失败，但如果返回 False，则调用 object 将肯定不会成功。 
            请注意类是可调用的（调用类将返回一个新的实例）；如果实例所属的类有 __call__() 则它就是可调用的。
            例子：def sum(a,b):
                     sum=a+b
                    print(sum)
                print(callable(sum)) #True
            
chr()：

classmethod()：类方法装饰器。把一个方法封装成类方法。一个类方法把类自己作为第一个实参，就像一个实例方法把实例自己作为第一个实参。
                请用以下习惯来声明类方法:
                class C:
                    @classmethod
                    def f(cls, arg1, arg2, ...): ...

compile()：compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)。
            将source编译成代码或AST对象。代码对象可以被exec()或eval()执行。source可以是常规的字符串、字节字符串，或者AST对象。

complex()：返回值为 real + imag*1j 的复数，或将字符串或数字转换为复数。class complex([real[, imag]])
        例子：print(complex(3,2)) #(3+2j)
        
delattr()：

dict()：创建一个新的字典。dict 对象是一个字典类。参见 dict 和 映射类型 --- dict 了解这个类。
        class dict(**kwarg)
        class dict(mapping, **kwarg)
        class dict(iterable, **kwarg)

dir()：dir([object])
        如果没有实参，则返回当前本地作用域中的名称列表。如果有实参，它会尝试返回该对象的有效属性列表。
        例子：import time  dir(time)=>['CLOCK_MONOTONIC', 'CLOCK_MONOTONIC_RAW', 'CLOCK_PROCESS_CPUTIME_ID', 'CLOCK_REALTIME', 'CLOCK_THREAD_CPUTIME_ID', 'CLOCK_UPTIME_RAW', '_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'clock_getres', 'clock_gettime', 'clock_gettime_ns', 'clock_settime', 'clock_settime_ns', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname', 'tzset']

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
def fun_type(name:str="张三",age:int=18):
    print(f"传入的参数为{name}{age}")

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
# def fun_2(a,b=1,c):
#     print(f"传入参数为：{b}")

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

"""作用域
函数体外的是全局变量，函数内部的是局部变量"""

a=1 #全局变量
def num():
    # global a #局部访问全局变量
    b=1 ##局部变量
    c=a+1
print(a)