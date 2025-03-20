# Practice Exercise: Virtual Environment Setup

## Objective
Practice creating a Python virtual environment using `venv` and explore `pyenv` for managing multiple Python versions.

## Tasks
1. **Create a Virtual Environment:**
   - Open your terminal and navigate to your project directory.
   - Run the command:  
     `python -m venv myenv`
   - This will create a folder named `myenv` containing an isolated Python environment.

2. **Activate Your Virtual Environment:**
   - On Windows:  
     `myenv\Scripts\activate`
   - On macOS/Linux:  
     `source myenv/bin/activate`

3. **Explore pyenv (Required):**

   a. **Installing pyenv**:
      - On Windows:
        ```
        pip install pyenv-win
        ```
        Set up environment variables:
        ```
        [System.Environment]::SetEnvironmentVariable('PYENV', "$env:USERPROFILE\.pyenv\pyenv-win", 'User')
        [System.Environment]::SetEnvironmentVariable('PYENV_HOME', "$env:USERPROFILE\.pyenv\pyenv-win", 'User')
        [System.Environment]::SetEnvironmentVariable('PATH', "$env:USERPROFILE\.pyenv\pyenv-win\bin;$env:USERPROFILE\.pyenv\pyenv-win\shims;$env:PATH", 'User')
        ```

      - On macOS:
        ```
        export PYENV_ROOT="$HOME/.pyenv"
        [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
        eval "$(pyenv init -)"

        fi

        # Check if pyenv is installed
        if command -v pyenv &> /dev/null; then
          echo -e "${GREEN}pyenv is already installed.${NC}"
        else
          echo -e "${YELLOW}pyenv is not installed. Installing pyenv...${NC}"
          curl https://pyenv.run | bash
        fi

        # As we just installed pyenv, we need to reconfigure our paths and initialise pyenv
        export PYENV_ROOT="$HOME/.pyenv"
        [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
        eval "$(pyenv init -)"

        # Reload shell configuration
        if ! command -v pyenv &> /dev/null; then
          echo -e "${RED}pyenv installation failed. Exiting.${NC}"
          exit 1
        ```

        Add to your shell configuration file (~/.bash_profile, ~/.zshrc, etc.):
        ```
        export PYENV_ROOT="$HOME/.pyenv"
        [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
        eval "$(pyenv init -)"
        ```

      - On Linux:
        ```
        curl https://pyenv.run | bash
        ```
        Add to your shell configuration:
        ```
        echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
        echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
        echo 'eval "$(pyenv init -)"' >> ~/.bashrc
        ```

   b. **Using pyenv**:
      - **List available Python versions**:
        ```
        pyenv install --list
        ```

      - **Install a specific Python version**:
        ```
        pyenv install 3.9.6
        ```

      - **Set a global Python version**:
        ```
        pyenv global 3.9.6
        ```

      - **Set a local (project-specific) Python version**:
        ```
        cd your_project
        pyenv local 3.8.12
        ```

      - **Check your current Python version**:
        ```
        python --version
        pyenv version
        ```

      - **List all installed Python versions**:
        ```
        pyenv versions
        ```

   c. **Managing Multiple Projects with Different Python Versions**:
      - Create two separate directories for testing
      - In directory 1:
        ```
        mkdir project1
        cd project1
        pyenv local 3.9.6
        python -m venv .venv
        # Activate the virtual environment
        # On Windows: .venv\Scripts\activate
        # On Unix: source .venv/bin/activate
        ```
      - In directory 2:
        ```
        mkdir project2
        cd project2
        pyenv local 3.8.12
        python -m venv .venv
        # Activate the virtual environment
        ```

   d. **Understanding pyenv and virtualenv together**:
      - pyenv manages Python versions
      - virtualenv manages packages and dependencies
      - Combined, they provide complete isolation for your Python projects
      - Important: After switching Python versions with pyenv, create a new virtual environment

4. **Practice and Exploration**:
   - Install at least two different Python versions with pyenv
   - Create projects that use different Python versions
   - Create a virtual environment in each project
   - Install a package in one environment and verify it's not available in the other
   - Document your observations about how pyenv helps manage Python versions

5. **Safeguards and Best Practices**:
   - Always activate your virtual environment before installing packages
   - When using tools that depend on system Python, temporarily disable pyenv with `pyenv shell system`
   - Use `pyenv doctor` to check for common issues
   - Add `.python-version` files to version control to ensure team members use the same Python version
   - Be careful when updating system-wide packages in a pyenv-managed Python installation
