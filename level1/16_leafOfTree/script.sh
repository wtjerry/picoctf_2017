#!/bin/sh

cd /problems/4052472b84e355d1e1a42f5899fe0e76
find -type f | while read f; do echo ""; cat $f; done
