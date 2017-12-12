#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: Zhy
 @file: socketClient.py
 @time: 17-12-12 上午10:26
    心有猛虎，细嗅蔷薇 
"""
import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('45.78.29.202', 43123))
    print(s.recv(1024).decode('utf-8'))
    sa = [b'aaa', b'bbb', b'ccc']
    sa.append(b'ddd')
    print(sa)
    for data in sa:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send('exit'.encode('utf-8'))
    s.close()
except IOError as e:
    print('IOError:..', e)
