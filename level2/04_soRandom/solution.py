#!/usr/bin/env python2

from subprocess import check_output
import random, string

encripted_flag = check_output(['nc', 'shell2017.picoctf.com', '63997'])[29:-1]
flag = ''
random.seed("random")
for c in encripted_flag:
  if c.islower():
    #rotate number around alphabet a random amount
    flag += chr((ord(c)-ord('a')-random.randrange(0,26))%26 + ord('a'))
  elif c.isupper():
    flag += chr((ord(c)-ord('A')-random.randrange(0,26))%26 + ord('A'))
  elif c.isdigit():
    flag += chr((ord(c)-ord('0')-random.randrange(0,10))%10 + ord('0'))
  else:
    flag += c
print flag
