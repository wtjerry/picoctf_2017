#!/bin/sh

cat text | ./rot13.py | cut -d'"' -f2
