#!/bin/bash

# Simple script to check for open ports on a given host
# Usage:
# ./check-ports.sh 192.168.20.134

for ports in {1..65535}
do
	timeout 1 bash -c "echo '' > /dev/tcp/$1/$ports" 2>/dev/null && echo "[+] PORT: $ports --> OPEN" &
done; wait
