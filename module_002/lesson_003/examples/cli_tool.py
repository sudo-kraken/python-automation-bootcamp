# cli_tool.py
"""
This script demonstrates how to create a simple command-line utility using the argparse module.
It accepts a positional argument for the user's name and an optional argument for the number of times to greet.
"""

import argparse

def greet(name, times):
    """Prints a greeting message multiple times."""
    for _ in range(times):
        print(f"Hello, {name}!")

def main():
    parser = argparse.ArgumentParser(
        description="A simple command-line greeting tool."
    )
    parser.add_argument("name", help="Name of the person to greet")
    parser.add_argument("-t", "--times", type=int, default=1,
                        help="Number of times to display the greeting")
    
    args = parser.parse_args()
    greet(args.name, args.times)

if __name__ == "__main__":
    main()
