import sqlite3
from pathlib import Path

def _create_intake_table(conn: sqlite3.Connection) -> None:
    table = """CREATE TABLE IF NOT EXISTS intake (
id integer PRIMARY KEY AUTOINCREMENT,
date text NOT NULL,
hour text NOT NULL,
medication text NOT NULL)"""
    cursor = conn.cursor()
    cursor.execute(table)

def _create_activities_mood_table(conn: sqlite3.Connection) -> None:
    table = """CREATE TABLE IF NOT EXISTS activities_mood (
id integer PRIMARY KEY AUTOINCREMENT,
date text NOT NULL,
activity text NOT NULL,
mood text NOT NULL)"""
    cursor = conn.cursor()
    cursor.execute(table)

def create_db() -> None:
    conn = db_conn()
    _create_intake_table(conn)
    _create_activities_mood_table(conn)

def db_conn() -> sqlite3.Connection:
    root = Path().absolute()
    return sqlite3.connect(root / "data/louzou.db")

if __name__ == "__main__":
    create_db()
