# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 18:47
# @Author  : yanfa
# @user   : yanfa 
# @File    : test_allure_for_run_mode.py
# @remark: 第二节 allure2运行方式
""""""
import pytest

"""
一、生成测试报告流程
通过测试框架运行测试用例（pytest/junit5）->生成中间结果，包括json，text格式
                                            ->执行allure serve命令->生成在线版本报告
                                            ->执行allure generate命令->生成静态文件报告

二、使用allure2运行方式-python
使用--alluredir参数生成报告且指定报告存放路径
1、在参数执行期间收集结果
pytest [测试用例/模块/包] --alluredir=./result/
pytest test_allure_for_run_mode.py --alluredir=./result

2、如果想每次清理报告目录，添加命令
pytest test_allure_for_run_mode.py --alluredir=./result --clean-alluredir

3、生成在线测试报告
allure serve ./result

4、生成静态报告
    应用场景：如果希望随时打开报告，可以生成一个静态资源文件报告，将这个报告部署在web服务器上，启动web服务，即可随时查看
    解决方案：使用allure generate生成带有index.html的结果报告
    分为2步：
        第一步，生成报告 allure generate ./result,
            返回Report successfully generated to allure-report，同目录下生成allure-report
        第二步，打开报告
            可以找到allure-report根目录下index.html,右键open in Browser选择浏览器打开
            可以通过命令allure open ./myreport/

5、常用参数 [allure --help查看帮助文档]
1)  allure generate可以指定输出路径，也可以清理上次的报告记录
    -o/-output 输出报告的路径
    -c/-clean 清理报告
    allure generate ./result -o ./myreport -c
2)  allure open打开报告
    -h/-host 主机ip地址，此主机将用于启动报表的服务器
    -p/-port 主机端口，此端口将用于启动报表的服务器，默认值为0
    allure open -h 127.0.0.1 -p 8883 ./myreport/
"""

#例子 先执行pytest test_allure_for_run_mode.py --alluredir=./result ，
# 若提示--alluredir命令没找到，在虚拟环境安装pip install allure-pytest后重试
# 然后执行allure serve ./result生成在线报告
def test_case1():
    assert True

def test_case2():
    assert False

@pytest.mark.skip
def test_case3():
    assert 1+1==2

"""三、使用allure2运行方式-java
使用allure:report参数生成测试报告
1、在参数执行期间收集结果
mvn命令行使用，maven插件安装
mvn clean test allure:report

2、生成在线测试报告
mvn 直接找target/allure-results目录
mvn allure:serve

问题：
1、运行mvn命令对应没有在target下面生成allure-results目录，怎么解决？
解决方案：
    在src/test/resources路径下配置allure配置文件allure.properties,指明allure报告生成路径
    allure.results.directory=target/allure-results
2、运行mvn命令一直卡在下载中
解决方案：
    在项目下创建.allure文件夹
    下载allure解压到.allure文件夹
"""