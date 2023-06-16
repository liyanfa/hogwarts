# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 20:37
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_add.py.py
# @remark:
import json
import pytest
from operation import my_add

def get_json_data():
    """
    读取json文件
    :return:
    """
    file_path = "/Users/yanfa/PycharmProjects/hogwarts/thematic_courses/pytest_and_allure/pytest_L3/pytest_for_json/data/data.json"
    with open(file_path,'r',encoding='utf-8') as f:
        data=json.load(f)
        print(data)
    return data


class TestWithJson:
    # 传统parametrize 代码冗余
    # @pytest.mark.parametrize('x,y,sum',[[1,2,3],[3,6,9],[100,200,300]])
    # 改造为数据驱动
    @pytest.mark.parametrize('x,y,sum',get_json_data())
    def test_add(self,x,y,sum):
        assert my_add(int(x),int(y)) == int(sum)

