#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

names = ['zhangsan', 'wangwu', 'zhaoliu', 'zhouqi']

itr = iter(names)

while True:
    try:
        print(next(itr))
    except StopIteration:
        sys.exit()


