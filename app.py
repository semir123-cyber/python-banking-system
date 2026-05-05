from flask import Flask, render_template, request , redirect , session , flash

from db_operations import (
    create_user,
    login_user,
    get_balance,
    deposit_money,
    withdraw_money,
    transfer_money, 
    get_transactions

)

app = Flask(__name__)
app.secret_key= "secret123"


# ---------------- HOME PART----------------
@app.route("/")
def home():
    return "Welcome to Your Banking System"


# ---------------- REGISTER PART----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        create_user(username, password)
        flash("User registered successfully!", "success")

        return redirect("/login")

    return render_template("register.html")


# ---------------- LOGIN PART----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = login_user(username, password)

        if user:
            session["user"] = username
            flash("Login successful!", "success")
            return redirect("/dashboard")
        else:
            flash("Invalid username or password!", "error")

    return render_template("login.html")

# ---------------- DASHBOARD PART----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    username = session["user"]
    balance = get_balance(username)
    transactions = get_transactions(username)

    return render_template(
        "dashboard.html",
        username=username,
        balance=balance,
        transactions=transactions
    )
# ---------------- DEPOSIT PART----------------
@app.route("/deposit", methods=["POST"])
def deposit():
    if "user" not in session:
        return redirect("/login")

    amount = float(request.form["amount"])
    username = session["user"]

    if amount <= 0:
        flash("Invalid amount", "error")
    else:
        deposit_money(username, amount)
        flash("Deposit successful", "success")

    return redirect("/dashboard")

# ---------------- WITHDRAW PART----------------
@app.route("/withdraw", methods=["POST"])
def withdraw():
    if "user" not in session:
        return redirect("/login")

    amount = float(request.form["amount"])
    username = session["user"]

    success = withdraw_money(username, amount)

    if success:
        flash("Withdraw successful", "success")
    else:
        flash("Insufficient balance", "error")

    return redirect("/dashboard")

# ---------------- TRANSFER PART----------------
@app.route("/transfer", methods=["POST"])
def transfer():
    if "user" not in session:
        return redirect("/login")

    sender = session["user"]
    receiver = request.form["receiver"]
    amount = float(request.form["amount"])

    result = transfer_money(sender, receiver, amount)

    if result == "success":
        flash("Transfer successful!", "success")
    elif result == "receiver_not_found":
        flash("Receiver not found!", "error")
    elif result == "same_user":
        flash("You cannot transfer to yourself!", "error")
    elif result == "invalid_amount":
        flash("Invalid amount!", "error")
    elif result == "insufficient":
        flash("Insufficient balance!", "error")

    return redirect("/dashboard")

# ---------------- LOGOUT PART----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

                                                        
if __name__ == "__main__":
    app.run(debug=True)