#!/usr/bin/env python3
"""
Interactive Pyenv Demonstration Script
--------------------------------------
This script demonstrates pyenv functionality with educational explanations
at each step. It shows how pyenv manages Python versions and integrates with
virtual environments.

How to use:
- Follow along with the script prompts and explanations
- Each section describes what's happening and why it matters
- Key pyenv concepts are highlighted and explained
"""

import os
import sys
import time
import subprocess
import platform
from pathlib import Path

# ANSI color codes for better readability
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
END = "\033[0m"

def clear_screen():
    """Clear terminal screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    """Print a formatted section header."""
    print(f"\n{BOLD}{BLUE}{'=' * 80}{END}")
    print(f"{BOLD}{BLUE}  {text}{END}")
    print(f"{BOLD}{BLUE}{'=' * 80}{END}")

def print_step(step_number, text):
    """Print a formatted step with description."""
    print(f"\n{BOLD}{GREEN}Step {step_number}: {text}{END}")

def print_note(text):
    """Print a highlighted note."""
    print(f"{YELLOW}NOTE: {text}{END}")

def print_warning(text):
    """Print a warning message."""
    print(f"{RED}WARNING: {text}{END}")

def print_command(cmd):
    """Display a command that will be executed."""
    print(f"{BOLD}$ {cmd}{END}")

def run_command(command, show_output=True):
    """Run a shell command and return the output with educational context."""
    try:
        print_command(command)
        
        # Short delay to make it feel interactive
        time.sleep(0.5)
        
        result = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        
        if show_output and result.stdout:
            print(result.stdout)
        
        return result.stdout
    except subprocess.CalledProcessError as e:
        if e.stderr:
            print(f"{RED}Error: {e.stderr}{END}")
        return f"Error: {e.stderr}"

def wait_for_user():
    """Pause execution until user presses Enter."""
    input(f"\n{BOLD}Press Enter to continue...{END}")

def is_pyenv_installed():
    """Check if pyenv is installed and available in PATH."""
    try:
        subprocess.run(
            "pyenv --version", 
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        return True
    except:
        return False

def main():
    """Main interactive demonstration function."""
    clear_screen()
    
    print_header("Interactive Pyenv Demonstration")
    print("""
This interactive script will guide you through using pyenv, explaining each
step along the way. You'll learn how pyenv works, how to manage Python versions,
and how it integrates with virtual environments.
    """)
    
    # SECTION 1: Understanding your current Python environment
    print_step(1, "Understanding your current Python environment")
    print("""
Before we start with pyenv, let's understand your current Python setup. This will
help you appreciate how pyenv creates isolated environments with different versions.
    """)
    
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Current Python: {platform.python_version()} ({platform.python_implementation()})")
    print(f"Python location: {sys.executable}")
    
    print_note("Without pyenv, you're limited to a single system-wide Python installation")
    
    wait_for_user()
    
    # SECTION 2: Check if pyenv is installed
    print_step(2, "Checking if pyenv is installed")
    print("""
Now, let's check if pyenv is already installed on your system. Pyenv should be
in your PATH so you can run it from anywhere.
    """)
    
    if is_pyenv_installed():
        pyenv_version = run_command("pyenv --version")
        print_note("Pyenv is already installed and ready to use!")
    else:
        print_warning("Pyenv doesn't appear to be installed or is not in your PATH")
        print("""
To install pyenv:

- On Windows:
  pip install pyenv-win
  
- On macOS/Linux:
  curl https://pyenv.run | bash
  
After installation, you'll need to set up your shell configuration as described
in the module documentation.
        """)
    
    wait_for_user()
    
    # SECTION 3: How pyenv works
    print_step(3, "Understanding how pyenv works")
    print("""
Here's what makes pyenv special:

1. Pyenv works by inserting shims into your PATH. When you type 'python', 
   the pyenv shim intercepts this command.

2. The shim checks various files to determine which Python version to use:
   - First, it checks the PYENV_VERSION environment variable
   - Then, it looks for a .python-version file in your current directory
   - Next, it searches parent directories for .python-version files
   - Finally, it uses the global pyenv version

