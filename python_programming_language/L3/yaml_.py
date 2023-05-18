# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 19:25
# @Author  : yanfa
# @user   : yanfa 
# @File    : yaml_.py
# @remark: 常用第三方库yaml
""""""
import yaml

"""一、什么是YAML
1、一种数据序列化格式
2、用于人类的可读性与脚本语言的交互
3、一种被认为可以超越xml、json的配置文件"""

"""二、YAML基本语法规则
1、大小写敏感
2、使用缩进表示层级关系
3、缩进时不允许使用tab键，只允许空格
4、缩进的空格数目不重要，只要相同层级的元素左侧对其即可
5、#表示注释，从这个字符一直到行尾，都会被解释器忽略"""

"""三、YAML支持的数据结构 见yaml.yaml
1、对象：键值对的集合，用冒号":"表示
2、数组：一组按次序排列的值，前加"-"
3、纯量：单个的，不可再分的值
    字符串、布尔值、浮点数、Null、时间、日期
"""

"""四、PyYaml
1、python的YAML解析器和生成器
2、官网：https://pypi.org/project/PyYAML/
3、安装：pip install PyYAML"""

"""五、创建yaml文件：yaml.dump()"""

# data={
#     'a':1,
#     'b': 1.23,
#     'c':"hello",
#     'd':[2,3],
#     'f':{'name':'yanfa'},
#     'g':True,
#     'h':False,
#     'i':None
# }
# # 直接dump可以把对象转为yaml文档
# with open('./my.yaml','w',encoding='utf-8') as f:
#     yaml.dump(data,f,allow_unicode=True)

"""六、读取yaml文件：yaml.safe_load()"""
file_path= 'file/my.yaml'
with open('file/my.yaml', 'r', encoding='utf-8') as f:
    data=yaml.safe_load(f)
print(data) #{'a': 1, 'b': 1.23, 'c': 'hello', 'd': [2, 3], 'f': {'name': 'yanfa'}, 'g': True, 'h': False, 'i': None}