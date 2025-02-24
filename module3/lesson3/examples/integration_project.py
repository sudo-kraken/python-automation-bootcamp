# integration_project.py
"""
This script demonstrates an integration of API data retrieval and network automation.

Steps performed:
1. Fetch configuration data from a public API using the requests library.
2. Use part of the API data to determine which command to run on a network device via Netmiko.
3. Execute the network command and print the output.

**Important:**  
- The API endpoint and network device details are placeholders.
- For actual use, replace them with real API URLs and device credentials.

Best Practices:
- Use error handling to manage failures in either API calls or network connections.
"""

import requests
from netmiko import ConnectHandler

def fetch_configuration():
    url = "https://jsonplaceholder.typicode.com/todos/1"  # Sample API endpoint for demonstration
    try:
        response = requests.get(url)
        if response.status_code == 200:
            config = response.json()
            print("Fetched configuration from API:")
            print(config)
            return config
        else:
            print(f"Failed to fetch configuration. Status code: {response.status_code}")
            return None
    except Exception as e:
        print("An error occurred while fetching configuration:")
        print(e)
        return None

def update_device(config):
    # For demonstration, we choose a command based on the API data.
    # In a real-world scenario, the API data might include device-specific parameters.
    command = "show version" if config and config.get("completed") else "show ip interface brief"
    
    # Replace these placeholders with your actual device details.
    device = {
        'device_type': 'cisco_ios',
        'ip': '192.168.1.1',
        'username': 'your_username',
        'password': 'your_password',
        'secret': 'your_secret'
    }
    try:
        print("Connecting to the network device...")
        connection = ConnectHandler(**device)
        connection.enable()
        print("Connected successfully.\n")
        
        print(f"Executing command: {command}")
        output = connection.send_command(command)
        print("Command Output:")
        print(output)
        
        connection.disconnect()
        print("Disconnected from the device.")
    except Exception as e:
        print("An error occurred during device automation:")
        print(e)

def main():
    print("=== Integration Project Demo ===")
    config = fetch_configuration()
    if config:
        update_device(config)
    else:
        print("Skipping network automation due to API fetch failure.")

if __name__ == "__main__":
    main()
