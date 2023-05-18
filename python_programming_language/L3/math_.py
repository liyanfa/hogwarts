# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 19:49
# @Author  : yanfa
# @user   : yanfa 
# @File    : math_.py
# @remark: 科学计算
"""了解math函数
python内置数学类函数库，包含很多数据公式。比如幂函数运算、三角函数、高等函数等"""

"""一、math函数操作
数字常数
数论与表示函数
幂对数函数
三角对数函数
高等特殊函数"""

"""数据常量
常数       数学表示      描述
math.pi	    π	圆周率，值为3.1415926535…
math.e	    e	自然对数，值为2.7182818…
math.inf	∞	正无穷大，负无穷-math.inf
math.nan	NAN	非数字 NAN(Not a Number) 
"""
import math

# print(math.pi) #输出：3.141592653589793
# print(math.e) #输出：2.718281828459045
# print(math.inf) #输出：inf
# print(-math.inf) #输出：-inf
# print(math.nan) #输出：nan


"""数论与表示函数
ceil(x): 向上取整
floor(x): 向下取整
factorial(x): 阶乘[阶乘是一个自然数 n 的阶乘，定义为从1到n所有正整数相乘的积，通常用符号 ! 表示，如：n! = 1 × 2 × 3 × … × (n-1) × n。当 n = 0 或 1 时，其阶乘为 1。]
perm(n,k=None): A k n =n!/(n-k)!=n(n−1)⋯(n−k+1) 排列是指从 n 个不同元素中取出 m 个元素进行排列，所得到的不同的排列数。
comb(n,k): 组合C k n = n!/(k!(n-k)!)= 组合（Combination）是指从 n 个不同元素中取出 m 个元素进行组合，所得到的不同的组合数。
gcd(a,b):最大公约数 [公约数（Common Divisor），指能够同时整除给定的两个或多个整数的数。也就是说，对于两个或多个整数而言，能够整除它们的公共因子就是它们的公约数。比如，10和15的公约数有1和5。公约数中最大的一个称为最大公约数（Greatest Common Divisor，简称GCD）或最大公因数。]
fsum(iterable):精确浮点值，比sum更精确
fabs(x):绝对值 fabs()使用浮点数时是首选，abs()使用整数时是首选
prod(iterable,x,start=1):计算输入的iterable所有元素的积，积的默认开始值是1
fmod(x,y):取余 fmod()使用浮点数时是首选，x%y使用整数时是首选
copysign(x,y):基于x的绝对值和y的符号的浮点数
frexp(x):以（m,e）的形式返回x的尾数和指数。m是一个浮点数，e是一个整数
isclose(a,b,*,rel_tol=le-09,abs_tol=0.0):a,b是否接近
        函数参数说明：
        a 和 b 是需要比较的两个数。
        rel_tol 是相对误差容限，如果两个数之间的相对差小于等于 rel_tol，则认为它们足够接近。默认值为 1e-9。
        abs_tol 是绝对误差容限，如果两个数之间的绝对差小于等于 abs_tol，则认为它们足够接近。默认值为 0.0。
"""
# ceil(x): 向上取整 大于它的最小值
# print(math.ceil(3.14)) #输出：4
# print(math.ceil(-3.14)) #输出：-3

# floor(x): 向下取整 小于它的最大值
# print(math.floor(3.14)) #输出：3
# print(math.floor(3.14)) #输出：-4

# factorial(x): 阶乘
# print(math.factorial(6)) #输出： 720 6！=6*5*4*3*2*1

# print(math.perm(4,2)) #输出： 12 排列 算出n-k+1=4-2+1=3 所以排列数=4*3
# print(math.comb(4,2)) #输出： 6 组合 算出4的阶乘=4*3*2*1=24 2的阶乘=2*1=2 4-2的阶乘=2*1 所以组合数=24/(2*2)=6

# gcd(a,b):最大公约数
# a=10
# b=15
# print(math.gcd(a,b)) #输出：5

# fsum(iterable) 浮点数求和 整数用内置函数sum()
# list_f=[1.1,2.2,3.3]
# print(math.fsum(list_f)) #6.6
# list_i=[1,2,3]
# print(sum(list_i)) #6

#fabs(x) 浮点数求和绝对值 整数用内置函数abs()
# print(math.fabs(-1.1))  #1.1
# print(math.fabs(-1))  #1.0 如果传入为整形也会转成浮点
# print(abs(-1))  #1
# print(abs(-1.1223))  #1.1223 如果传入为浮点也能处理

