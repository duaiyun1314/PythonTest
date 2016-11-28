#!/usr/bin/env python
# -*- coding:utf-8 -*-

test = 'Hello World!'


def printinfo(name, age, gender='男'):
    info = '我的名字叫：%s，我是 %s的，今年%d岁了' % (name, gender, age)
    print(info)
    return


def printstarfuc(name, *var_tuple):
    """
    一颗星会当做tuple来处理，传递的参数会加入到元祖当中
    :param name:
    :param var_tuple:
    :return:
    """
    print(name)
    for x in var_tuple:
        print(x)
    else:
        print('end')
    return


def printdoublestar(name, **var_dict):
    """
    两颗星不定长参数会作为dict来处理，传参相当于往dict中添加key-value
    :param name:
    :param var_dict:
    :return:
    """
    print(name)
    print(var_dict)

    pass


if __name__ == "__main__":
    print('自身在运行')
else:
    print('被其他模块引用')

# 常规参数
printinfo('zhangsan', 18)
printinfo('andy', 28, '男')

# 关键字参数
printinfo(name='lisi', age=18)
# 不定长参数 *
printstarfuc('xiaosna', 'haha', 'hehe')
printstarfuc('xiaohong', *('嘿嘿', '哈哈', '呵呵'))
# 不定长参数 **
printdoublestar('andy', age='22', gender='male')
printdoublestar('wang', **{"addr": '市南区', "weight": 160})
# lamda 函数

he = lambda x, y: x + y
print(he(10, 20))
