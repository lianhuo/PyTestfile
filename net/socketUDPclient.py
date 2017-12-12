#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: Zhy
 @file: socketUDPclient.py
 @time: 17-12-12 下午1:57
    心有猛虎，细嗅蔷薇 
"""
import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b'aaa', b'bbb', b'ccc']:
        s.sendto(data,('45.78.29.202',31323))
        print(s.recv(1024).decode('utf-8'))
    s.close()
except IOError as e:
    print('ioerror:', e)