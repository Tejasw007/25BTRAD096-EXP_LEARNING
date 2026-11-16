# ==============================================================================
# Name: Tejasw.s
# USN: 25BTRAD096
# Lab Exercise 1: Installing Python, Setting up VS Code / PyCharm, Jupyter Notebook
# Lab Exercise 2: Write and execute a basic Python program
# Lab Exercise 3: Programs using variables, operators, and input/output
# Lab Exercise 4: Simple calculator and area calculation programs
# ==============================================================================

# ------------------------------------------------------------------------------
# Lab Exercise 2: Write and execute a basic Python program
# ------------------------------------------------------------------------------
"""Print a basic introduction message."""

print("Hello, World!")
print("This is my first Python program.")
print("This program demonstrates basic python program.")


# ------------------------------------------------------------------------------
# Lab Exercise 3: Programs using variables, operators, and input/output
# ------------------------------------------------------------------------------
def main():
    """Demonstrate variables, operators, and input/output."""
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in centimeters: "))

    print(f"Hello my name is {name}")
    print(f"I am {age} years old.")
    print(f"My height is {height} centimeters.")


# ------------------------------------------------------------------------------
# Lab Exercise 4: Simple calculator and area calculation programs
# ------------------------------------------------------------------------------
def simple_calculator():
    """Perform basic arithmetic based on user input."""
    print("\nSimple Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Choose an operator (+, -, *, /): ").strip()

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return

    print(f"Result: {num1} {operator} {num2} = {result}")


def area_calculator():
    """Calculate the area of common shapes."""
    print("\nArea Calculator")
    shape = input("Choose a shape (rectangle/circle/triangle): ").strip().lower()

    if shape == "rectangle":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print(f"Area of rectangle = {area}")
    elif shape == "circle":
        radius = float(input("Enter radius: "))
        area = 3.14 * radius * radius
        print(f"Area of circle = {area}")
    elif shape == "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print(f"Area of triangle = {area}")
    else:
        print("Invalid shape selection.")


if __name__ == "__main__":
    print("--- Executing Lab Exercise 3 ---")
    main()

    print("\n--- Executing Lab Exercise 4 ---")
    try:
        while True:
            print("\n--- What would you like to do? ---")
            print("1. Simple Calculator")
            print("2. Area Finder")
            print("3. Exit")
            choice = input("Pick an option (1-3): ").strip()
            if choice == "1":
                simple_calculator()
            elif choice == "2":
                area_calculator()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
    except EOFError:
        print("No input available. Exiting.")
