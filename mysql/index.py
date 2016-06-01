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
    conn = MySQLdb.connect(host='192.168.0.143', user='root', passwd='whjx*8888', db='test')

# 普通的形式拿到数据，与字典相对

#     cur = conn.cursor()
    
# 以字典的形式拿到数据

    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
#     sql = "insert into salor (name,address) values(%s,%s)"
#     params = ('alex_1','usa_l')

# 删除名字

#     sql = "delete from salor where id=%s"
#     params =('3',)

# 更新名字

#     sql = "update salor set name=%s where id=4"
#     params = ('sb',)

# 批量插入数据

#     li =[
#      ('ale1x','us1a'),
#      ('sb1','usa1'),
#      ]
#     reCount = cur.executemany('insert into salor(Name,Address) values(%s,%s)',li)
#     reount = cur.execute(sql,params)
#     conn.commit()

# 取出所有的数据

    li = [
     ('ale11x', 'us11a'),
     ('sb11', 'usa11'),
    ]
    reCount = cur.executemany('insert into salor(Name,Address) values(%s,%s)', li)
#     reCount = cur.execute('select * from salor')
    conn.commit()
    new_id = cur.lastrowid
    print new_id
#     data = cur.fetchall()
#     data = cur.fetchone()
#     print data
#     
#     
#     data = cur.fetchone()
#     print data
# #     cur.scroll(-1,mode='relative')
#     cur.scroll(0,mode='absolute')
#     data = cur.fetchone()
#     print data
    cur.close()
    conn.close()
#     print reCount
   
except Exception, e:
    print 'ee'
    print e
