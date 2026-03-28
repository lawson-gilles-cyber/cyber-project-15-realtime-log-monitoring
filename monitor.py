# Real-Time Log Monitoring Script

import time

from core.detector import analyze_log

# File to monitor
log_file = "data/live_logs.txt"

print("=== Real-Time Monitoring Started ===\n")

# Open file in read mode
with open(log_file, "r") as file:
    # Move cursor to the end of file
    file.seek(0, 2)

    while True:
        line = file.readline()

        # If no new line, wait and retry
        if not line:
            time.sleep(1)
            continue

        line = line.strip()

        # Analyze new log line
        alert = analyze_log(line)

        if alert:
            print(alert)
