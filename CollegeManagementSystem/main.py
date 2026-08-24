"""
main.py
--------
Purpose:
    The application entry point. Displays the top-level console menu
    and routes the user into each module's submenu.

Why this file exists:
    Every console application needs a single starting point. main.py
    owns the top-level loop; it delegates everything else to the view
    layer for each module (department/student/staff).

How it communicates with the next layer:
    Creates a View object (e.g. DepartmentView) for the module the user
    selects and calls its show_menu() method. main.py never talks to
    controllers, services, or repositories directly — that would break
    the layering of the MVC architecture.

Before running:
    Make sure the database has been created first:
        python database/create_database.py
    Then start the application:
        python main.py0
"""

from views.department_view import DepartmentView
from views.staff_view import StaffView
from views.student_view import StudentView


def show_main_menu() -> None:
    """Display the top-level menu and route to each module's submenu."""
    department_view = DepartmentView()
    student_view = StudentView()
    staff_view = StaffView()

    while True:
        print("\n===== College Management System =====")
        print("1. Department")
        print("2. Student")
        print("3. Staff")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            department_view.show_menu()
        elif choice == "2":
            student_view.show_menu()
        elif choice == "3":
            staff_view.show_menu()
        elif choice == "0" :

            print("Exiting College Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    show_main_menu()
