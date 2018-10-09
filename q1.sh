#!/bin/bash

# check if proper number of arguments are specified 
if [ $# -ne 2 ]; then
  echo -e "Please provide an URL and a search term"
  exit 1
fi

# TODO: implement checking for output directory already exists
mkdir output
cd output

echo -e "Recursively searching all links in "$1"..."

# wget fetches .html files only at a depth of 1
wget -A.html --recursive --level=1 --convert-links -H -q $1

echo -e "\nNow finding search term "$2
# grep only looks at .html files
grep -r -i --include \*.html $2 .

if [[ $? != 0 ]]; then
  echo "No matching patterns found"
fi

# cleanup
cd ..
rm -r output

