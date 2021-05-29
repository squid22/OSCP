#!/bin/bash

# Simple script to discover hosts
# Usage:
# ./check-ip.sh 192.168.1


for ips in {1..254}
do
	timeout 1 bash -c "ping -c 1 $1.$ips" &> /dev/null && echo "[+] $1.$ips --> ACTIVE" &
done; wait
