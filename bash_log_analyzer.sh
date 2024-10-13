#!/bin/bash

# Check if run via command line argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <nginx-access-log-file>"
  exit 1
fi

LOG_FILE=$1

# Check if file exists
if [ ! -f "$LOG_FILE" ]; then
  echo "Error: File not found!"
  exit 1
fi

# Top 5 IP addresses
echo "Top 5 IP Addresses:"
awk '{print $1}' "$LOG_FILE" | sort | uniq -c | sort -rn | head -5
echo ""

# Copy Pasta Intensifies
# Top 5 Requested Paths
echo "Top 5 Requested Paths:"
awk '{print $7}' "$LOG_FILE" | sort | uniq -c | sort -rn | head -5
echo ""

# Top 5 Response Status Codes
echo "Top 5 Response Status Codes:"
awk '{print $9}' "$LOG_FILE" | sort | uniq -c | sort -rn | head -5
echo ""

# Top 5 User Agents
echo "Top 5 User Agents:"
awk -F\" '{print $6}' "$LOG_FILE" | sort | uniq -c | sort -rn | head -5
echo ""