#prod(iterable,x,start=1):计算输入的iterable所有元素的积，积的默认开始值是1
# print(math.prod([1,2,3])) #6 如果不传start，则默认为1，则6*1=6
# print(math.prod([1,2,3],start=2)) #12 如果传start开始值为2，则2*1*2*3=12

#fmod(x,y):取余 fmod()使用浮点数时是首选，x%y使用整数时是首选
# result1 = math.fmod(7.5, 2)
# result2 = math.fmod(10, 3.5)
# result3 = math.fmod(-5.5, 3)
# result4 = math.fmod(2, 0)
# result5 = math.fmod(math.pi, 2)
# print(result1)  # 输出 1.5
# print(result2)  # 输出 3.0
# print(result3)  # 输出 -2.5
# print(result4)  # 输出 NaN
# print(result5)  # 输出 1.5707963267948966

#isclose(a,b,*,rel_tol=le-09,abs_tol=0.0):a,b是否接近
# print(math.isclose(10,9.98,rel_tol=0.01)) #True 相对误差=（9.99-9.98）/0.99=小于等于中的小于1%
# print(math.isclose(10,9,rel_tol=0.1)) #True 小于等于中的刚好等于10%
# print(math.isclose(10,9,rel_tol=0.01)) #False 大于（10-9）/10=10%

# print(math.isclose(9.99,9.98,abs_tol=0.01)) #True 绝对误差=9.99-9.98=0.01小于等于中的刚好等于
# print(math.isclose(9.99,9.98,abs_tol=0.02)) #True 小于等于中的小于
# print(math.isclose(9.99,9.96,abs_tol=0.02)) #False 大于

#相对误差是指一个量的误差与这个量本身的比值，而绝对误差是指一个量的误差的实际值。
# 相对误差和绝对误差是表示测量精度的两个指标，两者的大小关系可以反映出测量的精度。
# 相对误差一般用百分数表示，绝对误差一般用原量的单位表示。
#比如，对于一个测量值为5的量，如果其真实值为4.8，那么其绝对误差就是0.2，
# 而相对误差就是0.2/4.8=0.0417，即4.17%。如果一个测量方法的相对误差很小，
# 说明该方法的精度很高，反之则说明该方法的精度不高。而绝对误差则与测量量的大小有关，
# 比如，对于两个测量值分别为5和50的量，其绝对误差相同，但相对误差会更高。

"""扩展 迭代中的排列组合
在 Python 中，itertools 模块中提供了 combinations 和 permutations 函数，用于生成给定集合中元素的组合和排列。
combinations(iterable, r) 函数会生成 iterable 中长度为 r 的所有组合，返回一个迭代器。
permutations(iterable, r) 函数会生成 iterable 中长度为 r 的所有排列，返回一个迭代器。"""
# from itertools import combinations,permutations
#
# lst = [1, 2, 3, 4]
# comb = combinations(lst, 2)

# for i in comb:
#     print(i)
#输出
# (1, 2)
# (1, 3)
# (1, 4)
# (2, 3)
# (2, 4)
# (3, 4)

# perm = permutations(lst, 2)
#
# for i in perm:
#     print(i)
#输出
# (1, 2)
# (1, 3)
# (1, 4)
# (2, 1)
# (2, 3)
# (2, 4)
# (3, 1)
# (3, 2)
# (3, 4)
# (4, 1)
# (4, 2)
# (4, 3)

"""幂函数与对数函数
"""
# 返回x的y次幂
# print(math.pow(2,3)) #8.0=2*2*2

#返回x的平方根
# print(math.sqrt(4)) #2.0

"""三角函数"""
# 返回（x,y）坐标到远点的距离
# print(math.hypot(3,4)) #5.0
#
# #返回x的正弦函数值
# print(math.sin(3))
# #返回x的余弦函数值
# print(math.cos(3))
# #返回x的正切函数值
# print(math.tan(3))


"""高等函数"""
# 高斯误差函数
# print(math.erf(4))
# # 余补高斯误差函数
# print(math.erfc(4))
# # 伽马函数
# print(math.gamma(4))
# # 伽马函数的自然对数
# print(math.lgamma(4))


"""实战练习
实例1：
天天向上的力量

一年365天，以第1天的能力值为基数，记为1.0，
当努力学习时，能力值相比前一天提高1%，
当没有学习时能力值相比前一天下降1%。
（每天努力和每天放任，一年下来的能力值相差多少呢? ）"""

best,worst=1.0,1.0

for i in range(365):
    best*=1.01
    worst*=0.99
print(f"每天努力{best}") #37.78343433288713
print(f"每天放任{worst}") #0.025517964452291184
print(f"一年下来的能力值相差{round(best-worst,4)}") #一年下来的能力值相差37.7579