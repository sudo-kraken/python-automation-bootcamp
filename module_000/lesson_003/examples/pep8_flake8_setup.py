import subprocess
import tempfile
import os

def create_temp_file_with_issues():
    # This sample code intentionally has style issues:
    # - Improper indentation (2 spaces instead of 4).
    # - Missing whitespace around operators.
    code_with_issues = """\
def foo():
  print("Hello, World!")  # Improper indentation and spacing
"""
    temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
    temp_file.write(code_with_issues)
    temp_file.close()
    return temp_file.name

def run_flake8_on_file(file_path):
    try:
        # Run flake8 on the temporary file.
        result = subprocess.run(['flake8', file_path], capture_output=True, text=True, check=False)
        return result.stdout.strip()
    except FileNotFoundError:
        return "flake8 is not installed. Please install it using: pip install flake8"

def main():
    temp_file_path = create_temp_file_with_issues()
    print("Temporary file created with intentional style issues:")
    print(temp_file_path)
    print("\nRunning flake8...\n")
    flake8_output = run_flake8_on_file(temp_file_path)
    if flake8_output:
        print("flake8 output:")
        print(flake8_output)
    else:
        print("No style issues found (unexpected).")
    # Clean up temporary file
    os.remove(temp_file_path)
    print("\nTemporary file removed.")

if __name__ == "__main__":
    main()