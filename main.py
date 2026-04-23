from user import User
from file_handler import save_users, load_users


# ---------------- INPUT HELPERS PART----------------
def get_float_input(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


# ---------------- MAIN SYSTEM  PART----------------
def main():
    users = load_users()

    while True:
        print("\n====== Banking System ======")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        # ---------------- REGISTER  PART----------------
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

        # ---------------- LOGIN  PART----------------
        elif choice == "2":
            username = input("Enter username: ")

            if username not in users:
                print("User not found")
                continue

            user = users[username]

            attempts = 3

            while attempts > 0:
                password = input("Enter password: ")
                hashed = User.hash_password(password)

                if user.password == hashed:
                    print(f"\nWelcome {user.username}")
                    break
                else:
                    attempts -= 1
                    print(f"Invalid password. Attempts left: {attempts}")

            if attempts == 0:
                print("Too many failed attempts. Access denied.")
                continue

            # ---------------- USER MENU  PART----------------
            while True:
                print("\n--- Menu ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. View History")
                print("5. Transfer Money")
                print("6. Delte acnount ")
                print("7. Logout")

                action = input("Choose option: ")

                if action == "1":
                    amount = get_float_input("Enter amount: ")
                    user.deposit(amount)
                    save_users(users)

                elif action == "2":
                    amount = get_float_input("Enter amount: ")
                    user.withdraw(amount)
                    save_users(users)

                elif action == "3":
                    user.check_balance()

                elif action == "4":
                    user.show_history()

                elif action == "5":
                    receiver_name = input("Enter recipient username: ")

                    if receiver_name not in users:
                        print("User not found")
                        continue

                    if receiver_name == user.username:
                        print("You cannot transfer to yourself")
                        continue

                    receiver = users[receiver_name]

                    amount = get_float_input("Enter amount to transfer: ")

                    if amount <= 0:
                        print("Invalid amount")
                    elif amount > user.balance:
                        print("Insufficient balance")
                    else:
                        user.balance -= amount
                        receiver.balance += amount

                        user.history.append(
                            f"[{User.get_time()}] Sent {amount} to {receiver_name}"
                        )
                        receiver.history.append(
                            f"[{User.get_time()}] Received {amount} from {user.username}"
                        )

                        save_users(users)
                        print("Transfer successful")
                elif action=="7":
                    confirm=input("Are you sure you want to delete your acount? (yes/no)")

                    if confirm.lower() !="yes":
                        print("Acount deletion canceled ")
                        continue 
                    password = input("Enter your password to confirm: ")
                    hashed=user.hash_password(password)

                    if user.password !=hashed:
                        print("Incorrect password.Deletion canceled ")
                        continue 

                    del User[user.username]
                    save_users(users)

                    print("Acount deleted successfully")
                    break 


       
                elif action == "7":
                    print("Logged out")
                    break

                else:
                    print("Invalid choice")

        # ---------------- EXIT ----------------
        elif choice == "3":
            save_users(users)
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()