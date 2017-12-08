#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '

__author__ = 'zhy'

import time, threading

def loop():
    print("thread %s is running" %(threading.current_thread().name))
    n = 0
    while n < 5:
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        n = n + 1
        time.sleep(1)
    print('thread %s end' % threading.current_thread().name)

if __name__ == '__main__':
    print("thread %s is running" % (threading.current_thread().name))
    t = threading.Thread(target=loop)
    t.start();
    t.join();
    print("thread %s is end" %(threading.current_thread().name))

