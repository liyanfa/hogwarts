# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 16:39
# @Author  : yanfa
# @user   : yanfa 
# @File    : main.py
# @remark:
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集的用例名name和用例标识nodeid的中文信息显示在控制台上
    参数items是指测试用例集，里面每个代表一个用例item，
    每个item有各种参数如name-用例名称、nodeid-用例路径等，可以打debug查看pytest_runtest_teardown,conftest.py
    注意：为什么是_nodeid而不是nodeid，因为nodeid是一个属性，真正要改的是self._nodeid
    @property
    def nodeid(self) -> str:
        return self._nodeid
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")
