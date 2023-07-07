# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 16:40
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_encode.py
# @remark:
import pytest


@pytest.mark.parametrize('name',['张三'])
def test_encode(name):
    print(f"name：{name}")