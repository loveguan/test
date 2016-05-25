#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#反射的应用

text = raw_input("please input your path")
arry = text.split('/')
try:
    t = __import__('file.'+arry[0])  #找到路径，文件的位置
    print t
    model = getattr(t, arry[0]) #找到模块
    print model
    func=getattr(model,arry[1]) #找到方法
    func()
except ImportError,e:
    print  e
    print '返回首页'
except Exception,e:
    print 2,e
    print 'heello'
else:
    print "it's ok"
finally:
    print 'bye'
        


 
