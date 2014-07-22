#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# 迭代

d = {'a':1,'b':2,'c':3}

for key in d:
	print key

for value in d.itervalues():
	print value

for k, v in d.iteritems():
	print k,v

for ch in 'ABC':
	print ch

# 判断一个对象是可迭代对象
from collections import Iterable
print isinstance('abc',Iterable) # str 是否可迭代
print isinstance([1,2,3],Iterable) # list 是否可迭代
print isinstance(123,Iterable) # 整数是否可迭代

# 输出索引和列表内容
for i, value in enumerate(['A','B','C']):
	print i,value

for x,y in [(1,2),(2,3),(3,4)]:
	print x,y