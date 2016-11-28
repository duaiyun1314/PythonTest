#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 全局变量要大写
NAME = 'andy'


def spell():
    """
    不能在函数内部直接给全局变量赋值如NAME = 'alex',这样python会当做是局部变量来处理
    如果要对全局变量重新赋值，需要先声明global variablename
    :return:
    """
    global NAME
    NAME = 'alex'
    print(NAME)
    pass


spell()
print(NAME)
