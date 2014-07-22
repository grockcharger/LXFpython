#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

classmates = ['Micheal','Bob','Tracy']
print "classmates = ['Micheal','Bob','Tracy']"
print classmates,"\n"

print len(classmates)

print classmates[0]
print classmates[len(classmates)-1]
print classmates[-1]
print classmates[-2], classmates[1],"\n"

classmates.append('Adam')
print "classmates.append('Adam')"
print classmates,"\n"

classmates.insert(1,'Jack')
print "classmates.insert(1,'Jack')"
print classmates,"\n"

classmates.pop()
print "classmates.pop()"
print classmates,"\n"

classmates.pop(1)
print "classmates.pop(1)"
print classmates,"\n"

classmates[1] = 'Sarah'
print "classmates[1] = 'Sarah'"
print classmates,"\n"

L = ['Apple',123,True]
print "L = ['Apple',123,True]"
print L,"\n"

s =['python','java',['asp','php'],'scheme']
print "s =['python','java',['asp','php'],'scheme']"
print s,len(s),s[2],s[2][1]

L = []
print "L=[]"
print L,len(L)