3. This approach is what allows you to have different Python versions 
   for different projects without conflicts.
    """)
    
    print_note("Pyenv doesn't modify your system Python! It's completely non-invasive")
    
    wait_for_user()
    
    # SECTION 4: Show installed Python versions
    if is_pyenv_installed():
        print_step(4, "Viewing installed Python versions")
        print("""
Pyenv maintains multiple Python versions in its installation directory.
Let's see what versions are currently installed:
        """)
        
        run_command("pyenv versions")
        
        print_note("The * indicates the currently active Python version")
        print_note("The 'system' version refers to your default system Python")
        
        wait_for_user()
        
        # SECTION 5: Installing a new Python version
        print_step(5, "Installing a new Python version")
        print("""
One of pyenv's key features is installing multiple Python versions.
Here's how to see available versions and install a new one:
        """)
        
        print("""
To see available versions: pyenv install --list
To install a specific version: pyenv install 3.9.6

Note: The installation process can take several minutes as it compiles Python
from source. For this demo, we won't actually install a new version.
        """)
        
        print_note("Pyenv installs each Python version in an isolated directory")
        print_note("This allows multiple versions to coexist without conflicts")
        
        wait_for_user()
        
        # SECTION 6: Switching Python versions
        print_step(6, "Switching between Python versions")
        print("""
Once you have multiple Python versions installed, switching between them
is simple. There are three main methods:
        """)
        
        print("""
1. Global switching (affects your entire system):
   pyenv global 3.9.6

2. Local switching (directory-specific):
   pyenv local 3.8.12
   This creates a .python-version file in the current directory

3. Shell switching (temporary, only for current shell session):
   pyenv shell 3.10.0
        """)
        
        print_note("The local setting (project-specific) takes priority over global settings")
        print_warning("Switching Python versions affects which packages are available to you")
        
        wait_for_user()
    
    # SECTION 7: Pyenv with virtualenv
    print_step(7, "Combining pyenv with virtual environments")
    print("""
For complete isolation, combine pyenv (for Python versions) with
virtual environments (for packages):

1. Select your Python version with pyenv:
   pyenv local 3.9.6

2. Create a virtual environment with that Python version:
   python -m venv .venv

3. Activate the virtual environment:
   source .venv/bin/activate (Linux/macOS)
   .venv\\Scripts\\activate (Windows)

This approach gives you:
- Control over your Python version (pyenv)
- Isolated packages for your project (virtualenv)
    """)
    
    print_warning("Always create new virtual environments after switching Python versions")
    
    wait_for_user()
    
    # SECTION 8: Compatibility considerations
    print_step(8, "Compatibility considerations")
    print("""
Using pyenv can occasionally lead to compatibility issues with certain tools
that expect Python to be in a specific location or use system libraries.

Common issues and solutions:

1. Some system tools might expect the system Python:
   - If a tool stops working, try: pyenv shell system
   - This temporarily switches back to system Python

2. Oracle tools in particular may have issues with pyenv:
   - Some Oracle tools look for Python in specific system paths
   - They may also depend on system-wide packages

3. IDE integration issues:
   - Make sure your IDE knows about the pyenv Python version
   - You may need to explicitly configure your IDE with the path
     to the pyenv Python executable
    """)
    
    print_warning("If critical tools stop working, temporarily disable pyenv with: pyenv shell system")
    
    wait_for_user()
    
    # SECTION 9: Best practices
    print_step(9, "Best practices for using pyenv")
    print("""
To get the most out of pyenv while avoiding common pitfalls:

1. Use .python-version files in your projects and commit them to version control
   so everyone on your team uses the same Python version

2. Create a new virtual environment after switching Python versions to
   ensure package compatibility

3. Consider using pyenv-virtualenv plugin to automate virtual environment
   creation and activation

4. Keep your pyenv installation updated with: pyenv update

5. Document your Python version requirements in your project README
    """)
    
    wait_for_user()
    
    # Conclusion
    print_header("Conclusion")
    print("""
You've now learned how pyenv works and how to use it effectively!

Remember these key points:
1. Pyenv manages multiple Python versions without affecting system Python
2. Different projects can use different Python versions
3. Combine pyenv with virtual environments for complete isolation
4. Be aware of potential compatibility issues with certain tools

For more information, refer to the documentation provided in this module.
    """)

if __name__ == "__main__":
    main()