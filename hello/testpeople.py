#!/usr/bin/env python
# -*- coding:utf-8 -*-

from hello.entity.people import People
from hello.entity.singer import Singer


# 单继承
class Student(People):
    """学生类

    用来表示学生

    """
    def study(self):
        print("我正在学习")

    def speak(self, language='chinese'):
        """说话

            因为python的方法参数可以设定默认值，所以不提供方法重载,只支持内置的运算符重载
        """
        print("我只是一个学生我会说", language)


# def speak(self, language):
#     print("我是个学生，但是我会说", language)


# 多继承
class SingerStudent(Student, Singer):
    def __init__(self, name, age, gender, weight, sang):
        Student.__init__(self, name, age, gender, weight)
        Singer.__init__(self, sang)


people = Student('andy', 28, '男', 170)
people.speak()
people.myweight()

singer = Singer("晴天")
singer.sing()

singerpeople = SingerStudent('zhangsan', 24, '男', 234, '借口')
singerpeople.speak()
singerpeople.speak('english')
singerpeople.sing()
