#!/usr/bin/env python
#_*_ coding:utf-8 _*_

'''
Created on 2016Äê5ÔÂ11ÈÕ

@author: admin
'''
#!/usr/bin/env python
#_*_ coding:utf-8 _*_

def login(username):
    if username == 'zhouguanjie':
        return 'ok'
    else:
        return 'error'
def detatil(user):
    print '--------'

if __name__ == '__main__':
    user = raw_input("please input you name:")
    res = login(user)
    if res == 'ok':
        detatil(user)
    else:
        print 'wrong user'