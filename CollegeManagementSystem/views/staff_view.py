"""
views/staff_view.py
----------------------
Purpose:
    Console input/output for staff-related menu options. Mirrors the
    pattern used in views/department_view.py — use that file as your
    reference implementation.

How it communicates with the next layer:
    Calls methods on StaffController and prints the returned messages.
    Never talks to the service or repository directly.

TODO (Student Exercise):
    Implement show_menu() and each handler method following the same
    pattern as DepartmentView. The menu should offer:
        1. Add Staff
        2. View Staff
        3. Update Staff
        4. Delete Staff
        5. Back
"""

from controllers.staff_controller import StaffController


class StaffView:
    """Handles console interaction for staff-related menu options."""

    def __init__(self) -> None:
        self.controller = StaffController()

    def show_menu(self) -> None:
        """
        TODO (Student Exercise):
        Display the staff submenu (see docstring above for options) and
        route the user's choice to the matching handler method,
        following the pattern in DepartmentView.show_menu().
        """
        while True:
            print("\n----- Staff Menu -----")
            print("1. Add Staff")
            print("2. View Staff")
            print("3. Update Staff")
            print("4. Delete Staff")
            print("5. Back")

            choice = input("Enter your choice: ").strip()

            if choice in ("1", "2", "3", "4"):
                print("\nTODO:\nStudents will implement this feature.")
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
