"""
database/create_database.py
----------------------------
Purpose:
    Creates the `cms.db` SQLite database file by executing the SQL
    statements found in `schema.sql`.

Why this file exists:
    Students should never hand-create the database. Running this script
    guarantees every student gets an identical, correctly-structured
    database. Run it once before starting the application:

        python database/create_database.py

How it communicates with the next layer:
    It talks directly to SQLite via the `sqlite3` module. Once cms.db
    exists, the rest of the application (repositories) will connect to
    it through config/database.py.
"""

import sqlite3
from pathlib import Path

# Paths are resolved relative to this file so the script works no matter
# where it is called from.
DATABASE_DIR = Path(__file__).resolve().parent
SCHEMA_FILE = DATABASE_DIR / "schema.sql"
DATABASE_FILE = DATABASE_DIR / "cms.db"


def create_database() -> None:
    """Create cms.db and build all tables defined in schema.sql."""
    schema_sql = SCHEMA_FILE.read_text(encoding="utf-8")

    connection = sqlite3.connect(DATABASE_FILE)
    try:
        connection.executescript(schema_sql)
        connection.commit()
        print(f"Database created successfully at: {DATABASE_FILE}")
    finally:
        connection.close()


if __name__ == "__main__":
    create_database()
