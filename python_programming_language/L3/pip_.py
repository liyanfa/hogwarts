# -*- coding: utf-8 -*-
# @Time    : 2023/5/16 21:51
# @Author  : yanfa
# @user   : yanfa 
# @File    : pip_.py
# @remark:pip环境管理
""""""

"""一、pip概述
pip是python包管理工具
    python2的279版本开始自带 （自带是指装了python就自带携带pip）
    python3的3。4版本开始自带
https://pypi.org/托管了大量流行的python包"""

"""二、pip常用命令
功能              指令
查看版本           pip -V
查看帮助文档        pip help
查看包列表         pip list
导出包列表         pip freeze
安装              pip install 包名 ）
升级              pip install -U 报名
卸载              pip uninstall 包名
"""

"""三、pip安装
普通安装：pip install 包名
指定版本：pip install 包名==版本号
从文件中安装：pip install -r requirments.txt 
"""
#文件格式
# pytest==6.20
# selenium==3.14.1

"""四、pip使用镜像加速
pip install -i 镜像源
国内常用源

阿里源：https://mirrors.aliyun.com/pypi/simple/
清华源：https://pypi.tuna.tsinghua.edu.cn/simple/
豆瓣源：http://pypi.douban.com/simple/
pip install pytest -i https://pypi.douban.com/simple
"""
