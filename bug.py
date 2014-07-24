#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# try:
try:
	print "try..."
	r = 10 / 0
	print 'Result',r
except ZeroDivisionError, e:
	print 'except:',e
else:
	pass
finally:
	print 'Finallly...'
print 'end'

# 没有错误发生，所以except语句块不会被执行
#但是finally如果有，则一定会被执行（可以没有finally语句）

try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END','\n'

# 调用堆栈
# err.py
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s)*2

def main():
	bar('0')

# main()

# 记录错误
# err.py
import logging

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s)*2

def main():
	try:
		bar('0')
	except StandardError, e:
		logging.exception(e)
	else:
		pass
	finally:
		pass

main() #程序打印完错误信息后会继续执行，并正常退出
print 'end','\n'

# 抛出错误
# raise语句抛出一个错误

class FooError(StandardError):
	pass

def foo(s):
	n = int(s)
	if n ==0:
		raise FooError('invalid value: %s' % s)
	return 10 / n

# foo(0)

# 另一种常见的方式

def foo(s):
	n = int(s)
	return 10 / n

def bar(s):
	try:
		return foo(s) *2
	except StandardError, e:
		print 'Error!'
		raise # raise语句如果不带参数，就会把当前错误原样抛出
	else:
		pass
	finally:
		pass

def main():
	bar('0')

#main()

# 调试

# 把关键的变量print出来，但还要删掉
# 。。。

# 断言(assert)
def foo(s):
	n = int(s)
	# assert的意思是，表达式n != 0应该是True，否则，后面的代码就会出错
	# 如果断言失败，assert语句本身就会抛出AssertionError
	assert n != 0,'n is zero!'
	return 10 / n
def main():
	foo('0')

# main()

# 程序中如果到处充斥着assert，
# 和print相比也好不到哪去。
# 不过，启动Python解释器时可以用-O参数来关闭assert
# python -O bug.py


# logging 
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
# print 10 / n


#pdb
# Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
s = '0'
n = int(s)
#print 10 / n
# 启动 python -m pdb bug.py
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：
# 任何时候都可以输入命令p 变量名来查看变量
# 输入命令q结束调试


# pdb.set_trace()
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点

import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print 10 / n

# 命令c继续运行

# 如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有PyCharm
# 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器











