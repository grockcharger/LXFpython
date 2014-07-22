#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

print abs(-20) # abs 就是一个函数 BIF

print cmp(1,2) # BIF 如果x<y，返回-1，如果x==y，返回0，如果x>y，返回1

print int('123'),int(12.34),float('12.34')
print str(1.23),unicode(100),bool(1),bool('')

a = abs
print a(-1)

# define a function

def my_abs(x):
	if x >= 0 :
		return x
	else:
		return -x

a = my_abs
print a(-1)

# 空函数
def nap():
	pass #pass 相当于一个占位符，占个位置

#参数检查
def my_abs(x):
	if not isinstance(x,(int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

a = my_abs
# print a('a') 直接弹出错误了就
print a(-1)

#返回多个值
import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny

print move(100,100,60,math.pi / 6)

#默认参数
def power(x):
	return x*x 

print power(5)

def power1(x,n=2): # 这里n=2 是默认参数
	s = 1
	while n > 0:
		n -= 1
		s *= x
	return s

print power1(5,2),power1(5),power1(5,3) #注意这里第二个power

# x,y = 0,0
# r = 20
# draw_circle(x,y,r) 画圆 多参数

#默认参数必须指向不变对象！
def add_end(L=[]):
	L.append('END')
	return L

print add_end([1,2,3])
print add_end()
print add_end()

#修改:
def add_end1(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
print add_end1([1,2,3])
print add_end1()
print add_end1()

#可变参数
def calc(number):
	sum = 0
	for n in number:
		sum = sum + n * n
	return sum

print calc([1,2,3])
#print calc(1,2,3)  #参数个数的错误，不是可变参数所以输出出错

def calc1(*number):
	sum = 0
	for n in number:
		sum = sum + n * n
	return sum

print calc1(1,2,3) #这回就可以了

nums = [1,2,3]
#print calc1(nums) #传入的是一个列表所以不能做运算
print calc1(nums[0],nums[1],nums[2])
print calc1(*nums)

#关键字参数
def person(name, age, **kw): 
	print 'name:',name,'age:',age,'others:',kw

person('Michael','35')
person('Bob','35',city='Beijing',job='Engineer')

dic1 = {'a':1,'b':2,'c':3}
for i,j in dic1.items():
	print "name:",i,"job:",j


kw = {'city':'Beijing','job':'Engineer'}
person('Jack',24,**kw)

#参数组合...参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数

def func(a,b,c=0,*args,**kw):
	print 'a=',a,'b=',b,'c=',c,'arg=',args,'kw=',kw

func(1,2)
func(1,2,3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=99)

args = (1,2,3,4)
kw = {'x':99}
func(*args,**kw)

# 默认参数一定要用不可变对象
# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict。

#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。