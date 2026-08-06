"""
models/staff.py
----------------
Purpose:
    Defines the Staff entity — a plain data object that mirrors a row
    in the `staff` table.

Why this file exists:
    Same reasoning as models/department.py: keep staff data typed and
    structured instead of passing raw tuples/dicts through the layers.

TODO (Student Exercise):
    This model is already complete for you to use as-is while you build
    the Staff CRUD flow in the controller/service/repository layers.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Staff:
    """Represents a single staff record."""

    staff_name: str
    designation: str
    phone: str
    email: str
    department_id: int
    staff_id: Optional[int] = None
    created_at: Optional[str] = None
