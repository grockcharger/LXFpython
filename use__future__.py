#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# 使用__future__

# 把下一个新版本的特性导入到当前版本，于是我们就可以在当前版本中测试一些新版本的特性。

from __future__ import unicode_literals
from __future__ import division

# unicode_literals
print '\'xxx\' is unicode?', isinstance('xxx',unicode)
print 'u\'xxx\'is unicode?', isinstance(u'xxx',unicode)
print '\'xxx\' is str?', isinstance('xxx',str)
print 'b\'xxx\' is str?', isinstance(b'xxx',str)

# division
print '10 / 3=',10/3
print '10.0 / 3=',10.0/3
print '10 // 3=',10 //3