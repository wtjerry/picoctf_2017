#!/usr/bin/env python3

import sys

n = int(sys.stdin.read(), 2)
s = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
print(s)

