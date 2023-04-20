# -*- coding: utf-8 -*-
# @Time    : 2023/4/18 20:58
# @Author  : yanfa
# @user   : yanfa 
# @File    : p_7.py
# @remark: 分支判断/循环

# 1、for in 循环
# 构造0-100的偶数序列
import random

for i in range(0,101,2):
    print(i)

# 2、while循环
count = 0
while count < 100:
    count += 1
    print(count)
    if count == 3:
        pass  # pass占位
    elif count == 9:
        break  # 跳出整个循环
    else:
        continue  # 跳出当次，进入下一循环

#  3、练习
# 3-1、使用分支结构实现1~100之间的偶数求和

sum,end=0,100
for i in range(1,end+1):
    if i%2==0:
        sum+=i
    else:
        continue
print(sum)

#3-2、不使用分支结构实现1~100之间的偶数求和
sum,end=0,100
for i in range(0,end+1,2):
    sum += i
print(sum)

"""猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别
给出提示大一点/小一点/猜对了"""

while True:
    computer_num = random.randint(1, 100)
    people_num = int(input("请输入数字："))
    if people_num<computer_num:
        print(f"电脑数字为：{computer_num}")
        print(f"你的数字为：{people_num}")
        print("大一点")
    elif people_num>computer_num:
        print(f"电脑数字为：{computer_num}")
        print(f"你的数字为：{people_num}")
        print("小一点")
    else:
        print(f"电脑数字为：{computer_num}")
        print(f"你的数字为：{people_num}")
        print("猜对了")
        break

"""课后练习
奇数-不能被2整除的数
"""
#不使用分支结构实现1~100之间的奇数求和
sum=0
for i in range(1,100,2):
    print(i)
    sum+=i
print(f"1~100之间的奇数求和为：{sum}")

#使用while语句实现1~100之间的奇数求和
num,sum=0,0
while num<100:
    num+=1
    print(f"num:{num}")
    if num%2 !=0:
        sum+=num
        print(f"sum:{sum}")
    else:
        continue
print(f"1~100之间的奇数求和为：{sum}")
