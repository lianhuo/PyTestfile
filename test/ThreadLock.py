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


from contextlib import closing
from contextlib import contextmanager
from urllib.request import urlopen


print(urlopen('https://www.python.org'))
for ab in urlopen('https://www.python.org'):
    print(ab)

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")