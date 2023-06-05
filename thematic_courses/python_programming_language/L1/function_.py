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

all()：迭代元素是否全真。all(iterable)，如果 iterable 的所有元素均为真值（或可迭代对象为空）则返回 True。
 例如：a=[1,2,False] print(all(a))=》False; a=[] print(all(a))=》True
 
any()：迭代元素是否有真。any(iterable)，如果 iterable 的任一元素为真值则返回 True。 如果可迭代对象为空，返回 False。
a=[1,False,False] print(any(a))=》True; a=[] print(any(a))=》False

breakpoint()：

bytearray()：class bytearray([source[, encoding[, errors]]])。返回一个新的 bytes 数组。 bytearray 类是一个可变序列，包含范围为 0 <= x < 256 的整数。
            它有可变序列大部分常见的方法，见 可变序列类型 的描述；同时有 bytes 类型的大部分方法

callable()：是否可调用。callable(object)。如果参数 object 是可调用的就返回 True，否则返回 False。 
            如果返回 True，调用仍可能失败，但如果返回 False，则调用 object 将肯定不会成功。 
            请注意类是可调用的（调用类将返回一个新的实例）；如果实例所属的类有 __call__() 则它就是可调用的。
            例子：def sum(a,b):
                     sum=a+b
                    print(sum)
                print(callable(sum)) #True
            
chr()：chr(i)
        返回 Unicode 码位为整数 i 的字符的字符串格式。例如，chr(97) 返回字符串 'a'，chr(8364) 返回字符串 '€'。这是 ord() 的逆函数。
        实参的合法范围是 0 到 1,114,111（16 进制表示是 0x10FFFF）。如果 i 超过这个范围，会触发 ValueError 异常。

classmethod()：类方法装饰器。把一个方法封装成类方法。一个类方法把类自己作为第一个实参，就像一个实例方法把实例自己作为第一个实参。
                请用以下习惯来声明类方法:
                class C:
                    @classmethod
                    def f(cls, arg1, arg2, ...): ...
staticmethod()： 静态方法装饰器
super()：重写父类同名方法
property()： 

compile()：compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)。
            将source编译成代码或AST对象。代码对象可以被exec()或eval()执行。source可以是常规的字符串、字节字符串，或者AST对象。
       
delattr()：


dir()：dir([object])
        如果没有实参，则返回当前本地作用域中的名称列表。如果有实参，它会尝试返回该对象的有效属性列表。
        例子：import time  dir(time)=>['CLOCK_MONOTONIC', 'CLOCK_MONOTONIC_RAW', 'CLOCK_PROCESS_CPUTIME_ID', 'CLOCK_REALTIME', 'CLOCK_THREAD_CPUTIME_ID', 'CLOCK_UPTIME_RAW', '_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'clock_getres', 'clock_gettime', 'clock_gettime_ns', 'clock_settime', 'clock_settime_ns', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname', 'tzset']

divmod()：

