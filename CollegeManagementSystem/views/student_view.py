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

            if choice in ("1", "2", "3", "4"):
                print("\nTODO:\nStudents will implement this feature.")
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
