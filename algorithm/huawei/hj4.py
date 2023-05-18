# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 10:18
# @Author  : yanfa
# @user   : yanfa 
# @File    : hj4.py
# @remark: 字符串分隔
"""
描述
•输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；

•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述：
连续输入字符串(每个字符串长度小于等于100)

输出描述：
依次输出所有分割后的长度为8的新字符串

示例1
输入：
abc
输出：
abc00000
"""
input_str = input()  # 输入一行字符串

while len(input_str) < 1 or len(input_str) > 100:
    if len(input_str) > 100:
        print("每个字符串长度小于等于100，请重新输入。")
        input_str = input()
    else:
        print("输入空字符串不处理，请重新输入。")

# 按8个分隔
input_str_list = [input_str[i:i + 8] for i in range(0, len(input_str), 8)]
# print(input_str_list)
for i in input_str_list:
    if len(i) != 8:
        i += (8 - len(i)) * '0'
        print(i)
    else:
        print(i)
        continue
