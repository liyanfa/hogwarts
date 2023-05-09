# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 21:05
# @Author  : yanfa
# @user   : yanfa 
# @File    : logging_advanced.py
# @remark: 日志的高级使用 logging
""""""
import os

"""一、
loggers：记录器 提供应用程序代码直接使用的接口
handler：处理器 用于将日志记录发送到指定的目的位置
filters：过滤器 提供更细粒度日志过滤功能，用于决定哪些日志记录将会被输出，其他的过滤
formatters：格式器 用于控制日志信息的最终输出格式

filters(选填)     
                handler1
          ----->        ----->loggers
                handler2    
formatters
"""
# import logging
#
# # 创建记录器
# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
#
# # 支持多个处理器
# # 创建处理器-流
# ch1 = logging.StreamHandler()
# # 创建处理器-文件
# ch2 = logging.FileHandler('mylog.log',encoding='utf-8')
# ch1.setLevel(logging.DEBUG)
# ch2.setLevel(logging.DEBUG)
#
# # 创建格式器
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# # 将格式器添加到处理器
# ch1.setFormatter(formatter)
# ch2.setFormatter(formatter)
#
# # 将处理器添加到记录器
# logger.addHandler(ch1)
# logger.addHandler(ch2)
#
# # 要记录的信息
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')


"""封装日志公共函数"""
# import logging
# def get_logger():
#     # create logger
#     logger=logging.getLogger(os.path.basename(__file__))
#     # 设置默认等级
#     logger.setLevel(logging.INFO)
#     # 创建处理器
#     ch=logging.FileHandler(filename='mylog.log',encoding='utf-8')
#     ch.setLevel(logging.INFO)
#     # 创建格式器
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     # 格式器加入日志器
#     ch.setFormatter(formatter)
#     #处理器加入记录器
#     logger.addHandler(ch)
#     return logger
#
# logger=get_logger()
#
# def log_info(message):
#     logger.info(message)
#
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

"""日志文件配置 logging.conf
例如：
[loggers] # loggers 对象列表
        keys=root,main

[handlers] # handlers 对象列表
        keys=consoleHandlers,fileHandlers

[formatters] # formatters 列表
        keys=fmt

[logger_root]
        level=DEBUG
        handlers=consoleHandlers,fileHandlers

[logger_main] # main logger
        level = DEBUG
        handlers = fileHandlers
        qualname=main
        propagate=0

[handler_consoleHandlers]# consoleHandlers 指定控制器的输出方向、级别、输出格式、参数
        class = StreamHandler
        level = DEBUG
        formatter = fmt
        args = (sys.stdout,)

[handler_fileHandlers]# 循环日志文件 以文件大小来 分割# 每隔 1000 Byte 划分一个日志文件，备份文件为 3 个
        class = logging.handlers.RotatingFileHandler
        level = DEBUG
        formatter = fmt
        args = ('./logs/test.log', 'a', 10000, 3, 'UTF-8')

[formatter_fmt] # fmt 格式
        format=%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)
        datefmt="""

import logging.config

logging.config.fileConfig("logging.config")
logger=logging.getLogger("main")
logger.debug("这是debug日志")