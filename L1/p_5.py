# -*- coding: utf-8 -*-
# @Time    : 2023/4/17 21:13
# @Author  : yanfa
# @user   : yanfa 
# @File    : p_5.py
# @remark:字符串

#不指定位置，按默认顺序
a="{} {}".format("h","e")
print(a)
# 设置指定位置
a="{0} {1}".format("h","e")
print(a)
b="{1} {0}".format("h","e")
print(b)
#通过名称传递变量
c="我的性别是{sex}".format(sex="男")

#常用api
#1、join将元素拼接=> hello
a=["h","e","l","l","o"]
print("".join(a))
#join将元素根据｜拼接 =>h｜e｜l｜l｜o
print("｜".join(a))

#2、切分split=> ['my', 'name']
a="my name"
print(a.split())

#3、替换replace
a="my name is a"
print(a.replace("a","b"))

#4、取消首位空格
a=" my name "
print(a.strip())