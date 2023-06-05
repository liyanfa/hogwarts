# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 23:17
# @Author  : yanfali
# @File    : poly_inhreritance.py
# @Software: PyCharm

class Human:
    """人类"""
    message="这是Human的类属性"

    #构造方法
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #实例方法
    def live(self):
        print("住在地球上")

class Student(Human):
    """学生类"""

    # 重写父类构造方法
    def __init__(self,name,age,school):
        #重写父类的构造方法，第一种方式：需要调用父类的构造方法
        # super().__init__(name,age)
        # self.school=school

        #第二种
        super(Student, self).__init__(name,age)
        self.school=school

    #重写父类实例方法-同名
    def live(self):
        print(f"住在{self.school}")

#实例化子类对象
stu=Student("yanfa",18,"清华大学")
print(stu.name)

#访问重写的实例方法
stu.live()  #住在清华大学  子类重写后会有更高的优先级
