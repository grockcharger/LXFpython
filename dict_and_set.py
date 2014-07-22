#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

names = ['Michael','Bob','Tracy']
scores = [95,75,85]

d = {'Michael':95,'Bob':75,'Tracy':85}
print d,d['Michael'],"\n"

d['Adam']=67
print "d['Adam']=67"
print d['Adam'],"\n"

d['Jack']=90
d['Jack']=88
print """d['Jack']=90
d['Jack']=88"""
print d['Jack'],"\n"

print "'Thomas' in d"
print 'Thomas' in d , "\n"

print "d.get('Thomas','not in d')"
print d.get('Thomas','not in d'),"\n"
print d,"\n"

d.pop('Bob')
print "d.pop('Bob')"
print d,"\n"

#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，
#正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
#这是因为dict根据key来计算value的存储位置，
#如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。
#这个通过key计算位置的算法称为哈希算法（Hash）。


s = set([1,2,3])
print "s = set([1,2,3])"
print s,"\n"

s = set([1,1,2,3,4,1,1,2,3])
print "s = set([1,1,2,3,4,1,1,2,3])"
print s,"\n"

s.add(5)
s.add(1)
print """s.add(5)
s.add(1)"""
print s,"\n"

s.remove(5)
print "s.remove(5)"
print s,"\n"

s1 = set([1,2,3])
s2 = set([2,3,4])
print """s1 = set([1,2,3])
s2 = set([2,3,4])
s1 & s2
s1 | s2"""
print s1 & s2
print s1 | s2

s = set([1,2])
s.add(('tuple',))
#s.add(['list',]) list 是可变对象所以不能添加
#s.add((1,[2,3]))同上
print s

#可变对象的操作
a = ['c','a','b']
print a,"a.sort()"
a.sort()
print a

#不可变对象的操作
a = 'abc'
b = a.replace('a','A')
print a,b