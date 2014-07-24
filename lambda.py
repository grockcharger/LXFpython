#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# 匿名函数
print map(lambda X:X*X,[1,2,3,4,5])

# 匿名函数只能有一个表达式
def f(x):
	return x*x

f1 = lambda x: x*x
print f1(5)
for i in range(3):
	print f(i)
	