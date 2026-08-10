"""
services/student_service.py
------------------------------
Purpose:
    Business logic and validation for student-related operations.
    Mirrors the pattern used in services/department_service.py — use
    that file as your reference implementation.

How it communicates with the next layer:
    - Downward: calls StudentRepository to persist/read data.
    - Upward: returns Student objects (or raises ValueError on invalid
      input) to student_controller.py.

TODO (Student Exercise):
    Implement each method below. Think about what validation rules make
    sense for a student:
        - student_name, gender, dob, phone, email must not be empty
        - email should contain "@"
        - department_id must refer to an existing department
          (consider calling DepartmentService/DepartmentRepository to
          check this, or let the database's FOREIGN KEY constraint
          raise an sqlite3.IntegrityError that you catch and translate
          into a friendly message)
"""

from typing import List

from models.student import Student
from repositories.student_repository import StudentRepository


class StudentService:
    """Business logic for student-related operations."""

    def __init__(self) -> None:
        self.repository = StudentRepository()

    def add_student(
        self,
        student_name: str,
        gender: str,
        dob: str,
        phone: str,
        email: str,
        department_id: int,
    ) -> Student:
        """
        TODO (Student Exercise):
        Validate input, build a Student object, and call
        self.repository.add(student).
        """
        raise NotImplementedError("Students will implement this feature.")

    def get_student(self, student_id: int) -> Student:
        try:
            student = self.repository.get_by_id(student_id)
            if student is None:
                raise ValueError(f"Student with ID {student_id} does not exist.")
            return student   
        finally:
            pass  # Ensure any necessary cleanup here, if needed    

    def get_all_students(self) -> List[Student]:
        """
        TODO (Student Exercise):
        Retrieve all students via the repository.
        """
        raise NotImplementedError("Students will implement this feature.")

    def update_student(self, student: Student) -> bool:
        """
        TODO (Student Exercise):
        Validate input and call self.repository.update(student).
        """
        raise NotImplementedError("Students will implement this feature.")

    def delete_student(self, student_id: int) -> bool:
        """
        TODO (Student Exercise):
        Call self.repository.delete(student_id).
        """
        raise NotImplementedError("Students will implement this feature.")
