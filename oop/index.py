#!/usr/bin/env python
#coding:utf-8

class Province(object):
    
    memo = 'hello,world!!!'
    
    #初始化
    def __init__(self,name,capital,leader,testt):
        self.name = name
        self.capital = capital
        self.leader = leader
        self.__taland = testt
    
    #静态方法
    @staticmethod
    def Foo():
        print 'hh '
    
    @staticmethod
    def Test():
        print 'test!'
    
    @staticmethod
    def static_func():
        
        print 'jingtai'
    
    #fangfa fagnwen xingshi bianwei ziduan fangwenxiangshi
    
    @property
    def bar(self):
        return 'test-texing'
    
    #访问私有属性的方法
    def tailand_test(self):
        return self.__taland
    
    #私有方法
    def __Foo2(self):
        return "私有方法"
    
    #访问私有方法的方法，不建议使用
    def Foo3(self):
        return self.__Foo2()
    
    #私有属性，只读
    @property
    def taland(self):
        return self.__taland
    
    #私有属性修改的方法
    @taland.setter
    def taland(self,value):
        self.__taland=value
         
sd = Province('山东','济南','周官杰',True)

#访问私有属性的方法，不建议使用
# print sd._Province__Foo2()
# print sd._Province__taland
# print sd.bar1
# print sd.__Foo2()

# print sd.Foo3()
# print sd.tailand_test()
# print sd.name,sd.capital,',',sd.leader
# print Province.memo
# print sd.memo
# print sd.bar
# # print sd.Foo()
# print '-------------------------'
# Province.Foo()
# Province.Test()
# print sd.taland
# sd.taland = False
# print sd.taland




