# -*- coding: utf-8 -*-
# @Time    : 2023/5/6 10:33
# @Author  : yanfa
# @user   : yanfa 
# @File    : hj7.py
# @remark: 取近似值
"""
描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于 0.5 ,向上取整；小于 0.5 ，则向下取整。

数据范围：保证输入的数字在 32 位浮点数范围内
输入描述：
输入一个正浮点数值

输出描述：
输出该数值的近似整数值

示例1
输入：
5.5
输出：
6
说明：
0.5>=0.5，所以5.5需要向上取整为6
示例2
输入：
2.499
输出：
2
说明：
0.499<0.5，2.499向下取整为2
"""
import math

input_str = float(input())  # 输入一行字符串

# 判断数据范围，不符合重新输入
while str(type(input_str))!="<class 'float'>" and input_str<0:
    print("必须输入正浮点,请重新输入")
    input_str = float(input())

if int(str(input_str).split('.')[1][0])>=5:
    print(math.ceil(input_str))
else:
    print(math.floor(input_str))
