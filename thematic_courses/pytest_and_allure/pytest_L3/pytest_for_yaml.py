# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 19:44
# @Author  : yanfa
# @user   : yanfa 
# @File    : pytest_for_yaml.py
# @remark: pytest结合数据驱动
""""""
"""一、什么是数据驱动？
数据驱动是数据的改变而驱动自动化测试的执行，最终引起测试结果的改变，简单来说就是参数化的应用。
数据量小的测试用例可以使用代码的参数化来实现数据驱动，数据量大的情况下建议使用结构化文件，如yaml/json/csv/excel对数据
进行存储，然后在测试用例中读取这些数据。

应用：
1、app/web/接口自动化测试
2、测试步骤的数据驱动
3、测试数据的数据驱动
4、配置的数据驱动"""
import datetime
import yaml

"""二、yaml文件介绍
对象：键值对的集合，用冒号：表示
数组：一组按次序排列的值，前面加-
纯量：单个的，不可再分的值
    字符串、布尔值、整型、浮点型、Null、时间、日期
见myyaml.yml
"""

"""三、yaml文件的使用
查看yaml文件：pycharm/txt记事本
读写yaml文件：
    安装：pip install pyyaml
    导入：import yaml
    写入方法：yaml.dump(f)
    读取方法：yaml.load(f)
"""

# 1、写入示例
myjson={'languages': ['Php', 'Java', 'Go'], 'book': {'python人们': {'price': 25.5, 'author': 'lily', 'available': True, 'repertory': 20, 'data': datetime.date(2018, 7, 27)}, 'java入门': {'price': 30, 'author': 'lily', 'available': False, 'repertory': None, 'data': datetime.date(2018, 5, 20)}}}
with open('./my.yaml','w',encoding='utf-8') as f:
    yaml.dump(myjson,f,allow_unicode=True)  #allow_unicode防止中文乱码

# 2、读取示例
file_path = "./my.yaml"
with open(file_path, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    print(data)

"""四、工程目录结构
data：存放yaml数据文件
func: 存放被测函数
testcase: 测试用例

测试准备：
    被测对象：opertion.py
    测试用例：test_add.py
    测试数据：data.yaml"""
