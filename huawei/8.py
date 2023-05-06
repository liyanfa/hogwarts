# -*- coding: utf-8 -*-
# @Time    : 2023/5/6 17:18
# @Author  : yanfa
# @user   : yanfa 
# @File    : 8.py
# @remark:
my_list=[[0,1],[0,2],[1,2],[3,4]]
my_list_new=[]
#思路：先找出键相同的进行排序或者逐一排序
for i in range(len(my_list)):
    # print(i) #0 1 2 3
    # 先找到相同键的
    while my_list[i][0]==my_list[i-1][0]:
        my_list[i][1] += my_list[i-1][1]
        print(my_list[i])


#     if i==0:
#         continue
#     elif i<len(my_list) and i>0:
#         if my_list[i][0]==my_list[i-1][0]:
#             my_list[i-1][1]+=my_list[i][1]
#             print(my_list[i])
#             # my_list_new.append(my_list[i])
#         else:
#             # print(my_list[i-1])
#             # my_list_new.append(my_list[i])
#             continue
#     else:
#         print(my_list[i])
#         # my_list_new.append(my_list[i])
#         continue
# for i in  my_list_new:
