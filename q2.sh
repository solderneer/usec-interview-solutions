#!/bin/bash

if [ $# -ne 2 ]; then
  echo -e "Invalid number of arguments"
  exit 1
fi

# TODO: Input validation to check for IP address
while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "IP address to be blocked: $line"
    iptables -A INPUT -s $line -j DROP
    echo "iptables -D INPUT -s $line -j DROP" | at now + $2 minutes
    echo "IP address("$lines") has been blocked for "$2" minutes\n"
done < "$1"
