"""
views/department_view.py
--------------------------
Purpose:
    The View layer is responsible ONLY for console input/output. It
    never contains business logic or SQL — it just asks the user for
    input and prints whatever the controller gives back.

Why this file exists:
    Keeping input/print statements isolated here means the rest of the
    application (controller/service/repository) never depends on the
    console. Those layers could be reused later with a web UI.

How it communicates with the next layer:
    Calls methods on DepartmentController and prints the returned
    messages. It never talks to the service or repository directly.
"""

from controllers.department_controller import DepartmentController


class DepartmentView:
    """Handles console interaction for department-related menu options."""

    def __init__(self) -> None:
        self.controller = DepartmentController()

    def show_menu(self) -> None:
        """Display the department submenu and route the user's choice."""
        while True:
            print("\n----- Department Menu -----")
            print("1. Add Department")
            print("2. View Department")
            print("3. Update Department")
            print("4. Delete Department")
            print("5. Back")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_department()
            elif choice == "2":
                self.view_department()
            elif choice == "3":
                self.update_department()
            elif choice == "4":
                self.delete_department()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_department(self) -> None:
        """Collect input for a new department and display the result."""
        print("\n--- Add Department ---")
        department_name = input("Enter department name: ")
        hod_name = input("Enter HOD name: ")

        message = self.controller.add_department(department_name, hod_name)
        print(message)

    def view_department(self) -> None:
<<<<<<< Updated upstream
        """
        TODO (Student Exercise):
        Ask the user for a department_id, call
        self.controller.view_department(department_id), and print the
        result.
        """
        print("\nTODO:\nStudents will implement this feature.")
        """
views/department_view.py
--------------------------
Purpose:
    The View layer is responsible ONLY for console input/output. It
    never contains business logic or SQL — it just asks the user for
    input and prints whatever the controller gives back.

Why this file exists:
    Keeping input/print statements isolated here means the rest of the
    application (controller/service/repository) never depends on the
    console. Those layers could be reused later with a web UI.

How it communicates with the next layer:
    Calls methods on DepartmentController and prints the returned
    messages. It never talks to the service or repository directly.
"""

from controllers.department_controller import DepartmentController


class DepartmentView:
    """Handles console interaction for department-related menu options."""

    def __init__(self) -> None:
        self.controller = DepartmentController()

    def show_menu(self) -> None:
        """Display the department submenu and route the user's choice."""
        while True:
            print("\n----- Department Menu -----")
            print("1. Add Department")
            print("2. View Department")
            print("3. Update Department")
            print("4. Delete Department")
            print("5. Back")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_department()
            elif choice == "2":
                self.view_department()
            elif choice == "3":
                self.update_department()
            elif choice == "4":
                self.delete_department()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_department(self) -> None:
        """Collect input for a new department and display the result."""
        print("\n--- Add Department ---")
        department_name = input("Enter department name: ")
        hod_name = input("Enter HOD name: ")

        message = self.controller.add_department(department_name, hod_name)
        print(message)

    def view_department(self) -> None:
        """
        TODO (Student Exercise):
        Ask the user for a department_id, call
        self.controller.view_department(department_id), and print the
        result.
        """
        print("\nTODO:\nStudents will implement this feature.")
        """
views/department_view.py
--------------------------
Purpose:
    The View layer is responsible ONLY for console input/output. It
    never contains business logic or SQL — it just asks the user for
    input and prints whatever the controller gives back.

Why this file exists:
    Keeping input/print statements isolated here means the rest of the
    application (controller/service/repository) never depends on the
    console. Those layers could be reused later with a web UI.

How it communicates with the next layer:
    Calls methods on DepartmentController and prints the returned
    messages. It never talks to the service or repository directly.
"""

from controllers.department_controller import DepartmentController


class DepartmentView:
    """Handles console interaction for department-related menu options."""

    def __init__(self) -> None:
        self.controller = DepartmentController()

    def show_menu(self) -> None:
        """Display the department submenu and route the user's choice."""
        while True:
            print("\n----- Department Menu -----")
            print("1. Add Department")
            print("2. View Department")
            print("3. Update Department")
            print("4. Delete Department")
            print("5. Back")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_department()
            elif choice == "2":
                self.view_department()
            elif choice == "3":
                self.update_department()
            elif choice == "4":
                self.delete_department()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_department(self) -> None:
        """Collect input for a new department and display the result."""
        print("\n--- Add Department ---")
        department_name = input("Enter department name: ")
        hod_name = input("Enter HOD name: ")

        message = self.controller.add_department(department_name, hod_name)
        print(message)

    def view_department(self) -> None:
        """
        TODO (Student Exercise):
        Ask the user for a department_id, call
        self.controller.view_department(department_id), and print the
        result.
        """
        print("\n--- View Department ---")

        department_id = input("Enter department ID to view: ")
        message = self.controller.view_department(department_id)
        print(message)
=======
        """Collect a department_id and display the department details."""
        print("\n--- View Department ---")
        try:
            department_id = int(input("Enter department ID: "))
            message = self.controller.view_department(department_id)
            print(message)
        except ValueError:
            print("Invalid input. Please enter a valid integer for department ID.")
>>>>>>> Stashed changes

    def update_department(self) -> None:
        """
        TODO (Student Exercise):
        Ask the user for a department_id and the new values, call
        self.controller.update_department(...), and print the result.
        """
        print("\nTODO:\nStudents will implement this feature.")

    def delete_department(self) -> None:
        """
        TODO (Student Exercise):
        Ask the user for a department_id, call
        self.controller.delete_department(department_id), and print the
        result.
        """
        print("\nTODO:\nStudents will implement this feature.")
