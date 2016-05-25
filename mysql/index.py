#!/usr/bin/env python
#coding:utf-8

import MySQLdb
'''
try:
    conn = MySQLdb.connect(host='192.168.0.143',user='root',passwd='whjx*8888',db='test')
    cur = conn.cursor()
    recount = cur.execute('select * from shop')
    data = cur.fetchall()
    cur.close()
    conn.close()
    print recount
    print data
except Exception,e:
    print 'ee'
    print e
else:
    print 'hh'
finally:
    print 'end'
'''

try:
    conn = MySQLdb.connect(host='192.168.0.143',user='root',passwd='whjx*8888',db='test')
    cur = conn.cursor()
    sql = "insert into salor (name,address) values(%s,%s)"
    params = ('alex_1','usa_l')
# 删除名字
#     sql = "delete from salor where id=%s"
#     params =('3',)
# 更新名字
#     sql = "update salor set name=%s where id=4"
#     params = ('sb',)
    recount = cur.execute(sql,params)
    conn.commit()
    data = cur.fetchall()
    cur.close()
    conn.close()
    print recount
except Exception,e:
    print 'ee'
    print e
else:
    print 'hh'
finally:
    print 'end'