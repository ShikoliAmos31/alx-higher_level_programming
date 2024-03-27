#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Define variables
URL="$1"
EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"

# Send POST request with curl
RESPONSE=$(curl -s -X POST "$URL" -d "email=$EMAIL" -d "subject=$SUBJECT")

# Display response body
echo "POST params:"
echo "$RESPONSE"

