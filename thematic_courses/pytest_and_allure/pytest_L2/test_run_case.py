# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 21:22
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_run_case.py
# @remark:
import pytest


def test_demo01():
    print("test_demo01")

def test_demo02():
    print("test_demo02")

class TestDemo:
    @pytest.mark.fail
    def test_demo03(self):
        print("test_demo03")
        assert 1==2
    def test_demo04(self):
        print("test_demo04")