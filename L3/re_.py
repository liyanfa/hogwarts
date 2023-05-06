# -*- coding: utf-8 -*-
# @Time    : 2023/5/6 20:26
# @Author  : yanfa
# @user   : yanfa 
# @File    : re_.py
# @remark: 正则表达式 内置库re
"""什么是正则表达式
1、正则表达式就是记录文本规则的代码
2、可以查找操作符合某和复杂规则的字符串"""

"""一、使用场景
1、处理字符串
2、处理日志"""

"""二、在python中使用正则表达式
1、把正则表达式作为模式字符串
2、正则表达式可以使用原生字符串来表示，在前方加上r'string'"""

"""三、使用re模块实现正则表达式操作"""
"""1、正则表达式对象转换
compile():将字符串转换为正则表达式对象
需要多次使用这个正则表达式的场景"""
import re
#prog:正则对象 pattern-正则表达式
# prog=re.compile(pattern='')

"""2、匹配字符串
1）mathch():从字符串的开始进行匹配 
2）search():在整个字符串中搜索第一个匹配的值
3）findall():在整个字符串中搜索所有符合正则表达式的字符串，返回列表

pattern:正则表达式
string：要匹配的字符串
flags：可选，控制匹配方式
    - A：只进行ASCII匹配
    - I:不区分大小写
    - M：将^和$用于包括整个字符串的开始和结尾的每一行
    - S：使用（.）字符匹配所有字符，包括换行符
    - X:忽略模式字符串中未转义的空格和注释
re.match(pattern,string,[flags])
re.search(pattern,string,[flags])
re.findall(pattern,string,[flags])
"""

####1、match() 匹配以hog开头的字符串
pattern=r'hog\w+'

s1="Hogwarts is a magic school"
# match1=re.match(pattern,s1)
# print(match1) #匹配以xx开头，但是默认区分大小写，匹配不到 输出：None
# match2=re.match(pattern,s1,re.I)
# print(match2) #加上re.I忽略大小写，则可以匹配到 输出：<re.Match object; span=(0, 8), match='Hogwarts'>

s2="I like hogwarts"
# match3=re.match(pattern,s2,re.I)
# print(match3) #完全不以hog开头，，匹配不到 输出：None

# 获取具体的信息
# print(f'匹配值的开始位置：{match2.start()}') #匹配值的开始位置：0
# print(f'匹配值的结束位置：{match2.end()}') #匹配值的结束位置：8
# print(f'匹配位置的元祖：{match2.span()}') #匹配位置的元祖：(0, 8)
# print(f'要匹配的字符串：{match2.string}') #要匹配的字符串：Hogwarts is a magic school
# print(f'匹配的数据为：{match2.group()}') #匹配的数据为：Hogwarts

####2、search() 在整个字符串中搜索第一个匹配的值
# match4=re.search(pattern,s2,re.I)
# print(f'匹配值的开始位置：{match4.start()}') #匹配值的开始位置：7
# print(f'匹配值的结束位置：{match4.end()}') #匹配值的结束位置：15
# print(f'匹配位置的元祖：{match4.span()}') #匹配位置的元祖：(7, 15)
# print(f'要匹配的字符串：{match4.string}') #要匹配的字符串：I like hogwarts
# print(f'匹配的数据为：{match4.group()}') #匹配的数据为：hogwarts

s3="I like hogwarts,but hogwarts not like me"
match5=re.search(pattern,s3,re.I)  #出现2个也只能匹配到第一条
# print(match5) #<re.Match object; span=(7, 15), match='hogwarts'>
# print(f'匹配值的开始位置：{match5.start()}') #匹配值的开始位置：7
# print(f'匹配值的结束位置：{match5.end()}') #匹配值的结束位置：15
# print(f'匹配位置的元祖：{match5.span()}') #匹配位置的元祖：(7, 15)
# print(f'要匹配的字符串：{match5.string}') #要匹配的字符串：I like hogwarts,but hogwarts not like me
# print(f'匹配的数据为：{match5.group()}') #匹配的数据为：hogwarts


####3、findall() 在整个字符串中搜索所有符合正则表达式的字符串，返回列表
# match6=re.findall(pattern,s1,re.I)  #['Hogwarts']
# print(match6)
# match7=re.findall(pattern,s2,re.I)  #['hogwarts']
# print(match7)
# match8=re.findall(pattern,s3,re.I)  #['hogwarts', 'hogwarts']
# print(match8)

"""4、替换字符串
sub():实现字符串替换

pattern:正则表达式
repl:要替换的字符串
string：要被查找替换的原始字符串
flags：可选，控制匹配方式
    - A：只进行ASCII匹配
    - I:不区分大小写
    - M：将^和$用于包括整个字符串的开始和结尾的每一行
    - S：使用（.）字符匹配所有字符，包括换行符
    - X:忽略模式字符串中未转义的空格和注释
re.sub(pattern,repl,string,[count],[flags])
"""
#匹配手机号
# pattern=r'1[345678]\d{9}'
#
# s4="中奖号码为12345，联系电话 15611111111"
# result=re.sub(pattern,'156xxxxxxxx',s4)
# print(result) #中奖号码为12345，联系电话 156xxxxxxxx

"""5、分割字符串
split():根据正则表达式分割字符串，返回列表

pattern:正则表达式
string：要被查找替换的原始字符串
maxsplit:可选，表示最大拆分次数
flags：可选，控制匹配方式
    - A：只进行ASCII匹配
    - I:不区分大小写
    - M：将^和$用于包括整个字符串的开始和结尾的每一行
    - S：使用（.）字符匹配所有字符，包括换行符
    - X:忽略模式字符串中未转义的空格和注释
re.split(pattern,string,[maxsplit],[flags])
"""
pattern=r'[?|&]'
url="https://www.baidu.com/s?name=yanfa&age=18&sex=boy"
result=re.split(pattern,url)
print(result) #['https://www.baidu.com/s', 'name=yanfa', 'age=18', 'sex=boy']
result=re.split(pattern,url,maxsplit=2) #只分割2次
print(result)  #['https://www.baidu.com/s', 'name=yanfa', 'age=18&sex=boy']

