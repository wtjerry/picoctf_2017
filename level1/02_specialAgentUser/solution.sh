#!/bin/sh

sudo tcpdump -A -r data.pcap | grep Agent | grep Chrome
