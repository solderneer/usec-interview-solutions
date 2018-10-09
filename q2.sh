#!/bin/bash

if [ $# -ne 2 ]; then
  echo -e "Invalid number of arguments"
  exit 1
fi

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Text read from file: $line"
    iptables -A INPUT -s $line -j DROP
done < "$1"
