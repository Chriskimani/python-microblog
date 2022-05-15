import os
from flask import (
    Flask,
    session,
    render_template,
    request,
    abort,
    flash,
    redirect,
    url_for,
)

app = Flask(__name__)
# Secret key generated with secrets.token_urlsafe()
app.secret_key = "lkaQT-kAb6aIvqWETVcCQ28F-j-rP_PSEaCDdTynkXA"

users = {}


@app.get("/")
def home():
    return render_template("home-1.html", email=session.get("email")) ## the email is coming from the cookie.


@app.get("/protected")
def protected():
    if not session.get("email"):
        abort(401) ## unauth
    return render_template("protected.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")