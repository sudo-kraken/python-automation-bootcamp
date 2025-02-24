# ai_exercise.py
"""
This script simulates an interactive AI-assisted development session.
It allows you to enter multiple queries and logs each query-response pair to a file named 'ai_log.txt'.

Steps:
1. Continuously prompt the user for input until they type 'exit'.
2. For each query, fetch a dynamic AI suggestion from the Advice Slip API.
3. Log the query and response to 'ai_log.txt'.
4. Display the AI suggestion to the user.

Note: This simulation uses a public API to mimic dynamic responses.
"""

import requests
from datetime import datetime

LOG_FILE = "ai_log.txt"

def get_ai_suggestion():
    url = "https://api.adviceslip.com/advice"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            advice = data.get("slip", {}).get("advice", "No advice found.")
            return advice
        else:
            return "Failed to fetch AI suggestion."
    except Exception as e:
        return f"Error: {e}"

def log_interaction(query, response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Query: {query}\n[{timestamp}] Response: {response}\n{'-'*40}\n"
    with open(LOG_FILE, "a") as file:
        file.write(log_entry)

def main():
    print("=== Interactive AI Dev Tools Session ===")
    print("Type 'exit' to finish the session.\n")
    
    while True:
        query = input("Enter your query: ")
        if query.strip().lower() == "exit":
            print("Session ended.")
            break
        
        suggestion = get_ai_suggestion()
        print("AI Response:", suggestion, "\n")
        log_interaction(query, suggestion)

if __name__ == "__main__":
    main()
