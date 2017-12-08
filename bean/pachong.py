#查找python的urllib库的request模块，导出urlopen函数
from urllib.request import urlopen
#urlopen用来打开并读取一个从网络获取的远程对象
html = urlopen("http://jxdxsw.com/")
print(html.read())