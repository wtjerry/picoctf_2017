#!/bin/sh

sudo tcpdump -q -A -r data.pcap | grep -o "pswrd=.*$" | cut -d'=' -f2 | python3 -c "import sys; from urllib.parse import unquote; print(unquote(sys.stdin.read()))" | base64 -d
