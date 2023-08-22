"""
Basic CLI to execute setup and teardown commands on course.db
"""

import sqlite3
import sys

args = sys.argv[1::]

DB_NAME = "course.db"

con = sqlite3.connect(DB_NAME)
cur = con.cursor()

def load_tables():
    """
    Load tables from CREATE_TABLE.sql
    """
    with open("sql/CREATE_TABLE.sql", "r", encoding="utf-8") as f:
        sql = f.read()
        cur.executescript(sql)

if __name__ == "__main__":
    command = args[0]

    if command == "load":
        print("Loading tables into database")
        load_tables()
