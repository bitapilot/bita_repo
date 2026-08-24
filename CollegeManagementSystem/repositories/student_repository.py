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

from config.database import get_connection
from models.staff import Staff
from models.student import Student


class StudentRepository:
    """Handles all direct database access for the student table."""

    def add(self, student: Student) -> Student:
        try:
            connection = get_connection()
            cursor = connection.execute(
                """
                INSERT INTO student (student_name, gender, dob, phone, email, department_id)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    student.student_name,
                    student.gender,
                    student.dob,
                    student.phone,
                    student.email,
                    student.department_id,
                ), 
            )
        finally:
            connection.close()

    def get_by_id(self, student_id: int) -> Optional[Student]:
        try:
            connection = get_connection()
            cursor = connection.execute(
                "SELECT * FROM student WHERE student_id = ?",
                (student_id,),
            )
            row = cursor.fetchone()
            if row:
                return Student(
                    student_id=row[0], student_name=row[1], gender=row[2], dob=row[3], phone=row[4], email=row[5], department_id=row[6]
                )
            else:
                return None
        finally:
            connection.close()  

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
