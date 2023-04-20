# -*- coding: utf-8 -*-
# @Time    : 2023/4/18 11:50
# @Author  : yanfa
# @user   : yanfa 
# @File    : p_6.py
# @remark:运算符

#1、算术运算符
a,b=4,2
print(a+b)  #加 6
print(a-b)  #减 2
print(a*b)  #乘 8
print(a/b)  #除 2.0
print(a%b)  #取模 0
print(a**b) #幂 16
print(a//b) #整除 2
b=3
print(a//b) #整除 向下取整1 4/3=1.33333=1
b=2.65
print(a//b) #整除 向下取整4/2.65=1.50943=1.0

#2、比较运算符
a,b=4,2
print(a==b)  #等于 False
print(a!=b)  #不等于 True
print(a>b)  #大于 True
print(a<b)  #小于 False
print(a>=b)  #大于等于 False
print(a<=b) #小于等于 False

#3、赋值运算符
a=1 #简单赋值
print(a)
a,b=1,2 #多个变量赋值
print(a)
print(b)

a+=1
print(a) #加法赋值 自增 a=a+1 <==> a+=1 1+1=2
a-=1
print(a) #减法赋值 自减 2-1=1
a*=1
print(a) #乘法赋值  2*1=2
a/=1
print(a) #除法赋值  2/1=2
a%=1
print(a) #取模赋值  2/1=2 余数为0.0
a=2
a**=1
print(a) #幂赋值  2^1=2
a=2
a//=1
print(a) #整除赋值 2/1=2

#4、逻辑运算符 and or not
a,b=1,2
print(a==1 and b==2) #True
print(a==1 or b==2) #True
print(not a==1) #False

#5、成员运算符 in 、not in 右边是序列
a=[1,2,3]
b=1
print(b in a) #True
print(b not in a) #False

#6、身份运算符 is 、is not
a=[1,2,3]
b=[1,2,3]
print(a is b) #False  内存地址不一致
print(id(a))
print(id(b))

print(a is not b) #True
print(a==b) #True
