#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# 排序算法

print sorted([1,3,2,4,0]) # 接收的必须是列表

# 指定排序方法
def reversed_cmp(x,y):
	if x>y:
		return -1
	if x<y:
		return 1
	return 0
print sorted([5,1,2,3,4],reversed_cmp) # reversed_cmp后面不用()

# 字符串的排序
print sorted(['Zoo','about','bob','Credit'])
# 默认情况下，对字符串排序，是按照ASCII的大小比较的
# 所以大写字母Z在小写字母a的前面
# 当然也可以写个函数指定顺序排序
def cmp_ignor_case(s1,s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1 < u2:
		return -1
	if u1>u2:
		return 1
	return 0
print sorted(['Zoo','about','bob','Credit'],cmp_ignor_case)

