# -*- coding: utf-8 -*-
# @Time    : 2023/4/28 16:50
# @Author  : yanfa
# @user   : yanfa 
# @File    : hj1.py
# @remark:字符串最后一个单词的长度
"""描述
计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
输入描述：
输入一行，代表要计算的字符串，非空，长度小于5000。

输出描述：
输出一个整数，表示输入字符串最后一个单词的长度。

示例1
输入：
hello nowcoder
复制
输出：
8
复制
说明：
最后一个单词为nowcoder，长度为8   """

str_a = input()  # 输入一行字符串
while not str_a or len(str_a) > 5000:  # 判断字符串是否为空或长度是否大于5000
    print("输入的字符串非法，请重新输入。")
    str_a = input()

print(len(str_a.split()[-1]))



