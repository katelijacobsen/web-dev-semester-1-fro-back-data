from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/signup.html")
def signup():
    return render_template("signup.html")

@app.route("/login.html")
def login():
    return render_template("login.html")