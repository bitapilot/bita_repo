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

from config.database import get_connection
from models import department
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
        connection = get_connection()
        try:
                cursor = connection.execute(
                        """
                        INSERT INTO staff (staff_name, designation, phone, email, department_id)
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        (staff.staff_name, staff.designation, staff.phone, staff.email, staff.department_id),
                    )
                connection.commit()
                staff.staff_id = cursor.lastrowid
                return staff
        
        finally:
                connection.close()
        
    def get_by_id(self, staff_id: int) -> Optional[Staff]:
        try:
            connection = get_connection()
            cursor = connection.execute(
                "SELECT * FROM staff WHERE staff_id = ?",
                (staff_id,),
            )
            row = cursor.fetchone()
            if row:
                return Staff(
                    staff_id=row[0], staff_name=row[1], designation=row[2], phone=row[3], email=row[4], department_id=row[5]
                )
            else:
                return None
        finally:
            connection.close()  

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
