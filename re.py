#!/usr/bin/python
import re

#email
email = 'sealzjh@gmail.com'
print re.findall("^sealzjh" , email)
print re.findall(".com$" , email)