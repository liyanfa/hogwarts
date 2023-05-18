# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 20:28
# @Author  : yanfa
# @user   : yanfa 
# @File    : urllib3.py
# @remark: 常用第三方库 urllib3
""""""
import json

import urllib3

"""一、urllib概述
内置模块：urllib
第三方库：requests、urllib3"""

"""二、urllib3概述
1、线程安全
2、连接池管理
3、客户端SSL/TLS验证
4、支持http、socks代理
官方文档：https://urllib3.readthedocs.io/en/stable/"""

"""三、urllib3安装
通过pip安装：pip install urllib3"""

"""四、urllib3发送http请求"""
# def test_http():
#     # 创建连接池子对象，默认会校验证书
#     pm=urllib3.PoolManager()
#     # 发送http请求
#     res=pm.request(method='GET',url='http://httpbin.org/robots.txt')
#     # res=pm.request(method='GET',url='http://httpbin.org/ip')
#
#     print(type(res))
# HTTPResponse对象
# print(res.status) #查看响应状态码
# print(res.headers) #查看响应头信息
# print(res.data) #查看响应原始二进制信息


"""五、HTTPResponse对象和解析响应内容"""
# def test_response():
#     # 创建连接池子对象，默认会校验证书
#     pm=urllib3.PoolManager()
#     # 发送http请求
#     res=pm.request(method='GET',url='http://httpbin.org/ip')
#     # 获取二进制形式的响应内容
#     raw=res.data
#     print(type(raw),raw) #<class 'bytes'> b'{\n  "origin": "121.35.45.212"\n}\n'
#
#     # 使用utf-8编码成字符串
#     content=raw.decode('utf-8')
#     print(type(content),content) #<class 'str'>
#                                  # {
#                                  #   "origin": "121.35.45.212"
#                                  # }
#
#     # 将json字符串解析成字典对象
#     dict_obj=json.loads(content)
#     print(type(dict_obj),dict_obj) #<class 'dict'> {'origin': '121.35.45.212'}
#     print(dict_obj["origin"]) #121.35.45.212

"""六、request 请求参数
语法：request(method, url, fields, headers, **)
必填
    method：请求方式
    url：请求地址
选填
    headers：请求头信息
    fields：请求体数据
    body：指定请求体类型
    tiemout：设置超时时间"""

"""6.1 定制请求头信息"""


# def test_headers():
#     # 创建连接池子对象，默认会校验证书
#     pm = urllib3.PoolManager()
#     # 自定义请求头
#     headers = {"school": "hogwarts"}
#     # 发送http请求
#     res = pm.request(method='GET', url='http://httpbin.org/get', headers=headers)
#     content = json.loads(res.data.decode('utf-8'))
#     print(content["headers"])


"""6.2 定制请求参数
定制查询字符串参数：
    fields参数：适用于get、head、delete请求
    拼接url：适用于post、put请求
"""

#get、head、delete请求
def test_querystr_get():
    # 创建连接池子对象，默认会校验证书
    pm = urllib3.PoolManager()
    url = 'http://httpbin.org/get'
    # 自定义请求头
    fields = {'school': 'hogwarts'}
    # 发送http请求
    res = pm.request('GET',url , fields=fields)
    content = json.loads(res.data.decode('utf-8'))
    print(content) #{'args': {'school': 'hogwarts'}, 'headers': {'Accept-Encoding': 'identity', 'Host': 'httpbin.org', 'User-Agent': 'python-urllib3/1.26.7', 'X-Amzn-Trace-Id': 'Root=1-64637a5e-4d8f155839b8372e538b12c1'}, 'origin': '121.35.45.212', 'url': 'http://httpbin.org/get?school=hogwarts'}


#适用于post、put请求
# 提交query数据
def test_querystr_post():
    # 创建连接池子对象，默认会校验证书
    pm = urllib3.PoolManager()
    url = 'http://httpbin.org/post'
    # 从内置库urllib中parse模块导入编码方法
    from urllib.parse import urlencode
    # urlencode
    encode_str = urlencode({'school': 'hogwarts'})
    # 拼接到url中发送请求
    res = pm.request('POST',url=url+'?'+encode_str)
    content = json.loads(res.data.decode('utf-8'))
    print(content) #{'args': {'school': 'hogwarts'}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept-Encoding': 'identity', 'Content-Length': '0', 'Host': 'httpbin.org', 'User-Agent': 'python-urllib3/1.26.7', 'X-Amzn-Trace-Id': 'Root=1-64637b50-4c70e0ba01981df202dd3139'}, 'json': None, 'origin': '121.35.45.212', 'url': 'http://httpbin.org/post?school=hogwarts'}

#适用于post、put请求
# 提交form表单数据，类型 content_type:multipart/form-data
def test_form():
    # 创建连接池子对象，默认会校验证书
    pm = urllib3.PoolManager()
    url = 'http://httpbin.org/post'
    # urlencode
    fields = {'school': 'hogwarts'}
    # 拼接到url中发送请求
    res = pm.request('POST',url,fields=fields)
    content = json.loads(res.data.decode('utf-8'))
    print(content)
    print(content['form']) #{'school': 'hogwarts'}

#适用于post、put请求
# 提交json格式数据，类型 content_type:application/json
def test_json():
    # 创建连接池子对象，默认会校验证书
    pm = urllib3.PoolManager()
    url = 'http://httpbin.org/post'
    # 定义信息头
    headers={'Content-Type':'application/json'}
    # 定义json字符串
    json_str = json.dumps({'school': 'hogwarts'})
    # 发起请求
    res = pm.request('POST',url,headers=headers,body=json_str)
    # 转码结果
    content = json.loads(res.data.decode('utf-8'))
    print(content['json']) #{'school': 'hogwarts'}


"""6.3 设置超时时间timeout=3.0
单位秒，值的格式为float
"""
def test_timeout():
    # 创建连接池子对象，默认会校验证书
    pm = urllib3.PoolManager()
    # 访问这个地址，服务器会3秒后响应
    url = 'http://httpbin.org/delay/3'
    # 设置超时时间
    # res=pm.request('GET',url,timeout=4.0)
    # print(res.status) #正常返回
    res=pm.request(method='GET',url=url,timeout=2.0) # 会重试直到失败
    print(res.status) #urllib3.exceptions.MaxRetryError

"""6.4 发送https请求
默认校验证书；
PoolManager的cert_reqs参数：
    CERT_REQUIRED：需要校验
    CERT_NONE：不需要校验"""
def test_https():
    # 创建连接池子对象
    # pm = urllib3.PoolManager() #默认校验证书，返回正常
    # pm = urllib3.PoolManager(cert_reqs="CERT_REQUIRED") #默认校验证书，返回正常
    #
    pm = urllib3.PoolManager(cert_reqs="CERT_NONE") #返回警告 InsecureRequestWarning: Unverified HTTPS requestxx

    url = 'https://httpbin.ceshiren.com/get'
    # 发送https请求
    res=pm.request('GET',url)
    content = json.loads(res.data.decode('utf-8'))
    print(content) #{'school': 'hogwarts'}
if __name__ == '__main__':
    # test_querystr_get()
    # test_querystr_post()
    # test_form()
    # test_json()
    test_https()
