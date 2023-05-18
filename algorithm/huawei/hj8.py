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

input_str = input()  # 输入一个正整数

# 判断数据范围，不符合重新输入
while str(type(input_str)) != "<class 'int'>" and int(input_str) < 0 and int(input_str) > 500:
    print("必须输入1-500的正整数键值对数,请重新输入")
    input_str = input()
# 定义列表存储键值对
my_list = []
for i in range(int(input_str)):
    key, value = map(int, input().split(" "))  # 使用逗号分隔
    while key < 0 or key > 11111111 or value < 1 or value > 100000:
        print("0 <= index <= 11111111,1 <= value <= 100000,请重新输入")
        key, value = map(int, input().split(" "))  # 使用逗号分隔
    my_list.append([key, value])

# 先拿出所有的键
my_key_list = [x[0] for x in my_list]
my_list_new = []
# 思路：1、先找出键相同的记录
for x in range(len(my_key_list)):
    my_list_new_e = []
    for i in range(len(my_list)):
        if my_list[i][0] == my_key_list[x]:
            my_list_new_e.append(my_list[i])
        else:
            continue
    if my_list_new_e not in my_list_new:
        my_list_new.append(my_list_new_e)

# 2、逐个处理相加
my_list_deal = []
for mln in my_list_new:
    # 如果列表有多条首值相同的，求和第二个元素
    if len(mln) > 1:
        value_sum = 0
        for m in mln:
            # 求第二个值相加
            value_sum += m[1]
        my_list_deal.append([mln[0][0], value_sum])
    else:
        my_list_deal.append(mln[0])

# 3、转成字典
my_list_deal_dict = {i[0]: i[1] for i in my_list_deal}
# print(my_list_deal_dict)
# 4、排序
my_list_deal_sort = sorted(my_list_deal_dict.items())
# print(my_list_deal_sort)

# 5、打印
for mlds in my_list_deal_sort:
    print(f"{mlds[0]} {mlds[1]}")
