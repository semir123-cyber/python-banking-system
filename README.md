# 🏦 Python Banking System

A full-stack banking system built using **Flask + SQLite**, designed to simulate real-world banking operations with secure authentication and transaction handling.

---

##  Live Demo

👉 https://python-banking-system.onrender.com

---

##  Features

* 🔐 Secure User Registration & Login (Password Hashing)
* 💰 Deposit & Withdraw Money
* 🔄 Transfer Money Between Users
* 📊 Real-Time Balance Tracking
* 📜 Transaction History (Database-based)
* 🌐 Web Interface with Clean UI
* ☁️ Deployed on Render

---

## How It Works

This system follows a real backend flow:

```
Frontend (HTML/CSS)
        ↓
Flask (Routes & Logic)
        ↓
SQLite Database
        ↓
Response back to UI
```

### Key Concepts:

* Authentication using hashed passwords
* Persistent data storage with SQLite
* Transaction logging system
* Session-based user management


## Tech Stack

* **Backend:** Python (Flask)
* **Database:** SQLite
* **Frontend:** HTML, CSS
* **Security:** Werkzeug (Password Hashing)
* **Deployment:** Render



## ▶ How to Run Locally

```bash
# Clone the repo
git clone https://github.com/semir123-cyber/python-banking-system.git

# Navigate into the folder
cd python-banking-system

# Install dependencies
pip install -r requirements.txt

# Setup database
python db.py

# Run the app
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

---

## 🔒 Security Features

* Passwords are hashed using `werkzeug.security`
* No plain-text password storage
* Basic session management for authentication

---

##  Future Improvements

* 🔐 Add JWT Authentication
* 🧾 Export transaction history (PDF/CSV)
* 🗄️ Upgrade to PostgreSQL
* ⚡ Build REST API (for mobile/frontend apps)
* 🎨 Improve UI with React or modern frontend

---

## 👨 Author

Built by **Samir Gebi Roba**
Aspiring Software Engineer focused on Python, Backend Systems, and AI.

---

##  Summary

This project demonstrates:

* Real backend architecture
* Secure authentication system
* Database integration
* Financial transaction logic

👉 Designed as a **practical learning project with real-world structure**

---
