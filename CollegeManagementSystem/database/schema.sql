-- =====================================================================
-- College Management System - Database Schema
-- =====================================================================
-- This file defines the complete table structure for the CMS database.
-- It is executed once by database/create_database.py to build cms.db.
-- =====================================================================

PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------------
-- Table: department
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS department (
    department_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name TEXT NOT NULL UNIQUE,
    hod_name        TEXT NOT NULL,
    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------
-- Table: student
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS student (
    student_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name    TEXT NOT NULL,
    gender          TEXT NOT NULL,
    dob             DATE NOT NULL,
    phone           TEXT NOT NULL,
    email           TEXT NOT NULL UNIQUE,
    department_id   INTEGER NOT NULL,
    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES department (department_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- ---------------------------------------------------------------------
-- Table: staff
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS staff (
    staff_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    staff_name      TEXT NOT NULL,
    designation     TEXT NOT NULL,
    phone           TEXT NOT NULL,
    email           TEXT NOT NULL UNIQUE,
    department_id   INTEGER NOT NULL,
    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES department (department_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
