#!/usr/bin/env python3
# -*- coding: utf-8 -*-
" 心有猛虎，细嗅蔷薇 "

__author__ = 'zhy'

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务队列
task_queue = queue.Queue()
# 接受任务队列
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


def getTaskQueue():
    return task_queue


# 把两个队列注册到网络
QueueManager.register('get_task_queue', callable=getTaskQueue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000 ，设置验证吗
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动队列
manager.start()
# 通过网络访问queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
for i in range(10):
    n = random.randint(0, 100)
    print('Put task %d' % n)
    task.put(n)
print('Try get results')
for i in range(10):
    try:
        r = result.get(timeout=10)
        print('Result: %s' % r)
    except Exception as e:
        print("execption %s" % e)
# 关闭队列
manager.shutdown
print('master exit')

