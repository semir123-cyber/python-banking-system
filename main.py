import json

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


# ---------------- FILE HANDLING ----------------

def save_users(users):
    data={}

    for username,user in users.items():
        data[username]={
            "password": user.password,
            "balance": user.balance,
            "history": user.history
        }

    with open("bank.json", "w") as file:
        json.dump(data,file,indent=4)

def load_users():
    users = {}
    try:
        with open("bank.json", "r") as file:
            data=json.load(file) 

            for username , info in data.items():
                users[username] = User(

                    username,

                    info["password"],
                    info["balance"],
                    info["history"]
                )
                

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
               password = input("Enter password: ")

               if username in users:
                 print("Username already exists")

               elif len(password) < 4:
                 print("Password must be at least 4 characters")
    
               else:
                 users[username] = User(username, password)
                 save_users(users)
                 print("Account created successfully")



       
        elif choice == "2":
             username = input("Enter username: ")
             password = input("Enter password: ")

             if username not in users:
                 print("User not found")
                 continue

             user = users[username]

             if user.password != password:
                print("Invalid password")
                continue

             print(f"\nWelcome {user.username}")

          
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