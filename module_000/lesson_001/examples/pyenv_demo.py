#!/usr/bin/env python3
"""
Demonstration script for pyenv functionality
This script shows how to programmatically check Python versions
and demonstrates the isolation that pyenv provides.
"""

import os
import sys
import subprocess
import platform

def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 50)
    print(f" {text}")
    print("=" * 50)

def run_command(command):
    """Run a shell command and return the output."""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

def main():
    """Main function to demonstrate pyenv functionality."""
    print_header("Python Environment Information")
    
    # System information
    print(f"Platform: {platform.platform()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Python Implementation: {platform.python_implementation()}")
    print(f"Python Path: {sys.executable}")
    
    # Check if pyenv is installed
    print_header("Pyenv Status")
    pyenv_path = run_command("which pyenv" if platform.system() != "Windows" else "where pyenv")
    
    if "Error" in pyenv_path:
        print("Pyenv is not installed or not in PATH.")
        print("Visit https://github.com/pyenv/pyenv#installation for installation instructions.")
    else:
        print(f"Pyenv is installed at: {pyenv_path}")
        
        # Show installed Python versions
        print_header("Installed Python Versions")
        versions = run_command("pyenv versions")
        print(versions)
        
        # Show current Python version
        print_header("Current Python Version")
        current = run_command("pyenv version")
        print(current)
        
        # Show python-version file if it exists
        print_header("Project Python Version")
        if os.path.exists(".python-version"):
            with open(".python-version", "r") as f:
                version = f.read().strip()
                print(f"This project uses Python {version} (defined in .python-version)")
        else:
            print("No project-specific Python version found.")
            print("You can set one with: pyenv local [version]")
    
    # Show virtual environment status
    print_header("Virtual Environment Status")
    if "VIRTUAL_ENV" in os.environ:
        venv_path = os.environ["VIRTUAL_ENV"]
        print(f"Active virtual environment: {venv_path}")
        
        # List installed packages
        print_header("Installed Packages")
        packages = run_command(f"{venv_path}/bin/pip list" if platform.system() != "Windows" 
                              else f"{venv_path}\\Scripts\\pip list")
        print(packages)
    else:
        print("No active virtual environment.")
        print("Create one with: python -m venv [name]")
        print("Activate with: source [name]/bin/activate (Unix) or [name]\\Scripts\\activate (Windows)")

if __name__ == "__main__":
    main()