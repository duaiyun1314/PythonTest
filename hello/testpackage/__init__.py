#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    需要声明在其他模块里面导入  from 本包 import * 时要导入的本包的模块，有两种方式
    - 定义__all__变量
    - import hello.testpackage.jian
      import hello.testpackage.chengchu
      from hello.testpackage import *

"""
import hello.testpackage.jian
import hello.testpackage.chengchu
from hello.testpackage import *

# __all__ = ['jian', 'chengchu']

print('包初始化操作在__init__文件中  ', __package__)


def test():
    print('test')
