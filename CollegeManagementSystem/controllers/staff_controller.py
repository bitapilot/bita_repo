"""
controllers/staff_controller.py
----------------------------------
Purpose:
    Coordinates between the staff view and the staff service. Mirrors
    the pattern used in controllers/department_controller.py — use that
    file as your reference implementation.

How it communicates with the next layer:
    - Downward: calls StaffService to perform the actual work.
    - Upward: returns simple result data/messages to staff_view.py.

TODO (Student Exercise):
    Implement each method below. Each one should:
        1. Call the corresponding StaffService method.
        2. Catch any ValueError raised for invalid input.
        3. Return a display-friendly string (success or error message)
           for the view to print.
"""

from models.department import Department
from models.staff import Staff
from services.staff_service import StaffService


class StaffController:
    """Coordinates between the staff view and the staff service."""

    def __init__(self) -> None:
        self.service = StaffService()

    def add_staff(
        self,
        staff_name: str,
        designation: str,
        phone: str,
        email: str,
        department_id: int,
    ) -> str:
        try:

            staff: Staff = self.service.add_staff(
                staff_name, designation, phone, email, department_id
            )
            return (
                f"Staff member '{staff.staff_name}' added successfully "
                f"with ID {staff.staff_id}."
            )
        except ValueError as error:
                    return f"Failed to add staff member: {error}"


    def view_staff(self, staff_id: int) -> str:
        try:
            staff: Staff = self.service.get_staff(staff_id)
            return (
                f"Staff ID: {staff.staff_id}\n"
                f"Name: {staff.staff_name}\n"
                f"Designation: {staff.designation}\n"
                f"Phone: {staff.phone}\n"
                f"Email: {staff.email}"
            )
        except ValueError as error:
            return f"Failed to view staff member: {error}"

    def view_all_staff(self) -> str:
        try:
            staff_list = self.service.get_all_staff()
            if not staff_list:
                return "No staff members found."
            return "\n".join(
                [
                    f"ID: {staff.staff_id}, Name: {staff.staff_name}, "
                    f"Designation: {staff.designation}, "
                    f"Phone: {staff.phone}, Email: {staff.email}"
                    for staff in staff_list
                ]
            )
        except ValueError as error:
            return f"Failed to view staff members: {error}"
        
    def update_staff(self, *args, **kwargs) -> str:
        try:
            updated_staff = self.service.update_staff(*args, **kwargs)
            staff_id = args[0] if args else kwargs.get("staff_id")
            if not updated_staff:
                return f"Failed to update staff member ID {staff_id}: staff member not found."
            return f"Staff member ID {staff_id} updated successfully."
        except ValueError as error:
            return f"Failed to update staff member: {error}"

    def delete_staff(self, staff_id: int) -> str:
        """TODO (Student Exercise): Implement using self.service.delete_staff()."""
        try:
            self.service.delete_staff(staff_id)
            return f"Staff member ID {staff_id} deleted successfully."
        except ValueError as error:
            return f"Failed to delete staff member: {error}"
