# College Management System (CMS)

A console-based College Management System built with **Python 3** and
**SQLite**, using the **MVC (Model-View-Controller)** architecture with
a **Repository** and **Service** layer.

This project is a **teaching template**. Only the **Add Department**
flow is fully implemented, end to end, as a worked example. Every other
CRUD operation (Department update/delete/view, all of Student, all of
Staff) is left as a **student exercise** with method signatures, TODO
comments, and hints already in place.

---

## 1. Folder Structure

```
CollegeManagementSystem/
│
├── main.py                        # Application entry point / top-level menu
│
├── config/
│   └── database.py                # Central SQLite connection helper
│
├── controllers/
│   ├── department_controller.py   # ✅ Fully implemented (Add Department)
│   ├── student_controller.py      # 🚧 Skeleton — student exercise
│   └── staff_controller.py        # 🚧 Skeleton — student exercise
│
├── models/
│   ├── department.py              # ✅ Department data class
│   ├── student.py                 # ✅ Student data class
│   └── staff.py                   # ✅ Staff data class
│
├── repositories/
│   ├── department_repository.py   # ✅ add() implemented, others TODO
│   ├── student_repository.py      # 🚧 Skeleton — student exercise
│   └── staff_repository.py        # 🚧 Skeleton — student exercise
│
├── services/
│   ├── department_service.py      # ✅ add_department() implemented, others TODO
│   ├── student_service.py         # 🚧 Skeleton — student exercise
│   └── staff_service.py           # 🚧 Skeleton — student exercise
│
├── views/
│   ├── department_view.py         # ✅ Fully implemented
│   ├── student_view.py            # 🚧 Skeleton — student exercise
│   └── staff_view.py              # 🚧 Skeleton — student exercise
│
├── database/
│   ├── cms.db                     # Generated — not committed until you run create_database.py
│   ├── schema.sql                 # ✅ Complete schema for all 3 tables
│   └── create_database.py         # ✅ Builds cms.db from schema.sql
│
└── README.md
```

### Folder responsibilities

| Folder | Responsibility |
|---|---|
| `config/` | Owns the one place that knows how to open a database connection. |
| `models/` | Plain data classes that mirror table rows. No SQL, no logic. |
| `repositories/` | The ONLY layer allowed to write SQL. Converts rows ↔ model objects. |
| `services/` | Business rules and validation. Calls repositories, never SQL directly. |
| `controllers/` | Bridges the view and the service. Turns exceptions into messages. |
| `views/` | Console input/output only. Never touches SQL or business rules. |
| `database/` | Schema definition and one-time database creation script. |

---

## 2. Technology

* Python 3 (standard library only — no external packages)
* SQLite via the built-in `sqlite3` module
* Console application (input/print) — no GUI, no web framework

---

## 3. Getting Started

```bash
# 1. Create the database (run once, from the CollegeManagementSystem folder)
python database/create_database.py

# 2. Run the application
python main.py
```

> Run both commands from inside the `CollegeManagementSystem/` folder so
> Python can resolve the package imports (`config`, `models`, etc.).

---

## 4. Database Schema

Defined in [`database/schema.sql`](database/schema.sql).

**department**
| Column | Type | Constraints |
|---|---|---|
| department_id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| department_name | TEXT | NOT NULL, UNIQUE |
| hod_name | TEXT | NOT NULL |
| created_at | TIMESTAMP | NOT NULL DEFAULT CURRENT_TIMESTAMP |

**student**
| Column | Type | Constraints |
|---|---|---|
| student_id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| student_name | TEXT | NOT NULL |
| gender | TEXT | NOT NULL |
| dob | DATE | NOT NULL |
| phone | TEXT | NOT NULL |
| email | TEXT | NOT NULL, UNIQUE |
| department_id | INTEGER | NOT NULL, FOREIGN KEY → department |
| created_at | TIMESTAMP | NOT NULL DEFAULT CURRENT_TIMESTAMP |

