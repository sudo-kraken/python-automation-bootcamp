# Lesson 1: Python Environments and Virtualisation

## Overview
When working on Python projects, it’s crucial to isolate your project's dependencies. This lesson explains:

- **venv:**  
  A built-in module for creating isolated Python environments.

- **virtualenv:**  
  An alternative tool for creating virtual environments (works similarly to venv).

- **pyenv:**  
  A tool to manage and switch between multiple Python versions.

### Why Is This Important?
- **Isolation:** Keeps project libraries separate to avoid conflicts.
- **Reproducibility:** Makes it easier to recreate your environment on different machines.
- **Flexibility:** Allows you to test your code with different Python versions.

## Objectives
- Learn how to create and activate a virtual environment using `venv`.
- Understand the basics of managing Python versions with `pyenv`.

## Instructions
1. Read through this explanation.
2. Run the provided example script (`virtualenv_setup.py`) to see how a virtual environment is created.
3. As a practice exercise, try creating and activating your own virtual environment using the steps below.

## Python Version Management with pyenv

### What is pyenv?
Pyenv is a powerful tool that allows developers to install and manage multiple Python versions on a single machine. This is particularly useful when:
- Different projects require different Python versions
- You need to test compatibility across multiple Python versions
- You want to try new Python features without affecting your system Python

### Key Features of pyenv
- **Multiple versions**: Install and manage multiple Python versions side-by-side
- **Project-specific versions**: Set Python versions per project directory
- **Virtual environments**: Integrate with virtualenv for isolated package management
- **No sudo required**: Install Python versions in your user space without admin rights
- **Shell integration**: Seamlessly switch between versions in your terminal

### How pyenv Works
Unlike other methods, pyenv works by inserting itself into your PATH and intercepting Python commands. When you run `python`, pyenv determines which Python version to use based on:
1. The `PYENV_VERSION` environment variable (if set)
2. The project-specific `.python-version` file (if present)
3. The global version set with `pyenv global`

This approach allows for flexible, context-aware Python version management without modifying the actual Python binaries.

### Potential Compatibility Issues with pyenv

While pyenv is a powerful tool for managing Python versions, it can occasionally cause compatibility issues with certain applications or tools that have strict requirements for how Python is installed or configured:

#### Common Issues and Solutions

1. **System Tools Dependency**:
   - Some system tools and applications are specifically designed to work with the system Python installation
   - If you encounter issues with system tools after setting up pyenv, temporarily switch back to the system Python with: `pyenv shell system`

2. **Oracle Tools Compatibility**:
   - Oracle tools in particular can be sensitive to Python environment changes
   - These tools often look for Python in specific system paths and may not work correctly when pyenv intercepts the Python command
   - If using Oracle tools, either:
     - Temporarily disable pyenv with `pyenv shell system` when working with these tools
     - Configure the Oracle tools to explicitly use the system Python path
     - Create a separate user account for Oracle work that doesn't have pyenv configured

3. **Path and Environment Variables**:
   - Pyenv modifies your PATH to insert its shims directory
   - This can occasionally conflict with other tools that have their own expectations about PATH ordering
   - If you notice unusual behavior in tools after installing pyenv, check their PATH requirements

4. **Performance Considerations**:
   - Python versions installed through pyenv might be compiled with different optimisations than system packages
   - This is rarely an issue, but in performance-critical applications, you might notice differences

5. **IDE Integration**:
   - Make sure to configure your IDE to recognise the pyenv Python version
   - Some IDEs may need manual configuration to work correctly with pyenv-managed Python installations

When troubleshooting compatibility issues, remember that you can always temporarily disable pyenv with `pyenv shell system` to determine if pyenv is the cause of the problem.
