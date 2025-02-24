# api_requests.py
"""
This script demonstrates how to use the requests library to fetch data from a RESTful API.

Steps performed:
1. Send a GET request to a sample public API endpoint.
2. Check the response status code.
3. Parse the JSON response and print specific fields.

Note: The API endpoint used here is from jsonplaceholder.typicode.com for demonstration purposes.
"""

import requests

def fetch_api_data():
    url = "https://jsonplaceholder.typicode.com/todos/1"  # Sample API endpoint
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()  # Parse JSON data
            # Print some key fields from the response
            print("User ID:", data.get("userId"))
            print("ID:", data.get("id"))
            print("Title:", data.get("title"))
            print("Completed:", data.get("completed"))
        else:
            print(f"Request failed with status code: {response.status_code}")
    except Exception as e:
        print("An error occurred:", e)

def main():
    print("=== API Requests Demonstration ===")
    fetch_api_data()

if __name__ == "__main__":
    main()
