#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from __builtin__ import enumerate
import pickle

class Atm:
#     def __init__(self,name,salary):
#         self.name = name 
#         self.salary = salary

    #将list转换为字典
    
    def show_dict(self,key):
        a = {}
        for i in enumerate(menu):
            a[i[0]] = i[1]
        return a[key-1]
    #展示菜单
    
    def show_menu(self):
        print '''welcome to atm
             what do you want to do?
             1)chan kan 
             2)quqian
             3)ye'e
             4)fanhui
             5)tyichu
            '''
    
    def input_choice(self):
        a = input('input your choice: ') 
        while a not in range(6):             
            a=input('input your choice: ')
        return a
    
    def input_name(self,content):
        a = raw_input('input your name :')
        i = 1
        while i <3:
            if a in content.keys():
                break
            else:
                a = raw_input('input your name: ')
        
        return a
            
    
  
    def test_passwd(self,name,content):
        i = 0
        b = False
        passwd = raw_input('input your passwd: ')
        while i<3:
            
            if content[name] == passwd:
                print 'welcome!'
                b= True
                break
            else:
                passwd = raw_input('input your passwd: ')
            i = i+1
        return b
                
if __name__ == '__main__':
    
    menu = ['chakan','quqian','yue','fanhui','tuichu']
    atm = Atm()
    a = {'zhou':'test'}
#     content = pickle.dump(a, open('D:/test.txt','w'))
    content = pickle.load(open('D:/test.txt','r'))
    print content
    name = atm.input_name(content)
    boo=atm.test_passwd(name,content)
    if not boo:
        print 'exit ,wrong passwd!'
    else:
        atm.show_menu()
        number=atm.input_choice()
        choice = atm.show_dict(number)
    
    

    
    
    
