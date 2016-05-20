#!/usr/bin/env python
#coding:utf-8

'''
继承与不继承的比较
私有属性的获取方法以及私有属性的修改方法
'''
class Test:
    def __init__(self,name):
        self.__name = name
    
    @property
    def get_name(self):
        return self.__name

#必须包含继承object
class Test1(object):
    def __init__(self,name):
        self.__name = name
    
    #获取私有属性
    @property
    def get_name(self):
        return self.__name
    #修改私有属性
    @get_name.setter
    def get_name(self,value):
        self.__name = value
    
t1 = Test('nihao')
print t1.get_name
t1.get_name = 'goodbye'
print t1.get_name

t2 = Test1('zhouguanjie')
print t2.get_name
t2.get_name = 'hello,zhou'
print t2.get_name