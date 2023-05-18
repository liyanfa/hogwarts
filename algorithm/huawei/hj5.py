# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 17:46
# @Author  : yanfa
# @user   : yanfa 
# @File    : hj5.py
# @remark: 进制转换

"""
描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。

数据范围：保证结果在

1≤n≤2^31-1

输入描述：
输入一个十六进制的数值字符串。

输出描述：
输出该数值的十进制字符串。不同组的测试用例用\n隔开。

示例1
输入：
0xAA
输出：
170
"""
input_str = input()  # 输入一行字符串

input_str_10 = int(input_str, 16)  # 转为十进制
# 判断数据范围，不符合重新输入
while input_str_10 < 1 or input_str_10 >2e31:
    print("转为10进制后的结果范围必须为：1≤n≤2^31-1,请重新输入")
    input_str = input()
    input_str_10 = int(input_str, 16)  # 转为十进制
    print(input_str_10)
print(input_str_10)

"""扩展"""
#1、十进制转二进制、八进制、十六进制：
# num = 42
# bin_num = bin(num)  # 十进制转二进制
# oct_num = oct(num)  # 十进制转八进制
# hex_num = hex(num)  # 十进制转十六进制
#
# print(bin_num)  # 0b101010
# print(oct_num)  # 0o52
# print(hex_num)  # 0x2a
#
# #2、二进制、八进制、十六进制转十进制：
# bin_num = '101010'
# oct_num = '52'
# hex_num = '2a'
#
# dec_num_from_bin = int(bin_num, 2)  # 二进制转十进制
# dec_num_from_oct = int(oct_num, 8)  # 八进制转十进制
# dec_num_from_hex = int(hex_num, 16)  # 十六进制转十进制
#
# print(dec_num_from_bin)  # 42
# print(dec_num_from_oct)  # 42
# print(dec_num_from_hex)  # 42
