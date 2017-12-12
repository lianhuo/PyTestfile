#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: Zhy
 @file: psUtilsTest.py
 @time: 17-12-11 下午2:27
    心有猛虎，细嗅蔷薇 
"""
import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.pids())
print(psutil.test())
