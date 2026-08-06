"""
controllers/staff_controller.py
----------------------------------
Purpose:
    Coordinates between the staff view and the staff service. Mirrors
    the pattern used in controllers/department_controller.py — use that
    file as your reference implementation.

How it communicates with the next layer:
    - Downward: calls StaffService to perform the actual work.
    - Upward: returns simple result data/messages to staff_view.py.

TODO (Student Exercise):
    Implement each method below. Each one should:
        1. Call the corresponding StaffService method.
        2. Catch any ValueError raised for invalid input.
        3. Return a display-friendly string (success or error message)
           for the view to print.
"""

from services.staff_service import StaffService


class StaffController:
    """Coordinates between the staff view and the staff service."""

    def __init__(self) -> None:
        self.service = StaffService()

    def add_staff(
        self,
        staff_name: str,
        designation: str,
        phone: str,
        email: str,
        department_id: int,
    ) -> str:
        """TODO (Student Exercise): See department_controller.add_department for the pattern."""
        raise NotImplementedError("Students will implement this feature.")

    def view_staff(self, staff_id: int) -> str:
        """TODO (Student Exercise): Implement using self.service.get_staff()."""
        raise NotImplementedError("Students will implement this feature.")

    def view_all_staff(self) -> str:
        """TODO (Student Exercise): Implement using self.service.get_all_staff()."""
        raise NotImplementedError("Students will implement this feature.")

    def update_staff(self, *args, **kwargs) -> str:
        """TODO (Student Exercise): Implement using self.service.update_staff()."""
        raise NotImplementedError("Students will implement this feature.")

    def delete_staff(self, staff_id: int) -> str:
        """TODO (Student Exercise): Implement using self.service.delete_staff()."""
        raise NotImplementedError("Students will implement this feature.")
