#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# 自行编写my_map()

def fun(x):
	return x*x

def my_map(fun,*args):
	# if args is None:
	# 	return None
	L = []
	for i in args:
		L.append(fun(i))
	return L
print my_map(fun)
print my_map(fun,1,2,3,4,5)

# 模仿 map() 的功能自制 myMap()

def myMap(fun, list):
	return [fun(n) for n in list]

# 模仿 reduce() 的功能自制 myReduce()

def myReduce(fun, list):
	length = len(list)
	temp = list[0]

	i = 1
	while i < length:
		temp = fun(temp, list[i])
		i += 1
	return temp

