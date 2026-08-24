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
        """Insert a new student row and return the student with its generated student_id."""
        connection = get_connection()
        try:
            cursor = connection.execute(
                """
                INSERT INTO student
                    (student_name, gender, dob, phone, email, department_id)
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
            connection.commit()
            student.student_id = cursor.lastrowid
            return student
        finally:
            connection.close()

    def get_by_id(self, student_id: int) -> Optional[Student]:
        """Fetch a single student row by primary key. Return None if not found."""
        connection = get_connection()
        try:
            row = connection.execute(
                "SELECT * FROM student WHERE student_id = ?",
                (student_id,),
            ).fetchone()
            if row is None:
                return None
            return Student(
                student_id=row["student_id"],
                student_name=row["student_name"],
                gender=row["gender"],
                dob=row["dob"],
                phone=row["phone"],
                email=row["email"],
                department_id=row["department_id"],
                created_at=row["created_at"],
            )
        finally:
            connection.close()

    def get_all(self) -> List[Student]:
        """Fetch every row from the student table."""
        connection = get_connection()
        try:
            rows = connection.execute(
                "SELECT * FROM student ORDER BY student_id"
            ).fetchall()
            return [
                Student(
                    student_id=row["student_id"],
                    student_name=row["student_name"],
                    gender=row["gender"],
                    dob=row["dob"],
                    phone=row["phone"],
                    email=row["email"],
                    department_id=row["department_id"],
                    created_at=row["created_at"],
                )
                for row in rows
            ]
        finally:
            connection.close()

    def update(self, student: Student) -> bool:
        """Update an existing student row matching student.student_id."""
        connection = get_connection()
        try:
            cursor = connection.execute(
                """
                UPDATE student
                SET student_name = ?, gender = ?, dob = ?, phone = ?, email = ?, department_id = ?
                WHERE student_id = ?
                """,
                (
                    student.student_name,
                    student.gender,
                    student.dob,
                    student.phone,
                    student.email,
                    student.department_id,
                    student.student_id,
                ),
            )
            connection.commit()
            return cursor.rowcount > 0
        finally:
            connection.close()

    def delete(self, student_id: int) -> bool:
        """Delete the student row matching student_id. Return True if a row was deleted."""
        connection = get_connection()
        try:
            cursor = connection.execute(
                "DELETE FROM student WHERE student_id = ?",
                (student_id,),
            )
            connection.commit()
            return cursor.rowcount > 0
        finally:
            connection.close()
