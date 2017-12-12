#!/usr/bin/env python3
# -*- coding: utf-8 -*-
" 心有猛虎，细嗅蔷薇 "

__author__ = 'zhy'

from urllib import request
import json


def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        jsondata = json.loads(data.decode('utf-8'))
    return jsondata


# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
print(data.get('query'))
print(data.get('query').get('results'))
print(data.get('query').get('results').get('channel'))
print(data.get('query').get('results').get('channel').get('location'))
print(data.get('query').get('results').get('channel').get('location').get('city'))
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
assert data.get('query').get('results').get('channel').get('location').get('city') == 'Beijing'
print('ok')