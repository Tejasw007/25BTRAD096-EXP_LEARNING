# ==============================================================================
# Name: Tejasw.s
# USN: 25BTRAD096
# Task 01: Python Basics, Data Types, and Input/Output Tasks
# ==============================================================================

# Program 1: Basic print statements
print("Tejasw.s")
print("Computer Science Engineering with specialisation in Artificial Intelligence and Data Engineering")
print("Jain Deemned-to-be-univeristy Faculty of Engineering and Technology")

# Program 2: Pattern printing
print('*******')
print('*******')
print('*******')

# Program 3: Simple string output
print("Python is Easy")

# Program 4: Number pattern
print('1')
print('12')
print('123')
print('1234')
print('12345')

# Program 5: Escape sequence - Newline
print("Computer\nScience\nEngineering")

# Program 6: Escape sequence - Tab
print("Tejasw.s\t19\tBengaluru")

# Program 7: Single-line comment
# This program prints a welcome message
print("Welcome")

# Program 8: Multi-line comment
"""
This program
prints a message
using multiple lines of comment
"""
print("Hello")

# Program 9: Multiple comments with prints
# Comment 1: print name
print("Tejasw.s")
# Comment 2: print age
print(19)
# Comment 3: print city
print("Bengaluru")

# Program 10: Variable assignment and print
name = "Tejasw.s"
print(name)

# Program 11: Multiple variables
a = 10
b = 20
c = 30
print(a)
print(b)
print(c)

# Program 12: Type conversion to integer
num = int("100")
print(num)
print(type(num))

# Program 13: Type conversion to float
num = float("25.6")
print(num)
print(type(num))

# Program 14: Input age
age = int(input("Enter your age: "))
print(age)

# Program 15: Sum of two numbers
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(f"The sum of {n1} and {n2} is: {n1 + n2}")

# Program 16: Formatted student details
sname = input("Enter name: ")
sage = int(input("Enter age: "))
cgpa = float(input("Enter CGPA: "))
print(f"My name is {sname}. I am {sage} years old and my CGPA is {cgpa}.")

# Program 17: Celsius to Fahrenheit conversion
c = float(input("Enter temperature in Celsius: "))
f = (c * 9 / 5) + 32
print(f"Temperature in Fahrenheit: {f:.2f}")

# Program 18: Even or odd check
number = int(input("Enter number: "))
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
