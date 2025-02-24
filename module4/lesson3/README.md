# Lesson 3: Integrating Network Automation into DevOps Workflows

## Overview
Integrating network automation into DevOps workflows enables coordinated changes across both applications and networks. In this lesson, you will see how to:
- Retrieve configuration data from an API.
- Use that data to decide which network command to execute.
- Connect to a network device using Netmiko and execute the command.

### Detailed Explanation
- **Integration Concept:**  
  API data can drive decisions in network automation—for example, determining if a device configuration needs updating.
- **Real-World Application:**  
  In production, you would fetch live configuration data and execute commands on actual devices. Here, we simulate this integration.
- **Requirements:**  
  The Netmiko part requires access to a real network device. In this demo, placeholder values are used. Replace them with actual device details to run the script against a live device.

## Objectives
- Combine API interfacing with network automation.
- Pass data from an API to a network automation function.
- Structure an integrated Python script for a coordinated workflow.

## Instructions
1. Read the explanation above.
2. Run the `netops_integration.py` script to observe an integrated process.
3. Practice by modifying the script:
   - Change the API endpoint or extract different data.
   - Adjust the network command based on the API data.
