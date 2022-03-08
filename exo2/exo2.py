#!/usr/bin/env python3

import re

p = re.compile('.* {\n(?:.* = .*\n)*}')
file = open("./exo2.txt", 'r')
test = p.findall(file.read())
print(test)
