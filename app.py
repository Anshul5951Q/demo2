import sqlite3
from flask import Flask, request

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-me"

@app.get("/user")
def get_user():
    username = request.args.get("username", "")
    connection = sqlite3.connect("training.db")
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    rows = cursor.fetchall()
    connection.close()
    return {"users": rows}

@app.get("/hello")
def hello():
    name = request.args.get("name", "guest")
    return "<h1>Hello " + name + "</h1>"