#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# 装饰器

def now():
	print "2014-7-23"

print now.__name__


# 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func): #1
	def wapper(*args,**kw):# 这里指wapper可以接受任意参数的调用
		print 'call %s():' % func.__name__ #3
		return func(*args,**kw) #4
	return wapper #2

@log	# 相当于 now = log(now)
def now():
	print "2014-7-23"
now()

# 其实就是多加一层 为了传个参数
def log1(text):
	def decorator(func):
		def wapper(*args,**kw):
			print "%s %s():" % (text, func.__name__)
			return func(*args,**kw)
		return wapper
	return decorator

@log1('execute')	#放在函数定义处 now = log('execute')(now)
def now():
	print "2014-7-23"
now()

#经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
print now.__name__

# 一个完整的decorator
import functools

def log(func):
	@functools.wraps(func)
	def wapper(*args,**kw):
		print "call %s():" % func.__name__
		return func(*args,**kw)
	return wapper

# 带参数的
import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wapper(*args,**kw):
			print "%s %s():" % (text,func.__name__)
			return func(*args,**kw)
		return wapper
	return decorator
	