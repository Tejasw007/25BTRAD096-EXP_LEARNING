# ==============================================================================
# Name: TEJASW
# USN: 25BTRAD096
# Lab Exercise 8: Contact book using lists and dictionaries
# Lab Exercise 9: Student grading system
# Lab Exercise 10: Frequency counter using dictionaries
# ==============================================================================

# ------------------------------------------------------------------------------
# Lab Exercise 8: Contact book using lists and dictionaries
# ------------------------------------------------------------------------------
def contact_book():
    contacts = {}
    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            phone = input("Enter phone number: ")
            if phone in contacts:
                print("Contact already exists!")
            else:
                name = input("Enter name: ")
                email = input("Enter email: ")
                contacts[phone] = {
                    "name": name,
                    "email": email
                }
                print("Contact added successfully!")

        elif choice == 2:
            phone = input("Enter phone number to search: ")
            if phone in contacts:
                print("Name:", contacts[phone]["name"])
                print("Email:", contacts[phone]["email"])
            else:
                print("Contact not found!")

        elif choice == 3:
            phone = input("Enter phone number to update: ")
            if phone in contacts:
                contacts[phone]["name"] = input("Enter new name: ")
                contacts[phone]["email"] = input("Enter new email: ")
                print("Contact updated successfully!")
            else:
                print("Contact not found!")

        elif choice == 4:
            phone = input("Enter phone number to delete: ")
            if phone in contacts:
                del contacts[phone]
                print("Contact deleted successfully!")
            else:
                print("Contact not found!")

        elif choice == 5:
            if not contacts:
                print("Contact book is empty!")
            else:
                for phone, details in contacts.items():
                    print("Phone:", phone, details)

        elif choice == 6:
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid choice! Try again.")


# ------------------------------------------------------------------------------
# Lab Exercise 9: Student grading system
# ------------------------------------------------------------------------------
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 50:
        return "E"
    else:
        return "F"


def student_grading_system():
    students = {}
    num = int(input("Enter number of students: "))

    for _ in range(num):
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        if 0 <= marks <= 100:
            students[name] = marks
        else:
            print("Invalid marks!")

    grades = {
        name: calculate_grade(marks)
        for name, marks in students.items()
    }

    print("\n--- STUDENT RESULTS ---")
    for name, marks in students.items():
        print(f"Name: {name}")
        print(f"Marks: {marks}")
        print(f"Grade: {grades[name]}")
        print("-------------------")


# ------------------------------------------------------------------------------
# Lab Exercise 10: Frequency counter using dictionaries
# ------------------------------------------------------------------------------
def frequency_counter():
    frequency = {}
    n = int(input("Enter number of elements: "))

    for i in range(n):
        num = input("Enter element: ")
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    print("\n--- ELEMENT FREQUENCY ---")
    for key, value in frequency.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    print("--- Running Contact Book (Lab Exercise 8) ---")
    contact_book()

    print("\n--- Running Student Grading System (Lab Exercise 9) ---")
    student_grading_system()

    print("\n--- Running Frequency Counter (Lab Exercise 10) ---")
    frequency_counter()
