#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: Zhy
 @file: requestsTest.py
 @time: 17-12-11 下午12:05
    心有猛虎，细嗅蔷薇 
"""

# 豆瓣首页
import json

import requests

r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.status_code)
print(r.url)


def fetch_data(url):
    return requests.get(url).json()

# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
print(data.get('query').get('results').get('channel').get('location').get('city'))