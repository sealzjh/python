import re

pattern = re.compile(r'hello')

print pattern

match = pattern.match('hello world!')

print match

if match:
    print match.group()