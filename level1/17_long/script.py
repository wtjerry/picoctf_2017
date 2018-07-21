#!/usr/bin/env python3

import re
import sys

solution = ''
with open('flag', 'w') as debug:
  with open('pipe_in', 'r') as p_in:
    i = 0
    for l in p_in:
      l = l.strip()
      #debug.write(l+"\n")
      if i is 1:
        matches = re.findall("Please give me the '(.*)' character '(.*)' times, followed by a single '(.*)'", l)[0]
        char1 = matches[0]
        times = int(matches[1])
        char2 = matches[2]
        solution = char1 * times + char2 + "\n"
      if i is 3:
        sys.stdout.write(solution)
        sys.stdout.close()
      if i is 5:
        flag_line = l + "\n"
        debug.write(flag_line)
      i = i+1
