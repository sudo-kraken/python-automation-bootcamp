# Lesson 1: OS Commands and File Automation

## Overview

Automating operating system tasks is a key part of scripting. In this lesson, you will learn:

   - How to run OS commands (like shell or terminal commands) directly from a Python script.

   - How to perform basic file operations (such as reading from, writing to, and deleting files, or listing directory contents) using Python.

   - The benefits of using Python to automate repetitive shell tasks, for example checking network connectivity or cleaning up files, to save time and reduce errors.

### Detailed Explanation

- **Running System Commands with Python:**

    Python's `subprocess` module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. This is more powerful and flexible than older functions like `os.system`. For instance, you can use `subprocess.run(["ping", "-c", "1", "hostname"])` to send a single ping to "hostname" (on Windows, use `"-n", "1"` instead of `"-c", "1"`). The `subprocess` call can capture the output and give you a return code to indicate if the command was successful, which you can use to decide what to do next in your script.

- **Automating File Operations:**

    Python's built-in `os` (and newer `pathlib`) modules let you interact with the file system. You can create directories, list files (`os.listdir()`), rename files (`os.rename()`), or remove files (`os.remove()`) directly from Python. By combining these functions, a script can, for example, search for all files of a certain type and rename or move them automatically. This is much faster and less error-prone than doing it by hand, especially when dealing with many files.

- **Use Cases:**

    Combining external commands and file operations opens up many possibilities. You could write a script to ping a list of important hosts and then log the results to a file, or a script to regularly clean up temporary files on your system. Python scripts can also check the success of each operation (via return codes or exceptions) and take action (e.g., retry or alert the user) if something goes wrong, making your automation robust.

## Objectives

- Understand how to invoke external system commands from within a Python program and capture their output or result.

- Use Python to perform basic file management tasks (such as listing files in a directory and renaming or deleting files).

- Develop a simple script that combines these capabilities to automate a real-world task (for example, checking network connectivity or tidying up files automatically).

## Instructions

1. Read the explanation above to familiarise yourself with using `subprocess` for running commands and `os` for file operations.

2. Run the `ping_hosts.py` demonstration script (located in the examples folder for this lesson). This script will prompt you to enter one or more hostnames/IP addresses and then attempt to ping each one. Observe how the script uses `subprocess.run` to execute the ping command and how it interprets the result (reachable or not reachable) based on the return code.

3. Practice Exercise: Modify the `ping_hosts.py` script or write a new script to automate a different OS task. For example, you could change it to run a directory listing command or check disk space on your system. Alternatively, use Python's `os` module to perform a file cleanup: ask the user for a directory path and delete all files with a certain extension within that directory (be careful to test on a safe directory!). Try to incorporate error handling – for instance, if a file or directory is not found, catch the exception and print a friendly message.