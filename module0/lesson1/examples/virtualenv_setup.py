# virtualenv_setup.py
"""
This script demonstrates basic commands for creating and activating a Python virtual environment using venv.
Note: In practice, you'll execute these commands in your terminal.

Steps demonstrated here:
1. Check the current Python version.
2. Create a virtual environment called 'env'.

Run this script to see the simulated process.
"""

import sys
import subprocess

def check_python_version():
    print("Current Python version:")
    print(sys.version)

def create_virtualenv(env_name="env"):
    print(f"Creating virtual environment: {env_name}")
    subprocess.run([sys.executable, "-m", "venv", env_name])
    print(f"Virtual environment '{env_name}' created.")

def main():
    check_python_version()
    create_virtualenv()

if __name__ == "__main__":
    main()
