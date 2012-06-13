import re

p = re.compile(r'\d+')
a = p.split('one1two2three3four4')
for index in a:
    print index
