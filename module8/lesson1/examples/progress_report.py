# progress_report.py
"""
This script demonstrates a continuous improvement and feedback mechanism.
It prompts the user to enter details about their progress, challenges, and improvement goals,
logs the input to a file named 'progress_report.log', and then reads back the log.

Steps:
1. Prompt the user for progress, challenges, and goals.
2. Write the responses with a timestamp to 'progress_report.log'.
3. Optionally, display the current contents of the log file.

Note: This script uses real file I/O operations.
"""

import os
from datetime import datetime

LOG_FILE = "progress_report.log"

def log_progress(progress, challenges, goals):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = (f"[{timestamp}] Progress: {progress}\n"
             f"[{timestamp}] Challenges: {challenges}\n"
             f"[{timestamp}] Improvement Goals: {goals}\n"
             + "-" * 40 + "\n")
    with open(LOG_FILE, "a") as f:
        f.write(entry)

def display_log():
    if os.path.exists(LOG_FILE):
        print("\n=== Current Progress Report Log ===")
        with open(LOG_FILE, "r") as f:
            print(f.read())
    else:
        print("\nNo log file found.")

def main():
    print("=== Continuous Improvement and Feedback Session ===")
    print("Enter your progress details. Type 'exit' at any prompt to finish the session.\n")
    
    while True:
        progress = input("Describe your current progress: ")
        if progress.strip().lower() == "exit":
            break
        challenges = input("What challenges have you encountered? ")
        if challenges.strip().lower() == "exit":
            break
        goals = input("What are your improvement goals for the next phase? ")
        if goals.strip().lower() == "exit":
            break
        
        log_progress(progress, challenges, goals)
        print("Your input has been logged.\n")
    
    display_log()

if __name__ == "__main__":
    main()