**staff**
| Column | Type | Constraints |
|---|---|---|
| staff_id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| staff_name | TEXT | NOT NULL |
| designation | TEXT | NOT NULL |
| phone | TEXT | NOT NULL |
| email | TEXT | NOT NULL, UNIQUE |
| department_id | INTEGER | NOT NULL, FOREIGN KEY → department |
| created_at | TIMESTAMP | NOT NULL DEFAULT CURRENT_TIMESTAMP |

---

## 5. The Complete "Add Department" Flow

This is the worked example every other CRUD operation should follow.

```
User types "1" (Department) → "1" (Add Department) at the console
        │
views/department_view.py            DepartmentView.add_department()
        │   collects department_name and hod_name via input()
        ▼
controllers/department_controller.py DepartmentController.add_department()
        │   calls the service, catches ValueError, returns a message string
        ▼
services/department_service.py       DepartmentService.add_department()
        │   validates input, builds a Department model object
        ▼
repositories/department_repository.py DepartmentRepository.add()
        │   runs INSERT INTO department ..., commits, sets department_id
        ▼
config/database.py                   get_connection()
        │   opens the SQLite connection used above
        ▼
database/cms.db                      (row persisted)
        │
        └──▲ Success message travels back up through repository → service
           → controller → view → printed to the console
```

Files involved, in call order:

1. [`views/department_view.py`](views/department_view.py)
2. [`controllers/department_controller.py`](controllers/department_controller.py)
3. [`services/department_service.py`](services/department_service.py)
4. [`repositories/department_repository.py`](repositories/department_repository.py)
5. [`config/database.py`](config/database.py)
6. [`models/department.py`](models/department.py)

Trace through these six files in this order to understand exactly how
one user action flows through every layer of the architecture.

---

## 6. Console Menus

```
===== College Management System =====

1. Department
2. Student
3. Staff
0. Exit
```

```
----- Department Menu -----
1. Add Department      <- fully working
2. View Department     <- prints TODO message
3. Update Department   <- prints TODO message
4. Delete Department   <- prints TODO message
5. Back
```

The Student and Staff menus follow the same 5-option layout, but every
option currently prints:

```
TODO:
Students will implement this feature.
```

---

## 7. Student Exercises

Everything marked 🚧 above is intentionally incomplete. Recommended
implementation order:

1. **Finish Department first** (it's the smallest table, no foreign
   keys to worry about):
   - `repositories/department_repository.py`: `get_by_id`, `get_all`, `update`, `delete`
   - `services/department_service.py`: matching service methods
   - `controllers/department_controller.py`: matching controller methods
   - `views/department_view.py`: replace the TODO prints with real input/output

2. **Then implement Student**, reusing the exact same pattern:
   - `repositories/student_repository.py`
   - `services/student_service.py`
   - `controllers/student_controller.py`
   - `views/student_view.py`

3. **Then implement Staff**, same pattern again:
   - `repositories/staff_repository.py`
   - `services/staff_service.py`
   - `controllers/staff_controller.py`
   - `views/staff_view.py`

**Things to think about while implementing:**

* Student and Staff both have a `department_id` foreign key. What
  should happen if someone tries to add a student to a department that
  doesn't exist? (Hint: SQLite will raise `sqlite3.IntegrityError` —
  decide whether to catch it in the repository or let it bubble up to
  the service.)
* What should `delete_department()` do if students/staff still
  reference that department? The schema uses `ON DELETE RESTRICT`, so
  SQLite will block the delete — how should the service/controller
  communicate that to the user?
* Keep validation logic in the **service** layer, not the controller or
  repository — that's the whole point of the layered architecture.

---

## 8. Architecture Principles Used

* **MVC** — View / Controller / Model separation
* **Repository Pattern** — isolates all SQL in one layer
* **Service Layer** — isolates business rules/validation
* **Separation of Concerns** — each file has exactly one job
* **PEP8**, type hints, and docstrings throughout
