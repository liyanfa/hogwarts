import random
# 输入多少个数
count = int(input())
# 判断数据范围1-1000 如果不是则重新输入
while count < 1 or count > 1000:
    print("输入数据个数错误，请重新输入1-1000。")
    count = int(input())

# 造随机整数
random_int_list = []
for i in range(count):
    # ri=random.randint(1,500)
    # print(ri)
    ri = int(input())
    # 判断数据范围1-1000 如果不是则重新输入
    while ri < 1 or ri > 500:
        print("请重新输入1-500的随机整数。")
        ri = int(input())
        random_int_list.append(ri)
    else:
        random_int_list.append(ri)

# 去重排序
# random_int_list_new=[]
# for i in random_int_list:
#     if i not in random_int_list_new:
#         random_int_list_new.append(i)
#     else:
#         continue
# random_int_list_new=sorted(random_int_list_new)
random_int_list_new=sorted(list(set(random_int_list)))

for ril in random_int_list_new:
    print(ril)