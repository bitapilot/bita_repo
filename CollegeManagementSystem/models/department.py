"""
models/department.py
---------------------
Purpose:
    Defines the Department entity — a plain data object that mirrors a
    row in the `department` table.

Why this file exists:
    Models keep data structured and typed instead of passing raw tuples
    or dictionaries around the application. This makes the code
    self-documenting and easier to refactor.

How it communicates with the next layer:
    Repositories build Department objects from SQLite rows and return
    them to services/controllers. Nothing in this file touches SQL.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Department:
    """Represents a single department record."""

    department_name: str
    hod_name: str
    department_id: Optional[int] = None
    created_at: Optional[str] = None
