# -*- coding: utf-8 -*-
# @Time    : 2023/6/26 20:11
# @Author  : yanfa
# @user   : yanfa 
# @File    : check_demo.py.py
# @remark:

# python_files = test_* check_* 则执行
import logging


def test_demo():
    print("测试demo")

# python_classes = Test* Check* 则执行
class CheckDemo():
    def test_demo1(self):
        logging.info("测试demo1")
        print("测试demo1")

    def test_demo2(self):

        print("测试demo2")

    #python_function = test_* check_* 则执行
    def check_demo3(self):
        print("测试demo3")