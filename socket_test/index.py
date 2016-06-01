
#!/usr/bin/env python

#coding:utf-8

import socket


def handle_request(client):
    
    buf=client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("Hello, World")


def main():
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.bind(('localhost',8080))
    sk.listen(5)    
    while True:
        connection,address = sk.accept()
        handle_request(connection)
        connection.close()
        
if __name__ =='__main__':
    main()