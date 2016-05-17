#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from __builtin__ import enumerate
import pickle

class Atm:
#     def __init__(self,name,salary):
#         self.name = name 
#         self.salary = salary

    
    def show_dict(self,key):
        a = {}
        for i in enumerate(menu):
            a[i[0]] = i[1]
        return a[key-1]
            
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
    def input_name(self):
        return input('input your name :')
    
    def input_passwd(self):
        return input('input your passed')
    
    
if __name__ == '__main__':
    
    menu = ['chakan','quqian','yue','fanhui','tuichu']
    atm = Atm()
    content = pickle.load(open('D:/test.txt','r'))
    print content
    name = atm.input_name()
    while i>0:
k
    atm.show_menu()
    number=atm.input_choice()
    choice = atm.show_dict(number)
    
    

    
    
    
