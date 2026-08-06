"""
repositories/staff_repository.py
-----------------------------------
Purpose:
    The Repository layer is the ONLY place allowed to write raw SQL for
    the staff table. Mirrors the pattern used in
    department_repository.py — use that file as your reference
    implementation.

How it communicates with the next layer:
    - Downward: uses config/database.get_connection() to talk to SQLite.
    - Upward: returns Staff model objects to staff_service.py.

TODO (Student Exercise):
    Implement each method below following the same pattern as
    DepartmentRepository in repositories/department_repository.py.
"""

from typing import List, Optional

from models.staff import Staff


class StaffRepository:
    """Handles all direct database access for the staff table."""

    def add(self, staff: Staff) -> Staff:
        """
        TODO (Student Exercise):
        Insert a new staff row and return the staff with its generated
        staff_id populated.

        Hint:
            INSERT INTO staff
                (staff_name, designation, phone, email, department_id)
            VALUES (?, ?, ?, ?, ?)
        """
        raise NotImplementedError("Students will implement this feature.")

    def get_by_id(self, staff_id: int) -> Optional[Staff]:
        """
        TODO (Student Exercise):
        Fetch a single staff row by primary key. Return None if not
        found.
        """
        raise NotImplementedError("Students will implement this feature.")

    def get_all(self) -> List[Staff]:
        """
        TODO (Student Exercise):
        Fetch every row from the staff table.
        """
        raise NotImplementedError("Students will implement this feature.")

    def update(self, staff: Staff) -> bool:
        """
        TODO (Student Exercise):
        Update an existing staff row matching staff.staff_id. Return
        True if a row was updated.
        """
        raise NotImplementedError("Students will implement this feature.")

    def delete(self, staff_id: int) -> bool:
        """
        TODO (Student Exercise):
        Delete the staff row matching staff_id. Return True if a row
        was deleted.
        """
        raise NotImplementedError("Students will implement this feature.")
