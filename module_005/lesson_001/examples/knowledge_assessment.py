# knowledge_assessment.py
"""
This script implements an interactive, multiple-choice quiz with 10 questions.
It tests your knowledge on Python basics, API interfacing, and network automation.
For each question, choose the correct option (A, B, C, or D). The quiz will give immediate feedback
and display your total score at the end.
"""

def ask_question(question_data):
    # Display the question and options
    print(question_data["question"])
    for option, text in question_data["options"].items():
        print(f"  {option}. {text}")
    
    # Get user's answer and normalize it to uppercase
    answer = input("Your answer (A, B, C, or D): ").strip().upper()
    if answer == question_data["answer"]:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect. The correct answer is {question_data['answer']}.\n")
        return False

def main():
    print("=== Knowledge Assessment Quiz ===\n")
    questions = [
        {
            "question": "1. What is the typical output of: print('Hello, World!')?",
            "options": {
                "A": "Hello, World!",
                "B": "'Hello, World!'",
                "C": "hello, world!",
                "D": "None"
            },
            "answer": "A"
        },
        {
            "question": "2. Which Python library is most commonly used to make HTTP requests?",
            "options": {
                "A": "flask",
                "B": "requests",
                "C": "django",
                "D": "numpy"
            },
            "answer": "B"
        },
        {
            "question": "3. Which Python library is used for automating network device interactions?",
            "options": {
                "A": "pandas",
                "B": "matplotlib",
                "C": "netmiko",
                "D": "scipy"
            },
            "answer": "C"
        },
        {
            "question": "4. What does the statement 'if __name__ == \"__main__\":' do in a Python script?",
            "options": {
                "A": "It checks if the script is being run directly.",
                "B": "It checks if the script is being imported as a module.",
                "C": "It initializes the main function.",
                "D": "It starts a new thread."
            },
            "answer": "A"
        },
        {
            "question": "5. Which data type is used for textual data in Python?",
            "options": {
                "A": "int",
                "B": "str",
                "C": "bool",
                "D": "float"
            },
            "answer": "B"
        },
        {
            "question": "6. Which operator is used for string concatenation in Python?",
            "options": {
                "A": "+",
                "B": "-",
                "C": "*",
                "D": "/"
            },
            "answer": "A"
        },
        {
            "question": "7. Which of these is NOT a built-in Python data type?",
            "options": {
                "A": "list",
                "B": "tuple",
                "C": "array",
                "D": "dictionary"
            },
            "answer": "C"
        },
        {
            "question": "8. What does the requests.get() method do?",
            "options": {
                "A": "Sends a GET request to a specified URL.",
                "B": "Sends a POST request to a specified URL.",
                "C": "Downloads a file from a URL.",
                "D": "Opens a web browser."
            },
            "answer": "A"
        },
        {
            "question": "9. In network automation using Netmiko, which method is used to send a command to a device?",
            "options": {
                "A": "send_command",
                "B": "execute_command",
                "C": "run_command",
                "D": "dispatch_command"
            },
            "answer": "A"
        },
        {
            "question": "10. Which Python statement is used for handling exceptions?",
            "options": {
                "A": "if/else",
                "B": "try/except",
                "C": "for/while",
                "D": "switch/case"
            },
            "answer": "B"
        }
    ]
    
    score = 0
    for question in questions:
        if ask_question(question):
            score += 1
    
    print(f"Quiz complete! You answered {score} out of {len(questions)} questions correctly.")

if __name__ == "__main__":
    main()
