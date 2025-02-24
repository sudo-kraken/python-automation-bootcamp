# Lesson 2: Practical Exercises with AI Dev Tools

## Overview
In this lesson, you'll enhance the simulation of AI-assisted development by creating an interactive session that logs your interactions. You will:
- Allow multiple queries in one session.
- Log each query and AI response to a file.
- Modify the simulation to include additional features.

### Detailed Explanation
Instead of a one-off query, you'll build an interactive tool that:
- Continuously prompts you for input until you choose to exit.
- Fetches a dynamic response for each query from the Quotable API.
- Logs each interaction (query and response) to a file named `ai_log.txt` using real file I/O operations.
- This setup simulates how AI tools might assist you continuously during development.

## Objectives
- Build an interactive session for AI assistance.
- Learn to use file I/O to log interactions.
- Practice error handling and looping for continuous input.

## Instructions
1. Read the explanation above.
2. Run the `ai_exercise.py` script to start an interactive AI session.
3. Experiment by entering multiple queries and then reviewing the contents of `ai_log.txt`.
