# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 16:39
# @Author  : yanfa
# @user   : yanfa 
# @File    : setup.py
# @remark:
"""
__author__ = 'hogwarts_xixi'
"""
from setuptools import setup,find_packages
setup(
    name='pytest_encode',
    url='https://github.com/thematic_courses/pytest_and_allure/pytest_L4/pytest_for_plugins/pytest_encode/pytest_encode',
    version='1.0',
    author="yanfa",
    author_email='xxxx@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[# 分类索引 ，pip 对所属包的分类
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    packages = find_packages(), #['pytest_encode'],
    keywords=[
        'pytest', 'py.test', 'pytest_encode',
    ],

    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],
    # 入口模块 或者入口函数
    entry_points={
        'pytest11': [
            'pytest_encode = pytest_encode.main',
        ]
    },
    zip_safe=False
)