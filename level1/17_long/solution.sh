#/bin/sh

rm -f pipe_in
mkfifo pipe_in

./script.py | nc shell2017.picoctf.com 44840 > pipe_in && cat flag && rm -f flag debug pipe_in
