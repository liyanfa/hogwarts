# -*- coding: utf-8 -*-
# @Time    : 2023/6/2 13:03
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_module.py
# @remark: 运行顺序

def setup_module():
    print("setup_module")

def teardown_module():
    print("teardown_module")

class TestDome:
    def setup_class(self):
        print("TestDome setup_class")
    def teardown_class(self):
        print("TestDome teardown_class")
    def setup(self):
        print("TestDome setup")
    def teardown(self):
        print("TestDome teardown")
    def test_demo1(self):
        print("test demo1")
    def test_demo2(self):
        print("test demo2")

class TestDemo1:
    def test_demo3(self):
        print("TestDemo1 test demo3")


