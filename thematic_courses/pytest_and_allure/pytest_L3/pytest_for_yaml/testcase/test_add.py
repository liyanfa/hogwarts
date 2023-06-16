# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 20:37
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_add.py.py
# @remark:
import pytest
import yaml
from operation import my_add


def get_yaml_data():
    """
    读取yaml文件
    :return:
    """
    file_path='../data/data.yaml'
    with open(file_path,'r',encoding='utf-8') as f:
        data=yaml.safe_load(f)
        return data



class TestWithYaml:
    # 传统parametrize 代码冗余
    # @pytest.mark.parametrize('x,y,sum',[[1,2,3],[3,6,9],[100,200,300]])
    # 改造为数据驱动
    @pytest.mark.parametrize('x,y,sum',get_yaml_data())

    def test_add(self,x,y,sum):
        assert my_add(int(x),int(y)) == sum

