# monitoring.py
"""
This script simulates a basic monitoring and troubleshooting process.

It performs the following:
1. Lists running processes using a system command.
2. Simulates a log file by creating a temporary file, writing sample log entries, and then tailing the file.
3. Displays the log file content to help troubleshoot potential issues.

Note:
- The command for listing processes may differ based on your operating system.
- On Unix-based systems, 'ps aux' is used; on Windows, 'tasklist' can be used.
"""

import os
import subprocess
import tempfile

def list_processes():
    print("=== Listing Running Processes ===")
    try:
        # Use 'ps aux' for Unix-based systems; adjust for Windows if needed.
        cmd = ["ps", "aux"] if os.name != "nt" else ["tasklist"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        print(result.stdout.strip())
    except Exception as e:
        print("Error listing processes:", e)
    print("")

def simulate_log_file():
    print("=== Simulating Log File ===")
    # Create a temporary log file with sample entries.
    with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".log") as temp_log:
        temp_log.write("2023-01-01 12:00:00 - Service started successfully.\n")
        temp_log.write("2023-01-01 12:05:00 - Warning: High memory usage detected.\n")
        temp_log.write("2023-01-01 12:10:00 - Error: Service crashed unexpectedly.\n")
        log_path = temp_log.name
    print(f"Temporary log file created: {log_path}\n")
    return log_path

def tail_log_file(log_path, lines=3):
    print(f"=== Displaying the Last {lines} Lines of the Log File ===")
    try:
        # Use 'tail' for Unix-based systems; for Windows, you may simulate by reading the file.
        if os.name != "nt":
            result = subprocess.run(["tail", f"-n{lines}", log_path], capture_output=True, text=True, check=False)
            print(result.stdout.strip())
        else:
            # Windows: read all lines and print the last 'lines'
            with open(log_path, "r") as f:
                log_lines = f.readlines()
            print("".join(log_lines[-lines:]).strip())
    except Exception as e:
        print("Error reading log file:", e)
    print("")

def main():
    list_processes()
    log_path = simulate_log_file()
    tail_log_file(log_path, lines=3)
    # Clean up the temporary log file
    os.remove(log_path)
    print("Temporary log file removed.")

if __name__ == "__main__":
    main()
