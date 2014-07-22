#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# 生成器（Generator）

L = [x*x for x in range(10)]
print L

g = (x*x for x in range(10))
print g
print g.next()

for n in g:
	print n

#斐波那契数列
def fab(max):
	n,a,b, = 0,0,1
	while n < max:
		print b
		a,b = b, a+b
		n += 1
fab(8)


# 生成器版斐波那契数列
def fab1(max):
	n,a,b, = 0,0,1
	while n < max:
		yield b
		a,b = b, a+b
		n += 1
print fab1(8)

def odd():
	print 'step 1'
	yield 1 	#生成器调用next的时候 遇到yield便返回
	print 'step 2'
	yield 3
	print 'step 3'
	yield 5

o = odd()
print o.next()
print o.next()
print o.next()

gen = (x for x in range(10))
print gen.next()

# for i in range(10):	这里yield的使用还是不太懂
# 	print gen.next()
	# if i > 5:
	# 	yield 1