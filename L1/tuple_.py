# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 20:18
# @Author  : yanfa
# @user   : yanfa 
# @File    : tuple_.py
# @remark:数据结构-元祖
""""""

"""一、元祖定义：
元祖是有序的不可变对象的集合
元祖使用小括号(),各个对象之间使用逗号，分隔
元祖是异构的，可以包含多种数据类型"""

"""二、元祖的使用：创建"""
# 1、直接使用逗号分隔
tup1 = 1, 2, 3, 4
print(type(tup1), tup1)

# 2、通过小括号填充元素
tup2 = (1, 2, 3, 4)
print(type(tup2), tup2)

# 3、通过构造函数 要为空或者可迭代对象，否则TypeError: 'xx' object is not iterable
tup3 = tuple()
print(type(tup3), tup3)  # 不传默认为（）
tup4 = tuple('hello')
print(type(tup4), tup4)  # 不传默认为（）
tup5 = tuple([1, 2, 3, 4, 5])
print(type(tup5), tup5)  # 不传默认为（）
##异常
tup4 = tuple(1)  # TypeError: 'int' object is not iterable

# 注意：单元素元祖，逗号不可缺少
tup6 = 1,
print(type(tup6), tup6)  # <class 'tuple'> (1,)
tup7 = (2,)
print(type(tup7), tup7)  # <class 'tuple'> (2,)
##不加逗号
tup7 = (2)
print(type(tup7), tup7)  # <class 'int'> 2

"""三、元祖的使用：索引切片与列表一致"""

"""四、元祖的常用方法："""
# 1、index
# index(item)
# 返回与目标元素相匹配的首个元素的索引
# 目标值必须在元祖中存在，否则会报错
li = 1, 2, 3
print(li.index(3))  # 2
print(li.index(4))  # ValueError: tuple.index(x): x not in tuple

# 2、conut
# index(item)
# 返回某个元素出现的次数
# 返回：次数
li = (1, 2, 3, 3, 3, 3)
print(li.count(3))  # 4
print(li.count(4))  # 如果输入不存在的对象则为0 0

"""五、元祖解包
把一个可迭代对象里的元素，一并赋值到由对应的变量组成的元祖中"""
# 1、传统逐一赋值 繁琐
t = (1, 2, 3)
a = t[0]
b = t[1]
c = t[2]
print(a, b, c)

# 2、使用元祖解包，一气呵成
a, b, c = [1, 2, 3]
print(a, b, c)  # 1 2 3

a, b, c = (1, 2, 3)
print(a, b, c)  # 1 2 3

"""六、元祖与列表的比较"""
"""
1、相同点：
1）都是有序的
2）都是异构的，能包含不同数据类型的对象
3）都支持索引和切片
2、区别：
1）声明方式不同，元祖使用()，列表使用[]
2)列表可变支持增删改，元祖不可变
"""
