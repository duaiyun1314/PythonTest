#!/usr/bin/env python
# -*- coding:utf-8 -*-

for letter in 'andy':
    print(letter)

for i in range(3):
    print("次数：", i)

for y in range(4):
    print("y=", y)
    pass
else:
    print("循环完成")

for z in range(5):
    if z == 3:
        break
    print("z=", z)

for letter in 'hello world':
    if letter == "w":
        continue
    print(letter)
