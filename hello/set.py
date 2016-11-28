#!/usr/bin/env python
# -*- coding:utf-8 -*-

se = {'a', 'b', 'c', 'X'}
se1 = {'1', '2', '3', "X"}

print(se)

se.discard('234')
print(se)

se2 = se.difference(se1)
se3 = se.symmetric_difference(se1)

print(se2)
print(se3)

ele = se.pop()
print(ele)
