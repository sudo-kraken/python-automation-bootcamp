# practical_challenge.py
"""
This script integrates interactive input, API data retrieval, and network automation.

Steps performed:
1. Prompts the user to choose a task:
   - Option 1: Fetch data from a public API.
   - Option 2: Connect to a network device and execute a command.
2. For Option 1, it sends a GET request to a sample API and displays key information.
3. For Option 2, it attempts to connect to a network device using Netmiko and execute a command.
   (Note: Replace placeholder values with real device details if available; otherwise, the error handling will show.)
"""

import requests
from netmiko import ConnectHandler

def perform_api_integration():
    url = "https://jsonplaceholder.typicode.com/todos/1"  # Sample API endpoint
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("\n=== API Integration Result ===")
            print("Fetched Data:")
            print(f"User ID: {data.get('userId')}")
            print(f"ID: {data.get('id')}")
            print(f"Title: {data.get('title')}")
            print(f"Completed: {data.get('completed')}\n")
        else:
            print(f"API request failed with status code: {response.status_code}\n")
    except Exception as e:
        print("An error occurred during API integration:")
        print(e)

def perform_network_automation():
    # Placeholder device details (update with real device info if available)
    device = {
        'device_type': 'cisco_ios',
        'ip': '192.168.1.1',
        'username': 'your_username',
        'password': 'your_password',
        'secret': 'your_secret'
    }
    try:
        print("\n=== Network Automation Simulation ===")
        print("Attempting to connect to the network device...")
        connection = ConnectHandler(**device)
        connection.enable()
        print("Connected successfully.")
        
        command = "show version"  # Example command; you can change this.
        print(f"Executing command: {command}")
        output = connection.send_command(command)
        print("Command Output:")
        print(output)
        
        connection.disconnect()
        print("Disconnected from the device.\n")
    except Exception as e:
        print("An error occurred during network automation:")
        print(e, "\n")

def main():
    print("=== Practical Challenge ===")
    print("Choose an option:")
    print("1. Perform API Integration")
    print("2. Perform Network Automation")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == '1':
        perform_api_integration()
    elif choice == '2':
        perform_network_automation()
    else:
        print("Invalid choice. Please run the script again and enter 1 or 2.")

if __name__ == "__main__":
    main()
