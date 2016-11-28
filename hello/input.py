#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = input("请输入您的名字:")
age = input("请输入您的年龄")
job = input("请输入您的工作")

msg = '''
Infomation of user %s:

---------
Name: %s
Age: %s
Job: %s
---------

''' % (name, name, age, job)

print(msg)
