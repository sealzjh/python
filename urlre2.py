#!/usr/bin/python
import re

fp = open('list.txt' , 'r')
html = fp.read()
fp.close()


#purl = re.compile(r'href=\"(.*)\" target')
#m = purl.findall(html)
#url = m[0];
#print url

ptitle = re.compile(r'<a class="title" (.*)<\/a>')
m = ptitle.findall(html)
print m