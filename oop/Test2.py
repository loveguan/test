#!/usr/bin/env python
# coding:utf-8

class Foo:
    def __init__(self):
        pass
    
    def __del__(self):
        print 'googbye'
    
    def Go(self):
        print 'Go'
        
    def __call__(self):
        print 'call method'

f1 = Foo()
f1.Go()
f1()
