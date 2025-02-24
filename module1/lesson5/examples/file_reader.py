# file_reader.py
# Demonstrates basic file reading operations in Python.
import os

def read_file(file_path):
    """
    Reads and prints the content of the specified file.
    Handles errors if the file is not found.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Get the absolute path of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the sample.txt file
    file_path = os.path.join(script_dir, 'sample.txt')
    read_file(file_path)

if __name__ == "__main__":
    main()
