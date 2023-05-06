# -*- coding: utf-8 -*-
# @Time    : 2023/5/6 19:30
# @Author  : yanfa
# @user   : yanfa 
# @File    : time_.py
# @remark: 日期和时间处理

"""工作应用
作为日志信息的内容输出
计算某个功能的执行时间
用日期命名一个日志文件的名称
生产随机数"""
import datetime

"""python中处理时间的模块
time
datetime
calendar"""

"""常见的时间表示方式
1、时间戳
2、格式化的时间字符串"""

"""datetime常用的类
datetime (from datetime import datetime) 时间日期相关
timedelta (from datetime import timedelta) 时间差
timezone (from datetime import timezone) 时区
"""

"""练习1 获取当前时间"""
# 当前时间
# nowtime=datetime.datetime.now()
# print(nowtime) #2023-05-06 19:37:45.762505
# print(nowtime.strftime('%Y-%m-%d %H:%M:%S')) # 格式化打印2023-05-06 19:39:47
# print(nowtime.day) #年 6
# print(nowtime.month) #月 5
# print(nowtime.year) #日 2023
# print(nowtime.hour) #时 19
# print(nowtime.minute) #分 40
# print(nowtime.second) #秒 41
#
# #转成时间戳
# print(nowtime.timestamp()) #1683373302.208905

"""练习2 字符串和时间的转换"""
#字符串转datetime实例 strptime()
# s="2023-05-06 18:00:00"
# s1=datetime.datetime.strptime(s,'%Y-%m-%d %H:%M:%S')
# print(s1)  #2023-05-06 18:00:00
# print(type(s1)) #<class 'datetime.datetime'>
#
# #时间转字符串 strftime()
# nowtime=datetime.datetime.now()
# nowtime_str=nowtime.strftime('%Y-%m-%d %H:%M:%S')
# print(nowtime_str) #2023-05-06 19:46:06
# print(type(nowtime_str)) #<class 'str'>

"""练习3 时间与时间戳转换"""
# mtimestamp=1683373685.660518
#将时间戳转换为时间 fromtimestamp()
# s=datetime.datetime.fromtimestamp(mtimestamp) #2023-05-06 19:50:59

#将时间转为时间戳 timestamp()
# print(s.timestamp()) #1683373685.660518

"""实例
写一段代码，生成一个以时间命名的日志文件。
并向日志文件中写入日志数据。"""

nowtime_str=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

file_name=nowtime_str+'.log'
with open(file_name,'w+',encoding='utf-8') as f:
    message=f'{nowtime_str} [info] line:14 this is message'
    f.write(message)