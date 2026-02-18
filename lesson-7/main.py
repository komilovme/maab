# ============================================================
# ================== 1️⃣ GENERALIZED VECTOR ==================
# ============================================================

import math
import os
import json
import csv
from abc import ABC, abstractmethod


class Vector:
    def __init__(self, *components):
        if not components:
            raise ValueError("Vector must have at least one component")
        self.components = tuple(float(c) for c in components)

    def __str__(self):
        return f"Vector{self.components}"

    def __len__(self):
        return len(self.components)

    def _check_dimension(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have same dimension")

    def __add__(self, other):
        self._check_dimension(other)
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        self._check_dimension(other)
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        else:
            raise TypeError("Invalid multiplication")

    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector(*(a / mag for a in self.components))


# ============================================================
# ============ 2️⃣ EMPLOYEE RECORDS MANAGER (OOP) ===========
# ============================================================

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = float(salary)

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary:.2f}"

    def to_file(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}\n"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            open(self.FILE_NAME, "w").close()

    def _read_all(self):
        with open(self.FILE_NAME, "r") as f:
            return f.readlines()

    def _write_all(self, lines):
        with open(self.FILE_NAME, "w") as f:
            f.writelines(lines)

    def add_employee(self):
        emp_id = input("Employee ID: ")

        if any(line.startswith(emp_id + ",") for line in self._read_all()):
            print("Employee ID already exists!")
            return

        name = input("Name: ")
        position = input("Position: ")
        salary = input("Salary: ")

        emp = Employee(emp_id, name, position, salary)

        with open(self.FILE_NAME, "a") as f:
            f.write(emp.to_file())

        print("Employee added successfully!")

    def view_all(self):
        lines = self._read_all()
        if not lines:
            print("No records found.")
            return

        print("\nEmployee Records:")
        for line in lines:
            print(line.strip())

    def search_employee(self):
        emp_id = input("Employee ID to search: ")
        for line in self._read_all():
            if line.startswith(emp_id + ","):
                print("Employee Found:")
                print(line.strip())
                return
        print("Employee not found.")

    def update_employee(self):
        emp_id = input("Employee ID to update: ")
        lines = self._read_all()
        updated = False

        with open(self.FILE_NAME, "w") as f:
            for line in lines:
                if line.startswith(emp_id + ","):
                    name = input("New Name: ")
                    position = input("New Position: ")
                    salary = input("New Salary: ")
                    emp = Employee(emp_id, name, position, salary)
                    f.write(emp.to_file())
                    updated = True
                else:
                    f.write(line)

        print("Updated!" if updated else "Employee not found.")

    def delete_employee(self):
        emp_id = input("Employee ID to delete: ")
        lines = self._read_all()
        new_lines = [line for line in lines if not line.startswith(emp_id + ",")]
        self._write_all(new_lines)
        print("Deleted successfully.")

    def menu(self):
        while True:
            print("\n===== Employee Manager =====")
            print("1. Add")
            print("2. View")
            print("3. Search")
            print("4. Update")
            print("5. Delete")
            print("6. Back")

            choice = input("Choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                break
            else:
                print("Invalid choice.")


# ============================================================
# =================== 3️⃣ TODO APPLICATION ===================
# ============================================================

class Storage(ABC):
    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass


class JSONStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w") as f:
            json.dump(tasks, f, indent=4)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except:
            return []


class ToDoApp:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self):
        task = {
            "id": input("Task ID: "),
            "title": input("Title: "),
            "description": input("Description: "),
            "due_date": input("Due Date: "),
            "status": input("Status: ")
        }
        self.tasks.append(task)
        print("Task added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks.")
            return
        for task in self.tasks:
            print(task)

    def update_task(self):
        task_id = input("Task ID to update: ")
        for task in self.tasks:
            if task["id"] == task_id:
                task["title"] = input("New Title: ")
                task["description"] = input("New Description: ")
                task["due_date"] = input("New Due Date: ")
                task["status"] = input("New Status: ")
                print("Updated.")
                return
        print("Task not found.")

    def delete_task(self):
        task_id = input("Task ID to delete: ")
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        print("Deleted.")

    def filter_tasks(self):
        status = input("Filter by status: ")
        for task in self.tasks:
            if task["status"] == status:
                print(task)

    def save(self):
        self.storage.save(self.tasks)
        print("Saved.")

    def menu(self):
        while True:
            print("\n===== ToDo App =====")
            print("1 Add")
            print("2 View")
            print("3 Update")
            print("4 Delete")
            print("5 Filter")
            print("6 Save")
            print("7 Back")

            c = input("Choice: ")

            if c == "1":
                self.add_task()
            elif c == "2":
                self.view_tasks()
            elif c == "3":
                self.update_task()
            elif c == "4":
                self.delete_task()
            elif c == "5":
                self.filter_tasks()
            elif c == "6":
                self.save()
            elif c == "7":
                break
            else:
                print("Invalid choice.")


# ============================================================
# ======================== MAIN MENU =========================
# ============================================================

def main():
    while True:
        print("\n=========== MAIN MENU ===========")
        print("1. Vector Demo")
        print("2. Employee Manager")
        print("3. ToDo App")
        print("4. Exit")

        choice = input("Select: ")

        if choice == "1":
            v1 = Vector(1, 2, 3)
            v2 = Vector(4, 5, 6)
            print(v1 + v2)
            print(v1 * v2)
            print(v1.normalize())
        elif choice == "2":
            manager = EmployeeManager()
            manager.menu()
        elif choice == "3":
            app = ToDoApp(JSONStorage("tasks.json"))
            app.menu()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


