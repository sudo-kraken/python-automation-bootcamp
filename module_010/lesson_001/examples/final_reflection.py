# final_reflection.py
"""
This script simulates a final reflection session.
It prompts you to record your bootcamp journey, challenges, lessons learned, and next steps.
Each response is logged to a file 'final_reflection.log' with a timestamp.
After logging, the script opens the file using a system command.

Note:
- On Windows, the command to open a file is 'start'.
- On macOS, it's 'open'.
- On Linux, it's 'xdg-open'.
"""

import os
import subprocess
from datetime import datetime

LOG_FILE = "final_reflection.log"

def log_reflection(journey, challenges, lessons, next_steps):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = (
        f"[{timestamp}] Bootcamp Journey: {journey}\n"
        f"[{timestamp}] Challenges: {challenges}\n"
        f"[{timestamp}] Lessons Learned: {lessons}\n"
        f"[{timestamp}] Next Steps: {next_steps}\n"
        + "=" * 50 + "\n"
    )
    with open(LOG_FILE, "a") as f:
        f.write(entry)

def open_log_file():
    try:
        if os.name == "nt":
            os.system(f"start {LOG_FILE}")
        elif os.uname().sysname == "Darwin":
            os.system(f"open {LOG_FILE}")
        else:
            os.system(f"xdg-open {LOG_FILE}")
    except Exception as e:
        print("Error opening log file:", e)

def main():
    print("=== Final Reflection Session ===")
    print("Enter your reflections on your bootcamp journey. Type 'exit' at any prompt to finish.\n")
    
    while True:
        journey = input("Describe your overall journey and accomplishments: ")
        if journey.strip().lower() == "exit":
            break
        challenges = input("What challenges did you face? ")
        if challenges.strip().lower() == "exit":
            break
        lessons = input("What lessons have you learned? ")
        if lessons.strip().lower() == "exit":
            break
        next_steps = input("What are your next steps? ")
        if next_steps.strip().lower() == "exit":
            break
        
        log_reflection(journey, challenges, lessons, next_steps)
        print("Your reflection has been logged.\n")
    
    print("Opening your final reflection log for review...")
    open_log_file()

if __name__ == "__main__":
    main()
