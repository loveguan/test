#!/usr/bin/env python
#_*_ coding:utf-8 _*_

# def login(username):
#     if username == 'zhouguanjie':
#         return 'ok'
#     else:
#         return 'error'
# def detatil(user):
#     print '--------'
# 
# if __name__ == '__main__':
#     user = raw_input("please input you name:")
#     res = login(user)
#     if res == 'ok':
#         detatil(user)
#     else:
#         print 'wrong user'

text = raw_input("please input your path")
str1 = text.split('/')
t = __import__('file'+'demo')
