# ==============================================================================
# Name: TEJASW
# USN: 25BTRAD096
# Mini Project_03: Attendance tracker
# Develop a Python-based attendance tracker for a class using lists and dictionaries.
# ==============================================================================

students = {}

def add_student():
    name = input("Enter student name: ")
    if name not in students:
        students[name] = []
        print(name, "added successfully!")
    else:
        print("Student already exists!")

def mark_attendance():
    name = input("Enter student name: ")
    if name in students:
        status = input("Enter P for Present or A for Absent: ").upper()
        if status in ["P", "A"]:
            students[name].append(status)
            print("Attendance marked successfully!")
        else:
            print("Invalid attendance status!")
    else:
        print("Student not found!")

def display():
    if not students:
        print("No student records available!")
        return
    print("\n========== ATTENDANCE REPORT ==========")
    print(f"{'Name':<15}{'Present':<10}{'Absent':<10}{'Percentage':<12}")
    print("-" * 47)
    for name, records in students.items():
        total = len(records)
        present = records.count("P")
        absent = records.count("A")
        percent = present / total * 100 if total else 0
        print(f"{name:<15}{present:<10}{absent:<10}{percent:.2f}%")
    print("=" * 47)

def low_attendance():
    limit = float(input("Enter attendance threshold: "))
    print("\n===== LOW ATTENDANCE STUDENTS =====")
    found = False

    for name, records in students.items():
        total = len(records)
        present = records.count("P")
        percent = present / total * 100 if total else 0
        if total > 0 and percent < limit:
            print(name, "-", round(percent, 2), "%")
            found = True
    if not found:
        print("No students below the threshold!")

def main():
    while True:
        print("\n================================")
        print("   STUDENT ATTENDANCE TRACKER")
        print("================================")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Display Attendance")
        print("4. Check Low Attendance")
        print("5. Exit")
        print("================================")
        ch = input("Enter your choice: ")
        if ch == '1':
            add_student()
        elif ch == '2':
            mark_attendance()
        elif ch == '3':
            display()
        elif ch == '4':
            low_attendance()
        elif ch == '5':
            print("Exiting Attendance Tracker. Thank you!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
