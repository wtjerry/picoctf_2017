#!/usr/bin/env python3

import sys

text_in = sys.stdin.read()
print(text_in)
l = []
for s in text_in:
    o = ord(s)
    h = hex(o)
    h = h[2:]
    l.append(h)
hexified = "".join(l)
print(hexified)
decimal = int(hexified, 16)
print(decimal)
