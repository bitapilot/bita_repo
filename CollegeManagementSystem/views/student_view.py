"""
views/student_view.py
------------------------
Purpose:
    Console input/output for student-related menu options. Mirrors the
    pattern used in views/department_view.py — use that file as your
    reference implementation.

How it communicates with the next layer:
    Calls methods on StudentController and prints the returned
    messages. Never talks to the service or repository directly.

TODO (Student Exercise):
    Implement show_menu() and each handler method following the same
    pattern as DepartmentView. The menu should offer:
        1. Add Student
        2. View Student
        3. Update Student
        4. Delete Student
        5. Back
"""

from controllers.student_controller import StudentController


class StudentView:
    """Handles console interaction for student-related menu options."""

    def __init__(self) -> None:
        self.controller = StudentController()

    def show_menu(self) -> None:
        """
        TODO (Student Exercise):
        Display the student submenu (see docstring above for options)
        and route the user's choice to the matching handler method,
        following the pattern in DepartmentView.show_menu().
        """
        while True:
            print("\n----- Student Menu -----")
            print("1. Add Student")
            print("2. View Student")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Back")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_student()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_student(self) -> None:
        try:
            print("\n--- Add Student ---")
            student_name = input("Enter student name: ")
            gender = input("Enter gender: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            department_id = int(input("Enter department ID: "))

            message = self.controller.add_student(
                student_name, gender, dob, phone, email, department_id
            )
            print(message)
        except ValueError:
            print("Invalid input. Please enter valid numeric values where required.")

    def view_student(self) -> None:
        try:
            print("\n--- View Student ---")
            student_id = int(input("Enter student ID: "))
            result = self.controller.view_student(student_id)
            print(result)
        except ValueError:
            print("Failed to view student: Student ID must be a number.")

    def update_student(self) -> None:
        try:
            print("\n--- Update Student ---")
            student_id = int(input("Enter student ID to update: "))
            student_name = input("Enter new student name: ")
            gender = input("Enter new gender: ")
            dob = input("Enter new date of birth (YYYY-MM-DD): ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            department_id = int(input("Enter new department ID: "))

            message = self.controller.update_student(
                student_id, student_name, gender, dob, phone, email, department_id
            )
            print(message)
        except ValueError:
            print("Failed to update student: Please enter valid data.")

    def delete_student(self) -> None:
        try:
            print("\n--- Delete Student ---")
            student_id = int(input("Enter student ID to delete: "))
            message = self.controller.delete_student(student_id)
            print(message)
        except ValueError:
            print("Failed to delete student: Student ID must be a number.")
