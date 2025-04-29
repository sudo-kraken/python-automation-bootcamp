# Lesson 2: Text Parsing and Regex

## Overview

Network engineers often need to sift through log files or configuration files to find specific information. In this lesson, you will learn:

   - How to read and process text files using Python (for example, reading a log file line by line).

   - What regular expressions (regex) are and how to use them to match patterns in text.

   - Techniques to filter out the information you need (such as errors, IP addresses, or specific configuration lines) from large amounts of text quickly and accurately.

### Detailed Explanation

- **Reading Files in Python:**

    Python makes it straightforward to read text files. Using a `with open('filename') as f:` block allows you to iterate through a file line by line. This is memory-efficient and ideal for large files like logs. You can also read the entire content at once with `f.read()`, but for parsing line by line (especially when looking for specific lines), iterating is more practical.

- **Regular Expressions (Regex):**

    Regular expressions are a powerful tool for pattern matching. The `re` module in Python lets you define patterns to search for in text. For example, the pattern `r"\d+\.\d+\.\d+\.\d+"` can find IPv4 addresses in a string, and `r"ERROR"` could find occurrences of the word "ERROR". Regex patterns can be very simple or very complex, depending on what you need to match. In Python, `re.search(pattern, string)` checks if the pattern appears anywhere in the string, and `re.findall(pattern, string)` returns all occurrences.

- **Practical Parsing Strategies:**

    When parsing logs, you might not need regex for simple keywords — you could just use an `if "ERROR" in line:` check. However, regex becomes essential for more flexible or complex matches (for example, finding all IP addresses, or lines that start with a timestamp). It's often useful to combine methods: first filter lines by a simple keyword, then apply regex to those lines for finer extraction. Always test your regex patterns on sample text to ensure they do what you expect.

## Objectives

- Open and read text files within a Python script, handling them safely and efficiently.

- Understand and construct basic regular expressions to match patterns (such as specific words, IP addresses, or other formats) in text data.

- Write a script that scans a file (like a log) for lines matching a user-specified pattern and outputs those lines, demonstrating a practical way to quickly find relevant information in large files.

## Instructions

1. Read through the overview and explanation. Make sure you have a basic understanding of how regex patterns are structured (for example, `\d` for digits, `\w` for word characters, `*` or `+` for repetition, etc.). If regex is new to you, start with simple literal patterns (like searching for the word "ERROR").

2. Run the `log_search.py` example script. When you execute it, it will ask you for the path to a log file and a search pattern (you can enter a simple word or a full regex). The script will then read the file line by line and print out any lines that match the pattern. Look at the code to see how it uses `re.search()` to check each line.

3. Practice Exercise: Create your own test log file (or use an existing one from your network device logs) and try searching for different patterns using `log_search.py`. Modify the script to enhance its functionality — for example, count the number of matches and display the count at the end, or write the matched lines to a new file instead of printing them. You could also experiment with more complex regex patterns; for instance, try to find all IP addresses in the file or extract all lines that start with a date (e.g., lines beginning with `[0-9]{4}-[0-9]{2}-[0-9]{2}` if the log has dates).