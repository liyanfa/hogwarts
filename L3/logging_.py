# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 20:28
# @Author  : yanfa
# @user   : yanfa 
# @File    : logging_.py
# @remark: 日志打印配置和使用 logging
""""""
"""一、日志作用
1、调试 2、辅助定位问题 3、数据分析"""

"""二、日志级别
DEBUG：细节信息，仅当诊断问题时使用
INFO: 确认程序按预期运行
WARNING：表明有已经或者即将发生的意外（例如：磁盘空间不足）。程序仍按预期进行
ERROR：由于程序的某些功能已经不能正常执行
CRITICAL：严重的错误，表明程序已不能继续执行"""

"""三、日志的用法
https://docs.python.org/zh-cn/3/howto/logging.html
logging.debug(msg,*args,**kwargs) 
logging.info(msg,*args,**kwargs)
logging.warning(msg,*args,**kwargs)
logging.error(msg,*args,**kwargs)
logging.critical(msg,*args,**kwargs)
logging.log(*args,**kwargs) 创建一条严重级别为level的日志记录
logging.basicConfig(**kwargs) 对logger进行一次性配置
"""
import logging

# 1、logging 默认设置的级别是warning，所以不打印比他级别低的info
# logging.warning('警告')
# logging.info('普通') #只输出：WARNING:root:警告。
# logging.error('这是error')

# 2、设置日志级别 打印它以及以上级别的日志
# logging.basicConfig(level=logging.INFO)
# logging.debug('调试') #不输出
# logging.warning('警告')
# logging.info('普通') #
# logging.error('这是error')

# 3、保存到文件里
# logging.basicConfig(filename='example.log',level=logging.DEBUG)
# logging.debug('调试') #不输出
# logging.warning('警告')
# logging.info('普通') #
# logging.error('这是error')

# 4、更改显示消息的格式，如加上日期
# logging.basicConfig(format='%(asctime)s %(message)s')
# logging.warning('is when this event was logged.') #2023-05-09 20:54:08,151 is when this event was logged.

# 也支持自定义格式 datefmt 参数的格式与 time.strftime() 支持的格式相同。
# https://docs.python.org/zh-cn/3/library/time.html#time.strftime
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %I:%M:%S')
# logging.warning('is when this event was logged.') #2023-05-09 08:53:49 is when this event was logged.

# 5、加上行号/文件名
# logging.basicConfig(filename='new.log',
#                     level=logging.INFO,
#                     format='%(asctime)s [%(levelname)s]%(message)s (%(filename)s)')
# logging.warning('警告')
# logging.info('普通') #
# logging.error('这是error')

"""执行逻辑
1、先执行basicconfig
2、再执行我们的代码"""