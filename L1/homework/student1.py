# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 21:49
# @Author  : yanfa
# @user   : yanfa 
# @File    : student.py
# @remark:
class Student:
    """
    1.编写学员实体类，对应属性包含：学号、姓名、性别。
    2.编写学员名单管理类，实现删除学员方法、查询学员方法
    """
    student_id=""
    name=""
    sex=""
    # # 构造方法 -自动执行,直接返回该类的实例，如果不行则默认创建一个构造方法
    # def __init__(self, student_id, name, sex):
    #     # 实例属性(变量)
    #     self.student_id = student_id  # 通过self绑定到自身
    #     self.name = name
    #     self.sex = sex
    #     print("这是构造方法")

    # 类方法 可以操作类的详细信息
    @classmethod  # 只能用这个装饰器
    def info(cls):  # cls是class的简写,是指类名本身
        print("这是类方法")
        info_list=[cls.student_id,cls.name,cls.sex]
        return info_list

class StudentList:
    def __init__(self, student_list):
        self.student_list = student_list

    def get(self, student_id):
        """
        根据 student_id 查询信息
        """
        student_info=Student.info()
        return student_info

    def delete(self, student_id):
        """
        根据 student_id 删除信息
        """
        student_info=Student.info()


if __name__ == '__main__':
    # 入参自己定义
    s1 = Student(1001, "1号", "男")
    s2 = Student(1002, "2号", "女")
    s3 = Student(1003, "3号", "男")
    # 初始化一个成员名单
    s_list = StudentList([s1, s2, s3])
    # 实现get()方法
    s_list.get(s1.student_id)
    # 实现delete
    s_list.delete(s1.student_id)
