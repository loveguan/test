#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#反射的应用

text = raw_input("please input your path")
arry = text.split('/')
t = __import__('file.'+arry[0])  #xiangdangyu lujing
print t
model = getattr(t, arry[0]) #xiang dangyu huoqu mokuai
print model
func=getattr(model,arry[1])
func()


 
