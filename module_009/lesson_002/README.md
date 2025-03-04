# Lesson 2: Monitoring & Troubleshooting

## Overview
After deploying your project, monitoring its performance and troubleshooting issues are essential for ensuring stability. In this lesson, you will learn:
- How to monitor your system and application status using real commands.
- Techniques for troubleshooting common issues by checking logs and system processes.
- How to simulate these tasks using file I/O and subprocess commands.

### Detailed Explanation
- **Monitoring:**  
  You can monitor a system by listing running processes, checking resource usage, or viewing log files. This script simulates monitoring by running commands like `ps aux` (on Unix) or `tasklist` (on Windows) and by tailing a log file.
- **Troubleshooting:**  
  Troubleshooting involves identifying problems and verifying that services are running as expected. The script demonstrates this by reading a sample log file and using system commands to display current process status.
- **Practical Application:**  
  In a real environment, you might set up automated alerts, use log analysis tools, or monitor system metrics. Here, we simulate these steps to give you a practical understanding.

## Objectives
- Learn to run system commands to check process status and view logs.
- Build a simple monitoring tool that reads and displays log file content.
- Understand basic troubleshooting techniques.

## Instructions
1. Read the explanation above.
2. Run the `monitoring.py` script to observe the monitoring and troubleshooting simulation.
3. Experiment by modifying the script (e.g., change the log file path, add new commands, or adjust the output format).