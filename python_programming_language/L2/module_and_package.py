# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 20:08
# @Author  : yanfa
# @user   : yanfa 
# @File    : module_and_package.py
# @remark: 模块与包
"""程序结构组成=package module function
"""
"""一、模块的定义
是在代码量变得相当⼤了之后，为了将需要重复使⽤的有组织的代码放在
⼀起，这部分代码可以被其他程序引⽤，从⽽使⽤该模块⾥的函数等功能，引
⽤的过程叫做导⼊（import）
一个.py文件就是一个模块"""

"""二、模块的导入
方法一：import module1[,modele2...[,moduleN]]
方法二：from module import <name[,name2,...[,nameN]]>
import 模块名   引入一个完整的模块
from <模块名> import <方法｜变量｜类> 引入模块中一个或多个指定部分
from <模块名> import * 导入模块里面的所有函数、变量
"""

"""三、模块的分类
1/系统内置模块：os、sys、time、json、math等
2/第三方开源模块：
    通过插件管理器或命令pip install进行安装
3/自定义模块："""

import json
a="{\"a\":1}"
b=json.loads(a)
print(type(b),b) #字符转json <class 'dict'> {'a': 1}
c=json.dumps(b)
print(type(c),c) #json转字符 <class 'str'> {"a": 1}


import sys
print("调用了sys模块")
for i in sys.argv:
    print(i)
#/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevconsole.py
#--mode=client
#--port=52887

"""四、作用域
搜索路径：sys.path 变量中
当你导入一个模块时，python解释器对模块位置的搜索顺序是：
1、当前目录
2、如果不在当前目录，则搜索shell变量的PYTHONPATH下的每个目录
3、如果找不到，python会察看默认路径"""

"""五、常用方法
dir():找出当前模块定义的对象
dir(sys)：找出参数模块定义的对象"""
print(dir()) #['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c', 'i', 'json', 'sys']
print(dir(sys)) #['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework', '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions']
print(sys.path) #返回路径集合


import time
print(dir(time)) #['CLOCK_MONOTONIC', 'CLOCK_MONOTONIC_RAW', 'CLOCK_PROCESS_CPUTIME_ID', 'CLOCK_REALTIME', 'CLOCK_THREAD_CPUTIME_ID', 'CLOCK_UPTIME_RAW', '_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'clock_getres', 'clock_gettime', 'clock_gettime_ns', 'clock_settime', 'clock_settime_ns', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname', 'tzset']

"""六、模块的作用
提⾼代码的可维护性
❖ ⼀个模块编写完毕之后，其他模块直接调⽤，不⽤再从零开始写代码了，节约
了⼯作时间；
❖ 避免函数名称和变量名称重复，在不同的模块中可以存在相同名字的函数名和
变量名（不要和系统内置的模块名称重复）
"""