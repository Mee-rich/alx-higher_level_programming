#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL

# Check if URL argument is provided
if [ $# -eq 0 ];
then
	echo "Usage: $0 <URL>";
	exit;
fi

# Send request using curl and get the size of the response body in bytes
curl -sI "$1" | wc -c 
