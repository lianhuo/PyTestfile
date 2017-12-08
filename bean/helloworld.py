#coding=utf-8
import collections


from builtins import print

age = 11

if not age > 12:
    print("1")
else:
    print("2")


print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#字符串拼接方法
s1 = 75
s2 = 85
r = (s2 - s1) *100/s1
print("小明的成绩从去年的%d分提升到了今年的  %d分，提高了%.1f %%" % (s1, s2, r))

#这是list
classmates = ["aa", "bb", "cc"]
classmates.append(1)
print(classmates[-1])

#二维list
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

#循环
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("Hello %s" % name)


#元祖
s = set([1,2,3])
print(s)

#绝对值
print(abs(-22))


d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)


#定义函数  定义好之后才能用
def powe(a, y):
    return a+y
print(powe(1, 2))

#默认参数函数
def enroll(name, gender, age=18, city="tianjin"):
    print("name", name)
    print("gender", gender)
    print("age", age)
    print("city", city)

enroll("张三", "man")
enroll("张三", "man", city="ti", age=20)


#可变参数
def cale(*number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum
print(cale((1, 2, 3)[0], (1, 2, 3)[1], (1, 2, 3)[2]))
print(cale(*(1, 2, 3)))
print(cale(1, 2, 3))
print(cale())

# 位置参数
def person(name, age, city, job):
    print(name, age, city, job)
# person('Jack', 24, city='Beijing', job='Engineer')
person('Jack', 24, job='Beijing', city='Engineer')

#命名关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)
person2('Jack', 24, city='Beijing', job='Engineer')

# 递归函数
def fack(n):
    if n == 1:
        return 1
    return n * fack(n-1)

print(fack(100))

def fact_iter(n,product):
    if n == 1:
        return product
    return fact_iter(n-1, n * product)
def fact(n):
    return fact_iter(n, 1)
print(fact(100))


# 递归汉诺塔
def move(n, a, b, c):
    if n == 1:
        print('move', a, '->', c)
    else:
        move(n-1, a, c, b)
        print('move', a, '->', c)
        move(n-1, b, a, c)
move(3, 'A', 'B', 'C')

print('ABCDEFG'[:3]+'ABCDEFG'[-3:])

cqlh = 'ABCDEFG'[::3]
print(cqlh)

dicta = {'a': 1, 'b': 2, 'c': 3}
for dictb in dicta:
    print(dictb, dicta[dictb])

print(isinstance({"a":1,'b':"a",1:'v'},collections.Iterable))

for a, b in {"a":1,'b':"a",1:'v'}.items():
    print(a,b)

# 获取当前位置文件列表
import os
print([d for d in os.listdir("/home/zhy")])
# 列表生成式
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)

# 生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'Done'
i = fib(6)
for a in i:
    print(a)


def triangles():
    L0 = [1, 1]
    n = 1
    while True:
        L = []
        for i in range(n):
            if i == 0 or i == n - 1:
                L.append(1)
            else:
                L.append(L0[i] + L0[i - 1])

        yield L
        L0 = L
        n = n + 1
n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break
triang = triangles()
print(next(triang))
print(next(triang))
print(next(triang))


# 高阶函数
from math import sqrt
print(hex(int(sqrt(abs(25)))))


def do_stha(x):
    return [ash(x_k) for x_k in x]

def do_sth(x,ash):
    return [ash(x_k) for x_k in x]

def ash(x):
    return hex(int(sqrt(abs(x))))
# ash=hex(int(sqrt(abs(25))))
# print(do_stha([1,-3,-4,16,5])
print(do_sth([1,-3,-4,16,5],lambda x:ash(x)))

print(abs)

#map
def normalize(name):
    return name.lower().capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce
