# -*- coding: utf-8 -*-
# @Time    : 2023/5/6 10:50
# @Author  : yanfa
# @user   : yanfa 
# @File    : hj8.py
# @remark: 合并表记录

"""描述
数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。


提示:
0 <= index <= 11111111
1 <= value <= 100000

输入描述：
先输入键值对的个数n（1 <= n <= 500）
接下来n行每行输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）

示例1
输入：
4
0 1
0 2
1 2
3 4
输出：
0 3
1 2
3 4
示例2
输入：
3
0 1
0 2
8 9
输出：
0 3
8 9"""

# input_str =input()  # 输入一个正整数
#
# # 判断数据范围，不符合重新输入
# while str(type(input_str))!="<class 'int'>" and int(input_str)<0 and int(input_str)>500 :
#     print("必须输入1-500的正整数键值对数,请重新输入")
#     input_str = input()
# # 定义列表存储键值对
# my_list=[]
# for i in range(int(input_str)):
#     key, value = map(int,input().split(" ")) # 使用逗号分隔
#     while key<0 or key>11111111 or value<1 or value>100000:
#         print("0 <= index <= 11111111,1 <= value <= 100000,请重新输入")
#         key, value = map(int, input().split(" "))  # 使用逗号分隔
#     my_list.append([key, value])
# 定义列表存储处理后的键值对
my_list=[[0,1],[0,2],[1,2],[3,4]]
my_list_new=[]
for i in range(len(my_list)):
    # print(i) #0 1 2 3
    # 判断第一个元素不处理
    if i==0:
        continue
    elif i<len(my_list) and i>0:
        if my_list[i][0]==my_list[i-1][0]:
            my_list[i-1][1]+=my_list[i][1]
            print(my_list[i])
            # my_list_new.append(my_list[i])
        else:
            # print(my_list[i-1])
            # my_list_new.append(my_list[i])
            continue
    else:
        print(my_list[i])
        # my_list_new.append(my_list[i])
        continue
for i in  my_list_new:
     print(i)
# print(my_list_new)
