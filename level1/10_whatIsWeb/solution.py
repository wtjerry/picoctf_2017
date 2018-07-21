#!/usr/bin/env python3

import re
import requests

r = requests.get('http://shell2017.picoctf.com:4079/')
f1 = re.findall('flag \(there are 3 parts\) is (.*) -->', r.text)[0]

r = requests.get('http://shell2017.picoctf.com:4079/hacker.css')
f2 = re.findall('flag is (.*)', r.text)[0].strip()

r = requests.get('http://shell2017.picoctf.com:4079/script.js')
f3 = re.findall('flag is (.*)', r.text)[0]

print(f1+f2+f3)
