from user import User, hash_password
from file_handler import save_users, load_users


# ---------------- MAIN SYSTEM ----------------

def main():
    users = load_users()

    while True:
        print("\n====== Banking System ======")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        # ---------------- REGISTER PART ----------------
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

        # ---------------- LOGIN PART ----------------
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")

            if username not in users:
                print(" User not found ")
                continue

            user = users[username]

            hashed = hash_password(password)

            if user.password != hashed:
                print("Invalid password")
                continue

            print(f"\nWelcome {user.username}")

            # ---------------- USER MENU PART ----------------
            while True:
                print("\n--- Menu ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. View History")
                print("5  Transfer Money")
                print("6. Logout")

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
                    reciver_name=input("Enter recipient username:  ")

                    if reciver_name not in users:
                        print("User not found ")
                        continue

                    if reciver_name == user.username:
                        print("you can not  transfare to your self ")
                        continue

                    reciver=users[reciver_name ]
                    try :

                      amount=float(input("Enter amount to transfare:  " ))
                    except ValueError:
                      
                      print("Invalid amount (enter a number)")

                    if amount <=0 :
                        print("Invalid amount  ")
                    elif amount > user.balance :
                        print("Insuficient balance")
                    else:
                        user.balance-=amount
                        reciver.balance+= amount 

                        user.history.append(f"sent {amount} to {reciver_name}")
                        reciver.history.append(f"recived {amount} from {user.username}")
                        
                        save_users(users) 
                        print("Transfer successful")
                       

  
                    
                        

                else:
                    print(" Invalid choice (enter 1-5) ")

        # ---------------- EXIT PART ----------------
        elif choice == "3":
            save_users(users)
            print("Goodbye 👋")
            break 

        else:
            print("Invalid choice (enter 1-3)")


if __name__ == "__main__":
    main()