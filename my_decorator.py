#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# import functools
# def log(*text):
# 	if text is None:
# 		def decorator(func):
# 			@functools.wraps(func)
# 			def wapper(*args,**kw):
# 				if text is None:
# 					print "begin call %s():" % func.__name__
# 					func(*args,**kw)
# 					print "end call %s():" % func.__name__
# 				else:
# 					print "%s %s():" % (text,func__name__)
# 					return func(*args,**kw)
# 			return wapper
# 		return decorator

# @log
# def now():
# 	print "I'm now"

# now()

# @log('calling')
# def now():
# 	print "I'm being calling"
# now()



import functools
def log(func,*text):
	if text is None:
		@functools.wraps(text)
		def wapper(*args,**kw):
			print "begin call %s():" % func.__name__
			a = func(*args,**kw)
			print "end call %s():" % func.__name__
			return a
		return wapper
	else:
		def decorator(func):
			@functools.wraps(func)
			def wapper(*args,**kw):
				print "%s %s():" % (text,func.__name__)
				return func(*args,**kw)
			return wapper
		return decorator

@log
def now():
	print "I'm now"
now()

@log('calling')
def now():
	print "I'm being calling"
now()