"""
services/staff_service.py
----------------------------
Purpose:
    Business logic and validation for staff-related operations.
    Mirrors the pattern used in services/department_service.py — use
    that file as your reference implementation.

How it communicates with the next layer:
    - Downward: calls StaffRepository to persist/read data.
    - Upward: returns Staff objects (or raises ValueError on invalid
      input) to staff_controller.py.

TODO (Student Exercise):
    Implement each method below. Think about what validation rules make
    sense for staff:
        - staff_name, designation, phone, email must not be empty
        - email should contain "@"
        - department_id must refer to an existing department
"""

from typing import List

from models.staff import Staff
from repositories.staff_repository import StaffRepository


class StaffService:
    """Business logic for staff-related operations."""

    def __init__(self) -> None:
        self.repository = StaffRepository()

    def add_staff(
        self,
        staff_name: str,
        designation: str,
        phone: str,
        email: str,
        department_id: int,
    ) -> Staff:
        """
        TODO (Student Exercise):
        Validate input, build a Staff object, and call
        self.repository.add(staff).
        """
        raise NotImplementedError("Students will implement this feature.")

    def get_staff(self, staff_id: int) -> Staff:
        """
        TODO (Student Exercise):
        Retrieve a single staff member by id via the repository.
        """
        raise NotImplementedError("Students will implement this feature.")

    def get_all_staff(self) -> List[Staff]:
        """
        TODO (Student Exercise):
        Retrieve all staff via the repository.
        """
        raise NotImplementedError("Students will implement this feature.")

    def update_staff(self, staff: Staff) -> bool:
        """
        TODO (Student Exercise):
        Validate input and call self.repository.update(staff).
        """
        raise NotImplementedError("Students will implement this feature.")

    def delete_staff(self, staff_id: int) -> bool:
        """
        TODO (Student Exercise):
        Call self.repository.delete(staff_id).
        """
        raise NotImplementedError("Students will implement this feature.")
