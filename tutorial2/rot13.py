#!/usr/bin/env python3

import sys

for line in sys.stdin:
    chars_as_int = [ord(c) for c in line.rstrip()]
    rot_chars_as_int = []
    for i in chars_as_int:
        if 65 <= i <= 90:
            x = ((i-65+13)%26)+65
            rot_chars_as_int.append(x)
        elif 97 <= i <= 122:
            x = ((i-97+13)%26)+97
            rot_chars_as_int.append(x)
        else:
            rot_chars_as_int.append(i)
    print("".join([chr(c) for c in rot_chars_as_int]))

