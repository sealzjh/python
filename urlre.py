#!/usr/bin/python
import re

#fp = open('list.txt' , 'r')
#html = fp.read()
#print html
#fp.close()

html = '<a href="http://www.aifang.com/loupan/11159.html">loupan</a>'

p = re.compile(r'href=\"(.*)\"')
m = p.findall(html)
for index in m:
    print index