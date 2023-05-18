# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 19:50
# @Author  : yanfa
# @user   : yanfa 
# @File    : pymysql_.py
# @remark: 常用第三方库 pymysql
""""""
import sys

"""一、pymysql概述
1、python的数据库接口标准是Python DB-API
2、PyMySQL是从python连接到MYSQL数据库服务器的接口
3、PyMySQL的目标是成为MySQL的替代品
4、官方文档：http://pymysql.readthedocs.io/"""

"""二、pymysql安装
1、使用pip安装：pip install pymysql
2、使用pycharm界面安装"""

"""三、pymysql连接数据库
host：服务器地址
user：用户名
password：密码
database：数据库名称
charset：编码方式，推荐使用utf8mb4
"""
# 1、导入包
import pymysql

# 2、建立连接
conn=pymysql.connect(host="主机地址",
                     user="用户名",
                     password="密码",
                     database="数据库名称",
                     charset="utf8mb4")
# 3、关闭连接
conn.close()

"""封装获取连接的函数"""
def get_conn():
    conn=pymysql.connect(host="主机地址",
                     user="用户名",
                     password="密码",
                     database="数据库名称",
                     charset="utf8mb4")
    return conn

"""四、pymysql入门实例
获取连接对象：打开、关闭
获取游标对象：执行sql-execute()、查询记录、关闭游标"""

# def test_demo():
#     # 1、获取连接对象
#     conn=get_conn()
#     # 2、获取游标对象
#     cursor=conn.cursor()
#     # 3、执行sql
#     cursor.execute("select * from table")
#     # 4、查询结果
#     result1=cursor.fetchone() #获取第一条
#     result2=cursor.fetchall() #获取全部
#     result3=cursor.fetchmany(10) #获取前10条
#     # 5、关闭游标
#     cursor.close()
#     # 6、关闭连接
#     conn.close()

"""五、常用数据库操作
CRUD操作：
1）创建表：
2）插入记录
3）查询记录
4）更新记录
5）删除记录
执行事务：
1)提交：commit
2)回滚：rollback"""

# 5.1 创建表testcase
def test_create():
    conn=get_conn() #获取连接
    cursor=conn.cursor() #获取游标
    sql="create table `testcase`(" \
        "`id` int(11) not null auto_increment" \
        "`name` varchar(255) collale utf8_bin not null)"
    cursor.execute(sql) #执行建表语句

    cursor.close() #关闭游标
    conn.close() #关闭连接

# 5.2 插入记录
def test_insert():
    conn=get_conn() #获取连接
    cursor=conn.cursor() #获取游标
    sql="insert into testcase (id,name) values('123','yanfa')"
    cursor.execute(sql) #执行建表语句
    conn.commit() #提交

    cursor.close() #关闭游标
    conn.close() #关闭连接

# 5.3 执行事务
def test_insert1():
    conn=get_conn() #获取连接
    cursor=conn.cursor() #获取游标
    sql="insert into testcase (id,name) values('123','yanfa')"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    finally:
        cursor.close()  # 关闭游标
        conn.close()

# 5.4 查询操作
def test_retrieve():
    conn=get_conn() #获取连接
    cursor=conn.cursor() #获取游标
    sql="select * from testcase "
    # 捕获异常
    try:
        cursor.execute(sql)
        record=cursor.fetchone()
        print(record)
    except Exception as e:
        print(sys.exc_info()) #打印错误信息
    finally:
        cursor.close()  # 关闭游标
        conn.close() # 关闭连接

# 5.5 更新操作
def test_update():
    conn=get_conn() #获取连接
    cursor=conn.cursor() #获取游标
    sql="update testcase set name='lisi' where name='yanfa'"
    # 捕获异常
    try:
        cursor.execute(sql) #执行sql
        conn.commit() #提交事务
    except:
        conn.rollback() # 回滚事务
    finally:
        cursor.close()  # 关闭游标
        conn.close() # 关闭连接

# 5.6 删除
def test_delete():
    conn=get_conn() #获取连接
    cursor=conn.cursor() #获取游标
    sql="delete from testcase where name='yanfa'"
    # 捕获异常
    try:
        cursor.execute(sql) #执行sql
        conn.commit() #提交事务
    except:
        conn.rollback() # 回滚事务
    finally:
        cursor.close()  # 关闭游标
        conn.close() # 关闭连接
