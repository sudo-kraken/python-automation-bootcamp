# Lesson 2: Automating Network Devices with Netmiko

## Overview
Network automation reduces manual work by using scripts to perform repetitive tasks on network devices. In this lesson, you will learn:
- What Netmiko is and how it simplifies SSH connections to network devices.
- How to establish a connection to a network device and execute commands.
- The importance of error handling and security best practices when automating network tasks.

### Detailed Explanation
- **Netmiko:**  
  Netmiko is a Python library built on top of Paramiko that simplifies SSH connections to network devices (such as routers and switches). It supports multiple device types.
  
- **Best Practices:**  
  - Use try/except blocks to handle connection errors.
  - Always secure your device credentials (do not hard-code sensitive information).
  - This demonstration uses placeholder values. For real execution, replace these with actual device details and credentials.

## Objectives
- Understand the basic structure of a network automation script.
- Learn to connect to a network device and execute a command using Netmiko.
- Practice error handling in network connections.

## Instructions
1. Read through the explanation above.
2. Run the `netmiko_example.py` demonstration script to see a simulated network automation task.
3. Practice by modifying the script:
   - Change the command to execute a different task.
   - If you have access to a network device, replace the placeholder values with real ones.
