"""
controllers/department_controller.py
--------------------------------------
Purpose:
    The Controller layer receives input already collected by the view,
    passes it to the service layer, and translates the result (or any
    error) back into something the view can display.

Why this file exists:
    Controllers keep the view "dumb" (just input/print) and the service
    layer free of any console-specific concerns. This separation is
    what allows the same service layer to be reused by a future web API
    without rewriting business logic.

How it communicates with the next layer:
    - Downward: calls DepartmentService to perform the actual work.
    - Upward: returns simple result data/messages to department_view.py.
"""

from models.department import Department
from services.department_service import DepartmentService


class DepartmentController:
    """Coordinates between the department view and the department service."""

    def __init__(self) -> None:
        self.service = DepartmentService()

    def add_department(self, department_name: str, hod_name: str) -> str:
        """
        Handle the "Add Department" use case.

        Args:
            department_name (str): Raw department name from the view.
            hod_name (str): Raw HOD name from the view.

        Returns:
            str: A success message including the new department_id, or
            an error message if validation failed.
        """
        try:
            department: Department = self.service.add_department(
                department_name, hod_name
            )
            return (
                f"Department '{department.department_name}' added successfully "
                f"with ID {department.department_id}."
            )
        except ValueError as error:
            return f"Failed to add department: {error}"

    def view_department(self, department_id: int) -> str:
        """
        TODO (Student Exercise):
        Call service.get_department() and format the result as a
        display-friendly string for the view.
        """
        try:
            department = self.service.get_department(department_id)
            return (
                f"Department ID: {department.department_id}\n"
                f"Name: {department.department_name}\n"
                f"HOD: {department.hod_name}"
            )
        except ValueError as error:
            return f"Error: {error}"

    def view_all_departments(self) -> str:
        """
        TODO (Student Exercise):
        Call service.get_all_departments() and format the list as a
        display-friendly string/table for the view.
        """
        raise NotImplementedError("Students will implement this feature.")

    def update_department(
        self, department_id: int, department_name: str, hod_name: str
    ) -> str:
        """
        TODO (Student Exercise):
        Call service.update_department() and return a success/failure
        message for the view.
        """
        raise NotImplementedError("Students will implement this feature.")

    def delete_department(self, department_id: int) -> str:
        """
        TODO (Student Exercise):
        Call service.delete_department() and return a success/failure
        message for the view.
        """
        raise NotImplementedError("Students will implement this feature.")
