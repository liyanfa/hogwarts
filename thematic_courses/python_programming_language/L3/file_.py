# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 19:05
# @Author  : yanfa
# @user   : yanfa 
# @File    : file_.py
# @remark: 文件处理
""""""

"""一、文件操作步骤
打开文件
操作文件：读写
关闭文件：读写完成，要及时关闭"""


"""二、open方法"""
# def open(file, mode='r', buffering=None,
# encoding=None, errors=None, newline=None,
# closefd=True):
#     pass

"""三、文件读写模式
r：只读模式，并将文件指针指向文件头；如果文件不存在则报错
w：只写模式，并将文件指针指向文件头；如果文件存在则清空其内容，如果不存在则创建
a：只追加可写模式，并并将文件指针指向文件尾；如果文件不存在则创建
r+：在r的基础上增加可写功能
w+：在w的基础上增加可读功能
a+：在a的基础上增加可读功能
b：读写二进制文件（默认是t,表示文本），需要和上面几个模式搭配使用，如ab,wb,ab,ab+ (POSIX系统，包括linux都会忽略改字符)
"""

"""四、读操作
read(): 一次读取文件所有内容，返回一个str。
read(size): 每次最多读取指定长度的内容，返回一个str;在python2中size指定的是字节长度，python3中指定的是字符长度
readlines(): 一次读取文件所有内容，按行返回一个list。
readline(): 每次只读取一行内容
"""

"""读操作实战"""
#第一步：只读模式打开
# f=open('/Users/yanfa/PycharmProjects/hogwarts/pytest_L3/data.txt','r',encoding='utf-8')
#第二步：读取文件内容
# print(f.read()) #输出：hello\n world
# print(f.read(1)) #输出：h
# f.seek(0) #设置游标为开始的位置
# print(f.readlines()) #输出：['hello\n', 'world']
# print(f.readline()) #输出：hello
# print(f.readline()) #输出：world
# f.close()

"""忘记关闭文件的危害
打开文件达到一定数量，将为导致打开失败
占用内存空间，非常浪费资源
会导致系统自动回收资源，而丢失数据"""


"""with用法
好处：会自动关闭文件"""
# with open('/Users/yanfa/PycharmProjects/hogwarts/pytest_L3/data.txt','r',encoding='utf-8') as f:
#     print(f.read())
# print(f.closed) #判断文件是否关闭，返回布尔 True


"""五、写操作实战
mode='w+',读写权限，会新建文件，清空内容再写入
mode='r+',读写权限，替换原来的内容
mode='a+',读写权限，追加内容
"""
#w+ 有文件会清空再写入，无文件会创建再写入。
# with open('/Users/yanfa/PycharmProjects/hogwarts/pytest_L3/data1.txt','w+',encoding='utf-8') as f:
#     print(f.write('china')) #输出：5 没文件会自动创建文件 文件内容为china

# with open('/Users/yanfa/PycharmProjects/hogwarts/pytest_L3/data.txt','w+',encoding='utf-8') as f:
#     print(f.write('china')) #输出：5 有文件会清空内容写入5个字符，文件内容变成china

#r+ 替换原来的内容,不是完全替换，从文件头按长度进行替换
# with open('/Users/yanfa/PycharmProjects/hogwarts/pytest_L3/data.txt','r+',encoding='utf-8') as f:
#     print(f.write('xixixi')) #输出：6  原来hahahachina 现在xixixichina

#a+ 文件尾追加
# with open('/Users/yanfa/PycharmProjects/hogwarts/pytest_L3/data.txt','a+',encoding='utf-8') as f:
#     print(f.write('world')) #输出：5  原来hello 现在helloworld

"""六、总结
使用with方法会自动完成关闭操作
通过python封装的api可以实现读写追加操作
文件打开要使用utf-8编码，防止中文乱码"""