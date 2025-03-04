# final_review.py
"""
This script simulates a final project review session.
It prompts you to enter a reflection on your project, including strengths, areas for improvement, and your next steps.
The responses are written to a file named 'final_review.log' and then displayed.

Steps:
1. Prompt the user for a final project review.
2. Log the responses with a timestamp to 'final_review.log'.
3. Read and display the logged review.
"""

import os
from datetime import datetime

LOG_FILE = "final_review.log"

def log_review(strengths, improvements, next_steps):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = (f"[{timestamp}] Strengths: {strengths}\n"
             f"[{timestamp}] Areas for Improvement: {improvements}\n"
             f"[{timestamp}] Next Steps: {next_steps}\n"
             + "=" * 40 + "\n")
    with open(LOG_FILE, "a") as f:
        f.write(entry)

def display_review():
    if os.path.exists(LOG_FILE):
        print("\n=== Final Project Review Log ===")
        with open(LOG_FILE, "r") as f:
            print(f.read())
    else:
        print("\nNo review log found.")

def main():
    print("=== Final Project Review Session ===")
    print("Enter your reflections on the project. Type 'exit' at any prompt to finish.\n")
    
    while True:
        strengths = input("What are the strengths of your project? ")
        if strengths.strip().lower() == "exit":
            break
        improvements = input("What are the areas that need improvement? ")
        if improvements.strip().lower() == "exit":
            break
        next_steps = input("What are your next steps for future development? ")
        if next_steps.strip().lower() == "exit":
            break
        
        log_review(strengths, improvements, next_steps)
        print("Your review has been logged.\n")
    
    display_review()

if __name__ == "__main__":
    main()
