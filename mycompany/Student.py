#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self,name):
        self.name = name

    def print_name(self):
        print("name:%s" %self.name)


lh = Student("aa")

lh.name = "lianhuo"
lh.print_name()
lh.age = 19
mh = Student("aaa")
mh.print_name()
print(lh.age)

import json
if __name__=='__main__':
    ss = json.dumps(mh, default=lambda obj: obj.__dict__)
    print(ss)

# import NameManagerSystem

# NameManagerSystem.names
import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org', 'www.baidu.com'])
# print('Exit code:', r)


p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)