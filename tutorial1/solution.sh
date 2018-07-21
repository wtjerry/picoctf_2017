#!/bin/sh

cat list | grep "^Robin [a-zA-Z]* Morris$" | cut -d' ' -f2
