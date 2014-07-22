#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

#列表生成式即List Comprehensions

print range(1,11)

L = []
for x in range(1,11):
	L.append(x*x)
print L

a = [x * x for x in range(1,11)]
print a

print [m+n for m in 'ABC' for n in 'XYZ']

# 列出当前目录下的所有文件和目录名

import os
# os.listdir可以列出文件和目录
print [d for d in os.listdir('.')],"\n"


d = {'x':'A','y':'B','z':'C'}

print [k + '=' +v for k,v in d.iteritems()],"\n"

L = ['HELLO','WORLD']
print [s.lower() for s in L]

print isinstance(123,str)