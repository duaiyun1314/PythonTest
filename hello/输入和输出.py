#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle
import pprint
import sys

hello = 'Hello World!\n您好'

print(str(hello))
print(repr(hello))  # 转义字符原样输出
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x * x * x).rjust(4))

"""
{0:2d}  0表示该参数名，在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用

d表示参数类型为整型

"""
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

"""
format 一个字典，通过[]来确定键值
"""
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; '
      'Taobao: {0[Taobao]:d}'.format(table))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {Runoob:d}; Google: {Google:d}; '
      'Taobao: {Taobao:d}'.format(**table))

f = open('../test.txt', 'w+')
count = f.write('HelloWorld \n你好！python世界')
print('写入%d个字符' % count)
f.close()

f = open('../test.txt', 'r')
info = f.read()
print(info)
f.close()

f = open('../test.txt', 'r')
info = f.readline(5)  # 只读取第一行的前5个字符
print(info)
info = f.readlines()
print(info)
f.close()
del f
"""
pickle.load()
pickle.dump()
"""
datadict = {
    'name': 'andy',
    'desc': u'\u6211\u53eb\u0061\u006e\u0064\u0079',
    'age': 18
}

output = open('../objtest.txt', 'wb+')
pickle.dump(datadict, output)
output.close()

input = open('../objtest.txt', 'rb')
data = pickle.load(input)
#pprint.pprint(data)
print(data)
input.close()

