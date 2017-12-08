#!/usr/bin/env python3
# -*- coding: utf-8 -*-
" 心有猛虎，细嗅蔷薇 "

__author__ = 'zhy'

import threading


class Student():

    def __init__(self, name):
        self.name = name

#创建全局的ThraedLocal对象


localSchool = threading.local()


def processStudent():
    std = localSchool.student
    print('Hellp %s (in %s)' % (std.name, threading.current_thread().name))


def processThread(stdent):
    localSchool.student = stdent
    processStudent()


if __name__ == "__main__":
    t1 = threading.Thread(target=processThread, args=(Student('张宏宇'), ), name="A")
    t2 = threading.Thread(target=processThread, args=(Student('zhy'), ), name="B")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    pass