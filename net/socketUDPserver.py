#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: Zhy
 @file: socketUDPserver.py
 @time: 17-12-12 下午1:50
    心有猛虎，细嗅蔷薇 
"""
import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', 31323))
    print('Bind UDP to 31323')
    while True:
        data, addr = s.recvfrom(1024)
        print('Received from %s:%s.' % addr)
        print(data)
        s.sendto(b'Hello, %s!' % data, addr)
    pass
except IOError as e:
    print('ioerror:', e)