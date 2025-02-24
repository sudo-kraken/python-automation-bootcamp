# Lesson 2: Building a CI/CD Pipeline for Automation

## Overview
A CI/CD pipeline automates code integration, testing, and deployment. In this lesson, you will see how to simulate a CI/CD pipeline by executing real commands from your system.

### Detailed Explanation
- **CI/CD Pipeline Stages:**  
  Common stages include pulling the latest code, running automated tests, and deploying the application.
- **Real Command Execution:**  
  This demonstration uses actual system commands (via subprocess.run) to simulate these stages.
  
For example:
- Pulling code might be simulated by running `git status` (if you have a repository).
- Testing might be simulated with a command that checks the environment.
- Deployment might use an `echo` command.

## Objectives
- Understand the stages of a CI/CD pipeline.
- See real commands executed to simulate each stage.
- Learn to modify and extend the simulation with additional stages.

## Instructions
1. Read the explanation above.
2. Run the `ci_cd_pipeline.py` script to observe the simulated CI/CD process.
3. Practice by modifying the script to add new stages or change the commands.
