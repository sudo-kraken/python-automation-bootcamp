# interactive_input.py
"""
This script demonstrates how to use the input() function to get user input and how to handle errors using try/except.
It prompts the user to enter their age and attempts to convert the input to an integer.
If the input is not a valid number, it catches the ValueError and informs the user.
"""

def get_user_age():
    try:
        age = int(input("Please enter your age: "))
        print(f"You entered: {age}")
    except ValueError:
        print("Invalid input. Please enter a valid number for your age.")

def main():
    print("=== Interactive Input and Exception Handling Demo ===")
    get_user_age()

if __name__ == "__main__":
    main()
