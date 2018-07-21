#!/usr/bin/env python3

import sys

for line in sys.stdin:
    r = int(line[0:2], 16)
    g = int(line[2:4], 16)
    b = int(line[4:6], 16)
    if r > 127 and g < 128 and b < 128:
        print(line)
