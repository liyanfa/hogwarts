# -*- coding: utf-8 -*-
# @Time    : 2023/4/28 17:14
# @Author  : yanfa
# @user   : yanfa 
# @File    : hj2.py
# @remark:计算某字符出现次数
"""描述
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）

数据范围：
1≤n≤1000
输入描述：
第一行输入一个由字母、数字和空格组成的字符串，第二行输入一个字符（保证该字符不为空格）。

输出描述：
输出输入字符串中含有该字符的个数。（不区分大小写字母）

示例1
输入：
ABCabc
A
输出：
2"""
input_str = input()  # 输入一行字符串
count_str=input()

while len(input_str) > 1000 or len(input_str) <1 :  # 判断字符串是否为空或长度是否大于5000
    print("输入非法，请输入1-1000直接的字符串，请重新输入。")
    input_str = input()
while count_str == "":  # 判断字符串是否为空或长度是否大于5000
    print("输入非法，不能输入空格，请重新输入。")
    count_str = input()

count=0
for i in input_str:
    if count_str.upper()==i or count_str.lower()==i:
        count+=1
    else:
        continue
print(count)