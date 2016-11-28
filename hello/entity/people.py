#!/usr/bin/env python
# -*- coding:utf-8 -*-


class People:
    name = ''
    age = 0
    gender = '男'
    __weight = 0

    def __init__(self, name, age, gender, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.__weight = weight

    def speak(self):
        print('我的名字叫%s,我是%s的，我今年%d岁了' % (self.name, self.gender, self.age))

    def myweight(self):
        print("我的体重是", self.__weight - 10)
