# ci_cd_pipeline.py
"""
This script simulates a CI/CD pipeline by executing real system commands.

Stages simulated:
1. Pulling the latest code from a repository (simulated using 'git status').
2. Running automated tests (simulated using 'echo' for test execution).
3. Deploying code (simulated using 'echo' to represent deployment).

Note: Ensure you have Git installed to run the 'git status' command.
"""

import subprocess

def pull_latest_code():
    print("Pulling the latest code...")
    # Run 'git status' to simulate checking the repository status.
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    print(result.stdout.strip())

def run_tests():
    print("Running automated tests...")
    # Simulate running tests using 'echo'.
    result = subprocess.run(["echo", "All tests passed."], capture_output=True, text=True)
    print(result.stdout.strip())

def deploy_code():
    print("Deploying code to production...")
    # Simulate deployment using 'echo'.
    result = subprocess.run(["echo", "Deployment successful."], capture_output=True, text=True)
    print(result.stdout.strip())

def main():
    print("=== CI/CD Pipeline Simulation ===")
    pull_latest_code()
    run_tests()
    deploy_code()
    print("CI/CD pipeline process complete.")

if __name__ == "__main__":
    main()
