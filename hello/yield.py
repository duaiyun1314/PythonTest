#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys


def fibonacci(x):
    a = 0
    b = 1
    counter = 0
    while counter < x:
        yield a  # 把当前值放到迭代器中输出
        counter += 1
        a, b = b, a + b


f = fibonacci(10)

while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()
