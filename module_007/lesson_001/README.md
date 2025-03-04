# Lesson 1: Advanced Project Kick-Off

## Overview
In this lesson, you will kick off your advanced automation project. The goal is to integrate multiple components you have learned:
- **API Integration:** Fetch live data from a public API.
- **CI/CD Simulation:** Execute real system commands (using subprocess) to simulate build, test, and deployment stages.
- **Network Automation:** Use Netmiko to connect to a network device and execute a command.

### Detailed Explanation
- **API Integration:**  
  We use the `requests` library to fetch data from a public API (e.g., jsonplaceholder). This simulates retrieving configuration or status data dynamically.
  
- **CI/CD Simulation:**  
  Instead of just printing messages, we execute actual commands (like `git status` or `echo`) via the `subprocess` module. This shows you how to integrate system commands into your automation workflow.
  
- **Network Automation:**  
  We use Netmiko to attempt an SSH connection to a network device. (The provided device details are placeholders; replace them with real values if you have access.)

## Objectives
- Combine API data, CI/CD pipeline stages, and network automation in a single script.
- Understand how to structure an integrated automation project.
- Learn best practices for error handling and secure credential management (for real scenarios).

## Instructions
1. Read through the explanation above.
2. Run the `advanced_project_setup.py` demonstration script.
3. Experiment with modifying the script to add new commands or alter the integration logic.
