#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l={'a': 1, 'b': 2, 'c': 3}
# 迭代key
for key in l:
    print("key:",key)
#迭代value
for value in l.values():
    print("value:",value)
#同时迭代key和value
for k, v in l.items():
    print("key:",k,"value:",v)
