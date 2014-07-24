#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

class Student(object):
	def __init__(self):
		pass

s = Student()
s.name = 'Michael'
print s.name
# 给实例绑定一个方法
def set_age(self,age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s,Student)
s.set_age(25)
print s.age

# 对另一个实例是不起作用的
s2 = Student()
try:
	s2.set_age(1)
except:
	print 'wrong'

# 也可以给class绑定方法，所有实例都可用
def set_score(self,score):
	self.score = score
Student.set_score = MethodType(set_score,None,Student)

# 使用__slots__
# 如果我们想要限制class的属性怎么办？比如，只允许对Student实例添加name和age属性
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性
class Student(object):
	__slots__ = ('name','age') # 用tuple定义允许绑定的属性名称

# 但是slots对子类是没有用的
# 如果在子类中定义__slots__ 那么就是允许自身定义的和父类的
s = Student()
s.name = 'lisa'
s.age = 21
print s.name
print s.age
try:
	s.score = 100
except AttributeError:
	print "no score"
