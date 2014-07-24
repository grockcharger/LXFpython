#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# 偏函数
print int('12345')
print int('12345',base=8)
print int ('12345',16),"\n"
# base是做为N进制的转换
print int('1000101',base=2)
import functools
int2 = functools.partial(int, base=2)
print int2('1000101',base=10)

# 当函数的参数个数太多，需要简化时
# 使用functools.partial可以创建一个新的函数
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。