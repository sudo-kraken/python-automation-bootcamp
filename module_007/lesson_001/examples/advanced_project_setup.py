# advanced_project_setup.py
"""
Advanced Project Setup Script

This script demonstrates an integrated automation project that:
1. Fetches data from a public API using the requests library.
2. Simulates CI/CD pipeline stages by executing real system commands.
3. Attempts network automation by connecting to a network device via Netmiko.

For demonstration:
- The API integration fetches a sample TODO item.
- The CI/CD simulation uses subprocess to run commands like 'git status' and 'echo'.
- The network automation part uses placeholder device details; replace these with real credentials for actual use.
"""

import requests
import subprocess
from netmiko import ConnectHandler

def api_integration():
    print("=== API Integration ===")
    url = "https://jsonplaceholder.typicode.com/todos/1"  # Sample API endpoint
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Fetched Data:")
            print(f"User ID: {data.get('userId')}")
            print(f"ID: {data.get('id')}")
            print(f"Title: {data.get('title')}")
            print(f"Completed: {data.get('completed')}\n")
            return data
        else:
            print(f"API request failed with status code: {response.status_code}\n")
            return None
    except Exception as e:
        print("Error during API integration:", e, "\n")
        return None

def ci_cd_simulation():
    print("=== CI/CD Pipeline Simulation ===")
    try:
        # Simulate pulling latest code using a real git command (requires Git installed and a repo)
        result = subprocess.run(["git", "status"], capture_output=True, text=True, check=False)
        print("Git Status Output:")
        print(result.stdout.strip() if result.stdout else "No repository found.")
    except Exception as e:
        print("Error during CI/CD simulation:", e)
    print("")
    try:
        # Simulate running tests using 'echo'
        result = subprocess.run(["echo", "All tests passed."], capture_output=True, text=True, check=False)
        print("Test Simulation Output:")
        print(result.stdout.strip())
    except Exception as e:
        print("Error during test simulation:", e)
    print("")
    try:
        # Simulate deployment using 'echo'
        result = subprocess.run(["echo", "Deployment successful."], capture_output=True, text=True, check=False)
        print("Deployment Simulation Output:")
        print(result.stdout.strip())
    except Exception as e:
        print("Error during deployment simulation:", e)
    print("")

def network_automation():
    print("=== Network Automation ===")
    # Replace these with actual device details to run against a real device.
    device = {
        'device_type': 'cisco_ios',
        'ip': '192.168.1.1',
        'username': 'your_username',
        'password': 'your_password',
        'secret': 'your_secret'
    }
    try:
        print("Attempting to connect to the network device...")
        connection = ConnectHandler(**device)
        connection.enable()
        print("Connected successfully.")
        
        command = "show version"  # Example command; modify as needed.
        print(f"Executing command: {command}")
        output = connection.send_command(command)
        print("Command Output:")
        print(output)
        
        connection.disconnect()
        print("Disconnected from the device.\n")
    except Exception as e:
        print("Network automation error:", e, "\n")

def main():
    print("=== Advanced Project Kick-Off ===\n")
    data = api_integration()
    ci_cd_simulation()
    network_automation()
    print("Advanced project setup complete.\n")
    
if __name__ == "__main__":
    main()
