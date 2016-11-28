#!/usr/bin/env python
# -*- coding:utf-8 -*-

username = "andy"
password = "123"

name = input("用户名：")
pwd = input("密码：")

if username == name and password == pwd:
    print("登陆成功")
elif username == name:
    print("密码不正确")
else:
    print("用户名不正确")
