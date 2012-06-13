#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

html = '<a class="title" href="http://beijing.aifang.com/loupan/237004.html" target="_blank">北京城建世华泊郡</a><a class="title" href="http://beijing.aifang.com/loupan/237004.html" target="_blank">beijing aifang</a>'
pattern = re.compile(r'<a class=\"title\" href=\"([\s\S]*?)\" [^>]*?>([\s\S]*?)<\/a>')
#pattern = re.compile(r'<a.*?href=.*?<\/a>');
#match = pattern.match(html)
#if match:
#    print match.group()
urls=pattern.findall(html)
for i in urls:
    print i[1]
