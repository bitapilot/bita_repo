"""
repositories/student_repository.py
-------------------------------------
Purpose:
    The Repository layer is the ONLY place allowed to write raw SQL for
    the student table. Mirrors the pattern used in
    department_repository.py — use that file as your reference
    implementation.

Why this file exists:
    Isolating SQL here keeps the service/controller/view layers free of
    database-specific code.

How it communicates with the next layer:
    - Downward: uses config/database.get_connection() to talk to SQLite.
    - Upward: returns Student model objects to student_service.py.

TODO (Student Exercise):
    Implement each method below following the same pattern as
    DepartmentRepository in repositories/department_repository.py.
"""

from typing import List, Optional

from models.student import Student


class StudentRepository:
    """Handles all direct database access for the student table."""

    def add(self, student: Student) -> Student:
        """
        TODO (Student Exercise):
        Insert a new student row and return the student with its
        generated student_id populated.

        Hint:
            INSERT INTO student
                (student_name, gender, dob, phone, email, department_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        raise NotImplementedError("Students will implement this feature.")

    def get_by_id(self, student_id: int) -> Optional[Student]:
        """
        TODO (Student Exercise):
        Fetch a single student row by primary key. Return None if not
        found.
        """
        raise NotImplementedError("Students will implement this feature.")

    def get_all(self) -> List[Student]:
        """
        TODO (Student Exercise):
        Fetch every row from the student table.
        """
        raise NotImplementedError("Students will implement this feature.")

    def update(self, student: Student) -> bool:
        """
        TODO (Student Exercise):
        Update an existing student row matching student.student_id.
        Return True if a row was updated.
        """
        raise NotImplementedError("Students will implement this feature.")

    def delete(self, student_id: int) -> bool:
        """
        TODO (Student Exercise):
        Delete the student row matching student_id. Return True if a
        row was deleted.
        """
        raise NotImplementedError("Students will implement this feature.")
