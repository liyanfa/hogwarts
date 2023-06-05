# -*- coding: utf-8 -*-
# @Time    : 2023/5/17 20:29
# @Author  : yan_fa
# @user   : yan_fa
# @File    : student_info_manage_system.py
# @remark: 学习信息管理系统-重写版
from dataclasses import dataclass, field
from typing import List

"""项目简介
随着学校的规模变大，对应的学员回越来越多，相应的管理越来越难。 学员信息管理系统主要是对学员的各种信息进行管理，能够让学员的信息关系变得科学化、系统化和规范化。

知识点
    实体类
    成员变量属性
    方法
    Python 类型注解
    Python 数据类dataclass
    python封装与property装饰器
    文件处理
    异常类
    venv 环境管理
    pip 环境管理
受众
    高级测试工程师
作业要求
    1.编写学员实体类，对应属性包含：学号、姓名、性别。
    2.编写学员名单管理类，实现删除学员方法、查询学员方法。
    3.学员实体类添加一个私有属性成绩，要求实现对应的 getter 和 setter。
    4.实现更新学员、添加学员操作。
    5.添加学员时，把学员信息写入文件中；查看学员时，读取文件中学员的信息。
    6.自定义异常类：添加学员传入参数不合理时抛出自定义异常。
    7.创建一个venv 环境，实现环境隔离。
"""
"""根据示例代码中的注释信息，完成此题目的代码逻辑。
class Student:
    # 自己根据题目要求实现
    pass


class StudentList:
    def __init__(self, student_list: List[Student]):
        self.s_list = student_list

    def get(self, student_uuid: int):

        # 根据 student_uuid 查询信息
        pass

    def delete(self, student_uuid: int):
        #根据 student_uuid 删除信息
        pass

    def update(self, student: Student):
        pass

    def save(self, student: Student):
        pass


if __name__ == '__main__':
    # 入参自己定义
    s1 = Student()
    s2 = Student()
    s3 = Student()
    # 初始化一个成员名单
    s_list = StudentList([s1, s2, s3])
    #实现save
    s_list.save()
    # 实现update
    s_list.update()
    # 实现get()方法
    s_list.get()
    # 实现delete
    s_list.delete()
"""


class ErrorParameterException(Exception):
    """自定义参数异常，继承Exception"""
    pass


@dataclass()
class Student:
    # 数据类：指定参数，类型，默认值
    uuid: int = field(default=1001)
    name: str = field(default="张三")
    sex: str = field(default="男")
    __scores: float = field(default=60.00)

    # def __init__(self,uuid:int,name:str,sex:str):
    #     """构造方法"""
    #     self.uuid=uuid
    #     self.name=name
    #     self.sex=sex

    # def __str_(self):
    #     """打印对象信息"""
    #     return f"uuid:{self.uuid} name:{self.name} sex:{self.sex} scores:{self.scores}"

    # # 私有属性-成绩
    # __scores = None

    # 数据访问getter
    @property
    def scores(self):
        return self.__scores

    # 数据操作setter
    @scores.setter
    def scores(self, value):
        if value < 0 or value > 100:
            raise ErrorParameterException("分数请输入1-100的浮点型")
        self.__scores = value


class StudentList:

    def __init__(self, student_list: List[Student]):
        """构造方法 student_list: List[Student] 指定类型为list的Student对象"""
        self.s_list = student_list

    def save(self, student: Student):
        """根据 student 新增学员"""
        try:
            self.s_list.append(student)
            self.write_to_file(student)
        except ErrorParameterException:
            print("student参数不正确请检查")
        else:
            print(f"学号{student.uuid}添加成功")
        finally:
            print(f"学号{student.uuid}处理完毕\n")

    def update(self, student: Student):
        """根据 student 更新学员信息"""
        # 枚举函数获取索引和元素
        for index, element in enumerate(self.s_list):
            # 如果新加的学员uuid已经存在则替换整个student对象
            if student.uuid == element.uuid:
                self.s_list[index] = student
                print(f"【学号{student.uuid}更新成功】")
                # 替换完成后跳出整个循环
                break

    def get(self, uuid: int) -> Student:
        """根据 student_uuid 查询信息"""
        for student in self.s_list:
            if student.uuid == uuid:
                print(f"【学号{uuid}查询成功】")
                return student
        else:
            raise ErrorParameterException("uuid不正确请检查")

    def delete(self, uuid: int):
        """根据 student_uuid 删除信息"""
        for student in self.s_list:
            if student.uuid == uuid:
                self.s_list.remove(student)
                print(f"【学号{uuid}删除成功】")
                break
        else:
            raise ErrorParameterException("uuid不正确请检查")

    @staticmethod
    def write_to_file(student: Student):
        """保存时写入文件"""
        # 调用a-追加模式
        with open('student.txt', 'a', encoding='utf-8') as f:
            info = f"uuid:{student.uuid} name:{student.name} sex:{student.sex} scores:{student.scores}"
            f.write(info)
            f.write("\n")
            print(f"学号{student.uuid}写入成功")

    @staticmethod
    def read_from_file():
        """读取学员文件信息"""
        # 调用r-读取模式
        with open('student.txt', 'r', encoding='utf-8') as f:
            # 全部读取
            print(f"文件读取成功：\n")
            for i in f.readlines():
                print(i)

    @staticmethod
    def print_student_info():
        """打印学员列表信息"""
        print(f"当前学员列表信息为：")
        for s in s_list.s_list:
            print(s)
        print('\n')


if __name__ == '__main__':
    # 初始化空的学员列表
    s_list = StudentList([])

    # 实例化
    s1 = Student(1, '百里', '男')
    s2 = Student(2, '安安', '女')
    s3 = Student(3, '子期', '男')

    # 私有成绩赋值
    s1.scores = 100
    s2.scores = 59.50
    # s3.scores = 85.50 #不设置则为默认值

    # 实现新增，并保存到文件
    s_list.save(s1)
    s_list.save(s2)
    s_list.save(s3)

    # 读取文件
    s_list.read_from_file()

    # 实现更新
    s4 = Student(3, '亚瑟', '男')
    s4.scores = 33
    s_list.update(s4)
    print(f"学号{s4.uuid}更新后的信息为：{s4}")
    s_list.print_student_info()

    # 实现查询
    find_uuid = 2
    student_info = s_list.get(find_uuid)
    print(f"学号{find_uuid}获取到的信息为：{student_info}\n")

    # 实现删除
    s_list.delete(3)
    s_list.print_student_info()
