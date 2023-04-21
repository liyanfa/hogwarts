# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 17:44
# @Author  : yanfa
# @user   : yanfa 
# @File    : student.py
# @remark:
class Student:
    def __init__(self, id, name, sex):
        self.id = id
        self.name = name
        self.sex = sex

    def info(self):
        """获取信息组装为列表"""
        info=[self.id,self.name,self.sex]
        return  info

class StudentList:
    def __init__(self, student_list):
        self.student_list = student_list

    def get(self, student_id):
        for student in self.student_list:
            if student[0] == student_id:
                print(f"学员信息获取成功：\n学号：{student[0]} 姓名：{student[1]} 性别：{student[2]}")
                return student
        return  print(f"学员信息获取失败,请检查学号是否正确")

    def delete(self, student_id):
        for student in self.student_list:
            if student[0]== student_id:
                self.student_list.remove(student)
                print(f"删除成功，删除后学员列表为：{self.student_list}")
                return self.student_list
        return print("删除失败,请检查学号是否正确")

if __name__ == '__main__':
    s1 = Student("1001", "1号", "男").info()
    s2 = Student("1002", "2号", "女").info()
    s3 = Student("1003", "3号", "男").info()
    student_list = StudentList([s1,s2,s3])
    student_list.get("1001")
    student_list.delete("1003")
