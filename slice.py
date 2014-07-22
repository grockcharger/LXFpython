#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# 切片
# 1 
L = ['Michael','Sarah','Tracy','Bob','Jack']
print L,"\n"
print [L[0],L[1],L[2]],"\n"

# 2 
r = []
n = 3
for i in range(n):
	r.append(L[i])

print r,"\n"

print L[0:3],"\t",L[:3]

print L[-2:],"\t",L[-2:-1],"\n"

L = range(100)
print L,"\n"

print L[:10]
print L[-10:]
print L[:10:2]
print L[::5]
print L[:],"\n"

# tuple ，字符串或者unicode字符串都可以切片
print (1,2,3,4)[:3]
print 'ABCDE'[:1]