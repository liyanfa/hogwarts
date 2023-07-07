# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 17:25
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_allure_for_install.py
# @remark: 第一节 allure2安装
""""""
"""
一、allure2介绍
1、allure是由java语言开发的轻量级，灵活的测试报告工具
2、alllre多平台的report框架
3、allure支持多语言，包括python，javascript、PHP、Ruby等
4、可以给开发/测试/管理等人员提供详细的测试报告，包括测试类别、测试步骤、日志、图片、视频等
5、可以为管理层提供高水准的统计报告
6、可以集成到jenkins生成在线的趋势汇总报告

二、allure报告展示
github 地址：https://github.com/allure-framework/allure2
官网：https://qameta.io/allure-report/

三、allure2安装
1、安装java,需要配置环境变量
2、安装allure，需要配置环境变量
3、安装插件：
    python: pip install allure-pytest
    java: maven插件安装

四、jdk下载与安装
java下载：
    官网：https://www.oracle.com/java/technologies/downloads/
    网盘：提取码: xwd9
    
Java 安装贴（windows 系统）：https://ceshiren.com/t/topic/13450 
Java 安装贴（mac 系统）：https://ceshiren.com/t/topic/6967

注意：
1、不推荐用帖子的：解决brew命令没找到，参考https://zhuanlan.zhihu.com/p/470873649
2、下载1.8后直接默认安装pkg，安装后，java -version
yanfa@yanfadeMacBook-Pro ~ % java -version 
java version "1.8.0_371"
Java(TM) SE Runtime Environment (build 1.8.0_371-b11)
Java HotSpot(TM) 64-Bit Server VM (build 25.371-b11, mixed mode)

五、allure下载与安装
1、先下载allure源码包到本地
   详细安装步骤参考：https://ceshiren.com/t/topic/3386

    mac：直接执行brew install allure
    windw:
        allure代码仓库：https://github.com/allure-framework/allure2/releases
        allure-commandline：https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/
    验证环境：allure --version
2、配置环境变量：解压后将bin目录加入path环境变量中
    mac无需操作
    
六、插件安装-python
安装python插件allure-pytest
1、执行命令：pip install allure-pytest，如果不行用pip3 install allure-pytest

2、查看是否安装
linux/mac:
pip3 list |grep allure
出现下面就代表安装成功
allure-pytest           2.13.2
allure-python-commons   2.13.2

windows:
pip list ｜findstr allure
"""