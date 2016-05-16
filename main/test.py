#!/usr/bin/env python
#_*_ coding:utf-8 _*_

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