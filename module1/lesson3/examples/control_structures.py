# control_structures.py
# Demonstrates the use of conditionals and loops in Python.

# Conditional statement example:
number=int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# For loop example: printing numbers 1 to 5
for i in range(1, 6):
    print("For loop iteration:", i)

# While loop example: countdown from 5
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1
