# netmiko_example.py
"""
This script demonstrates how to use the Netmiko library to automate network tasks.
**Important:** To run this script with a real device, replace the placeholder values with actual device details and credentials.

Steps performed:
1. Establish an SSH connection to a network device.
2. Execute a command (e.g., "show version") and print the output.
3. Disconnect from the device.

Best Practices:
- Use try/except blocks to catch and handle connection errors.
- Securely manage and store your device credentials.
"""

from netmiko import ConnectHandler

def connect_and_execute():
    # Replace these placeholders with your actual device details.
    device = {
        'device_type': 'cisco_ios',        # Adjust for your device type.
        'ip': '192.168.1.1',                 # Replace with the device's IP address.
        'username': 'your_username',         # Replace with your username.
        'password': 'your_password',         # Replace with your password.
        'secret': 'your_secret'              # Replace with your enable secret, if required.
    }
    try:
        print("Connecting to the network device...")
        connection = ConnectHandler(**device)
        connection.enable()
        print("Connected successfully.\n")
        
        command = "show version"  # Example command; change as needed.
        print(f"Executing command: {command}")
        output = connection.send_command(command)
        print("Command Output:")
        print(output)
        
        connection.disconnect()
        print("Disconnected from the device.")
    except Exception as e:
        print("An error occurred during connection or command execution:")
        print(e)

def main():
    print("=== Netmiko Automation Demonstration ===")
    connect_and_execute()

if __name__ == "__main__":
    main()
