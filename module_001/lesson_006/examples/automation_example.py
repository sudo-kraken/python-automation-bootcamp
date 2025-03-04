# automation_example.py
"""
This script demonstrates how to use the Netmiko library to automate network tasks.
**Note:** To run this script successfully, you must have access to a network device and valid credentials.
The device details here are placeholders. Replace them with actual values for real execution.

Best Practices:
- Use try/except blocks to handle connection errors.
- Securely manage your device credentials.
- Use logging to track command execution.

The script performs the following steps:
1. Connects to a network device using Netmiko.
2. Executes a command (e.g., "show version") and prints the output.
3. Disconnects from the device.
"""

from netmiko import ConnectHandler

def connect_and_execute():
    # Replace these placeholder values with actual device details.
    device = {
        'device_type': 'cisco_ios',        # Adjust for your device type.
        'ip': '192.168.1.1',                 # Replace with the actual IP address.
        'username': 'your_username',         # Replace with your username.
        'password': 'your_password',         # Replace with your password.
        'secret': 'your_secret'              # Replace with your enable secret, if needed.
    }
    try:
        print("Attempting to connect to the network device...")
        connection = ConnectHandler(**device)
        connection.enable()
        print("Connection successful.")
        
        # Execute a command (for example, "show version")
        print("Executing command: show version")
        output = connection.send_command("show version")
        print("Command Output:")
        print(output)
        
        # Disconnect the session
        connection.disconnect()
        print("Disconnected from the device.")
    except Exception as e:
        print("An error occurred during connection or command execution:")
        print(e)

def main():
    print("=== Network Automation Example using Netmiko ===")
    connect_and_execute()

if __name__ == "__main__":
    main()
