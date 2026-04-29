import hashlib
from datetime import datetime


class User:

    # ---------------- PASSWORD HASHING PART----------------
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    # ---------------- TIME HELPER PART----------------
    @staticmethod
    def get_time():
        return datetime.now().strftime("%Y-%m-%d %H:%M")

    # ---------------- INIT PART----------------
    def __init__(self, username, password, balance=0, history=None, is_hashed=False):
        self.username = username

        if is_hashed:
            self.password = password
        else:
            self.password = User.hash_password(password)

        self.balance = balance
        self.history = history if history else []

    # ---------------- DEPOSIT PART----------------
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return

        self.balance += amount
        self.history.append(f"[{User.get_time()}] Deposited {amount}")
        print("Deposit successful")

    # ---------------- WITHDRAW PART----------------
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")

        elif amount > self.balance:
            print("Insufficient amount")

        else:
            self.balance -= amount
            self.history.append(f"[{User.get_time()}] Withdrew {amount}")
            print("Withdraw successful")

    # ---------------- BALANCE PART----------------
    def check_balance(self):
        print(f"Current balance: {self.balance}")

    # ---------------- HISTORY PART----------------
    def show_history(self):
        if not self.history:
            print("No transactions yet")
        else:
            print("\nTransaction History:")
            for h in self.history:
                print("-", h)

 