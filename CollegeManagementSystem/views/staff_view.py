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

            if choice == "1":
                self.add_staff()
            elif choice == "2":
                self.view_staff()
            elif choice == "3":
                self.update_staff()
            elif choice == "4":
                self.delete_staff()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_staff(self) -> None:
        print("\n--- Add Staff ---")
        staff_name = input("Enter staff name: ")
        designation = input("Enter designation: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        department_id = int(input("Enter department ID: "))

        message = self.controller.add_staff(staff_name, designation, phone, email, department_id)
        print(message)

    def view_staff(self) -> None:
        print("\n--- View Staff ---")
        try:
            staff_id = int(input("Enter staff ID: "))
            message = self.controller.view_staff(staff_id)
            print(message)
        except ValueError:
            print("Invalid input. Please enter a valid integer for staff ID.")
    

    def update_staff(self) -> None:
        print("\n--- update staff ---")
        try:
            staff_id = int(input("Enter staff ID: "))
            staff_name = input("Enter new staff name: ")
            designation = input("Enter designation: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            message = self.controller.update_staff(staff_id, staff_name, designation, phone, email)
            print(message)
        except ValueError:
            print("Invalid input. Please enter a valid integer for staff ID.")

    
    def delete_staff(self) -> None:
        print("\n--- delete staff ---")
        try:
            staff_id = int(input("Enter Staff id"))
            message = self.controller.delete_staff(staff_id)
            print(message)
        except ValueError:
            print("Invalid input. Please enter a valid integer for staff ID.")
