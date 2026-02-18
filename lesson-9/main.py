============================================================
📚 TASK 1 — LIBRARY MANAGEMENT SYSTEM (Custom Exceptions)
============================================================
# ===============================
# Custom Exceptions
# ===============================

class BookNotFoundException(Exception):
    pass


class BookAlreadyBorrowedException(Exception):
    pass


class MemberLimitExceededException(Exception):
    pass


# ===============================
# Book Class
# ===============================

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({status})"


# ===============================
# Member Class
# ===============================

class Member:
    MAX_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BOOKS:
            raise MemberLimitExceededException("Borrowing limit exceeded (3 books).")

        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Book is already borrowed.")

        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"Member: {self.name}, Borrowed: {[b.title for b in self.borrowed_books]}"


# ===============================
# Library Class
# ===============================

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.title] = book

    def add_member(self, member):
        self.members[member.name] = member

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException("Book not found in library.")

        member = self.members.get(member_name)
        book = self.books[book_title]

        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = self.members.get(member_name)
        book = self.books.get(book_title)
        member.return_book(book)


# ===============================
# Library Test Demo
# ===============================

def library_demo():
    library = Library()

    b1 = Book("1984", "George Orwell")
    b2 = Book("Python 101", "John Doe")

    m1 = Member("Alice")

    library.add_book(b1)
    library.add_book(b2)
    library.add_member(m1)

    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "Python 101")
        print(m1)

        library.borrow_book("Alice", "Unknown Book")  # triggers exception
    except Exception as e:
        print("Error:", e)


============================================================
📊 TASK 2 — STUDENT GRADES MANAGEMENT (CSV)
============================================================
import csv

# ===============================
# Create grades.csv (if needed)
# ===============================

def create_sample_grades():
    data = [
        ["Name", "Subject", "Grade"],
        ["Alice", "Math", "85"],
        ["Bob", "Science", "78"],
        ["Carol", "Math", "92"],
        ["Dave", "History", "74"]
    ]

    with open("grades.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


# ===============================
# Read and Calculate Averages
# ===============================

def calculate_averages():
    subject_grades = {}

    with open("grades.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            subject = row["Subject"]
            grade = float(row["Grade"])

            if subject not in subject_grades:
                subject_grades[subject] = []

            subject_grades[subject].append(grade)

    averages = {sub: sum(grades)/len(grades) for sub, grades in subject_grades.items()}

    with open("average_grades.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Subject", "Average Grade"])
        for sub, avg in averages.items():
            writer.writerow([sub, round(avg, 2)])

    print("Averages calculated and saved.")


# ============================================================
# 🗂 TASK 3 — JSON HANDLING
# ============================================================

import json


# ===============================
# Load JSON
# ===============================

def load_tasks():
    with open("tasks.json", "r") as f:
        return json.load(f)


# ===============================
# Save JSON
# ===============================

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)


# ===============================
# Display Tasks
# ===============================

def display_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, "
              f"Completed: {task['completed']}, Priority: {task['priority']}")


# ===============================
# Calculate Stats
# ===============================

def task_stats(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    avg_priority = sum(t["priority"] for t in tasks) / total

    print("\nTask Statistics:")
    print("Total:", total)
    print("Completed:", completed)
    print("Pending:", pending)
    print("Average Priority:", round(avg_priority, 2))


# ===============================
# Convert JSON to CSV
# ===============================

def convert_json_to_csv(tasks):
    with open("tasks.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for t in tasks:
            writer.writerow([t["id"], t["task"], t["completed"], t["priority"]])

    print("Converted to tasks.csv")


============================================================
🧠 MAIN CONTROLLER
============================================================
def main():
    while True:
        print("\n=========== MAIN MENU ===========")
        print("1. Library Demo")
        print("2. Grades CSV")
        print("3. JSON Tasks")
        print("4. Exit")

        choice = input("Select: ")

        if choice == "1":
            library_demo()

        elif choice == "2":
            create_sample_grades()
            calculate_averages()

        elif choice == "3":
            tasks = load_tasks()
            display_tasks(tasks)
            task_stats(tasks)
            convert_json_to_csv(tasks)

        elif choice == "4":
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
