# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 18:36
# @Author  : yanfa
# @user   : yanfa 
# @File    : venv_.py
# @remark: 环境管理
""""""

"""一、什么是venv环境
1/虚拟环境是什么
2/虚拟环境的用途
3/venv&virtualenv"""

"""二、虚拟环境的优点
1/独立的python环境，不会产生冲突
2/有助于包的管理
3/删除和卸载方便"""

"""三、venv使用方法
1、创建虚拟环境 执行指令：python3 -m venv test
2、激活虚拟环境 
    切换指定文件夹 
        windows: /Scripts/
        macos: /bin/
    执行指令：activate  (macos：source ./test/bin/activate)

3、安装pyhton包"""

"""四、venv安装python包
python版本选择
    进入python2.7环境：python
    进入python3.x环境：python3
pip安装python包：
    安装python2.x 版本的包：pip install xx
    安装python3.x 版本的包：pip3 install xx  
"""

"""五、venv进入、退出和删除
进入虚拟环境：cd 虚拟环境名 (需要激活后，前头括号（test）代表在虚拟环境中)
退出虚拟环境：deactivate （win/masos相同指令,）
删除虚拟环境：删除环境目录 (会把安装的包一起删除rm -rf test)
"""

"""其他命令积累：
exit() 退出控制台
pip list :罗列安装包 pip3 list
"""