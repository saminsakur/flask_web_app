from flask import Blueprint, render_template, request
from flask.helpers import flash

auth = Blueprint(__name__, "views")


@auth.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must me greater than 4 characters.", category="error")
        elif len(first_name) < 2:
            flash("First name must me greater than 4 characters.", category="error")
        elif password1 != password2:
            flash("Passwords doesn't match", category="error")
        elif len(password1) < 6:
            flash("Password must me greater than 6 characters", category="error")
        else:
            flash("Account created!", category="success")

    return render_template("signup.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return render_template("logout.html")
