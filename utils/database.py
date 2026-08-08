import sqlite3

import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database.db")
conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT NOT NULL,

    email TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL

)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS analysis_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    resume_name TEXT,
    ats_score INTEGER,
    matched INTEGER,
    missing INTEGER,
    analysis_date TEXT
)
""")

conn.commit()

conn.close()

print("Database Created Successfully!")