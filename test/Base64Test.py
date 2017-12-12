#!/usr/bin/env python3
# -*- coding: utf-8 -*-
" 心有猛虎，细嗅蔷薇 "

__author__ = 'zhy'

import base64


def safe_base64_decode(s):
    if not len(s) % 4 == 0:
        if isinstance(s, str):
            s = s.encode('utf-8')
        s += b'=' * (4 - len(s) % 4)
    print(s)
    return base64.b64decode(s)


assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')