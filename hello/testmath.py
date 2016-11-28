#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
（1）导入单个模块
   import hello.testpackage.maths   引用时需要写全路径包名
   from hello.testpackage2 import chengfang  引用时只写模块名


（2） 一次性导入一个包下的多个模块

    from hello.testpackage import *这种方式只会导入__init__模块;
    - 在包下__init__中定义__all__变量
    - 在包下__init__中
      import hello.testpackage.jian
      import hello.testpackage.chengchu
      from hello.testpackage import *
"""
import hello.testpackage.maths
from hello.testpackage import *
from hello.testpackage2 import chengfang

print(hello.testpackage.maths.jia(10, 20))
# test()

print(jian.jian(30, 40))
print(chengchu.cheng(30, 10))
print(chengfang.chengfang(2, 10))