enumerate()：enumerate(iterable, start=0) 枚举
            返回一个枚举对象。iterable 必须是一个序列，或 iterator，或其他支持迭代的对象。 enumerate() 返回的迭代器的 __next__() 方法返回一个元组，里面包含一个计数值（从 start 开始，默认为 0）和通过迭代 iterable 获得的值。
            例子1：
            seasons = ['Spring', 'Summer', 'Fall', 'Winter']
            list(enumerate(seasons))
            >>>[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
            list(enumerate(seasons, start=1))
            >>>[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
            例子2：
            for index,i in enumerate(seasons):
                
exec()： exec(object[, globals[, locals]]) 动态执行代码
这个函数支持动态执行 Python 代码。 object 必须是字符串或者代码对象。 如果是字符串，那么该字符串将被解析为一系列 Python 语句并执行（除非发生语法错误）。 1 如果是代码对象，它将被直接执行。 
在任何情况下，被执行的代码都应当是有效的文件输入（见参考手册中的“文件输入”一节）。 请注意即使在传递给 exec() 函数的代码的上下文中，nonlocal, yield 和 return 语句也不能在函数定义以外使用。 
该函数的返回值是 None。 filter()： 
        例子：exec("print('执行代码')")  #执行代码
        
frozenset()： 


oct()：八进制 
hex()： 十六进制
int()： 十进制 
bin()：将一个整数转变为一个前缀为“0b”的二进制字符串。结果是一个合法的 Python 表达式。
        如果 x 不是 Python 的 int 对象，那它需要定义 __index__() 方法返回一个整数。
        例子：bin(3)=》'0b11'  format(14, 'b')=》'1110'
        #1、十进制转二进制、八进制、十六进制：
        # num = 42
        # bin_num = bin(num)  # 十进制转二进制
        # oct_num = oct(num)  # 十进制转八进制
        # hex_num = hex(num)  # 十进制转十六进制
        #
        # print(bin_num)  # 0b101010
        # print(oct_num)  # 0o52
        # print(hex_num)  # 0x2a
        
        # #2、二进制、八进制、十六进制转十进制：
        # bin_num = '101010'
        # oct_num = '52'
        # hex_num = '2a'
        #
        # dec_num_from_bin = int(bin_num, 2)  # 二进制转十进制
        # dec_num_from_oct = int(oct_num, 8)  # 八进制转十进制
        # dec_num_from_hex = int(hex_num, 16)  # 十六进制转十进制
        
        # print(dec_num_from_bin)  # 42
        # print(dec_num_from_oct)  # 42
        # print(dec_num_from_hex)  # 42

isinstance()： 是否为实例对象
issubclass()： 是否为子类
 
locals()： 返回当前作用域的所有局部变量和它们的值的字典。
globals()： 返回表示当前全局符号表的字典。这总是当前模块的字典（在函数或方法中，不是调用它的模块，而是定义它的模块）。
        例子：
        def test_func():
            x = 10
            y = 20
            print(locals()) #输出：{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x1001b8cd0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/yanfa/PycharmProjects/hogwarts/function_inner.py', '__cached__': None, 'test_func': <function test_func at 0x100202280>}
            print(globals()) #输出：{'x': 10, 'y': 20}

        test_func() 
        
memoryview()： 返回由给定实参创建的“内存视图”对象
 
next()： next(iterator[, default]) 下一元素
        通过调用 iterator 的 __next__() 方法获取下一个元素。如果迭代器耗尽，则返回给定的 default，如果没有默认值则触发 StopIteration。
        例子：
        my_list = [1, 2, 3, 4, 5]
        my_iterator = iter(my_list)
        while True:
            try:
                next_element = next(my_iterator)
                print(next_element)
            except StopIteration:
                break
                
iter()： iter(object[, sentinel]) 转迭代对象
        返回一个 iterator 对象。根据是否存在第二个实参，第一个实参的解释是非常不同的。如果没有第二个实参，object 
        必须是支持迭代协议（有 __iter__() 方法）的集合对象，或必须支持序列协议（有 __getitem__() 方法，且数字参数从 0 开始）。
        如果它不支持这些协议，会触发 TypeError。如果有第二个实参 sentinel，那么 object 必须是可调用的对象。这种情况下生成的迭代器，
        每次迭代调用它的 __next__() 方法时都会不带实参地调用 object；如果返回的结果是 sentinel 则触发 StopIteration，否则返回调用结果。
        序列类型有list, tuple 和 range 对象
        例子：同上
               
 
open()：打开文件 
ord()： 
pow()： 
print()： 控制台打印
input()： 控制台输入

repr()： repr(object)
        用于将一个对象转换为一个可打印的字符串表示形式，通常用于调试和开发过程中。该函数返回的字符串可以通过 eval() 函数来还原出原始对象。
        在实际开发中，常常使用 repr() 函数将对象的字符串表示形式打印到日志中，方便调试。
        例子：
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def __repr__(self):
                return f"Person(name='{self.name}', age={self.age})"
        
        if __name__ == '__main__':
            person = Person("John", 25)
            person_str = repr(person)
            print(person_str)  # 输出：Person(name='John', age=25)
            print(type(person_str)) #输出：<class 'str'>
ascii()：与 repr() 类似，返回一个包含对象的可打印表示形式的字符串，但是使用 \x、\u 和 \U 对 repr() 返回的字符串中非 ASCII 编码的字符进行转义。 生成的字符串和 Python 2 的 repr() 返回的结果相似。

eval()：eval(expression[, globals[, locals]]) 表达式求值
        实参是一个字符串，以及可选的 globals 和 locals。globals 实参必须是一个字典。locals 可以是任何映射对象。
        expression 参数会作为一个 Python 表达式（从技术上说是一个条件列表）被解析并求值，并使用 globals 和 locals 字典作为全局和局部命名空间。
        例子1：
            x=1
            eval('x+1')  #2
        例子2：    
            person = eval(person_str)
            print(person) # 输出：Person(name='John', age=25)
            print(type(person)) #输出：<class '__main__.Person'>
            

round()： round(number[, ndigits]) 求精度
        返回 number 舍入到小数点后 ndigits 位精度的值
        例子：a=1.2345
            print(round(a,2)) #1.23
            
bytes()：class bytes([source[, encoding[, errors]]]).返回一个新的“bytes”对象， 
        是一个不可变序列，包含范围为 0 <= x < 256 的整数。bytes 是 bytearray 的不可变版本 - 它有其中不改变序列的方法和相同的索引、切片操作            
str()： 返回字符串对象            
float()： 返回浮点对象
set()：返回集合对象
list()： 返回列表对象
tuple()：返回元祖对象
dict()：创建一个新的字典。dict 对象是一个字典类。参见 dict 和 映射类型 --- dict 了解这个类。
        class dict(**kwarg)
        class dict(mapping, **kwarg)
        class dict(iterable, **kwarg)
range()： 不可变的序列类型
map()： 返回一个将 function 应用于 iterable 中每一项并输出其结果的迭代器
        # 将一个函数应用到一个或多个可迭代对象中的每个元素，并返回一个新的可迭代对象，其中每个元素是原可迭代对象中对应元素经过函数处理后的结果。
        #例子1：将一个列表中的元素全部转换为字符串：
        lst = [1, 2, 3, 4, 5]
        lst_str = list(map(str, lst))
        print(lst_str)  # 输出：['1', '2', '3', '4', '5']
        #例子2：两个列表中的元素按位置相加，并返回一个新的列表
        lst1 = [1, 2, 3, 4, 5]
        lst2 = [10, 20, 30, 40, 50]
        lst_sum = list(map(lambda x, y: x + y, lst1, lst2))
        print(lst_sum)  # 输出：[11, 22, 33, 44, 55]
bool()：返回bool对象，给定的参数转换为对应的布尔值。如果参数是一个假值，那么bool()函数将返回False，否则返回True。
        什么是假值：
        在Python中，一个值被视为假值（False）的条件是：
            False：布尔类型，表示假。
            None：表示空或缺失的值。
            0：表示整数的零。
            0.0：表示浮点数的零。
            ''：表示空字符串。
            []、()、{}：表示空的列表、元组、字典等容器类型。
            set()：表示空集合。
            其他自定义对象：如果对象定义了__bool__()方法（Python 3.x）或者__nonzero__()方法（Python 2.x）并返回False，那么该对象也被视为假值。
            除了上述值外，其他所有值都被视为真值（True）。在进行布尔运算时，Python会自动将操作数转换为对应的布尔值，然后执行运算。
hash()：返回该对象的哈希值（如果它有的话）。哈希值是整数。它们在字典查找元素时用来快速比较字典的键。相同大小的数字变量有相同的哈希值（即使它们类型不同，如 1 和 1.0）。 
        例子:
        # hash() 用于获取数字的哈希值
        print(hash(10)) #10
        print(hash(3.14)) #322818021289917443
        print(hash(-100)) #-100

        # hash() 用于获取字符串的哈希值
        print(hash('hello')) #5688181077494711701
        print(hash('world')) #-1269255543628528962
        print(hash('python')) #-6487319042922840049
        
        # hash() 用于获取元组的哈希值
        print(hash((1, 2, 3))) #529344067295497451
        print(hash(('apple', 'banana', 'orange'))) #3971057772394176090
        print(hash((1, 2, 'hello', 'world'))) #-5631078449820410852

##操作对象属性
getattr(): 从一个对象中获取指定的属性。如果该属性不存在，则可以提供一个默认值，如果没有提供默认值，则会抛出 AttributeError 异常。    
setattr()：给对象的属性赋值。如果对象中不存在该属性，则会新建该属性。 
hasattr()： 检查对象是否有指定的属性。
    例子：
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
    
slice()：
 
sorted()： 
reversed()：
 
abs()：绝对值。abs(x)，返回一个数的绝对值。 参数可以是一个整数或浮点数。 如果参数是一个复数，则返回它的模。
complex()：返回值为 real + imag*1j 的复数，或将字符串或数字转换为复数。class complex([real[, imag]])
        例子：print(complex(3,2)) #(3+2j)
sum()：求和 sum(iterable, /, start=0) 
max()：求最大 max(arg1, arg2, *args[, key])
min()：求最小 min(iterable, *[, key, default])
例子：
    list=[1,2,3]
    print(sum(list)) #输出：6
    print(min(list)) #输出：1
    print(max(list)) #输出：3
 
 
type()： type(object) 对象类型
        例子：
            str1='a'
            bool1=True
            list1=[1,2,3]
            set1={1,2,3}
            tuple1=(1,2,3)
            dict1={'a':1}
            print(type(str1)) #<class 'list'>
            print(type(bool1)) #<class 'bool'>
            print(type(list1)) #<class 'list'>
            print(type(set1)) #<class 'set'>
            print(type(tuple1)) #<class 'tuple'>
            print(type(dict1)) #<class 'dict'>
id()： 获取内存地址
len()： 获取对象长度 
format()： 格式化
help()： 查看帮助文档 例子:help(os)
object()： 
 
zip()：创建一个聚合了来自每个可迭代对象中的元素的迭代器。
        例子：
            list1=['a','b','c']
            list2=[1,2,3]
            print(zip(list1,list2)) #输出：<zip object at 0x100dc3800>
            print(list(zip(list1,list2)))#输出：[('a', 1), ('b', 2), ('c', 3)]
            
__import__()： """

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