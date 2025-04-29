# Practice Exercise: OS Commands and File Automation

## Objective
Complete the following tasks to practise automating system commands and basic file operations using Python.

## Tasks
1. **Host Pinger with File Input:**

    - Create a Python script that reads a list of hostnames or IP addresses from a text file.
    - Ping each host three times.
    - Log the results (hostname and whether it is reachable or not) to a new output file called ping_results.txt.
    - Include a timestamp next to each result.

2. **Directory File Lister:**

   - Write a Python script that asks the user for a directory path.
   - List all files in the directory, displaying the filename and size in bytes.
   - Sort the list by file size, smallest to largest.

3. **Simple Backup Script:**

    - Create a script that prompts the user for a source directory and a destination directory.
    - Copy all files from the source to the destination, keeping the original filenames.
    - Use only built-in libraries such as shutil, os, or pathlib.
    - (Bonus) Only copy files modified within the last 24 hours.

Save your scripts in the examples/ folder for this lesson.

This exercise will help you become comfortable with interactive input, file I/O, and system command integration in Python.
