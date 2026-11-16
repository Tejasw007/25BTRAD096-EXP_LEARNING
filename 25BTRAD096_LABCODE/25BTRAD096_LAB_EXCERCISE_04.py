# ==============================================================================
# Name: TEJASW
# USN: 25BTRAD096
# Lab Exercise 11: Log file reader program
# Lab Exercise 12: Student data manager using files
# Lab Exercise 13: CSV-based payroll management system
# ==============================================================================

import os
import csv

# ------------------------------------------------------------------------------
# Lab Exercise 11: Log file reader program
# ------------------------------------------------------------------------------
def read_log():
    try:
        # Create directory and sample log file if not present
        os.makedirs("25BTRAD096_LAB_EXPERIMENTS", exist_ok=True)
        log_path = "25BTRAD096_LAB_EXPERIMENTS/log.txt"
        if not os.path.exists(log_path):
            with open(log_path, "w") as f:
                f.write("INFO: System started\nINFO: Process running\nWARNING: High memory usage\nERROR: Service failed\n")

        f = open(log_path, "r")
        data = f.read()

        print("--- LOG SUMMARY ---")
        print("ERROR:", data.count("ERROR"))
        print("WARNING:", data.count("WARNING"))
        print("INFO:", data.count("INFO"))

        print("--- LOG FILE CONTENTS ---")
        print(data)

        f.close()
    except FileNotFoundError:
        print("File not found!")


# ------------------------------------------------------------------------------
# Lab Exercise 12: Student data manager using files
# ------------------------------------------------------------------------------
def add():
    os.makedirs("25BTRAD096_LAB_EXPERIMENTS", exist_ok=True)
    f = open("25BTRAD096_LAB_EXPERIMENTS/students.txt", "a")
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")
    f.write(roll + "," + name + "," + marks + "\n")
    f.close()
    print("Record added!")


def display():
    os.makedirs("25BTRAD096_LAB_EXPERIMENTS", exist_ok=True)
    try:
        f = open("25BTRAD096_LAB_EXPERIMENTS/students.txt", "r")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("No records found.")


def search():
    roll = input("Enter roll number: ")
    try:
        f = open("25BTRAD096_LAB_EXPERIMENTS/students.txt", "r")
        for line in f:
            if line.startswith(roll + ","):
                print(line)
                break
        else:
            print("Record not found!")
        f.close()
    except FileNotFoundError:
        print("No records found.")


def student_manager():
    while True:
        ch = input("\n1.Add 2.Display 3.Search 4.Exit: ")
        if ch == '1':
            add()
        elif ch == '2':
            display()
        elif ch == '3':
            search()
        elif ch == '4':
            break


# ------------------------------------------------------------------------------
# Lab Exercise 13: CSV-based payroll management system
# ------------------------------------------------------------------------------
def create_file():
    with open("employee.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Basic"])
        n = int(input("Enter number of employees: "))
        for i in range(n):
            name = input("Enter employee name: ")
            basic = float(input("Enter basic salary: "))
            writer.writerow([name, basic])
    print("\nEmployee file created successfully!")


def payroll():
    try:
        with open("employee.csv", "r") as f:
            reader = csv.DictReader(f)

            print("\n--- PAYROLL SUMMARY ---")
            for row in reader:
                name = row["Name"]
                basic = float(row["Basic"])

                hra = basic * 0.20
                da = basic * 0.10
                pf = basic * 0.12

                gross = basic + hra + da
                net = gross - pf

                print("\nEmployee:", name)
                print("Basic Salary:", basic)
                print("HRA:", hra)
                print("DA:", da)
                print("Gross Salary:", gross)
                print("Deduction (PF):", pf)
                print("Net Salary:", net)
    except FileNotFoundError:
        print("employee.csv not found!")


if __name__ == "__main__":
    print("--- Log File Reader (Lab Exercise 11) ---")
    read_log()

    print("\n--- Student Data Manager (Lab Exercise 12) ---")
    student_manager()

    print("\n--- CSV Payroll Management (Lab Exercise 13) ---")
    create_file()
    payroll()
