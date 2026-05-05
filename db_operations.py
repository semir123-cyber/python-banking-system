import sqlite3
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash

print("DB PATH:", os.path.abspath("bank.db"))

def create_user(username, password):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    hashed_password = generate_password_hash(password)

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )
        conn.commit()
        print("User created successfully!")

    except sqlite3.IntegrityError:
        print("Username already exists!")

    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username = ?",
        (username,)
    )

    result = cursor.fetchone()
    conn.close()

    if result and check_password_hash(result[0], password):
        print("Login successful!")
        return True
    else:
        print("Invalid username or password!")
        return False

def get_balance(username):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT balance FROM users WHERE username = ?",
        (username,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    return 0

def deposit_money(username, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET balance = balance + ? WHERE username = ?",
        (amount, username)
    )

    conn.commit()
    conn.close()

    #  SAVE HISTORY
    save_transaction("SYSTEM", username, amount, "deposit")

def withdraw_money(username, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT balance FROM users WHERE username = ?",
        (username,)
    )
    balance = cursor.fetchone()[0]

    if amount > balance:
        conn.close()
        return False

    cursor.execute(
        "UPDATE users SET balance = balance - ? WHERE username = ?",
        (amount, username)
    )

    conn.commit()
    conn.close()

    #  SAVE HISTORY
    save_transaction(username, "SYSTEM", amount, "withdraw")

    return True

def transfer_money(sender, receiver, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM users WHERE username = ?", (receiver,))
    if not cursor.fetchone():
        conn.close()
        return "receiver_not_found"

    cursor.execute("SELECT balance FROM users WHERE username = ?", (sender,))
    sender_balance = cursor.fetchone()[0]

    if sender == receiver:
        conn.close()
        return "same_user"

    if amount <= 0:
        conn.close()
        return "invalid_amount"

    if amount > sender_balance:
        conn.close()
        return "insufficient"

    cursor.execute(
        "UPDATE users SET balance = balance - ? WHERE username = ?",
        (amount, sender)
    )

    cursor.execute(
        "UPDATE users SET balance = balance + ? WHERE username = ?",
        (amount, receiver)
    )

    conn.commit()
    conn.close()

    #  SAVE HISTORY
    save_transaction(sender, receiver, amount, "transfer")

    return "success"

def save_transaction(sender, receiver, amount, t_type):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO transactions (sender, receiver, amount, type, time)
        VALUES (?, ?, ?, ?, ?)
    """, (sender, receiver, amount, t_type, time))

    conn.commit()
    conn.close()

def get_transactions(username):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT sender, receiver, amount, type, time
        FROM transactions
        WHERE sender = ? OR receiver = ?
        ORDER BY id DESC
    """, (username, username))

    data = cursor.fetchall()
    conn.close()

    return data