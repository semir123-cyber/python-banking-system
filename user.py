class User:
    def __init__(self, username, password , balance=0, history=None):
        self.username = username
        self.password=password
        self.balance = balance
        self.history = history if history else []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self.balance += amount
        self.history.append(f"Deposited {amount}")
        print("Deposit successful ")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient amount ")
        else:
            self.balance -= amount
            self.history.append(f"Withdrew {amount}")
            print("Withdraw successful ")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def show_history(self):
        if not self.history:
            print("No transactions yet")
        else:
            print("\nTransaction History:")
            for h in self.history:
                print("-", h)
