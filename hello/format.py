#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 1、使用%来格式化
s1 = 'I am %s,age %d' % ('andy', 18)
print(s1)

# 2、使用format来格式化,{}作为占位符，里面如果是具体key的话需要传参的时候指定

s2 = 'I am {0},age {1}'.format('andy', 18)
print(s2)

s3 = 'I am {0},age {1}'.format(*('andy', 18))

print(s3)

s4 = 'I am {name},age {age}'.format(name='andy', age=18)

print(s4)

s5 = 'I am {name},age {age}'.format(**{'name': 'andy', 'age': 28})
