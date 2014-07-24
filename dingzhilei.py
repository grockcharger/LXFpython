#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# __str__

class Student(object):
	def __init__(self,name):
		self.name = name

print Student('Michael')

class Student(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student object (name:%s)' % self.name

print Student('Michael')
#__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的

class Student(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student object (name:%s)' % self.name
	__repr__ = __str__

# __iter__

#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环

class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1

	def __iter__(self):
		return self # 实例本身就是迭代对象，所以返回自己

	def next(self):
		self.a,self.b = self.b,self.a+self.b
		if self.a > 100000: # 退出循环的条件
			raise StopIteration();
		return self.a

for n in Fib():
	print n

#__getitem__

# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行
# 不能使用Fib()[5]来获取元素 会出错

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib(object):
	def __getitem__(self,n):
		a,b = 1,1
		for x in range(n):
			a,b = b,a+b
		return a
f = Fib()
print f[3],f[100]

# 想要切片功能的话还要加一些判断
# 因为原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice

class Fib(object):
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			a,b = 1,1
			L = []
			for x in range(stop+1):
				if x >= start:
					L.append(a)
				a,b = b,a+b
			return L
f = Fib()
print f[0:5],f[1:3]

# __getattr__

#动态返回一个属性
# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
class Student(object):
	def __init__(self):
		self.name = 'Michael'

	def __getattr__(self,attr):
		if attr == 'score':
			return 99
		if attr == 'age':
			return lambda:25
		raise AttributeError('\'Student\' has no attribute \'%s\'' % attr) 
s = Student()
print s.name
print s.score
print s.age()
# print s.abc

# API一旦改动，SDK也要改。
#利用完全动态的__getattr__，我们可以写出一个链式调用

class Chain(object):
	def __init__(self,path=''):
		self._path = path

	def __getattr__(self,path):
		return Chain('%s/%s' % (self._path,path))

	def __str__(self):
		return self._path

print Chain().status.user.timeline.list


#__call__

# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用

class Student(object):
	def __init__(self,name):
		self.name = name
	def __call__(self):
		print ('My name is %s' % self.name)

s = Student('Michael')
s()

#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

print callable(Student('name'))
print callable([1,2,3])
print callable(None)
print callable(max)

