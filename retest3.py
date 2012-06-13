#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

fp = open('html/list.txt' , 'r');
html = fp.read();

pattern = re.compile(r'<a class=\"title\" href=\"([\s\S]*?)\" [^>]*?>([\s\S]*?)<\/a>')
urls=pattern.findall(html)
for i in urls:
    print i[1]+"\t"+i[0]+"\n"
