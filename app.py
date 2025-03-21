from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy user data (replace this with a database in real applications)
users = {"admin": "password123", "dhruv": "mysecret"}  

@app.route("/")
def home():
    return render_template("login.html")  # Load the login page

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username in users and users[username] == password:
        return f"Welcome, {username}! You have successfully logged in."
    else:
        return "Invalid username or password. Please try again."

if __name__ == "__main__":
    app.run(debug=True)