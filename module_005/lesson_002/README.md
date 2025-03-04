# Lesson 2: Practical Challenge

## Overview
In this lesson, you will integrate the skills learned in previous modules to build a practical automation script. The script will:
- Prompt you to choose between two tasks: fetching API data or automating a network device.
- If you choose API integration, it will make a real HTTP request to a public API and display key data.
- If you choose network automation, it will attempt to connect to a network device using Netmiko and execute a command (using simulated or real device details).

### Detailed Explanation
- **Interactive Choice:**  
  The script uses the `input()` function to let you choose which task to perform.
- **API Integration:**  
  Uses the requests library to fetch data from a sample public API (jsonplaceholder). This simulates retrieving dynamic configuration or status information.
- **Network Automation:**  
  Uses Netmiko to connect to a network device and execute a command. If you don't have access to a real device, you can observe the error handling or simulate the output.

This integrated exercise demonstrates how you might combine various automation components into one cohesive script.

## Objectives
- Combine interactive input, API data retrieval, and network automation into a single script.
- Learn to structure an integrated automation project.
- Understand how to handle different tasks based on user input.

## Instructions
1. Read the explanation above.
2. Run the `practical_challenge.py` script to see the integrated process.
3. Experiment by modifying the API endpoint, changing the command logic, or simulating different network responses.
