# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 21:48
# @Author  : yanfa
# @user   : yanfa 
# @File    : pytest_for_json.py
# @remark:pytest数据驱动json文件
""""""
import json

"""一、json文件介绍
1/json是JS对象
2/全称是JavaScriptObjectNotation
3/是一种轻量级的数据交换格式
4/json结构
    对象{}
    数组[]
"""

"""二、json文件使用
查看json文件：pycharm/txt记事本
读取json文件：
    安装：内资无需安装
    内置函数：open()
    内置库：json
    读取方法：json.load()
    写入方法：json.dump()
"""
# 例子1、写入json
def write_json():
    data=[[1,1,2],[3,6,9],[100,200,300]]
    file_path="pytest_for_json/data/data.json"
    with open(file_path,'w',encoding='utf-8') as f:
        json.dump(data,f)

# 例子2、读取json
def get_json():
    file_path = "pytest_for_json/data/data.json"
    with open(file_path,'r',encoding='utf-8') as f:
        data=json.load(f)
        print(data)
    return data

if __name__ == '__main__':
    # write_json()
    get_json()