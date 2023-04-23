# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 19:13
# @Author  : yanfa
# @user   : yanfa 
# @File    : dict_.py
# @remark: 字典
""""""

"""一、字典的定义
字典是无序的键值对集合
字典用大括号{}包围
每个键值对之间用逗号（，）分隔
每个键和值用冒号（：）分隔
字典的动态的"""

"""二、字典的创建"""

#第一种：使用大括号{}
dic1={}
dic2={"a":1,"b":[1,2]}

#第二种:构造方法
dic3=dict()
dic4=dict([("a",1),("b",2)])  #{'a': 1, 'b': 2}
print(dic4)

#第三种，推导式
dic_5={k:v for k,v in [("a",1),("b",2)]}

"""三、字典的使用：访问元素
支持括号记法[key]
字典使用键来访问其关联的值
访问时对应的key必须要存在"""

dic_6={"a":1,"b":[1,2]}
#1、访问存在的key
print(dic_6["a"]) #1

#2、访问不存在的key
# print(dic_6["c"]) #KeyError: 'c'

"""三、字典的使用：操作元素
语法：dict[key]=value
添加元素-键不存在：
修改元素-键存在"""

#1、添加元素
dic_6["c"]=2
print(dic_6) #{'a': 1, 'b': [1, 2], 'c': 2}

#2、修改元素
dic_6["c"]=3
print(dic_6) #{'a': 1, 'b': [1, 2], 'c': 3}

"""四、字典使用：嵌套字典
字典的值也可以是字典对象"""
dic_6={"a":{"b":1}}
print(dic_6["a"]["b"]) #1

"""五、字典方法"""
dic_7={"a":1,"b":[1,2]}
#1、keys(),# 返回视图对象，通过list()将视图转成列表
print(dic_7.keys()) #dict_keys(['a', 'b'])
print(list(dic_7.keys())) #['a', 'b']

#2、values()
print(dic_7.values()) #dict_values([1, [1, 2]])
print(list(dic_7.values())) #[1, [1, 2]]

#3、items()
print(dic_7.items()) #dict_items([('a', 1), ('b', [1, 2])])
print(list(dic_7.items())) #[('a', 1), ('b', [1, 2])]

#4、get() 找不到不报错，返回None。方法的好处是无需担心 key 是否存在，永远都不会引发 KeyError 错误
dic_8={"a":1,"b":2,"c":3}
print(dic_8.get("a")) #1
print(dic_8.get("d")) #None


#5、update，使用来自 dict 的键/值对更新字典，覆盖原有的键和值。
dic_9={"a":1,"b":2,"c":3}
data={"b":20,"d":4}
dic_9.update(data)
print(dic_9) #{'a': 1, 'b': 20, 'c': 3, 'd': 4}


#6、pop() 删除指定 key 的键值对，并返回对应 value 值。
dic_10={"a":1,"b":2,"c":3}
print(dic_10.pop("a"))  #如果 key 存在于字典中，则将其移除并返回 value 值 1
print(dic_10.pop("d"))  #如果 key 不存在于字典中，则会引发 KeyError。

#7、clear() 清空元素
dic_11={"a":1,"b":2,"c":3}
dic_11.clear()
print(dic_11) #{}

#8、copy() 拷贝
dic_12={"a":1,"b":2,"c":3}
dic_13=dic_12.copy() #{'a': 1, 'b': 2, 'c': 3}
print(dic_13)


"""六、字典推导式
可以从任何以键值对作为元素的可迭代对象中构建出字典"""
#例子1 给定一个字典对象{'a': 1, 'b': 2, 'c': 3}，找出其中所有大于 1 的键值对，同时 value 值进行平方运算
dic_11={k:v for k,v in[("a","b","c"),(1,2,3)]}
print(dic_11)

#例子2 将大于1的值平方返回一个新字典
dic_12={"a":1,"b":2,"c":3}
dic_13={k:v**2 for k,v in dic_12.items() if v>1}
print(dic_13) #{'b': 4, 'c': 9}

#例子3 将键换成值
dic_14={"a":1,"b":2,"c":3}
dic_15={v:k for k,v in dic_14.items()}
print(dic_15) #{1: 'a', 2: 'b', 3: 'c'}
