#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

try:
    # f = open('myfile.txt')
    f = open('../test.txt')
    s = f.readline()
    # i = int(s.strip())
    strs = str(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise RuntimeError("哈哈 出错了")
else:
    print('并没有发生任何错误')
finally:
    print('无论如何都会被执行')

'''
预定义清理行为，即使出现错误了，文件对象仍然能够关闭

'''
with open('../haha.txt', 'r') as f:
    for line in f:
        print(line, end='')
