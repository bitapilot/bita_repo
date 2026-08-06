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
        """TODO (Student Exercise): See department_controller.add_department for the pattern."""
        raise NotImplementedError("Students will implement this feature.")

    def view_student(self, student_id: int) -> str:
        """TODO (Student Exercise): Implement using self.service.get_student()."""
        raise NotImplementedError("Students will implement this feature.")

    def view_all_students(self) -> str:
        """TODO (Student Exercise): Implement using self.service.get_all_students()."""
        raise NotImplementedError("Students will implement this feature.")

    def update_student(self, *args, **kwargs) -> str:
        """TODO (Student Exercise): Implement using self.service.update_student()."""
        raise NotImplementedError("Students will implement this feature.")

    def delete_student(self, student_id: int) -> str:
        """TODO (Student Exercise): Implement using self.service.delete_student()."""
        raise NotImplementedError("Students will implement this feature.")
