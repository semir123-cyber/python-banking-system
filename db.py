import sqlite3


conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# USERS TABLE 
cursor.execute("""
               
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    balance REAL DEFAULT 0
)
               
""")

# TRANSACTIONS TABLE
cursor.execute("""
               
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT,
    receiver TEXT,
    amount REAL,
    type TEXT,
    time TEXT
)
               
""")

conn.commit()
conn.close()

print("Database setup complete!")