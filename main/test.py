#!/usr/bin/env python
#_*_ coding:utf-8 _*_

'''
import random
code = []
for i in range(6):
    if i == random.randint(1,5):
        code.append(str(random.randint(1,9)))
    else:
        temp = random.randint(65,90)
        code.append(chr(temp))
        
print ''.join(code)

import hashlib
hash = hashlib.md5()
hash.update('admin')
print hash.hexdigest()
'''

import pickle
from _elementtree import dump
li = ['alex',11,22,'ok']

dumpsed = pickle.dumps(li)
print dumpsed    
print type(dumpsed)
loaded = pickle.loads(dumpsed)
print loaded
print type(loaded)


dumpsed = pickle.dump(li, open('D:/test.txt','w'))
print type(dumpsed)
loaded = pickle.load(open('D:/test.txt','r'))

print type(loaded)
print loaded





