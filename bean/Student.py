#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    # __slots__ = ("name")

    def __init__(self,name = ""):
        self.name = name

    def print_name(self):
        print("name:%s" %self.name)


lh = Student()

lh.name = "lianhuo"
lh.print_name()
lh.age = 19
mh = Student("aaa")
mh.print_name()
print(lh.age)

import mycompany.hello
mycompany.hello.test()
print(dir(mycompany.hello))
obj = Student()
if hasattr(obj, 'x'):
    print("ok")
