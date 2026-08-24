"""
leave_let/leave.py
-------------------
Purpose:
    Generates leave letters as PDF files for students.
    Fetches student details from the database and creates formatted letters.
"""

import sqlite3
from datetime import datetime
from html import escape
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os


class LeaveLetterGenerator:
    """Generates formatted leave letters in PDF format."""

    def __init__(self, db_path: str = "database/cms.db"):
        self.db_path = db_path
        self.output_folder = "leave_letters"
        os.makedirs(self.output_folder, exist_ok=True)

    def get_student_info(self, student_id: int) -> dict:
        """Find the student's name and department."""
        query = """
            SELECT s.student_name, d.department_name
            FROM student AS s
            JOIN department AS d ON s.department_id = d.department_id
            WHERE s.student_id = ?
        """

        conn = sqlite3.connect(self.db_path)
        try:
            conn.row_factory = sqlite3.Row
            row = conn.execute(query, (student_id,)).fetchone()
        except sqlite3.Error as error:
            raise Exception(f"Database error: {error}") from error
        finally:
            conn.close()

        if row is None:
            raise ValueError(f"Student with ID {student_id} not found.")

        return {
            "student_name": row["student_name"],
            "department": row["department_name"],
        }

    def validate_dates(self, start_date: str, end_date: str) -> tuple:
        """Check that both dates use YYYY-MM-DD format."""
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError as error:
            raise ValueError(
                "Use valid dates in YYYY-MM-DD format."
            ) from error

        return start, end

    def generate_leave_letter_pdf(
        self,
        student_id: int,
        start_date: str,
        end_date: str,
        purpose: str,
    ) -> str:
        """Create a PDF leave letter and return its file path."""
        student = self.get_student_info(student_id)
        start, end = self.validate_dates(start_date, end_date)

        filename = (
            f"Leave_Letter_{student_id}_"
            f"{start_date.replace('-', '')}_to_{end_date.replace('-', '')}.pdf"
        )
        filepath = os.path.join(self.output_folder, filename)
        self._build_pdf(filepath, student, student_id, start, end, purpose)
        return filepath

    def _build_pdf(
        self,
        filepath: str,
        student: dict,
        student_id: int,
        start: datetime,
        end: datetime,
        purpose: str,
    ) -> None:
        """Write a simple leave letter to a PDF."""
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            "LeaveTitle",
            parent=styles["Heading1"],
            fontSize=16,
            spaceAfter=12,
            alignment=1,
        )
        text_style = ParagraphStyle(
            "LeaveText", parent=styles["Normal"], fontSize=11, spaceAfter=6
        )

        name = escape(str(student["student_name"]))
        department = escape(str(student["department"]))
        safe_purpose = escape(str(purpose))
        elements = [
            Spacer(1, 0.3 * inch),
            Paragraph("Leave Letter", title_style),
            Spacer(1, 0.3 * inch),
            Paragraph(
                datetime.now().strftime("%d %B %Y"),
                text_style,
            ),
            Spacer(1, 0.15 * inch),
            Paragraph("To the Head of Department,", text_style),
            Spacer(1, 0.2 * inch),
            Paragraph("Dear Sir/Madam,", text_style),
            Spacer(1, 0.1 * inch),
            Paragraph(
                f"I am {name}, a student of the {department} department. "
                f"Please grant me leave from {start.strftime('%d %B %Y')} "
                f"to {end.strftime('%d %B %Y')} because of {safe_purpose}.",
                text_style,
            ),
            Spacer(1, 0.25 * inch),
            Paragraph("Thank you.", text_style),
            Spacer(1, 0.15 * inch),
            Paragraph("Yours faithfully,", text_style),
            Spacer(1, 0.6 * inch),
            Paragraph(name, text_style),
            Paragraph(f"Student ID: {student_id}", text_style),
            Paragraph(department, text_style),
        ]
        SimpleDocTemplate(filepath, pagesize=letter).build(elements)


def main():
    """Run the interactive leave letter generator."""
    input_leave_details()

def input_leave_details() -> tuple:
    """Collect leave details and generate the student's leave letter."""
    print("===== Leave Letter Generator =====\n")

    try:
        student_id = int(input("Enter Student ID: "))
        start_date = input("Enter Start Date (YYYY-MM-DD): ")
        end_date = input("Enter End Date (YYYY-MM-DD): ")
        purpose = input("Enter Purpose of Leave: ")

        purpose = purpose.strip()
        if not purpose:
            raise ValueError("Purpose of leave cannot be empty.")

        print("\nGenerating leave letter...")
        generator = LeaveLetterGenerator()
        filepath = generator.generate_leave_letter_pdf(
            student_id, start_date, end_date, purpose
        )

        print("\nLeave letter generated successfully!")
        print(f"Saved at: {filepath}")
        return student_id, start_date, end_date, purpose, filepath
    except ValueError as error:
        print(f"\nInput Error: {error}")
    except Exception as error:
        print(f"\nError: {error}")

    return None


if __name__ == "__main__":
    main()


