import json

from user import User   



def save_users(users):
    User_data = {}

    for username, user in users.items():
        User_data[username] = {
            "password": user.password,
            "balance": user.balance,
            "history": user.history
        }

    with open("bank.json", "w") as file:
        json.dump(User_data, file, indent=4)




def load_users():
    users = {}

    try:
        with open("bank.json", "r") as file:
            User_data = json.load(file)

            for username, info in User_data.items():
                users[username] = User(
                    username,
                    info["password"],
                    info["balance"],
                    info["history"],
                    is_hashed=True
                )

    except FileNotFoundError:
        pass

    return users