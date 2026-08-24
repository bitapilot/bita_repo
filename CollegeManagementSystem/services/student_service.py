


import sqlite3
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
       
        try:
            # Validate input
            student_name = student_name.strip()
            gender = gender.strip()
            dob = dob.strip()
            phone = phone.strip()
            email = email.strip()

            if not student_name:
                raise ValueError("Student name cannot be empty.")
            if not gender:
                raise ValueError("Gender cannot be empty.")
            if not dob:
                raise ValueError("Date of birth cannot be empty.")
            if not phone:
                raise ValueError("Phone number cannot be empty.")
            if not email:
                raise ValueError("Email cannot be empty.")
            if "@" not in email:
                raise ValueError("Email must contain '@'.")

            student = Student(
                student_name=student_name,
                gender=gender,
                dob=dob,
                phone=phone,
                email=email,
                department_id=department_id,
            )
            return self.repository.add(student)
        except sqlite3.IntegrityError as error:
            raise ValueError(
                f"Failed to add student: department_id {department_id} may not exist."
            ) from error
        except ValueError as error:
            raise error

    def get_student(self, student_id: int) -> Student:

        try:
            student = self.repository.get_by_id(student_id)
            if student is None:
                raise ValueError(f"Student with ID {student_id} not found.")
            return student
        except ValueError as error:
            raise ValueError(f"Failed to retrieve student: {error}")

    def get_all_students(self) -> List[Student]:

       
        return self.repository.get_all()

    def update_student(
        self,
        student_id: int,
        student_name: str,
        gender: str,
        dob: str,
        phone: str,
        email: str,
        department_id: int,
    ) -> bool:
        try:
            student = self.repository.get_by_id(student_id)
            if student is None:
                return False

            student_name = student_name.strip()
            gender = gender.strip()
            dob = dob.strip()
            phone = phone.strip()
            email = email.strip()

            if not student_name:
                raise ValueError("Student name cannot be empty.")
            if not gender:
                raise ValueError("Gender cannot be empty.")
            if not dob:
                raise ValueError("Date of birth cannot be empty.")
            if not phone:
                raise ValueError("Phone number cannot be empty.")
            if not email:
                raise ValueError("Email cannot be empty.")
            if "@" not in email:
                raise ValueError("Email must contain '@'.")

            student.student_name = student_name
            student.gender = gender
            student.dob = dob
            student.phone = phone
            student.email = email
            student.department_id = department_id
            return self.repository.update(student)
        except sqlite3.IntegrityError as error:
            raise ValueError(
                f"Failed to update student: department_id {department_id} may not exist."
            ) from error
        except ValueError as error:
            raise error

    def delete_student(self, student_id: int) -> bool:
       
    
        try:
            return self.repository.delete(student_id)
        except sqlite3.IntegrityError as error:
            raise ValueError(
                "Cannot delete this student due to database constraints."
            ) from error
