#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# 定义一个类
class Student(object):

	def __init__(self,name,score):
		self.name = name
		self.score = score

bart = Student('Michael',59)
print bart.name
print bart.score

# 数据封装-->类的方法
class Student(object):

	def __init__(self,name,score): #外部传入的参数
		self.name = name
		self.score = score

	def print_score(self):
		print "%s:%s" % (self.name,self.score)

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'
bart = Student('Michael',99)
bart.print_score()
print bart.get_grade()

#Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
bart.age = 21
lisa = Student('lisa',54)
print bart.age
try:
	print lisa.age
except:
	print "no age"

# 访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# 只有内部可以访问，外部不能访问

class Student(object):

	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print "%s:%s" % (self.__name,self.__score)

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.score

	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			print "wrong score"
# 这样就确保了外部代码不能随意修改对象内部的状态
bart = Student('lisa',80)
try:
	print bart.name
	print bart.__name
except:
	print 'no'
bart.name = 1
bart.__name = 2
print bart.name
print bart.__name
print bart._Student__name #不建议这么调用类内部的变量
bart.print_score()
bart.set_score(12)
bart.print_score()
bart.set_score(111)
bart.print_score()

#以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的


# 继承和多态

# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()

class Animal(object):

	def run(self):
		print 'Animal is runing...'
# 自动继承run
class Cat(Animal):
	pass

# 这就是多态
class Dog(Animal):
	def run(self):
		print 'Dog is runing...'


dog = Dog()
cat = Cat()
dog.run()
cat.run()

# 定义一个class的时候，我们实际上就定义了一种数据类型
# 我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样

print isinstance(cat,Animal)
print isinstance(dog,Dog)

# 多态的好处

# “开闭”原则
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
def run_twice(animal):
	animal.run()
	animal.run()

run_twice(Animal())
run_twice(Dog())

# 使用type()

#我们来判断对象类型，使用type()函数

print type(123),type('123'),type(None)
print type(abs),type(cat),type(Dog())
print type(132) == type(123123)
import types
print type('123') == types.StringType
print type(u'123') == types.UnicodeType

print type(int) == type(str) ==types.TypeType

# 使用isinstance()

# 对于class的继承关系来说，使用type()就很不方便
# 我们要判断class的类型，可以使用isinstance()函数

print isinstance(dog,Dog)
print isinstance(cat,Dog)
print isinstance(cat,(Cat,Animal)) # 是否其中之一

# str和unicode都是从basestring继承下来的
print isinstance(u'a',(str,unicode))
print isinstance(u'a',basestring)


# 使用dir()
#如果要获得一个对象的所有属性和方法，可以使用dir()函数

print dir(str)
print len('abc')
print 'abc'.__len__()
print dir(Animal)

# 仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()
class MyObject(object):

	def __init__(self):
		self.x = 9
	def power(self):
		return self.x*self.x

obj = MyObject()

print hasattr(obj,'x') #有属性x吗？
print obj.x
print hasattr(obj,'y')
setattr(obj,'y','y') # 设置属性y 值是y
print hasattr(obj,'y')
print getattr(obj,'y')
print obj.y

k = getattr(obj,'x')
# 这里如果obj的x是一个方法的话 调用k()和 obj.x()相同
print k