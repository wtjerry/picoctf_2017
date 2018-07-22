#!/usr/bin/env python3

with open('data.pcap', 'rb') as f:
    d = f.read()
    chars = []
    for i in range(0, 3390, 51):
        for i2 in range(0, 51):
            if i2 == 18:
                num = d[i+i2]
                if num == 0:
                    continue
                elif 4 <= num <= 29:
                    chars.append(chr(num+61))
                elif num == 39:
                    chars.append('0')
                elif 30 <= num <= 38:
                    chars.append(chr(num+19))
                elif num == 45:
                    chars.append('_')
                elif num == 47:
                    chars.append('[')
                elif num == 48:
                    chars.append(']')
                else:
                    chars.append('unknown num:', num)
    print(''.join(chars))
