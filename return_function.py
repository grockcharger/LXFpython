#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# 函数作为返回值

def calc_sum(*args):
	ax = 0
	for n in args:
		ax += n
	return ax

# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数！
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax += n
		return ax
	return sum

print calc_sum(1,2,3)
print lazy_sum(1,2,3)
f = lazy_sum(1,2,3)
print f()

