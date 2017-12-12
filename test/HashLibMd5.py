import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


md5a = hashlib.md5()
md5a.update('how to use md5 in '.encode('utf-8'))
md5a.update('python hashlib?'.encode('utf-8'))
print(md5a.hexdigest())