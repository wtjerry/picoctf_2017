#!/usr/bin/env python3

from gmpy2 import invert, to_binary, digits
import codecs

with open('RSA.txt', 'r') as f:
    lines = f.readlines()
    c = int(lines[0][3:])
    p = int(lines[1][3:])
    q = int(lines[2][3:])
    dp = int(lines[3][4:])
    dq = int(lines[4][4:])
    invQ = invert(q, p)
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)
    h = (invQ * (m1 - m2)) % p
    m = m2 + h * q
    s = str(hex(m)[2:])
    print(''.join([chr(int(s[i:i+2], 16)) for i in range(0, len(s), 2)]))
