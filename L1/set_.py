# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 20:47
# @Author  : yanfa
# @user   : yanfa 
# @File    : set_.py
# @remark: 数据结构-集合

""""""
"""一、集合的定义
无序的唯一对象集合
用大括号{}包围，对象相互之间用逗号分割
集合是动态的，可以随时添加或者删除
集合是异构的，可以包含不同数据类型的数据"""

"""二、集合的使用：创建"""
#1、通过{}创建
set1={1,2,3}
print(type(set1),set1) #<class 'set'> {1, 2, 3}

#2、通过构造方法 set(interable)
set2=set("hello")
print(type(set2),set2) #<class 'set'> {'h', 'o', 'e', 'l'}
set3=set()
print(type(set3),set3) #<class 'set'> set()
#3、通过集合推导式
set4={i for i in range(5) if i%2==0}
print(type(set4),set4) #<class 'set'> {0, 2, 4}

"""集合的使用：成员检测in/not in"""
set1={1,2,3}
print(1 in set1) #True
print(1 not in set1) #False
print(4 in set1) #False
print(4 not in set1) #True

"""三、集合常用方法"""
#1、增 add(item)
##将单个对象添加到集合中，入参-item 返回-None
set1={1,2,3}
set1.add(4)
print(set1)

#2、update(iterable)
#批量添加来自可迭代对象中的所有元素
#入参：可迭代对象iterable
#返回：None
set1=set()
set1.update("hello")
print(type(set1),set1) #<class 'set'> {'e', 'l', 'o', 'h'}
set1.update([1,2,3])
print(type(set1),set1) #<class 'set'> {1, 2, 3, 'o', 'e', 'l', 'h'}

#3、删 remove(item)
#从集合中移除指定元素
#入参：指定元素值
#返回：None
#如果item不存在集合中则会引发KeyError

#元素存在
set1={1,2,"a"}
set1.remove("a") #{1, 2}
print(set1)
#元素不存在则报错
set1.remove(3) #KeyError: 3

#4、删 discard(item)
#从集合中移除指定对象item
#入参：指定对象值 返回-None,元素item不存在没影响，不会抛出KeyError
#1）元素存在
set1={1,2,"a"}
set1.discard("a") #{1, 2}
print(set1)
#2）元素不存在则报错
set1.discard(3) #返回空

#5、随机删 pop()
#随机从集合中移除并返回一个元素
#入参：无
#返回：被移除的元祖
#如果集合为空则会引发KeyError
#1)随机删除某个对象
set1={1,2,3,4,5}
item=set1.pop()
print(item,type(item),set1) #1 {2, 3, 4, 5}


#6、全部删 clear()
#清空所有元素
set1={1,2,3,4,5}
set1.clear()
print(set1) # set()

"""四、集合运算"""

#1、交集运算 itersection &
a={1,2,3}
b={4,3,6}
print(a.intersection(b)) #{3}
print(a&b)  #{3}

#2、并集运算 union |
a={1,2,3}
b={4,3,6}
print(a.union(b)) #{1, 2, 3, 4, 6}
print(a|b) #{1, 2, 3, 4, 6}

#3、差集运算 difference -
a={1,2,3}
b={4,3,6}
print(a.difference(b)) #{1, 2}
print(a-b) #{1, 2}
print(b.difference(a)) #{4, 6}
print(b-a)  #{4, 6}

"""五、集合推导式
语法：{x for x in ...if...}
"""
#寻找共同abc与bcd的字母
#1、传统
set1=set()
for s in 'abc':
    if s in 'bcd':
        set1.add(s)
print(set1) #{'b', 'c'}

#2、简洁
set1={s for s in 'abc'if s in 'bcd'}
print(set1) #{'b', 'c'}
