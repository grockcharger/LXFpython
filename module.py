#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-


# 模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
'a test module'
# 作者是谁。。。
__auther__ = 'Michael Liao'

import sys


# argv至少有一个元素，因为第一个参数永远是该.py文件的名称
# 用list存储了命令行的所有参数
def test():
	args = sys.argv
	if len(args)==1:
		print 'Hello World!'
	elif len(args)==2:
		print 'Hello, %s !' % args[1]
	else:
		print 'too many arguments!'

# 当我们在命令行运行hello模块文件时，
# Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码
# 最常见的就是运行测试。
if __name__=='__main__':
	test()


# 别名 ...as
try:
	import cStringIO as cStringIO
except ImportError:
	import StringIO


# 作用域

#内部函数的命名，不是无法被调用，但是习惯上这么写
def _private_1(name):
	return 'Hello, %s' % name

def _private_2(name):
	return 'Hi, %s' % name

#外部函数的命名，调用的时候用到的
def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)

