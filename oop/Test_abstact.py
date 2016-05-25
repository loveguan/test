#!/usr/bin/env python
#coding:utf-8

#接口，抽象
from abc import abstractmethod, ABCMeta
from _pyio import __metaclass__

class bar(object):
    __metaclass__ = ABCMeta
    @abstractmethod 
    def Foo(self):
        pass
    
class foo(bar):
    def __init__(self):
        pass
    
    def Foo(self):
        print 'hello,world!!!'
foo().Foo()

    