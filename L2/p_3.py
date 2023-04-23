# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 23:08
# @Author  : yanfali
# @File    : p_3.py
# @Software: 多态与super
""""""
"""一、多态的概念
多态Polymorphism：同名方法呈现多种行为"""
"""二、运算符的多态表现
+号
1/加法：数字+数字  print(1+1) #2
2/拼接：字符串+字符串 print("a"+"b") #ab
3/合并：列表+列表 print([1,2]+[3,4]) #[1, 2, 3, 4]

len()函数
1/可以接收字符串 print(len("abc")) #3 
2/可以接收列表 print(len([1,2,3])) #3

同名变量"""

class China:
    def speak(self):
        print("汉语")

class Usa:
    def speak(self):
        print("english")

#实例化对象
cn=China()
en=Usa()

#遍历
for x in (cn,en):
    print(x)

"""三、多态与继承"""