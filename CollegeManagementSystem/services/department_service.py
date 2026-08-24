"""
services/department_service.py
--------------------------------
Purpose:
    The Service layer holds business logic and validation rules. It
    sits between the controller (which handles user interaction flow)
    and the repository (which handles raw data access).

Why this file exists:
    Validation and business rules (e.g. "department name is required")
    do not belong in the controller or the repository. Keeping them
    here means the same rules apply no matter how add_department() is
    triggered (console app, future web API, tests, etc.).

How it communicates with the next layer:
    - Downward: calls DepartmentRepository to persist/read data.
    - Upward: returns Department objects (or raises ValueError on
      invalid input) to department_controller.py.
"""

import sqlite3
from typing import List

from models.department import Department
from repositories.department_repository import DepartmentRepository


class DepartmentService:
    """Business logic for department-related operations."""

    def __init__(self) -> None:
        self.repository = DepartmentRepository()

    def add_department(self, department_name: str, hod_name: str) -> Department:
        """
        Validate input and create a new department.

        Args:
            department_name (str): Name of the department (required).
            hod_name (str): Name of the Head of Department (required).

        Returns:
            Department: The newly created department, including its
            generated department_id.

        Raises:
            ValueError: If department_name or hod_name is blank.
        """
        department_name = department_name.strip()
        hod_name = hod_name.strip()

        if not department_name:
            raise ValueError("Department name cannot be empty.")
        if not hod_name:
            raise ValueError("HOD name cannot be empty.")

        department = Department(department_name=department_name, hod_name=hod_name)
        return self.repository.add(department)

    def get_department(self, department_id: int) -> Department:
        try:
            department = self.repository.get_by_id(department_id)
            if department is None:
                raise ValueError(f"Department with ID {department_id} does not exist.")
            return department   
        finally:
            pass  # Ensure any necessary cleanup here, if needed    

    def get_all_departments(self) -> List[Department]:
        """
        TODO (Student Exercise):
        Retrieve all departments via the repository.
        """
        return self.repository.get_all()

    def update_department( self, department_id: int, department_name: str, hod_name: str ) -> bool:
        
        department_id = department_id
        department_name = department_name.strip()
        hod_name = hod_name.strip()

        if not department_name:
            raise ValueError("Department name cannot be empty.")
        if not hod_name:
            raise ValueError("HOD name cannot be empty.")
            
        department = Department(department_id=department_id, department_name=department_name, hod_name=hod_name)
        return self.repository.update(department)

        
       
    def delete_department(self, department_id: int) -> bool:
        """
        TODO (Student Exercise):
        Call repository.delete(). Consider validating that the
        department exists first, and how to handle the case where
        students/staff still reference this department.
        """
        try:
            return self.repository.delete(department_id)
        except sqlite3.IntegrityError as error:
            raise ValueError(
                "Cannot delete this department because students or staff are assigned to it."
            ) from error
