#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib
from urllib import request

def getHtml(url):
    html = request.urlopen(url).read()
    return html.decode('UTF-8')

html = getHtml("http://www.baidu.com")
print(html)