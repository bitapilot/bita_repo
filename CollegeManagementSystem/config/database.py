"""
config/database.py
-------------------
Purpose:
    Provides a single, reusable way to open a connection to cms.db.

Why this file exists:
    Without a central connection helper, every repository would
    duplicate the same sqlite3.connect(...) path logic. Centralizing it
    here means the database location only needs to change in one place.

How it communicates with the next layer:
    Repositories import `get_connection()` from this module whenever
    they need to talk to SQLite. This is the ONLY file that knows the
    physical path of cms.db.
"""

import sqlite3
from pathlib import Path

DATABASE_FILE = Path(__file__).resolve().parent.parent / "database" / "cms.db"


def get_connection() -> sqlite3.Connection:
    """
    Open and return a new SQLite connection to cms.db.

    Returns:
        sqlite3.Connection: An open connection with foreign key
        enforcement turned on and Row factory enabled so query
        results can be accessed like dictionaries.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    connection.execute("PRAGMA foreign_keys = ON;")
    connection.row_factory = sqlite3.Row
    return connection



