# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 20:37
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_add.py.py
# @remark:
import pytest
import yaml
from operation import my_add
import openpyxl

def get_excel_data():
    """
    读取excel文件
    :return:
    """
    file_path = "/Users/yanfa/PycharmProjects/hogwarts/thematic_courses/pytest_and_allure/pytest_L3/pytest_for_excel/data/data.xlsx"
    # 获取工作簿
    book=openpyxl.load_workbook(file_path)
    #获取活动行（非空白行）
    sheet=book.active

    # 提取数据，格式[[],[],[]]
    values=[]
    for row in sheet:
        line=[]
        for cell in row:
            line.append(cell.value)
        values.append(line)
    return values


class TestWithExcel:
    # 传统parametrize 代码冗余
    # @pytest.mark.parametrize('x,y,sum',[[1,2,3],[3,6,9],[100,200,300]])
    # 改造为数据驱动
    @pytest.mark.parametrize('x,y,sum',get_excel_data())

    def test_add(self,x,y,sum):
        assert my_add(int(x),int(y)) == sum

