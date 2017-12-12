#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: Zhy
 @file: socket.py
 @time: 17-12-12 上午9:30
    心有猛虎，细嗅蔷薇
"""
import socket
import threading

import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 43123))
s.listen(5)
print('Waiting for connection')


def tcplink(sock, adrr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s !' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    pass


while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


