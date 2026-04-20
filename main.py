class User:
    def __init__(self, username, balance=0, history=None):
        self.username = username
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


# ---------------- FILE HANDLING ----------------

def save_users(users):
    with open("bank.txt", "w") as file:
        for username, user in users.items():
            history_str = "|".join(user.history)
            file.write(f"{username},{user.balance},{history_str}\n")

def load_users():
    users = {}
    try:
        with open("bank.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                username = parts[0]
                balance = float(parts[1])
                history = parts[2].split("|") if len(parts) > 2 and parts[2] else []

                users[username] = User(username, balance, history)
    except FileNotFoundError:
        pass

    return users


# ---------------- MAIN SYSTEM ----------------

def main():
    users = load_users()

    while True:
        print("\n====== Banking System ======")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

      
        if choice == "1":
            username = input("Enter username: ")

            if username in users:
                print("Username already exists")
            else:
                users[username] = User(username)
                save_users(users)
                print("Account created successfully ")

       
        elif choice == "2":
            username = input("Enter username: ")

            if username not in users:
                print("User not found")
                continue

            user = users[username]
            print(f"\nWelcome {user.username} ")

          
            while True:
                print("\n--- Menu ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. View History")
                print("5. Logout")

                action = input("Choose option: ")

                if action == "1":
                    amount = float(input("Enter amount: "))
                    user.deposit(amount)
                    save_users(users)

                elif action == "2":
                    amount = float(input("Enter amount: "))
                    user.withdraw(amount)
                    save_users(users)

                elif action == "3":
                    user.check_balance()

                elif action == "4":
                    user.show_history()

                elif action == "5":
                    print("Logged out ")
                    break

                else:
                    print("Invalid choice (pleace enter only number 1-5 )  ")


   
        elif choice == "3":
            save_users(users)
            print("Goodbye ")
            break

        else:
            print("Invalid choice (enter only number 1-3)")


if __name__ == "__main__":
    main()