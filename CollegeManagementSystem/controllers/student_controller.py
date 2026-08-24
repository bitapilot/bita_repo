"""
controllers/student_controller.py
------------------------------------
Purpose:
    Coordinates between the student view and the student service.
    Mirrors the pattern used in controllers/department_controller.py —
    use that file as your reference implementation.

How it communicates with the next layer:
    - Downward: calls StudentService to perform the actual work.
    - Upward: returns simple result data/messages to student_view.py.

TODO (Student Exercise):
    Implement each method below. Each one should:
        1. Call the corresponding StudentService method.
        2. Catch any ValueError raised for invalid input.
        3. Return a display-friendly string (success or error message)
           for the view to print.
"""

from models.staff import Staff
from models.student import Student
from services.student_service import StudentService


class StudentController:
    """Coordinates between the student view and the student service."""

    def __init__(self) -> None:
        self.service = StudentService()

    def add_student(
        self,
        student_name: str,
        gender: str,
        dob: str,
        phone: str,
        email: str,
        department_id: int,
    ) -> str:
        """
        Handle the "Add Student" use case.

        Args:
            student_name (str): Name of the student.
            gender (str): Gender of the student.
            dob (str): Date of birth.
            phone (str): Phone number.
            email (str): Email address.
            department_id (int): ID of the department.

        Returns:
            str: A success message with the new student ID, or an error message.
        """
        try:
            student: Student = self.service.add_student(
                student_name, gender, dob, phone, email, department_id
            )
            return (
                f"Student '{student.student_name}' added successfully "
                f"with ID {student.student_id}."
            )
        except ValueError as error:
            return f"Failed to add student: {error}"

    def view_student(self, student_id: int) -> str:
        """
        Handle the "View Student" use case.

        Args:
            student_id (int): The ID of the student to view.

        Returns:
            str: A formatted string with student details, or an error message.
        """
        try:
            student: Student = self.service.get_student(student_id)
            return (
                f"Student ID: {student.student_id}\n"
                f"Name: {student.student_name}\n"
                f"Gender: {student.gender}\n"
                f"Date of Birth: {student.dob}\n"
                f"Phone: {student.phone}\n"
                f"Email: {student.email}"
            )
        except ValueError as error:
            return f"Failed to view student: {error}"
    def view_all_students(self) -> str:
        try:
            students = self.service.get_all_students()
            if not students:
                return "No students found."
            result = "All Students:\n"
            for student in students:
                result += (
                    f"ID: {student.student_id}, "
                    f"Name: {student.student_name}, "
                    f"Gender: {student.gender}, "
                    f"DOB: {student.dob}, " 
                    f"Phone: {student.phone}, "
                    f"Email: {student.email}\n"
                )
            return result
        except ValueError as error:
            return f"Failed to view all students: {error}"

    def update_student(self, *args, **kwargs) -> str:
        """TODO (Student Exercise): Implement using self.service.update_student()."""
        try:
            updated_student = self.service.update_student(*args, **kwargs)
            return f"Student ID {updated_student.student_id} updated successfully."
        except ValueError as error:
            return f"Failed to update student: {error}"

    def delete_student(self, student_id: int) -> str:
        """TODO (Student Exercise): Implement using self.service.delete_student()."""
        try:
            self.service.delete_student(student_id)
            return f"Student ID {student_id} deleted successfully."
        except ValueError as error:
            return f"Failed to delete student: {error}"
