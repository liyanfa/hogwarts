# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 19:13
# @Author  : yanfa
# @user   : yanfa 
# @File    : list_.py
# @remark: 常用数据结构-列表
""""""
"""一、列表的定义
列表是有序的可变元素的集合，使用中括号[]包围，元素之间用逗号分隔
列表是动态的，可以随时扩展和收缩
列表是异构的，可以同时存放不同类型的对象
列表中允许出现重复元素"""

"""二、列表的使用：创建"""
#1.构造方法
list_a=list()
print(type(list_a),list_a)

#2、中括号填充元素
list_b=[1,"a",{"a":1},[1,2],(1,2,3)]

#3、列表推导式
list_c=[i for i in range(1,10)if i%2==0]
print(type(list_c),list_c)

"""三、列表的使用：索引/切片"""
#1、索引 （正索引，0开始；负索引，-1开始）
list_d=[1,2,3,4,5]
print(list_d[0]) #首个元素
print(list_d[-1]) #最后元素

#2、切片 获取多个元素
# [start:stop:step] 三种方式同前面rangestep-步长默认为1
#基本方法
li=['h','o','g','w','a','r','t','s']
print(li[0:5:2]) #第一个到第五个元素中按步长2 ['h', 'g', 'a']
print(li[2:4]) #第3个到第4个元素 'g', 'w']
print(li[:4]) #第1个到第4个元素 ['h', 'o', 'g', 'w']
print(li[2:]) #第3个到最后 ['g', 'w', 'a', 'r', 't', 's']
print(li[::2]) #全部元素，按步长2 ['h', 'g', 'a', 't']
print(li[::-1]) #全部元素，按步长2，倒序打印['s', 't', 'r', 'a', 'w', 'g', 'o', 'h']

"""三、列表的使用：运算符
重复：使用 * 运算符可以重复生成列表元素。
合并：使用 + 加号运算符，可以将两个列表合二为一。"""
# 1、* 重复生成列表元素
li1=[1]
print(li1*5) #[1, 1, 1, 1, 1]
# 2、+ 列表合并
li2=[1,2,3]
li3=[4,5,6]
print(li2+li3) #[1, 2, 3, 4, 5, 6]

"""四、列表的使用：成员检测
in：检查一个对象是否在列表中，如果在则返回 True，否则返回 False。
not in：检查一个列表是否不包含某个元素。如果不在返回 True，否则返回 False。"""
li1=[1,2,3]
print(1 in li1) #True
print(1 not in li1) #False
print(4 in li1) #False
print(4 not in li1) #True

"""五、列表方法"""
li=[1,2,3]
#扩展加元素
#1、append(item)
# 将一个对象item添加到列表末，入参-item,返回-None
li.append(4)
print(li) #[1, 2, 3, 4]

#2、extend(iterable)
# 将一个可迭代对象到所有元素，添加到列表末;入参-可迭代对象iterable;返回-None
li=[1,2,3]
li.extend('hello')
print(li) #[1, 2, 3, 'h', 'e', 'l', 'l', 'o']
li1=[1,2,3]
li2=[4,5,6]
li1.extend(li2) #[1, 2, 3, 4, 5, 6]

#3、insert(index,item)
# 将一个元素插入指定到索引位置;入参-索引值index和一个对象item;返回-None;原索引位置以及后面到元素后移一位
li=[1,2,3]
li.insert(1,"a")
print(li) #[1, 'a', 2, 3]

#缩小元素
#4、pop()、pop(index)
# 移除指定索引位置到元素；若索引值不正确则引发IndexError
# pop() 默认移除最后一个元素
li=[1,2,3]
li.pop(2) #删除第三个元素
print(li) #[1, 2]
li.pop() #删除最后元素，[1]
#2种异常情况
print(li)
li.pop(3) #IndexError: pop index out of range
li=[]
li.pop() #IndexError: pop from empty list


#5、remove(item)
# 移除列表第一个等于item的元素，入参-item，返回-None，目标元素必须存在，否则ValueError
li=[1,2,3]
li.remove(1) #[2, 3]
print(li)
li.remove(4) #ValueError: list.remove(x): x not in list

#排序
#6、sort(key=None,reverse=Flase)
#对列表进行原地排序，只使用<来进行元素比较
#入参：支持2个关键字
#key:指定带有一个参数的函数，用于从每个列表元素种提取比较键
#reverse:默认值为False表示升序，为True表示降序
#返回：None

#1)不传参数，默认升序，数字从小到大排序
li=[2,4,3,1]
li.sort()
print(li) #1, 2, 3, 4]

#2）指定key=len,按元素的长度排序
words=["python","go","java","c"]
words.sort(key=len)
print(words) #['c', 'go', 'java', 'python']

#3）指定reverse=True,降序
nums=[2,4,3,1]
nums.sort(reverse=True)
print(nums) #[4, 3, 2, 1]


#7、反转 reverse
"""reverse():将列表元素反转
参数：无
返回：None
反转只是针对索引值，元素间不互相比较"""
nums=[5,3,2,4,1]
nums.reverse()
print(nums) #[1, 4, 2, 3, 5]


"""六、列表嵌套
嵌套列表是指在列表里存放列表
列表的常用方法都适用于嵌套列表"""
#1、创建嵌套列表
list1=[[1,2,3],['a','b','c']]
print(type(list1)) #<class 'list'>
print(len(list1)) #2

#2、访问嵌套列表中的元素
print(list1[0][2]) #3

"""七、列表推导式
列表推导式是指循环创建列表，相当于 for 循环创建列表的简化版
语法：[x for x in li if x ...]"""

#实例：将1-10中所有的偶数开方后组成新的列表
#1、传统
result=[]
for e in range(1,11):
    if e%2==0:
        result.append(e**2)
print(result) #[4, 16, 36, 64, 100]
#2、列表推导式
result=[e**2 for e in range(1,11) if e%2==0 ]
print(result) #[4, 16, 36, 64, 100]
