# -*- coding: utf-8 -*-
# @Time    : 2023/5/6 19:58
# @Author  : yanfa
# @user   : yanfa 
# @File    : json_.py
# @remark: 内置库json
"""json
json是用于存储和交换数据u的语法，是一种轻量级的数据交换格式
使用场景：1/接口数据传输 2/序列化 3/配置文件
"""

"""json结构
键值对形式-json对象{}
数组形式-json数组[]"""

"""python与json数据类型对应
python      json    说明
dict        object  字典
list,tuple  array   序列
str         string  字符串
int,float   number  数字类型
True        true    布尔值True
False       false   布尔值False
None        null    空值
"""

"""常用方法
1、dumps()   将python对象编码成json字符串
2、loads()   将解码json数据，该函数返回python对象
3、dump()    python对象编码，并将数据写入json文件中
4、load()    从json文件中读取数据并解码成python对象
"""

import json

# 定义python结构
data={
    'a':1,
    'b': 1.23,
    'c':"hello",
    'd':[2,3],
    'e':(1,2),
    'f':{'name':'yanfa'},
    'g':True,
    'h':False,
    'i':None
}

#1、将python对象编码为json字符串 参照上表，注意都是双引号
# json_str=json.dumps(data)
# print(json_str) #{"a": 1, "b": 1.23, "c": "hello", "d": [2, 3], "e": [1, 2], "f": {"name": "yanfa"}, "g": true, "h": false, "i": null}
# print(type(json_str)) #<class 'str'>

# 2、将json字符串转换为python对象
# json_object=json.loads(json_str)
# print(json_object) #{'a': 1, 'b': 1.23, 'c': 'hello', 'd': [2, 3], 'e': [1, 2], 'f': {'name': 'yanfa'}, 'g': True, 'h': False, 'i': None}
# print(type(json_object)) #<class 'dict'>

# 3、把python对象转成json格式的数据并写入json文件
# with open('data.json','w')as f:
#     json.dump(data,f)

# 4、读取json文件，并且转成python对象
# with open('data.json') as f:
#     json.load(f)
#     print(data) #{'a': 1, 'b': 1.23, 'c': 'hello', 'd': [2, 3], 'e': (1, 2), 'f': {'name': 'yanfa'}, 'g': True, 'h': False, 'i': None}
#     print(type(data)) #<class 'dict'>

"""dumps常用参数
1、indent:根据数据格式缩进显示，默认为None,没有缩进
2、ensure_ascii:对中文使用ascii码，默认为True,改成False才能正常显示中文"""

data1={
    'school':'霍格沃滋',
    'name':'yanfa',
    'age':18
}
json_str1=json.dumps(data1)

json_str2=json.dumps(data1,ensure_ascii=False,indent=4)

print(json_str1) #{"school": "\u970d\u683c\u6c83\u6ecb", "name": "yanfa", "age": 18}
print(json_str2) #输出
# {
#     "school": "霍格沃滋",
#     "name": "yanfa",
#     "age": 18
# }