import re

p = re.compile(r'\d+')
print p.findall('one1two2three3four4')