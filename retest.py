#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
loupan = {}

fp = open('html/237004.txt' , 'r');
html = fp.read();

out=re.findall(r'<h1 class=\"t_name\" [^>]*?>([\s\S]*?)<\/h1>',html)
loupan['name'] = out[0]

out=re.findall(r'<li class="s">参考售价：<span [^>]*?><a [^>]*?>([\s\S]*?)<i>元\/平米</i>',html)
loupan['price'] = out[0]

out=re.findall(r'<li>开盘时间：<em>([\s\S]*?)<\/em>',html)
loupan['kaipan_date'] = out[0]

out=re.findall(r'<li><span [^>]*?>楼盘地址：\[<em>([\s\S]*?)</em>\] ([\s\S]*?)</span>',html)
loupan['region'] = out[0][0]
loupan['address'] = out[0][1]

for i in loupan:
    print loupan[i]