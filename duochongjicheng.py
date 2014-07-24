#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# 多重继承
class Animal(object):
	pass

# 大类:
class Mammal(Animal):
	pass

class Bird(Animal):
	pass

#各种动物
class Dog(Mammal):
	pass
class Bat(Bird):
	pass

class Runnable(object):
	def run(self):
		print 'run'

class Flyable(object):
	def fly(self):
		print 'fly'

class Dog(Mammal,Runnable):
	pass

class Bat(Bird,Flyable):
	pass

# Mixin
#让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为Mixin

#Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixin和ThreadingMixin提供
# 编写一个多进程模式的TCP服务
class MyTCPServer(TCPServer,ForkingMixin):
	pass

# 编写一个多线程模式的UDP服务
class MyUDPServer(UDPServer,ThreadingMinxin):
	pass

# 如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixin
class MyTCPServer(TCPServer,CoroutineMixin):
	pass