# filter 返回函数 匿名函数
def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# reduce
from functools import reduce
def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    if '.' in s:
        a = reduce(lambda x, y: x * 10 + y, map(char2num, s.replace('.', '')))
        print(a)
        print(10**(len(s) - s.index('.')-1))
        print((len(s) - s.index('.') -1))
        print(len(s))
        print(s.index('.')-1)
        print(s.index('.'))
        print(s.find('.'))
        return reduce(lambda x, y: x*10+y,map(char2num,s.replace('.',''))) / 10**(len(s) - s.index('.') -1)
        # return reduce(lambda x, y: x*10+y,map(char2num,s.replace('.',''))) / 10**(len(s) - s.find('.')-1)
    else:
        return reduce(lambda x, y: x*10+y,map(char2num,s)) / 1
    # return reduce(lambda x, y: x*10+y,[ int(c) for c in s if c != '.'])/ 10**(len(s) - s.index('.')-1)
    # return reduce(lambda x, y: x * 10 + y, [int(c) for c in s if c != '.']) / pow(10, len(s) - s.index('.') - 1)
print('str2float(\'123.456\') =', str2float('123.456'))

print('str2float(\'123.456\') =', str2float('123456'))
print('123.456'.index('.') - 1)
print(len('123.456'))
print('123.456'.find('.'))

import math
d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2float(s):
    def str2int(s):
        return reduce(lambda x,y : x * 10 + y,map(lambda x :d[x],s))
    index = s.find('.')
    if index == -1:        #没有小数点
        return str2int(s)
    s = s.replace('.','')
    return str2int(s) / math.pow(10,len(s) - index)
print('str2float(\'123.456\') =', str2float('123.456'))


# 回数

def is_palindrome(n):
    # return str(n) == str(n)[::-1]
    return list(map(int, str(n)[:int(len(str(n)) / 2)])) == list(map(int, str(n)[int(len(str(n)) / 2) + 1:len(str(n))]))[::-1]
output = filter(is_palindrome, range(10, 1000))
print(list(output))

print(list(map(int, str(101)[:int(len(str(101)) / 2)])))
print(list(map(int, str(101)[int(len(str(101)) / 2) + 1:len(str(101))]))[::-1])

# 素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    # def f(x):
    #     return x % n > 0
    # return f
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
for n in primes():
    if n < 100:
        print(n)
    else:
        break


print(sorted([36, 5, -12, 9, -21],key=abs))
print(sorted([36, 5, -12, 9, -21]))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)
print(sorted(L, key=lambda x:x[1],reverse=True))
print(sorted(L, key=lambda x:x[1]))


def calc_sum(*args):
    ax = 0
    for i in args:
        ax = ax +i
    return ax
print(calc_sum(*[1,2,3]))

def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum
print(lazy_sum(1,2,3)())


def count(*args):
    def g(i):
        def f():
            return i * i
        return f
    fs = []
    for j in args:
        fs.append(g(j))
    return fs


# def count(*args):
#     fs = []
#     for i in args:
#         def f():
#             return i * i
#         fs.append(f())
#     return fs

print(list(count(1,2,3))[0](),list(count(1,2,3))[1](),list(count(1,2,3))[2]())
# print(list(count(1,2,3))[0],list(count(1,2,3))[1],list(count(1,2,3))[2])

def count(*args):
    fs = []
    for i in args:
        fs.append(lambda i=i:i**i)
    return fs
print(list(count(1,2,3))[0]())

def f():
    def g(n):
        return n * n
    return g
print(f.__name__)
print(f().__name__)
print(f()(2))


# 装饰器

import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015.10.1')
now()

print(now.__name__)
now = log(now)
now()

def log2(x):
    def decorator(func,text=x):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s, %s():' % (text,func.__name__))
            func(*args,**kw)
            print('end,%s' % func.__name__)
            return
        return wrapper
    return decorator(func=x,text="call")if callable(x) else decorator

@log2
def f():
    print('fff')

@log2('text')
def b():
    print('fff')

f()
b()
# print(f.__name__)
# print(b.__name__)
#
print(callable(f))



def int2(x):
    return int(x,base=2)
print(int2("111"))

int3 = functools.partial(int, base=2)
print(int3('111'))
