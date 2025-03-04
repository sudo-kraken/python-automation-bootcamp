# ai_overview.py
"""
This script simulates an AI code assistant by fetching a random piece of advice from the Advice Slip API.
The fetched advice represents a dynamic "AI suggestion" based on your query.

Steps:
1. Prompt the user for a query.
2. Use the requests library to fetch a random advice slip from the Advice Slip API.
3. Display the advice as the simulated AI's response.

Note: In a real-world scenario, you would connect to an AI API with proper authentication.
"""

import requests

def get_ai_suggestion():
    url = "https://api.adviceslip.com/advice"  # Alternative API endpoint for random advice
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Extract advice from the JSON response
            advice = data.get("slip", {}).get("advice", "No advice available.")
            return f"AI Suggestion: {advice}"
        else:
            return f"Failed to fetch AI suggestion. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    print("=== AI Dev Tools Overview ===")
    prompt = input("Enter your query for AI assistance: ")
    print(f"You asked: {prompt}\n")
    suggestion = get_ai_suggestion()
    print(suggestion)

if __name__ == "__main__":
    main()
