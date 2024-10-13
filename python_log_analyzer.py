import re
import sys
from collections import defaultdict
from datetime import datetime

# Regex to match Nginx log format given.
LOG_PATTERN = (
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - \[(?P<time>.*?)\] "(?P<method>[A-Z]+) '
    r'(?P<path>.*?) HTTP/.*?" (?P<status>\d{3}) (?P<size>\d+) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"'
)

# parse a single log line.
def parse_log_line(line):
    match = re.match(LOG_PATTERN, line)
    if match:
        return match.groupdict()
    return None

# Function to analyze the logs.
def analyze_logs(log_file_path):
    ip_counts = defaultdict(int)
    path_counts = defaultdict(int)
    status_counts = defaultdict(int)
    user_agent_counts = defaultdict(int)

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            data = parse_log_line(line)
            if data:
                ip_counts[data['ip']] += 1
                path_counts[data['path']] += 1
                status_counts[data['status']] += 1
                user_agent_counts[data['user_agent']] += 1

    return {
        "top_ips": sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:5],
        "top_paths": sorted(path_counts.items(), key=lambda x: x[1], reverse=True)[:5],
        "top_status_codes": sorted(status_counts.items(), key=lambda x: x[1], reverse=True)[:5],
        "top_user_agents": sorted(user_agent_counts.items(), key=lambda x: x[1], reverse=True)[:5],
    }

# display the top 5 results
def display_analysis(analysis_data):
    print("\nTop 5 IP Addresses:")
    for ip, count in analysis_data['top_ips']:
        print(f"  {ip}: {count} requests")
    
    print("\nTop 5 Requested Paths:")
    for path, count in analysis_data['top_paths']:
        print(f"  {path}: {count} requests")
    
    print("\nTop 5 Response Status Codes:")
    for status, count in analysis_data['top_status_codes']:
        print(f"  {status}: {count} occurrences")
    
    print("\nTop 5 User Agents:")
    for user_agent, count in analysis_data['top_user_agents']:
        print(f"  {user_agent}: {count} requests")

# ability to run via command line argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <nginx-access-log-file>")
        sys.exit(1)

    log_file = sys.argv[1]
    analysis = analyze_logs(log_file)
    display_analysis(analysis)
