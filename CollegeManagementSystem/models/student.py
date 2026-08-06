"""
models/student.py
------------------
Purpose:
    Defines the Student entity — a plain data object that mirrors a row
    in the `student` table.

Why this file exists:
    Same reasoning as models/department.py: keep student data typed and
    structured instead of passing raw tuples/dicts through the layers.

TODO (Student Exercise):
    This model is already complete for you to use as-is while you build
    the Student CRUD flow in the controller/service/repository layers.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Student:
    """Represents a single student record."""

    student_name: str
    gender: str
    dob: str
    phone: str
    email: str
    department_id: int
    student_id: Optional[int] = None
    created_at: Optional[str] = None
