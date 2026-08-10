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

from models.department import Department
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
        staff_name = staff_name.strip()
        designation = designation.strip()
        phone = phone.strip()
        email = email.strip()

        if not staff_name:
            raise ValueError("Staff name cannot be empty.")
        if not designation:
            raise ValueError("Designation cannot be empty.")
        if not phone:
            raise ValueError("Phone cannot be empty.")
        if not email:
            raise ValueError("Email cannot be empty.")
        if "@" not in email:
            raise ValueError("Invalid email format.")

        staff = Staff(
            staff_name=staff_name,
            designation=designation,
            phone=phone,
            email=email,
            department_id=department_id
        )
        return self.repository.add(staff)
    

    def get_staff(self, staff_id: int) -> Staff:
        try:
            staff = self.repository.get_by_id(staff_id)
            if staff is None:
                raise ValueError(f"Staff with ID {staff_id} does not exist.")
            return staff   
        finally:
            pass  # Ensure any necessary cleanup here, if needed    

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
