#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: Zhy
 @file: socketClient.py
 @time: 17-12-12 上午10:26
    心有猛虎，细嗅蔷薇 
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 43123))
print(s.recv(1024).decode('utf-8'))
for data in [b'aaa', b'bbb', b'ccc']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send('exit')
s.close()
