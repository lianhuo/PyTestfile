#!/usr/bin/env python3
# -*- coding: utf-8 -*-
" 心有猛虎，细嗅蔷薇 "

__author__ = 'zhy'

import time, threading

balance = 0
lock = threading.Lock()

def change_it(n):
    #先存后取
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            pass
            lock.release()

if __name__ == "__main__":
    t1 = threading.Thread(target=run_thread, args=(5, ))
    t2 = threading.Thread(target=run_thread, args=(8, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
