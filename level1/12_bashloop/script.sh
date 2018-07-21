#!/bin/sh

cd /problems/bd058e83a119c78a006543d23d9f6422
for i in {1..4096}; do ./bashloop $i | grep -v Nope | grep -o "[a-z0-9]*$"; done
