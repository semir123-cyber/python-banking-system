from flask import Flask, render_template, request , redirect , session , flash
from user import User
from file_handler import load_users, save_users

app = Flask(__name__)
app.secret_key= "secret123"


# ---------------- HOME PART----------------
@app.route("/")
def home():
    return "Welcome to Your Banking System"


# ---------------- REGISTER PART----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    users = load_users()

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            return "Username already exists"

        users[username] = User(username, password)
        save_users(users)

        return "Account created successfully!"

    return render_template("register.html")


# ---------------- LOGIN PART----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    users = load_users()

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username not in users:
            return "User not found"

        user = users[username]
        hashed = User.hash_password(password)

        if user.password != hashed:
            flash("Invalid password", "error")
            return redirect("/login")

        session["user"] = user.username
        return redirect("/dashboard")

    return render_template("login.html")

# ---------------- DASHBOARD PART----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    username = session["user"]
    users = load_users()
    user = users[username]

    return render_template("dashboard.html", user=user)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

@app.route("/deposit", methods=["POST"])
def deposit():
    if "user" not in session:
        return redirect("/login")

    users = load_users()
    username = session["user"]
    user = users[username]

    amount = float(request.form["amount"])

    if amount <= 0:
       flash("Invalid amount", "error")
    else:
        user.deposit(amount)
        flash("Deposit successful", "success")
    save_users(users)

    return redirect("/dashboard")

@app.route("/withdraw", methods=["POST"])
def withdraw():
    if "user" not in session:
        return redirect("/login")

    users = load_users()
    username = session["user"]
    user = users[username]

    amount = float(request.form["amount"])

    user.withdraw(amount)
    save_users(users)

    return redirect("/dashboard")

@app.route("/transfer", methods=["POST"])
def transfer():
    if "user" not in session:
        return redirect("/login")

    users = load_users()
    sender_name = session["user"]
    sender = users[sender_name]

    receiver_name = request.form["receiver"]
    amount = float(request.form["amount"])

    # checks validation 
    if receiver_name not in users:
        return "User not found"

    if receiver_name == sender_name:
        return "You cannot transfer to yourself"

    receiver = users[receiver_name]

    if amount <= 0:
        return "Invalid amount"

    if amount > sender.balance:
        return "Insufficient balance"

    #  transfer part 
    sender.balance -= amount
    receiver.balance += amount

    sender.history.append(
        f"[{User.get_time()}] Sent {amount} to {receiver_name}"
    )
    receiver.history.append(
        f"[{User.get_time()}] Received {amount} from {sender_name}"
    )

    save_users(users)

    return redirect("/dashboard")

                                                        
if __name__ == "__main__":
    app.run(debug=True)