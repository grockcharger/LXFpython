#!/usr/bin/env python  in Linux/OS X 
# -*- coding: utf-8 -*-

# type()

# type()函数可以查看一个类型或变量的类型
# type()函数既可以返回一个对象的类型，又可以创建出新的类型
def fn(self,name='World'):
	print('Hello, %s.' % name)

# 创建Hello class
Hello = type('Hello',(object,),dict(hello=fn))

h = Hello()
h.hello()

# 要创建一个class对象，type()函数依次传入3个参数：

# 1.class的名称；
# 2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# metaclass
# metaclass，直译为元类
# 先定义metaclass，就可以创建类，最后创建实例
# metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”

# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add'] = lambda self,value : self.append(value)
		return type.__new__(cls,name,bases,attrs)

class MyList(list):
	__metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类

L = MyList()
L.add(1)
print L
l = list()
try:
	l.add(1)
except:
	print "no add"


# 总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子

#ORM全称“Object Relational Mapping”，即对象-关系映射，
#就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，
#这样，写代码更简单，不用直接操作SQL语句

#让我们来尝试编写一个ORM框架
#编写底层模块的第一步，就是先把调用接口写出来。
#比如，使用者如果使用这个ORM框架，
#想定义一个User类来操作对应的数据库表User，
#我们期待他写出这样的代码

# class User(Model):
# 	#定义类的属性到列的映射：
# 	id = IntegerField('id')
# 	name = StringField('name')
# 	email = StringField('email')
# 	password = StringField('password')

# # 创建一个实例
# u = User(id=12345,name='Michael',email='test@orm.org',password='my-pwd')
# # 保存到数据库:
# u.save()
# 其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，剩下的魔术方法比如save()全部由metaclass自动完成。虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。


# 首先来定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
	def __init__(self,name,column_type):
 		self.name =name 
 		self.column_type = column_type
	def __str__(self):
 		return '<%s:%s>' %(self.__class__.__name__,self.name)

# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等
class StringField(Field):
	def __init__(self,name):
		super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
	def __init__(self,name):
		super(IntegerField,self).__init__(name,'bigint')

# 下一步，就是编写最复杂的ModelMetaclass了：

class ModelMetaclass(type):
	def __new__(cls,name,bases,attrs):
		if name == 'Model':
			return type.__new__(cls,name,bases,attrs)
		mappings = dict()
		for k,v in attrs.iteritems():
			if isinstance(v,Field):
				print('Found mapping: %s ==> %s' % (k,v))
				mappings[k]=v
		for k in mappings.iterkeys():
			attrs.pop(k)

		attrs['__table__'] = name # 假设表名和类名一样
		attrs['__mappings__'] = mappings # 保存属性和列的映射关系
		return type.__new__(cls,name,bases,attrs)

# 以及基类Model：
class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
	#定义类的属性到列的映射：
	id = IntegerField('id')
	name = StringField('name')
	email = StringField('email')
	password = StringField('password')

# 创建一个实例
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库:
u.save()



# 在ModelMetaclass中，一共做了几件事情：

# 排除掉对Model类的修改；

# 在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误；

# 把表名保存到__table__中，这里简化为表名默认为类名。





