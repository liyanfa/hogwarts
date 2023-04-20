# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 21:44
# @Author  : yanfa
# @user   : yanfa 
# @File    : static_method.py
# @remark:
class Human:

    # 定义静态方法
    @staticmethod
    def grow_up():
        print("这是静态方法")

#访问静态方法
Human.grow_up()