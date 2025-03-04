# career_development.py
"""
This script simulates a career development planning session.
It prompts you to enter details about your current skills, areas for improvement, and career goals.
Each input is logged to a file named 'career_development.log' with a timestamp.
After logging, the script opens the file using a system command so you can review your career plan.

Note:
- Adjust the system command for opening files based on your operating system.
"""

import os
import subprocess
from datetime import datetime

LOG_FILE = "career_development.log"

def log_career_plan(skills, improvements, goals, strategies):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = (
        f"[{timestamp}] Current Skills: {skills}\n"
        f"[{timestamp}] Areas for Improvement: {improvements}\n"
        f"[{timestamp}] Career Goals: {goals}\n"
        f"[{timestamp}] Strategies: {strategies}\n"
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
    print("=== Career Development Planning Session ===")
    print("Enter your professional development details. Type 'exit' at any prompt to finish.\n")
    
    while True:
        skills = input("List your current key skills: ")
        if skills.strip().lower() == "exit":
            break
        improvements = input("What areas would you like to improve? ")
        if improvements.strip().lower() == "exit":
            break
        goals = input("What are your short-term and long-term career goals? ")
        if goals.strip().lower() == "exit":
            break
        strategies = input("What strategies will you use to achieve these goals? ")
        if strategies.strip().lower() == "exit":
            break
        
        log_career_plan(skills, improvements, goals, strategies)
        print("Your career development plan has been logged.\n")
    
    print("Opening your career development log for review...")
    open_log_file()

if __name__ == "__main__":
    main()
