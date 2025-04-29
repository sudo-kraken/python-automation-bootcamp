# Example script: log_search.py
import re

file_path = input("Enter the log file path: ").strip()
pattern = input("Enter a search term or regex pattern: ").strip()

# Compile the regex pattern to catch errors early
try:
    regex = re.compile(pattern)
except re.error as err:
    print(f"Invalid regex pattern: {err}")
    exit(1)

try:
    with open(file_path, 'r') as logfile:
        found_any = False
        for line in logfile:
            if regex.search(line):
                print(line.rstrip())
                found_any = True
        if not found_any:
            print("No matches found for the pattern.")
except FileNotFoundError:
    print(f"File not found: {file_path}")
