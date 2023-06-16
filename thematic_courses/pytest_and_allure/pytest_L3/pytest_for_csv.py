# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 21:22
# @Author  : yanfa
# @user   : yanfa 
# @File    : pytest_for_csv.py
# @remark:pytest数据驱动csv文件
""""""

"""一、csv文件结束
1/通过逗号分隔
2/Comma-Separated Values的缩写
3/以纯文本形式存储数字和文本
4/文件由任意数目的记录组成
5/每行记录由多个字段组成"""

"""二、csv文件使用
1/安装：是内置包无需安装
2/导入：import csv
3/读取文件：
    内置函数：open()
    内置模块：csv
    方法：csv.reader(iterable)    
        参数：iterable,文件或者列表对象
        返回：迭代器，每次迭代返回一行数据
4/ 写入
    方法：csv.writer(iterable)    
"""

import csv


# 例子1：写入
# def write_csv():
#     # 要写入的数据
#     data = [
#         [1, 2, 3],
#         [3, 6, 9],
#         [100, 200, 300]
#     ]
#
#     # 将数据写入CSV文件
#     file_path = 'pytest_for_csv/data/data.json'
#     with open(file_path, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(data)


# 例子2：读取
def get_csv():
    file_path = "pytest_for_csv/data/data.csv"
    with open(file_path, "r", encoding='utf-8') as f:
        raw = csv.reader(f)
        data = []
        for line in raw:
            data.append(line)
    # print(data) #[['1', '2', '3'], ['3', '6', '9'], ['100', '200', '300']]
    return data


if __name__ == '__main__':
    # write_csv()
    get_csv()
