#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#zhuang shi qi

#带参数和返回值的装饰器

def outer(fun):
    def wrapper( arg):
        print 'xxxxxx'
        tet=fun(arg)
        return tet
    return wrapper
    


@outer
def Func1(arg):
    print 'func1',arg
    return 'return'

    
test = Func1('nihao')
print test

#不带参数的装饰器

def outer1(fun):
    def wrapper():
        print 'xxxxxx'
        fun()
        
    return wrapper


@outer1
def Func2():
    print 'func1'
 
   
test = Func2()

#带参数的装饰器

def outer2(fun):
    def wrapper(arg):
        print 'xxxxxx'
        fun(arg)
        
    return wrapper


@outer2
def Func3(arg):
    print 'func1',arg
 
   
test = Func3('zhouguanjie')


#