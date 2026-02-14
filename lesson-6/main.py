# ===============================
# Task 1
# Zero Check Decorator
# ===============================

# answer-1 decorator
def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper


# answer-2 function with decorator
@check
def div(a, b):
    return a / b


# test
print(div(6, 2))   # 3
print(div(6, 0))   # Denominator can't be zero



# ===============================
# Task 2
# Employee Records Manager
# ===============================

FILE_NAME = "employees.txt"


# answer-1 Add Employee
def add_employee():
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    position = input("Position: ")
    salary = input("Salary: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{emp_id},{name},{position},{salary}\n")

    print("Employee added successfully.\n")


# answer-2 View Employees
def view_employees():
    try:
        with open(FILE_NAME, "r") as f:
            data = f.readlines()
            if not data:
                print("No records found.\n")
            else:
                for line in data:
                    print(line.strip())
    except FileNotFoundError:
        print("File not found.\n")


# answer-3 Search Employee
def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False

    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                if line.startswith(emp_id + ","):
                    print("Record found:", line.strip())
                    found = True
                    break
        if not found:
            print("Employee not found.")
    except FileNotFoundError:
        print("File not found.")


# answer-4 Update Employee
def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated = False

    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()

        with open(FILE_NAME, "w") as f:
            for line in lines:
                if line.startswith(emp_id + ","):
                    print("Enter new details:")
                    name = input("Name: ")
                    position = input("Position: ")
                    salary = input("Salary: ")
                    f.write(f"{emp_id},{name},{position},{salary}\n")
                    updated = True
                else:
                    f.write(line)

        if updated:
            print("Employee updated successfully.")
        else:
            print("Employee not found.")
    except FileNotFoundError:
        print("File not found.")


# answer-5 Delete Employee
def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    deleted = False

    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()

        with open(FILE_NAME, "w") as f:
            for line in lines:
                if not line.startswith(emp_id + ","):
                    f.write(line)
                else:
                    deleted = True

        if deleted:
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")
    except FileNotFoundError:
        print("File not found.")


# answer-6 Menu
def employee_menu():
    while True:
        print("\n1. Add new employee record")
        print("2. View all employee records")
        print("3. Search by Employee ID")
        print("4. Update employee")
        print("5. Delete employee")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")



# ===============================
# Task 3
# Word Frequency Counter
# ===============================

import os
import string
from collections import Counter


FILE_INPUT = "sample.txt"
FILE_OUTPUT = "word_count_report.txt"


# answer-1 Ensure file exists
def ensure_sample_file():
    if not os.path.exists(FILE_INPUT):
        print("sample.txt not found. Please enter a paragraph:")
        text = input()
        with open(FILE_INPUT, "w") as f:
            f.write(text)


# answer-2 Word count logic
def word_frequency(top_n=5):
    ensure_sample_file()

    with open(FILE_INPUT, "r") as f:
        text = f.read()

    # remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)

    words = text.lower().split()
    total_words = len(words)

    counter = Counter(words)
    most_common = counter.most_common(top_n)

    print(f"\nTotal words: {total_words}")
    print(f"Top {top_n} most common words:")

    for word, count in most_common:
        print(f"{word} - {count} times")

    # save report
    with open(FILE_OUTPUT, "w") as f:
        f.write("Word Count Report\n")
        f.write(f"Total Words: {total_words}\n")
        f.write(f"Top {top_n} Words:\n")
        for word, count in most_common:
            f.write(f"{word} - {count}\n")

    print("\nReport saved to word_count_report.txt")

