import json 

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